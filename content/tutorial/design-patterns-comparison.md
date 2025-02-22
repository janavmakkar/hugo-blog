---
date: 2024-09-23
title: " Comparison | Design Patterns 🏗️"
keywords: ["design-patterns", "python"]
categories: [design-patterns]
draft: false
defaultTheme: auto
tags: ["design-patterns", "python"]
showToc: true
comments: true
cover:
  image: posts/systems.jpeg
  alt: systems
---

# Main Design Patterns

Design patterns are typical solutions to common problems in software design.
They are like pre-made blueprints that one can customize to solve recurring design problems in code.
There are 23 classic design patterns defined by the "Gang of Four".
But some are more frequently used in real-world applications than others.

## Categories of Design Patterns

There are three main categories of design patterns:

## 1. Creational Patterns

### 1.1 Singleton

- Purpose: Ensure a class has only one instance and provide a global point of access to it.
- Applicability:
  - When exactly one instance of a class is needed to coordinate actions across the system.
- Pros:
  - Ensures single instance
  - Provides global access point
  - Allows lazy initialization
- Cons:
  - Can make unit testing difficult
  - Violates Single Responsibility Principle
  - Can be overused

### 1.2 Factory Method

- Purpose: Define an interface for creating an object, but let subclasses decide which class to instantiate.
- Applicability:
  - When a class can't anticipate the class of objects it must create
  - When a class wants its subclasses to specify the objects it creates
- Pros:
  - Promotes loose coupling
  - Adheres to Single Responsibility Principle
  - Supports Open/Closed Principle
- Cons:
  - Can lead to many subclasses
  - Can be overkill for simple cases

### 1.3 Abstract Factory

- Purpose: Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
- Applicability:
  - When a system should be independent of how its products are created, composed, and represented
  - When a system should be configured with one of multiple families of products
- Pros:
  - Promotes consistency among products
  - Isolates concrete classes
  - Makes exchanging product families easy
- Cons:
  - Adding new products can be difficult
  - Can become too complex

### 1.4 Builder

- Purpose: Separate the construction of a complex object from its representation.
- Applicability:
  - When the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled
  - When the construction process must allow different representations for the object that's constructed
- Pros:
  - Allows finer control over construction process
  - Isolates code for construction and representation
  - Provides better control over final product
- Cons:
  - Can lead to mutable objects
  - Requires creating separate ConcreteBuilder for each type of product

### 1.5 Prototype

- Purpose: Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
- Applicability:
  - When a system should be independent of how its products are created, composed, and represented
  - When instances of a class can have one of only a few different combinations of state
- Pros:
  - Adds/removes products at runtime
  - Specifies new objects by varying values
  - Reduces subclassing
  - Configures application dynamically
- Cons:
  - Each subclass must implement the cloning method
  - Complicated to implement if objects have circular references

## 2. Structural Patterns

### 2.1 Adapter

- Purpose: Convert the interface of a class into another interface clients expect.
- Applicability:
  - When you want to use an existing class, and its interface does not match the one you need
  - When you want to create a reusable class that cooperates with unrelated or unforeseen classes
- Pros:
  - Allows two incompatible interfaces to work together
  - Improves reusability of existing code
- Cons:
  - Can add complexity to the system
  - Sometimes many adaptations are required along an adapter chain

### 2.2 Bridge

- Purpose: Decouple an abstraction from its implementation so that the two can vary independently.
- Applicability:
  - When you want to avoid a permanent binding between an abstraction and its implementation
  - When both the abstractions and their implementations should be extensible by subclassing
- Pros:
  - Decouples interface from implementation
  - Improves extensibility
  - Hides implementation details from clients
- Cons:
  - Increases complexity
  - Can be overkill for simple scenarios

### 2.3 Composite

- Purpose: Compose objects into tree structures to represent part-whole hierarchies.
- Applicability:
  - When you want clients to be able to ignore the difference between compositions of objects and individual objects
- Pros:
  - Defines class hierarchies consisting of primitive and complex objects
  - Makes client code simple
  - Makes it easy to add new kinds of components
- Cons:
  - Can make design overly general
  - Can be difficult to restrict components of a composite

### 2.4 Decorator

- Purpose: Attach additional responsibilities to an object dynamically.
- Applicability:
  - When you want to add responsibilities to individual objects dynamically and transparently, without affecting other objects
  - When you want to add responsibilities that can be withdrawn
- Pros:
  - More flexible than static inheritance
  - Avoids feature-laden classes high up in the hierarchy
  - Allows for a pay-as-you-go approach
- Cons:
  - Can result in many small objects
  - Can be confusing to developers unfamiliar with the pattern

### 2.5 Facade

- Purpose: Provide a unified interface to a set of interfaces in a subsystem.
- Applicability:
  - When you want to provide a simple interface to a complex subsystem
  - When there are many dependencies between clients and the implementation classes of an abstraction
- Pros:
  - Simplifies the interface of a set of classes
  - Promotes weak coupling between subsystems and clients
