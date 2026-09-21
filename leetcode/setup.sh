#!/usr/bin/env bash
# Set up the DSA pattern bot on this machine. Safe to re-run: every step is
# skipped if it is already done, and nothing existing is overwritten.
set -euo pipefail

LEETCODE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$LEETCODE_DIR/.." && pwd)"
VENV="$LEETCODE_DIR/.venv"
PY="$VENV/bin/python"
KEY="$HOME/.ssh/hugo-blog-deploy"
SSH_ALIAS="github.com-hugo-blog"
UNIT_DIR="$HOME/.config/systemd/user"

say()  { printf '\n\033[1m==> %s\033[0m\n' "$*"; }
note() { printf '    %s\n' "$*"; }
warn() { printf '\033[33m    ! %s\033[0m\n' "$*"; }

# ---------------------------------------------------------------- 1. virtualenv
say "Python environment"
if [[ ! -x "$PY" ]]; then
  # ensurepip is missing on this Ubuntu without python3-venv, so bootstrap pip
  # from get-pip.py instead of requiring sudo apt install.
  python3 -m venv --without-pip "$VENV"
  curl -sS https://bootstrap.pypa.io/get-pip.py -o "$LEETCODE_DIR/.get-pip.py"
  "$PY" "$LEETCODE_DIR/.get-pip.py" -q
  rm -f "$LEETCODE_DIR/.get-pip.py"
  note "created $VENV"
else
  note "$VENV already exists"
fi
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -r "$LEETCODE_DIR/requirements.txt"
note "dependencies installed"

# ---------------------------------------------------------------------- 2. .env
say "Configuration"
if [[ ! -f "$LEETCODE_DIR/.env" ]]; then
  cp "$LEETCODE_DIR/.env.example" "$LEETCODE_DIR/.env"
  chmod 600 "$LEETCODE_DIR/.env"
  note "created leetcode/.env from the example"
else
  chmod 600 "$LEETCODE_DIR/.env"
  note "leetcode/.env already present (left untouched)"
fi

# ------------------------------------------------------------------ 3. database
say "Database"
if [[ ! -f "$LEETCODE_DIR/dsa.db" ]]; then
  ( cd "$LEETCODE_DIR" && "$PY" -m bot.seed )
else
  note "dsa.db exists; refreshing the sheet import only"
  ( cd "$LEETCODE_DIR" && "$PY" -m bot.seed --skip-enrich )
fi

# ---------------------------------------------------------------- 4. deploy key
say "GitHub push access"
if [[ ! -f "$KEY" ]]; then
  ssh-keygen -t ed25519 -N "" -C "hugo-blog-deploy@$(hostname -s)" -f "$KEY" >/dev/null
  note "generated $KEY"
fi
if ! grep -q "Host $SSH_ALIAS" "$HOME/.ssh/config" 2>/dev/null; then
  mkdir -p "$HOME/.ssh" && chmod 700 "$HOME/.ssh"
  cat >> "$HOME/.ssh/config" <<EOF

Host $SSH_ALIAS
  HostName github.com
  User git
  IdentityFile $KEY
  IdentitiesOnly yes
EOF
  chmod 600 "$HOME/.ssh/config"
  note "added an ssh alias for $SSH_ALIAS"
fi

CURRENT_REMOTE="$(git -C "$REPO_ROOT" remote get-url origin)"
SLUG="$(printf '%s' "$CURRENT_REMOTE" | sed -E 's#.*github\.com(-[a-z-]+)?[:/]##; s#\.git$##')"
if [[ "$CURRENT_REMOTE" != *"$SSH_ALIAS"* ]]; then
  git -C "$REPO_ROOT" remote set-url origin "git@$SSH_ALIAS:$SLUG.git"
  note "origin -> git@$SSH_ALIAS:$SLUG.git  (was $CURRENT_REMOTE)"
fi

if ssh -o StrictHostKeyChecking=accept-new -o ConnectTimeout=10 -T "git@$SSH_ALIAS" 2>&1 \
     | grep -q "successfully authenticated"; then
  note "deploy key is authorised ✓"
else
  warn "Deploy key not authorised yet. Add this key to the repo:"
  warn "  https://github.com/$SLUG/settings/keys/new"
  warn "  tick 'Allow write access'"
  echo
  cat "$KEY.pub"
  echo
fi

# -------------------------------------------------------------------- 5. service
say "Background service"
mkdir -p "$UNIT_DIR"
sed "s#__LEETCODE_DIR__#$LEETCODE_DIR#g" \
  "$LEETCODE_DIR/systemd/dsa-bot.service.in" > "$UNIT_DIR/dsa-bot.service"
loginctl enable-linger "$USER" >/dev/null 2>&1 || warn "could not enable linger; the bot may stop at logout"
systemctl --user daemon-reload
note "unit installed at $UNIT_DIR/dsa-bot.service"

# ------------------------------------------------------------------- 6. next up
say "Next steps"
MISSING="$( ( cd "$LEETCODE_DIR" && "$PY" -c 'from bot import config; print(",".join(config.missing_settings()))' ) )"
if [[ -n "$MISSING" ]]; then
  note "Still to fill in leetcode/.env: $MISSING"
  note "  1. Talk to @BotFather on Telegram, /newbot, copy the token"
  note "     -> TELEGRAM_BOT_TOKEN in leetcode/.env"
  note "  2. Message your new bot, then run:"
  note "       cd $LEETCODE_DIR && .venv/bin/python -m bot.whoami"
  note "     -> TELEGRAM_CHAT_ID in leetcode/.env"
  note "  3. Re-run ./setup.sh, then: systemctl --user enable --now dsa-bot"
else
  systemctl --user enable --now dsa-bot
  note "bot started. Logs: journalctl --user -u dsa-bot -f"
fi
