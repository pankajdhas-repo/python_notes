# Object-Oriented Programming (OOP)

Object-Oriented Programming is a programming paradigm that organizes code into objects, which combine data (attributes) and behavior (methods).

---

## Core OOP Concepts

1. **Class**: A blueprint for creating objects
2. **Object**: An instance of a class
3. **Encapsulation**: Bundling data and methods together
4. **Inheritance**: Creating new classes from existing ones
5. **Polymorphism**: Using a unified interface for different types
6. **Abstraction**: Hiding complex implementation details

---

## Classes and Objects

### Defining a Class

```python
class Dog:
    """A simple Dog class."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # Another instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
```

### Creating Objects

```python
# Create instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes
print(dog1.name)      # Buddy
print(dog2.age)       # 5
print(dog1.species)   # Canis familiaris (class attribute)

# Call methods
print(dog1.bark())         # Buddy says Woof!
print(dog2.description())  # Max is 5 years old

# Modify attributes
dog1.age = 4
print(dog1.age)  # 4
```

---

## The `__init__` Method

The constructor initializes new objects.

```python
class Person:
    def __init__(self, name, age, email=None):
        """Initialize a Person instance."""
        self.name = name
        self.age = age
        self.email = email or "Not provided"
        self._created_at = datetime.now()  # Private attribute
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Creating instances
p1 = Person("Alice", 25)
p2 = Person("Bob", 30, "bob@example.com")

print(p1.email)  # Not provided
print(p2.email)  # bob@example.com
```

---

## Instance vs Class Attributes

```python
class Counter:
    # Class attribute - shared by all instances
    total_count = 0
    
    def __init__(self, name):
        # Instance attribute - unique to each instance
        self.name = name
        self.count = 0
        Counter.total_count += 1
    
    def increment(self):
        self.count += 1

# Create instances
c1 = Counter("Counter 1")
c2 = Counter("Counter 2")

print(Counter.total_count)  # 2 (class attribute)
print(c1.count)             # 0 (instance attribute)

c1.increment()
c1.increment()
print(c1.count)             # 2
print(c2.count)             # 0 (different instance)
```

---

## Methods

### Instance Methods

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # Instance method - has access to self
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def circumference(self):
        import math
        return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.area())          # 78.54...
print(circle.circumference()) # 31.42...
```

### Class Methods

```python
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    
    # Class method - receives class as first argument
    @classmethod
    def get_population(cls):
        return cls.population
    
    # Alternative constructor
    @classmethod
    def from_string(cls, person_str):
        """Create Person from 'name,age' string."""
        name, age = person_str.split(',')
        return cls(name)

print(Person.get_population())  # 0

p1 = Person("Alice")
p2 = Person("Bob")

print(Person.get_population())  # 2

# Using alternative constructor
p3 = Person.from_string("Charlie,25")
print(p3.name)  # Charlie
```

### Static Methods

```python
class MathUtils:
    # Static method - no access to class or instance
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_positive(n):
        return n > 0
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# Can be called on class or instance
print(MathUtils.add(3, 5))        # 8
print(MathUtils.is_positive(-5))  # False
print(MathUtils.factorial(5))     # 120
```

### When to Use Which?

| Method Type | First Argument | Use Case |
|------------|----------------|----------|
| Instance | `self` | Access/modify instance data |
| Class | `cls` | Access/modify class data, alternative constructors |
| Static | None | Utility functions logically related to class |

---

## Encapsulation

### Public, Protected, and Private

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._balance = balance     # Protected (convention)
        self.__pin = "1234"         # Private (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 1000)

# Public - freely accessible
print(account.owner)  # Alice

# Protected - accessible but shouldn't be modified directly
print(account._balance)  # 1000 (convention: don't touch)

# Private - name mangling applied
# print(account.__pin)  # AttributeError
print(account._BankAccount__pin)  # 1234 (still accessible, but discouraged)
```

### Properties (Getters and Setters)

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)

# Using properties like attributes
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.fahrenheit = 100
print(temp.celsius)     # 37.78