- Cons:
  - Can become a "god object" coupled to all classes of an app
  - May not provide enough customization options

### 2.6 Flyweight

- Purpose: Use sharing to support large numbers of fine-grained objects efficiently.
- Applicability:
  - When an application uses a large number of objects
  - When storage costs are high because of the sheer quantity of objects
- Pros:
  - Reduces memory usage
  - Improves performance in apps with many similar objects
- Cons:
  - May introduce complexity
  - Requires careful synchronization in multithreaded environment

### 2.7 Proxy

- Purpose: Provide a surrogate or placeholder for another object to control access to it.
- Applicability:
  - When you need a more versatile or sophisticated reference to an object than a simple pointer
- Pros:
  - Controls access to the original object
  - Allows operations before/after the request gets through
  - Can manage the lifecycle of the original object
- Cons:
  - Introduces another layer of abstraction
  - Response might be delayed

## 3. Behavioral Patterns

### 3.1 Chain of Responsibility

- Purpose: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
- Applicability:
  - When more than one object may handle a request, and the handler isn't known a priori
  - When you want to issue a request to one of several objects without specifying the receiver explicitly
- Pros:
  - Reduces coupling
  - Increases flexibility in assigning responsibilities to objects
- Cons:
  - Request can go unhandled
  - Can be hard to debug

### 3.2 Command

- Purpose: Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
- Applicability:
  - When you want to parameterize objects by an action to perform
  - When you want to specify, queue, and execute requests at different times
- Pros:
  - Decouples the object that invokes the operation from the object that performs it
  - Easy to add new commands
- Cons:
  - Can lead to a large number of small classes

### 3.3 Interpreter

- Purpose: Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
- Applicability:
  - When you need to interpret a simple language with simple grammar
- Pros:
  - Easy to change and extend the grammar
  - Implementing the grammar is straightforward
- Cons:
  - Complex grammars are hard to maintain
  - Can be inefficient for large grammars

### 3.4 Iterator

- Purpose: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- Applicability:
  - When you want to access an aggregate object's contents without exposing its internal representation
  - When you want to support multiple traversals of aggregate objects
- Pros:
  - Simplifies the aggregate interface
  - Supports variations in the traversal of an aggregate
- Cons:
  - Can be overkill for simple collections
  - Might not be as efficient as direct access

### 3.5 Mediator

- Purpose: Define an object that encapsulates how a set of objects interact.
- Applicability:
  - When a set of objects communicate in well-defined but complex ways
  - When you want to customize a behavior that's distributed between several classes without creating subclasses
- Pros:
  - Reduces coupling between Colleagues
  - Centralizes control
  - Simplifies object protocols
- Cons:
  - Can become a monolith
  - Can be difficult to maintain

### 3.6 Memento

- Purpose: Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.
- Applicability:
  - When you need to provide undo functionality
  - When a snapshot of an object's state must be saved so that it can be restored later
- Pros:
  - Preserves encapsulation boundaries
  - Simplifies the originator
- Cons:
  - Can be expensive if a lot of state needs to be copied
  - Caretakers might accumulate many mementos

### 3.7 Observer

- Purpose: Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- Applicability:
  - When a change to one object requires changing others, and you don't know how many objects need to be changed
  - When an object should be able to notify other objects without making assumptions about who these objects are
- Pros:
  - Supports loose coupling
  - Allows for broadcast communication
- Cons:
  - Unexpected updates
  - Can be difficult to track the flow of callbacks

### 3.8 State

- Purpose: Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
- Applicability:
  - When an object's behavior depends on its state, and it must change its behavior at runtime depending on that state
  - When operations have large, multipart conditional statements that depend on the object's state
- Pros:
  - Localizes state-specific behavior
  - Makes state transitions explicit
- Cons:
  - Can lead to a large number of classes
  - Can be overkill for simple state machines

### 3.9 Strategy

- Purpose: Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
- Applicability:
  - When many related classes differ only in their behavior
  - When you need different variants of an algorithm
- Pros:
  - Defines a family of algorithms
  - Eliminates conditional statements
  - Allows the choice of implementations at runtime
- Cons:
  - Clients must be aware of different strategies
  - Increased number of objects

### 3.10 Template Method

- Purpose: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
- Applicability:
  - When you want to implement the invariant parts of an algorithm once and leave it up to subclasses to implement the behavior that can vary
- Pros:
  - Reuses common code
  - Provides a framework for creating algorithms
- Cons:
  - Difficult to maintain a large number of algorithms
  - Can lead to a rigid design

### 3.11 Visitor

- Purpose: Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.
- Applicability:
  - When an object structure contains many classes of objects with differing interfaces, and you want to perform operations on these objects that depend on their concrete classes
- Pros:
  - Makes adding new operations easy
  - Gathers related operations and separates unrelated ones
- Cons:
  - Adding new ConcreteElement classes is hard
  - Can result in a loss of encapsulation
