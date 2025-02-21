---
title: "OOPs - 3 | OOPs Application of Advanced OOP Techniques in Programming Challenges 📦"
keywords: ["OOPs" ,"python"]
categories: [OOPs]
date: 2024-09-25T11:30:03+05:30
draft: false
defaultTheme: auto
tags: ["OOPs" ,"python"]
showToc: true
comments: true
cover:
    image: posts/oops1.jpeg 
    alt: oops1

---

## 1. Database Connection Pool using Singleton and Context Manager

Problem: Managing database connections efficiently in a multi-threaded application.

Solution: Use the Singleton pattern to ensure a single connection pool, and a context manager for safe connection handling.

```python
import threading
from contextlib import contextmanager

class DatabasePool:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.connections = []
        return cls._instance

    def create_connection(self):
        # Simulating connection creation
        return f"Connection-{len(self.connections)}"

    def get_connection(self):
        if not self.connections:
            return self.create_connection()
        return self.connections.pop()

    def return_connection(self, connection):
        self.connections.append(connection)

@contextmanager
def db_connection():
    pool = DatabasePool()
    connection = pool.get_connection()
    try:
        yield connection
    finally:
        pool.return_connection(connection)

# Usage
def worker():
    with db_connection() as conn:
        print(f"Thread {threading.current_thread().name} using {conn}")

threads = [threading.Thread(target=worker) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
```

This solution uses the Singleton pattern to ensure a single pool of connections and a context manager to safely acquire and release connections.

## 2. Configurable Data Validation using Descriptors

Problem: Implementing reusable and configurable data validation for class attributes.

Solution: Use descriptors to create a flexible validation system.

```python
class Validator:
    def __init__(self, min_value=None, max_value=None, regex=None):
        self.min_value = min_value
        self.max_value = max_value
        self.regex = regex

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be no more than {self.max_value}")
        if self.regex and not re.match(self.regex, str(value)):
            raise ValueError(f"{self.name} must match the pattern {self.regex}")
        instance.__dict__[self.name] = value

class Person:
    age = Validator(min_value=0, max_value=150)
    name = Validator(regex=r'^[A-Za-z]+$')

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
try:
    person = Person("John123", 30)  # Raises ValueError for invalid name
except ValueError as e:
    print(e)

try:
    person = Person("John", 200)  # Raises ValueError for invalid age
except ValueError as e:
    print(e)

person = Person("John", 30)  # Valid
print(f"Name: {person.name}, Age: {person.age}")
```

This solution uses descriptors to create a reusable validation system that can be easily applied to multiple attributes and classes.

## 3. Plugin System using Abstract Base Classes and Metaclasses

Problem: Creating a flexible plugin system for a text processing application.

Solution: Use Abstract Base Classes to define the plugin interface and a metaclass for automatic plugin registration.

```python
from abc import ABC, abstractmethod

class PluginMeta(type):
    plugins = {}
    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        if name != 'Plugin':
            cls.plugins[new_cls.name] = new_cls
        return new_cls

class Plugin(ABC, metaclass=PluginMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def process(self, text):
        pass

class UppercasePlugin(Plugin):
    name = 'uppercase'
    def process(self, text):
        return text.upper()

class ReversePlugin(Plugin):
    name = 'reverse'
    def process(self, text):
        return text[::-1]

class TextProcessor:
    def __init__(self):
        self.plugins = PluginMeta.plugins

    def process(self, text, plugin_name):
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin {plugin_name} not found")
        return self.plugins[plugin_name]().process(text)

# Usage
processor = TextProcessor()
text = "Hello, World!"
print(processor.process(text, 'uppercase'))  # Output: HELLO, WORLD!
print(processor.process(text, 'reverse'))    # Output: !dlroW ,olleH
```

This solution uses an Abstract Base Class to define the plugin interface and a metaclass for automatic plugin registration, allowing for easy extension of the text processing capabilities.

## 4. Efficient Data Storage using Properties and Slots

Problem: Optimizing memory usage for a large number of instances with a fixed set of attributes.

Solution: Use `__slots__` to restrict attribute creation and properties for controlled access.

```python
class Point:
    __slots__ = ('_x', '_y')

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = value

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Usage
points = [Point(i, i*2) for i in range(1000000)]
print(points[500000])  # Output: Point(500000, 1000000)

# This will raise an AttributeError
try:
    points[0].z = 5
except AttributeError as e:
    print(e)
```

This solution uses `__slots__` to restrict attribute creation, saving memory, and properties to provide controlled access to the attributes.