# Validation works
# temp.celsius = -300  # ValueError: Temperature below absolute zero!
```

---

## Inheritance

### Basic Inheritance

```python
class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")
    
    def describe(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    """Dog class inherits from Animal."""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed
    
    def speak(self):
        return f"{self.name} says Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    """Cat class inherits from Animal."""
    
    def speak(self):
        return f"{self.name} says Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching!"

# Using inherited classes
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 5)

print(dog.describe())  # Buddy is 3 years old (inherited)
print(dog.speak())     # Buddy says Woof! (overridden)
print(dog.fetch())     # Buddy is fetching the ball! (new method)

print(cat.describe())  # Whiskers is 5 years old
print(cat.speak())     # Whiskers says Meow!
```

### The super() Function

```python
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent __init__ called for {name}")
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's __init__
        self.age = age
        print(f"Child __init__ called for {name}")
    
    def greet(self):
        parent_greeting = super().greet()  # Call parent's method
        return f"{parent_greeting}, and I'm {self.age} years old"

child = Child("Alice", 10)
# Parent __init__ called for Alice
# Child __init__ called for Alice

print(child.greet())
# Hello, I'm Alice, and I'm 10 years old
```

### Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying!"

class Swimmer:
    def swim(self):
        return "Swimming!"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())   # Flying!
print(duck.swim())  # Swimming!
print(duck.quack()) # Quack!

# Method Resolution Order (MRO)
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyer'>, <class 'Swimmer'>, <class 'object'>)
```

### Diamond Problem and MRO

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B -> " + super().method()

class C(A):
    def method(self):
        return "C -> " + super().method()

class D(B, C):
    def method(self):
        return "D -> " + super().method()

d = D()
print(d.method())  # D -> B -> C -> A

# Python uses C3 linearization for MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

---

## Polymorphism

### Duck Typing

```python
class Duck:
    def speak(self):
        return "Quack!"
    
    def walk(self):
        return "Waddle waddle"

class Person:
    def speak(self):
        return "Hello!"
    
    def walk(self):
        return "Step step"

def make_it_speak(thing):
    """Works with any object that has a speak() method."""
    print(thing.speak())

# Both work - duck typing
make_it_speak(Duck())    # Quack!
make_it_speak(Person())  # Hello!
```

### Method Overriding

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

# Polymorphic function
def print_area(shape):
    print(f"Area: {shape.area():.2f}")

shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 8)]
for shape in shapes:
    print_area(shape)
# Area: 20.00
# Area: 28.27
# Area: 16.00
```

### Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(v1 + v2)  # Vector(6, 4)
print(v1 - v2)  # Vector(-2, 2)
print(v1 * 3)   # Vector(6, 9)
print(abs(v1))  # 3.605...
```

---

## Abstract Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass
    
    def describe(self):
        """Non-abstract method available to all subclasses."""
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

# shape = Shape()  # TypeError: Can't instantiate abstract class

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

rect = Rectangle(4, 5)
circle = Circle(3)

print(rect.describe())    # Area: 20.00, Perimeter: 18.00
print(circle.describe())  # Area: 28.27, Perimeter: 18.85
```

---

## Magic (Dunder) Methods

### Common Magic Methods

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation
    def __str__(self):
        """Human-readable string (for print)."""
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        """Developer-friendly string (for debugging)."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Comparison
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __le__(self, other):
        return self.pages <= other.pages
    
    # Length
    def __len__(self):
        return self.pages
    
    # Boolean
    def __bool__(self):
        return self.pages > 0
    
    # Containment
    def __contains__(self, word):
        return word.lower() in self.title.lower()
    
    # Callable
    def __call__(self):
        return f"Reading {self.title}..."

book = Book("Python Guide", "Alice", 350)

print(str(book))     # Python Guide by Alice
print(repr(book))    # Book('Python Guide', 'Alice', 350)
print(len(book))     # 350
print(bool(book))    # True
print("python" in book)  # True
print(book())        # Reading Python Guide...
```

### Container Magic Methods

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []
    
    def __len__(self):
        return len(self._songs)
    
    def __getitem__(self, index):
        return self._songs[index]
    
    def __setitem__(self, index, value):
        self._songs[index] = value
    
    def __delitem__(self, index):
        del self._songs[index]
    
    def __iter__(self):
        return iter(self._songs)
    
    def __contains__(self, song):
        return song in self._songs
    
    def add(self, song):
        self._songs.append(song)

playlist = Playlist("My Favorites")
playlist.add("Song A")
playlist.add("Song B")
playlist.add("Song C")

print(len(playlist))        # 3
print(playlist[0])          # Song A
print("Song B" in playlist) # True

for song in playlist:
    print(song)
```

### Context Manager Magic Methods

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exceptions, False to propagate
        return False

# Usage
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

---

## Data Classes (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float

# Automatically generates __init__, __repr__, __eq__
p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)

print(p1)        # Point(x=3.0, y=4.0)
print(p1 == p2)  # True

