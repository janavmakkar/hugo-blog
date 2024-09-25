---
title: "OOPs - 1 | Basic Concepts 📦"
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


## 1. Class and Object

A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects of that class will have.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())  # Output: Buddy says Woof!
```

Illustration:
```
     Class (Dog)
    +-------------------+
    |  Attributes       |
    |   - name          |
    |   - breed         |
    |                   |
    |  Methods          |
    |   - bark()        |
    +-------------------+
            ^
            |
            | Instance
            |
    +-------------------+
    |  Object (my_dog)  |
    |   name: Buddy     |
    |   breed: Golden   |
    |         Retriever |
    +-------------------+
```

## 2. Encapsulation

Encapsulation is the bundling of data and the methods that operate on that data within a single unit (class). It restricts direct access to some of an object's components, which is a means of preventing accidental interference and misuse of the methods and data.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # This would raise an AttributeError
```

Illustration:
```
    BankAccount
   +-------------------+
   |                   |
   |   __balance       |
   |   (Private)       |
   |                   |
   |   deposit()       |
   |   withdraw()      |
   |   get_balance()   |
   |   (Public)        |
   |                   |
   +-------------------+
```

## 3. Inheritance

Inheritance allows a class to inherit attributes and methods from another class. This promotes code reuse and establishes a relationship between parent and child classes.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

Illustration:
```
        Animal
      /        \
    Dog        Cat
```

## 4. Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables you to use a single interface with different underlying forms (data types or classes).

```python
def animal_sound(animal):
    return animal.speak()

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal_sound(dog))  # Output: Buddy says Woof!
print(animal_sound(cat))  # Output: Whiskers says Meow!
```

Illustration:
```
    animal_sound(animal)
            |
     +------+------+
     |             |
    Dog           Cat
  speak()       speak()
```

## 5. Abstraction

Abstraction is the process of hiding the complex implementation details and showing only the necessary features of an object. Abstract classes and methods are used to achieve abstraction in Python.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")        # Output: Area: 15
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 16
```

Illustration:
```
    Shape (Abstract)
    +-------------------+
    |                   |
    |   area()          |
    |   perimeter()     |
    |                   |
    +-------------------+
            ^
            |
            |
    +-------------------+
    |     Rectangle     |
    |                   |
    |   length          |
    |   width           |
    |   area()          |
    |   perimeter()     |
    +-------------------+
```

These are the main concepts of Object-Oriented Programming as implemented in Python. Each concept builds on the others to create a powerful paradigm for organizing and structuring code.
