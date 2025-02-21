---
title: " Essentials | Design Patterns Gist 🤌🤌"
keywords: ["design-patterns", "python"]
categories: [design-patterns]
date: 2024-09-23T01:30:03+05:30
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

### 1. Creational Patterns

Creational patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or add complexity to the design. Creational design patterns solve this problem by somehow controlling this object creation.

Key characteristics:

- They abstract the instantiation process.
- They help make a system independent of how its objects are created, composed, and represented.

### 2. Structural Patterns

Structural patterns are concerned with how classes and objects are composed to form larger structures. They use inheritance to compose interfaces or implementations.

Key characteristics:

- They focus on simplifying the structure by identifying the relationships between entities.
- They help in building flexible and efficient software by forming large object structures between many disparate objects.

### 3. Behavioral Patterns

Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects. They characterize complex control flow that's difficult to follow at run-time.

Key characteristics:

- They focus on communication between objects.
- They deal with how objects distribute work and describe how disparate parts of a system communicate.

Now, let's focus on the most widely used design patterns across these categories, with multiple examples for each.

## Widely Used Design Patterns With Examples

### 1. Singleton (Creational Pattern)

**Purpose**: Ensures a class has only one instance and provides a global point of access to it.

**Real-World Usage**: Database connections, logging, caching, thread pools.

**Example 1: Classic Singleton**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```

**Example 2: Thread-Safe Singleton**

```python
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Usage
def worker():
    singleton = ThreadSafeSingleton()
    print(f"ID of singleton in {threading.current_thread().name}: {id(singleton)}")

