# Python Basics

## Variables and Data Types

### What are Variables?

Variables are containers for storing data values. In Python, you don't need to declare variable types explicitly - Python infers them automatically.

```python
# Creating variables
name = "Alice"          # String
age = 25                # Integer
height = 5.7            # Float
is_student = True       # Boolean

# Python is dynamically typed
x = 10          # x is an integer
x = "hello"     # now x is a string
```

### Variable Naming Rules

1. Must start with a letter or underscore
2. Can contain letters, numbers, and underscores
3. Case-sensitive (`name` and `Name` are different)
4. Cannot use Python keywords

```python
# Valid variable names
my_variable = 1
_private = 2
camelCase = 3
PascalCase = 4
variable123 = 5

# Invalid variable names
# 123variable = 1   # Cannot start with number
# my-variable = 2   # Hyphens not allowed
# my variable = 3   # Spaces not allowed
# class = 4         # 'class' is a keyword
```

### Naming Conventions (PEP 8)

```python
# Variables and functions: snake_case
user_name = "Alice"
total_count = 100

# Constants: UPPERCASE
MAX_SIZE = 1000
PI = 3.14159

# Classes: PascalCase
class MyClass:
    pass

# Private variables: leading underscore
_internal_value = 42

# "Very private" variables: double underscore
__private_var = "secret"
```

---

## Data Types

Python has several built-in data types:

### Numeric Types

#### Integer (int)
Whole numbers without decimals.

```python
x = 10
y = -5
big_number = 1_000_000  # Underscores for readability

# Check type
print(type(x))  # <class 'int'>

# Integer operations
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.3333... (float division)
print(10 // 3)  # 3 (integer division)
print(10 % 3)   # 1 (modulo - remainder)
print(10 ** 3)  # 1000 (exponentiation)
```

#### Float (float)
Numbers with decimal points.

```python
pi = 3.14159
temperature = -40.5
scientific = 1.5e10  # Scientific notation: 1.5 × 10^10

print(type(pi))  # <class 'float'>

# Float precision
print(0.1 + 0.2)  # 0.30000000000000004 (floating point imprecision)

# For precise decimal calculations, use the decimal module
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
```

#### Complex Numbers (complex)
Numbers with real and imaginary parts.

```python
z = 3 + 4j
print(type(z))      # <class 'complex'>
print(z.real)       # 3.0
print(z.imag)       # 4.0
print(abs(z))       # 5.0 (magnitude)
```

### String (str)

Text data enclosed in quotes.

```python
# Creating strings
single = 'Hello'
double = "World"
triple = '''This is a
multi-line string'''

# String with quotes inside
quote1 = "He said 'Hello'"
quote2 = 'She said "Hi"'
escaped = "He said \"Hello\""

# Raw strings (ignore escape sequences)
path = r"C:\Users\name\folder"

# f-strings (formatted strings) - Python 3.6+
name = "Alice"
age = 25
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Hello, Alice! You are 25 years old.

# f-string expressions
print(f"2 + 2 = {2 + 2}")           # 2 + 2 = 4
print(f"Uppercase: {name.upper()}")  # Uppercase: ALICE
```

#### String Operations

```python
s = "Hello, World!"

# Length
print(len(s))  # 13

# Indexing (0-based)
print(s[0])    # H
print(s[-1])   # ! (last character)

# Slicing
print(s[0:5])   # Hello
print(s[7:])    # World!
print(s[:5])    # Hello
print(s[::2])   # Hlo ol! (every 2nd character)
print(s[::-1])  # !dlroW ,olleH (reversed)

# String methods
print(s.lower())        # hello, world!
print(s.upper())        # HELLO, WORLD!
print(s.title())        # Hello, World!
print(s.strip())        # Remove whitespace
print(s.replace("World", "Python"))  # Hello, Python!
print(s.split(", "))    # ['Hello', 'World!']
print("-".join(["a", "b", "c"]))  # a-b-c

# String checking
print(s.startswith("Hello"))  # True
print(s.endswith("!"))        # True
print("World" in s)           # True
print(s.isalpha())            # False (contains comma and space)
print("hello".isalpha())      # True
print("123".isdigit())        # True
```

### Boolean (bool)

Represents True or False values.

