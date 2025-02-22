---
title: "OOPs - 2 | Advanced Tricks in OOPs 📦"
keywords: ["OOPs" ,"python"]
categories: [OOPs]
draft: false
defaultTheme: auto
tags: ["OOPs" ,"python"]
showToc: true
comments: true
cover:
    image: posts/oops1.jpeg 
    alt: oops1
---
## 1. Property Decorators

Properties allow you to use methods like attributes, providing a clean way to implement getters, setters, and deleters.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # Output: 25
print(temp.fahrenheit)  # Output: 77.0
temp.fahrenheit = 100
print(temp.celsius)     # Output: 37.77777777777778
```

## 2. Class Methods and Static Methods

Class methods operate on the class itself, while static methods are utility functions that don't need access to class or instance attributes.

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])

    @staticmethod
    def is_vegetarian(ingredients):
        return "ham" not in ingredients

margherita = Pizza.margherita()
prosciutto = Pizza.prosciutto()
print(Pizza.is_vegetarian(margherita.ingredients))  # Output: True
print(Pizza.is_vegetarian(prosciutto.ingredients))  # Output: False
```

## 3. Abstract Base Classes

Abstract Base Classes (ABCs) define a common API for subclasses, ensuring that derived classes implement particular methods.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Running on four legs"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "Flying"

dog = Dog()
bird = Bird()
print(dog.make_sound(), dog.move())   # Output: Woof! Running on four legs
print(bird.make_sound(), bird.move()) # Output: Chirp! Flying
```

## 4. Multiple Inheritance and Method Resolution Order (MRO)

Python supports multiple inheritance, allowing a class to inherit from multiple parent classes.

```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

d = D()
d.method()  # Output: B method
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

## 5. Metaclasses

Metaclasses are classes for classes. They define how classes behave, allowing you to customize class creation.

```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```

## 6. Descriptors

Descriptors define how attribute access is handled, allowing for sophisticated attribute management.

```python
class Age:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return getattr(obj, f"_{self.name}", None)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be positive")
        setattr(obj, f"_{self.name}", value)

class Person:
    age = Age()

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.age)  # Output: 30
person.age = 31    # This works
try:
    person.age = -5  # This raises a ValueError
except ValueError as e:
    print(e)  # Output: Age must be positive
```

## 7. Context Managers

Context managers allow you to allocate and release resources precisely using the `with` statement.

```python
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with File('example.txt', 'w') as f:
    f.write('Hello, World!')
# File is automatically closed after the with block
```