@dataclass
class Person:
    name: str
    age: int
    email: str = "Not provided"
    hobbies: List[str] = field(default_factory=list)
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Alice", 25)
print(person)  # Person(name='Alice', age=25, email='Not provided', hobbies=[])

@dataclass(frozen=True)  # Immutable
class ImmutablePoint:
    x: float
    y: float

p = ImmutablePoint(1.0, 2.0)
# p.x = 3.0  # FrozenInstanceError

@dataclass(order=True)  # Adds comparison methods
class Student:
    name: str
    grade: float = field(compare=True)
    student_id: str = field(compare=False)

students = [
    Student("Alice", 90.5, "S001"),
    Student("Bob", 85.0, "S002"),
    Student("Charlie", 92.0, "S003")
]
print(sorted(students))  # Sorted by grade
```

---

## Composition vs Inheritance

### Inheritance ("is-a" relationship)

```python
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):  # A Car IS-A Vehicle
    def move(self):
        return "Driving on the road"
```

### Composition ("has-a" relationship)

```python
class Engine:
    def start(self):
        return "Engine started"
    
    def stop(self):
        return "Engine stopped"

class Car:  # A Car HAS-AN Engine
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()
    
    def stop(self):
        return self.engine.stop()

car = Car()
print(car.start())  # Engine started
```

### When to Use Which?

```python
# Prefer composition when:
# - You need flexibility to swap components
# - The relationship is "has-a" not "is-a"
# - You want to avoid deep inheritance hierarchies

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class EmailSender:
    def send(self, to, message):
        print(f"Sending email to {to}: {message}")

class UserService:
    def __init__(self, logger: Logger, email_sender: EmailSender):
        self.logger = logger
        self.email_sender = email_sender
    
    def register_user(self, email):
        self.logger.log(f"Registering user: {email}")
        self.email_sender.send(email, "Welcome!")
        return f"User {email} registered"

# Easy to swap implementations
service = UserService(Logger(), EmailSender())
```

---

## Practical Example: E-Commerce System

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Product:
    id: str
    name: str
    price: float
    stock: int = 0
    
    def is_available(self):
        return self.stock > 0

@dataclass
class CartItem:
    product: Product
    quantity: int
    
    @property
    def total(self):
        return self.product.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self._items: List[CartItem] = []
    
    def add_item(self, product: Product, quantity: int = 1):
        # Check if product already in cart
        for item in self._items:
            if item.product.id == product.id:
                item.quantity += quantity
                return
        self._items.append(CartItem(product, quantity))
    
    def remove_item(self, product_id: str):
        self._items = [item for item in self._items 
                       if item.product.id != product_id]
    
    @property
    def total(self):
        return sum(item.total for item in self._items)
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount:.2f} on card {self.card_number[-4:]}")
        return True

class PayPal(PaymentMethod):
    def __init__(self, email: str):
        self.email = email
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount:.2f} via PayPal ({self.email})")
        return True

@dataclass
class Order:
    id: str
    items: List[CartItem]
    total: float
    payment_method: PaymentMethod
    created_at: datetime = field(default_factory=datetime.now)
    status: str = "pending"
    
    def process(self):
        if self.payment_method.process_payment(self.total):
            self.status = "completed"
            return True
        self.status = "failed"
        return False

# Usage
laptop = Product("P001", "Laptop", 999.99, stock=10)
mouse = Product("P002", "Mouse", 29.99, stock=50)

cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)

print(f"Cart total: ${cart.total:.2f}")  # Cart total: $1059.97

for item in cart:
    print(f"{item.product.name} x{item.quantity} = ${item.total:.2f}")

payment = CreditCard("1234-5678-9012-3456")
order = Order("O001", list(cart), cart.total, payment)
order.process()  # Processing $1059.97 on card 3456
print(f"Order status: {order.status}")  # Order status: completed
```

---

## Summary

- **Classes** are blueprints, **objects** are instances
- Use `__init__` to initialize objects
- **Instance methods** access `self`, **class methods** access `cls`, **static methods** access neither
- **Encapsulation**: Use `_protected` and `__private` naming conventions
- **Properties** provide getter/setter with attribute syntax
- **Inheritance** creates hierarchies; use `super()` to call parent methods
- **Polymorphism** allows different classes to share interfaces
- **Abstract classes** define interfaces that subclasses must implement
- **Magic methods** customize object behavior
- **Data classes** reduce boilerplate for data containers
- Prefer **composition** over inheritance for flexibility

## Next Steps

Continue to [File Handling](08-file-handling.md) to learn about reading and writing files.