```python
is_active = True
is_deleted = False

print(type(is_active))  # <class 'bool'>

# Booleans are also integers
print(True + True)   # 2
print(True * 10)     # 10
print(int(True))     # 1
print(int(False))    # 0

# Truthy and Falsy values
# Falsy values: None, False, 0, 0.0, "", [], {}, set()
# Everything else is truthy

print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("hello")) # True
print(bool([]))      # False
print(bool([1, 2]))  # True
```

### None Type

Represents the absence of a value.

```python
result = None

print(type(result))  # <class 'NoneType'>
print(result is None)  # True

# Common use: default function return
def greet(name):
    print(f"Hello, {name}")
    # No explicit return, so returns None

value = greet("Alice")
print(value)  # None
```

---

## Operators

### Arithmetic Operators

```python
a, b = 10, 3

print(a + b)   # 13  - Addition
print(a - b)   # 7   - Subtraction
print(a * b)   # 30  - Multiplication
print(a / b)   # 3.333... - Division (float)
print(a // b)  # 3   - Floor division
print(a % b)   # 1   - Modulo (remainder)
print(a ** b)  # 1000 - Exponentiation

# Operator precedence (PEMDAS)
result = 2 + 3 * 4    # 14 (not 20)
result = (2 + 3) * 4  # 20
```

### Comparison Operators

```python
a, b = 10, 5

print(a == b)  # False - Equal to
print(a != b)  # True  - Not equal to
print(a > b)   # True  - Greater than
print(a < b)   # False - Less than
print(a >= b)  # True  - Greater than or equal to
print(a <= b)  # False - Less than or equal to

# Chained comparisons
x = 5
print(1 < x < 10)  # True
print(1 < x and x < 10)  # Equivalent

# Comparing strings (lexicographic)
print("apple" < "banana")  # True
print("Apple" < "apple")   # True (uppercase < lowercase)
```

### Logical Operators

```python
a, b = True, False

print(a and b)  # False - Both must be True
print(a or b)   # True  - At least one must be True
print(not a)    # False - Negation

# Short-circuit evaluation
# 'and' stops at first False
# 'or' stops at first True

x = 5
print(x > 0 and x < 10)  # True
print(x < 0 or x > 3)    # True

# Practical use
name = ""
default_name = name or "Anonymous"
print(default_name)  # Anonymous
```

### Bitwise Operators

```python
a, b = 5, 3  # Binary: 5 = 101, 3 = 011

print(a & b)   # 1   - AND (001)
print(a | b)   # 7   - OR (111)
print(a ^ b)   # 6   - XOR (110)
print(~a)      # -6  - NOT (inverts all bits)
print(a << 1)  # 10  - Left shift (1010)
print(a >> 1)  # 2   - Right shift (10)

# Practical uses
# Check if number is even
print(10 & 1 == 0)  # True (even)
print(7 & 1 == 0)   # False (odd)

# Multiply/divide by 2
print(5 << 1)  # 10 (5 * 2)
print(10 >> 1) # 5 (10 / 2)
```

### Assignment Operators

```python
x = 10

x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0
x //= 2  # x = x // 2 → 3.0
x %= 2   # x = x % 2  → 1.0
x **= 3  # x = x ** 3 → 1.0

# Walrus operator (Python 3.8+)
# Assigns and returns value in one expression
if (n := len("hello")) > 3:
    print(f"String has {n} characters")
```

### Identity Operators

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# 'is' checks if same object in memory
print(a is c)      # True (same object)
print(a is b)      # False (different objects)
print(a is not b)  # True

# 'is' vs '=='
print(a == b)  # True (same values)
print(a is b)  # False (different objects)

# Use 'is' for None checks
x = None
print(x is None)      # True (preferred)
print(x == None)      # True (works but not preferred)
```

### Membership Operators

```python
# 'in' and 'not in'
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Works with strings too
text = "Hello, World!"
print("World" in text)  # True
print("world" in text)  # False (case-sensitive)

# Works with dictionaries (checks keys)
person = {"name": "Alice", "age": 25}
print("name" in person)   # True
print("Alice" in person)  # False (checks keys, not values)
print("Alice" in person.values())  # True
```

---

## Input and Output

### Output with print()

```python
# Basic print
print("Hello, World!")