threads = [threading.Thread(target=worker) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
```

### 2. Factory Method (Creational Pattern)

**Purpose**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate.

**Real-World Usage**: GUI libraries, database access layers, file format parsers.

**Example 1: Simple Factory Method**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```

**Example 2: Factory Method with Subclasses**

```python
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "Result of ConcreteProduct1"

class ConcreteProduct2(Product):
    def operation(self):
        return "Result of ConcreteProduct2"

# Usage
creator1 = ConcreteCreator1()
print(creator1.some_operation())

creator2 = ConcreteCreator2()
print(creator2.some_operation())
```

### 3. Observer (Behavioral Pattern)

**Purpose**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

**Real-World Usage**: Event handling systems, Model-View-Controller (MVC) architectures, publish-subscribe systems.

**Example 1: Weather Station**

```python
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

class Display:
    def update(self, temperature):
        print(f"Current temperature: {temperature}°C")

# Usage
weather_station = WeatherStation()
display1 = Display()
display2 = Display()

weather_station.register_observer(display1)
weather_station.register_observer(display2)

weather_station.set_temperature(25)  # Both displays will show: Current temperature: 25°C
weather_station.set_temperature(30)  # Both displays will show: Current temperature: 30°C
```

**Example 2: Stock Market**

```python
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def set_price(self, price):
        self.price = price
        self.notify()

class Investor:
    def __init__(self, name):
        self.name = name

    def update(self, stock):
        print(f"{self.name} notified. {stock.symbol} now at ${stock.price}")

# Usage
stock = Stock("AAPL", 150)
investor1 = Investor("John")
investor2 = Investor("Jane")

stock.attach(investor1)
stock.attach(investor2)

stock.set_price(155)
stock.set_price(160)
```

### 4. Strategy (Behavioral Pattern)

**Purpose**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

**Real-World Usage**: Sorting algorithms, payment processing systems, compression algorithms.

**Example 1: Sorting Strategy**

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using bubble sort")
        return sorted(data)

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using quick sort")
        return sorted(data)

class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

# Usage
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorter = Sorter(BubbleSort())
print(sorter.sort(data))

sorter = Sorter(QuickSort())
print(sorter.sort(data))
```

**Example 2: Payment Strategy**

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card {self.card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal account {self.email}")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def calculate_total(self):
        return sum(price for _, price in self.items)

    def checkout(self, payment_strategy):
        total = self.calculate_total()
        payment_strategy.pay(total)

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 1000)
cart.add_item("Mouse", 50)

credit_card = CreditCardPayment("1234-5678-9012-3456", "123")
paypal = PayPalPayment("user@example.com")

cart.checkout(credit_card)
cart.checkout(paypal)
```

### 5. Decorator (Structural Pattern)

**Purpose**: Attaches additional responsibilities to an object dynamically.

**Real-World Usage**: UI component enhancements, adding features to objects without affecting other objects of the same class, middleware in web frameworks.

**Example 1: Coffee Shop**

```python
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Plain coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return f"{self._coffee.description()}, milk"

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return f"{self._coffee.description()}, sugar"

# Usage
coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)

print(f"{coffee_with_milk_and_sugar.description()}: ${coffee_with_milk_and_sugar.cost()}")
# Output: Plain coffee, milk, sugar: $8
```

**Example 2: Text Formatting**

```python
class Text:
    def __init__(self, content):
        self._content = content

    def render(self):
        return self._content

class BoldDecorator:
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"

class ItalicDecorator:
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"

class UnderlineDecorator:
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<u>{self._wrapped.render()}</u>"

# Usage
text = Text("Hello, World!")
bold_text = BoldDecorator(text)
italic_bold_text = ItalicDecorator(bold_text)
final_text = UnderlineDecorator(italic_bold_text)

print(final_text.render())
# Output: <u><i><b>Hello, World!</b></i></u>
```

## 6. Builder (Creational Pattern)

**Purpose**: Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

**Real-World Usage**: Creating complex objects step by step, constructing composite structures, implementing fluent interfaces.

**Example 1: Computer Builder**

```python
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Computer [CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB]"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def configure_ram(self, ram):
        self.computer.ram = ram
        return self

    def configure_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer

# Usage
builder = ComputerBuilder()
computer = builder.configure_cpu("Intel i7").configure_ram(16).configure_storage(512).build()
print(computer)  # Output: Computer [CPU: Intel i7, RAM: 16GB, Storage: 512GB]
```

**Example 2: Pizza Builder**

```python
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.mushrooms:
            toppings.append("mushrooms")
        return f"{self.size} inch Pizza with {', '.join(toppings)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def build(self):
        return self.pizza

# Usage
builder = PizzaBuilder()
pizza = builder.size(12).add_cheese().add_pepperoni().build()
print(pizza)  # Output: 12 inch Pizza with cheese, pepperoni
```

## 7. Adapter (Structural Pattern)

**Purpose**: Allows objects with incompatible interfaces to collaborate.

**Real-World Usage**: Integrating new systems with legacy code, working with third-party libraries, creating wrappers for existing classes.

**Example 1: Power Adapter**

```python
class EuropeanSocketInterface:
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

class USASocketInterface:
    def voltage(self):
        return 120

    def live(self):
        return 1

    def neutral(self):
        return -1

class Adapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.socket.live()

    def neutral(self):
        return self.socket.neutral()

class ElectricKettle:
    def __init__(self, power):
        self.power = power

    def boil(self):
        if self.power.voltage() > 110:
            print("Kettle on fire!")
        else:
            print("Coffee time!")

# Usage
eu_socket = EuropeanSocketInterface()
adapter = Adapter(eu_socket)
kettle = ElectricKettle(adapter)
kettle.boil()  # Output: Coffee time!
```

**Example 2: Media Player Adapter**

```python
from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type, file_name):
        pass

class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, file_name):
        pass

    @abstractmethod
    def play_mp4(self, file_name):
        pass

class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        print(f"Playing vlc file. Name: {file_name}")

    def play_mp4(self, file_name):
        pass

class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        pass

    def play_mp4(self, file_name):
        print(f"Playing mp4 file. Name: {file_name}")

class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == "vlc":
            self.advanced_music_player = VlcPlayer()
        elif audio_type == "mp4":
            self.advanced_music_player = Mp4Player()

    def play(self, audio_type, file_name):
        if audio_type == "vlc":
            self.advanced_music_player.play_vlc(file_name)
        elif audio_type == "mp4":
            self.advanced_music_player.play_mp4(file_name)

class AudioPlayer(MediaPlayer):
    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            print(f"Playing mp3 file. Name: {file_name}")
        elif audio_type == "vlc" or audio_type == "mp4":
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)
        else:
            print("Invalid media. " + audio_type + " format not supported")

# Usage
audio_player = AudioPlayer()
audio_player.play("mp3", "beyond_the_horizon.mp3")
audio_player.play("mp4", "alone.mp4")
audio_player.play("vlc", "far_far_away.vlc")
audio_player.play("avi", "mind_me.avi")
```

## 8. Facade (Structural Pattern)

**Purpose**: Provides a simplified interface to a library, a framework, or any other complex set of classes.

**Real-World Usage**: Simplifying complex library interactions, providing a single entry point for a subsystem, wrapping poorly designed collections of APIs.

**Example 1: Home Theater Facade**

```python
class Amplifier:
    def on(self):
        print("Amplifier on")

    def off(self):
        print("Amplifier off")

    def set_volume(self, level):
        print(f"Setting volume to {level}")

class DVDPlayer:
    def on(self):
        print("DVD Player on")

    def off(self):
        print("DVD Player off")

    def play(self, movie):
        print(f"Playing '{movie}'")

class Projector:
    def on(self):
        print("Projector on")

    def off(self):
        print("Projector off")

class HomeTheaterFacade:
    def __init__(self, amp, dvd, projector):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.projector.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.amp.off()
        self.dvd.off()
        self.projector.off()

# Usage
amp = Amplifier()
dvd = DVDPlayer()
projector = Projector()
home_theater = HomeTheaterFacade(amp, dvd, projector)

home_theater.watch_movie("Inception")
home_theater.end_movie()
```

**Example 2: Online Shopping Facade**

```python
class Inventory:
    def check(self, item_name):
        print(f"Checking inventory for {item_name}")
        return True

class Payment:
    def process(self, amount):
        print(f"Processing payment of ${amount}")
        return True

class Shipping:
    def ship(self, address):
        print(f"Shipping to {address}")

class OnlineShoppingFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def place_order(self, item, amount, address):
        if self.inventory.check(item):
            if self.payment.process(amount):
                self.shipping.ship(address)
                print("Order placed successfully!")
            else:
                print("Payment failed.")
        else:
            print("Item out of stock.")

# Usage
shop = OnlineShoppingFacade()
shop.place_order("Laptop", 999, "123 Main St, Anytown, USA")
```

## 9. Command (Behavioral Pattern)

**Purpose**: Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

**Real-World Usage**: GUI buttons and menu items, macro recording, multi-level undo/redo, job queues.

**Example 1: Remote Control**

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Usage
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Output: Light is on

remote.set_command(light_off)
remote.press_button()  # Output: Light is off
```

**Example 2: Stock Trading**

```python
from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def execute(self):
        pass

class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def buy(self):
        print(f"Stock [ Name: {self.name}, Quantity: {self.quantity} ] bought")

    def sell(self):
        print(f"Stock [ Name: {self.name}, Quantity: {self.quantity} ] sold")

class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class Broker:
    def __init__(self):
        self.order_list = []

    def take_order(self, order):
        self.order_list.append(order)

    def place_orders(self):
        for order in self.order_list:
            order.execute()
        self.order_list = []

# Usage
stock = Stock("ABC", 100)
buy_stock_order = BuyStock(stock)
sell_stock_order = SellStock(stock)

broker = Broker()
broker.take_order(buy_stock_order)
broker.take_order(sell_stock_order)

broker.place_orders()
```

# Comparison of all Design Patterns

## 🍨Creational Patterns

### 1. Singleton

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

### 2. Factory Method

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

### 3. Abstract Factory

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

### 4. Builder

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

### 5. Prototype

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

## 🏢Structural Patterns

### 6. Adapter

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

### 7. Bridge

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

### 8. Composite

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

### 9. Decorator

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

### 10. Facade

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

### 11. Flyweight

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

### 12. Proxy

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

## 🤗Behavioral Patterns

### 13. Chain of Responsibility

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

### 14. Command

- Purpose: Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
- Applicability:
  - When you want to parameterize objects by an action to perform
  - When you want to specify, queue, and execute requests at different times
- Pros:
  - Decouples the object that invokes the operation from the object that performs it
  - Easy to add new commands
- Cons:
  - Can lead to a large number of small classes

### 15. Interpreter

- Purpose: Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
- Applicability:
  - When you need to interpret a simple language with simple grammar
- Pros:
  - Easy to change and extend the grammar
  - Implementing the grammar is straightforward
- Cons:
  - Complex grammars are hard to maintain
  - Can be inefficient for large grammars

### 16. Iterator

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

### 17. Mediator

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

### 18. Memento

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

### 19. Observer

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

### 20. State

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

### 21. Strategy

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

### 22. Template Method

- Purpose: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
- Applicability:
  - When you want to implement the invariant parts of an algorithm once and leave it up to subclasses to implement the behavior that can vary
- Pros:
  - Reuses common code
  - Provides a framework for creating algorithms
- Cons:
  - Difficult to maintain a large number of algorithms
  - Can lead to a rigid design

### 23. Visitor

- Purpose: Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.
- Applicability:
  - When an object structure contains many classes of objects with differing interfaces, and you want to perform operations on these objects that depend on their concrete classes
- Pros:
  - Makes adding new operations easy
  - Gathers related operations and separates unrelated ones
- Cons:
  - Adding new ConcreteElement classes is hard
  - Can result in a loss of encapsulation
