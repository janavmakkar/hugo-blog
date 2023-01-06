---
title: "Docker Commands"
keywords: [docker ,cheatsheet]
date: 2020-09-15T11:30:03+05:30
# draft: true
# defaultTheme: auto
tags: ["first"]
showToc: true
# disableThemeToggle: true
ShowPostNavLinks: true
ShowBreadCrumbs: true
# ShareButtons: [“linkedin”, “twitter”]
comments: true

---

## Docker Commands 🐳
|S.No| Use Cases | Commands |
|-----| -------- | ------- |
|1. |See all images present in your local machine|```docker images```|
|2. |Search images in docker-hub (registry)| ```docker search MODULENAME```|
|3. |Download image from docker-hub to local machine|```docker pull MODULENAME```|
|4. |Run Docker (Create+Start+Name+Go Inside the Container)|```docker run -it --name CONTAINERNAME IMAGENAME /bin/bash```|
|5. |Check service start or not|```service docker status``` OR ``` docker info```|
|6. |Start Container|``` docker start CONTAINERNAME```|
|7. |Go inside Container |```docker attach CONTAINERNAME ```|
|8. |See all Containers |```docker ps -a ```|
|9. |See only running Containers |```docker ps ```|
|10.|Stop Container |```docker stop CONTAINERNAME ```|
|11.|Delete Container |```docker rm CONTAINERNAME ```|
|12.|Start Docker |```service docker start ```|
|13.|Shows changes b/w Conatiner and its Base Image|```docker diff CONTAINERNAME```|
|14.|Make Image from Container |```docker commit CONTAINERNAME NEW_IMAGENAME ```|
|15.|Make Image from DockerFile |```docker build -t NEW_IMAGENAME .```|