# Multiple arguments
print("Hello", "World", "!")  # Hello World !

# Custom separator
print("a", "b", "c", sep="-")  # a-b-c

# Custom end character
print("Hello", end=" ")
print("World")  # Hello World (on same line)

# Printing variables
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Formatted output
print(f"Name: {name}, Age: {age}")

# Format specifiers
pi = 3.14159265359
print(f"Pi: {pi:.2f}")          # Pi: 3.14
print(f"Pi: {pi:10.2f}")        # Pi:       3.14 (padded)
print(f"Number: {42:05d}")      # Number: 00042 (zero-padded)
print(f"Percent: {0.75:.1%}")   # Percent: 75.0%
print(f"Binary: {10:b}")        # Binary: 1010
print(f"Hex: {255:x}")          # Hex: ff
```

### Input with input()

```python
# Basic input (always returns string)
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Converting input
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# Multiple inputs on one line
x, y = input("Enter two numbers: ").split()
x, y = int(x), int(y)

# Or using map
x, y = map(int, input("Enter two numbers: ").split())

# List of integers
numbers = list(map(int, input("Enter numbers: ").split()))
```

---

## Comments and Documentation

### Single-line Comments

```python
# This is a single-line comment
x = 5  # This is an inline comment
```

### Multi-line Comments

```python
# Python doesn't have true multi-line comments
# Just use multiple single-line comments

"""
This is often used as a multi-line comment,
but it's actually a string that's not assigned
to any variable (docstring syntax).
"""
```

### Docstrings

```python
def greet(name):
    """
    Greets a person by name.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"

# Access docstring
print(greet.__doc__)

# Using help()
help(greet)
```

---

## Type Conversion

### Implicit Conversion (Coercion)

```python
# Python automatically converts types when safe
x = 5       # int
y = 2.5     # float
z = x + y   # z is float (7.5)

print(type(z))  # <class 'float'>
```

### Explicit Conversion (Casting)

```python
# int() - Convert to integer
print(int(3.7))      # 3 (truncates)
print(int("42"))     # 42
print(int(True))     # 1
print(int("42", 16)) # 66 (hex to decimal)

# float() - Convert to float
print(float(42))     # 42.0
print(float("3.14")) # 3.14
print(float("inf"))  # inf

# str() - Convert to string
print(str(42))       # "42"
print(str(3.14))     # "3.14"
print(str(True))     # "True"

# bool() - Convert to boolean
print(bool(0))       # False
print(bool(42))      # True
print(bool(""))      # False
print(bool("hello")) # True

# list() - Convert to list
print(list("hello"))     # ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))   # [1, 2, 3]
print(list({1, 2, 3}))   # [1, 2, 3]

# tuple() - Convert to tuple
print(tuple([1, 2, 3]))  # (1, 2, 3)

# set() - Convert to set
print(set([1, 2, 2, 3])) # {1, 2, 3}

# dict() - Convert to dictionary
print(dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2}
```

### Type Checking

```python
x = 42

# Using type()
print(type(x))           # <class 'int'>
print(type(x) == int)    # True

# Using isinstance() (preferred)
print(isinstance(x, int))           # True
print(isinstance(x, (int, float)))  # True (check multiple types)

# Check if numeric
from numbers import Number
print(isinstance(42, Number))    # True
print(isinstance(3.14, Number))  # True
```

---

## Practice Exercises

### Exercise 1: Variable Swap
```python
# Swap two variables without using a third variable
a = 5
b = 10

# Solution
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 10, b = 5
```

### Exercise 2: Temperature Converter
```python
# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### Exercise 3: Calculate Circle Area
```python
import math

radius = float(input("Enter circle radius: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
```

### Exercise 4: String Manipulation
```python
text = input("Enter a sentence: ")

print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Word count: {len(text.split())}")
print(f"Reversed: {text[::-1]}")
```

---

## Summary

- Variables store data and are dynamically typed in Python
- Python has several built-in data types: int, float, str, bool, None, and more
- Operators allow you to perform operations on values
- Input/output is handled with `input()` and `print()`
- Comments document code; docstrings document functions/classes
- Type conversion can be implicit or explicit

## Next Steps

Continue to [Control Flow](03-control-flow.md) to learn about conditional statements and loops.
