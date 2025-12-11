# Control Flow

Control flow determines the order in which statements are executed in a program. Python provides several structures for controlling program flow.

---

## Conditional Statements

### The if Statement

Executes code only if a condition is true.

```python
age = 18

if age >= 18:
    print("You are an adult")
```

### The if-else Statement

Provides an alternative when the condition is false.

```python
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### The if-elif-else Statement

Checks multiple conditions in sequence.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")  # Your grade is: B
```

### Nested if Statements

```python
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```

### Conditional Expressions (Ternary Operator)

A concise way to write simple if-else statements.

```python
age = 20

# Traditional way
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator
status = "adult" if age >= 18 else "minor"

# Can be chained (use sparingly - reduces readability)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
```

### Multiple Conditions

```python
age = 25
has_license = True
is_sober = True

# Using 'and' - all conditions must be true
if age >= 18 and has_license and is_sober:
    print("You can drive")

# Using 'or' - at least one condition must be true
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Using 'not' - negates the condition
is_raining = False
if not is_raining:
    print("Let's go outside!")

# Combining operators
temperature = 25
is_sunny = True
if temperature > 20 and (is_sunny or not is_raining):
    print("Nice weather for a walk!")
```

### Checking Multiple Values

```python
day = "Monday"

# Instead of multiple 'or' conditions
if day == "Monday" or day == "Tuesday" or day == "Wednesday":
    print("Weekday")

# Use 'in' with a tuple or list
if day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("Weekday")
else:
    print("Weekend")
```

---

## Match Statement (Python 3.10+)

Pattern matching provides a powerful way to check values against patterns.

### Basic Match

```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # Wildcard pattern (default)
            return "Unknown status"

print(http_status(200))  # OK
print(http_status(999))  # Unknown status
```

### Matching Multiple Values

```python
def is_weekend(day):
    match day.lower():
        case "saturday" | "sunday":
            return True
        case _:
            return False
```

### Matching with Patterns

```python
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, 0):
            return f"On X-axis at x={x}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"

print(describe_point((0, 0)))    # Origin
print(describe_point((0, 5)))    # On Y-axis at y=5
print(describe_point((3, 4)))    # Point at (3, 4)
```

### Matching with Guards

```python
def classify_number(num):
    match num:
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"
        case n if n > 0 and n <= 10:
            return "Small positive"
        case n if n > 10:
            return "Large positive"

print(classify_number(-5))   # Negative
print(classify_number(5))    # Small positive
print(classify_number(100))  # Large positive
```

### Matching with Classes

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe(obj):
    match obj:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=y):
            return f"On Y-axis at {y}"
        case Point(x=x, y=0):
            return f"On X-axis at {x}"
        case Point():
            return f"Point at ({obj.x}, {obj.y})"
        case _:
            return "Not a point"
```

---

## Loops

### The for Loop

Iterates over a sequence (list, tuple, string, range, etc.).

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)

# Iterating over a dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Keys only
for key in person:
    print(key)

# Keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Values only
for value in person.values():
    print(value)
```

### The range() Function

Generates a sequence of numbers.

```python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - start to stop-1
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Counting backwards
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1

# Using range with len for index access
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")
```

### The enumerate() Function

Gets both index and value while iterating.

```python
fruits = ["apple", "banana", "cherry"]

# Without enumerate
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (preferred)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output: 1: apple, 2: banana, 3: cherry
```

### The zip() Function

Iterates over multiple sequences simultaneously.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# Zip two lists
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Zip three lists
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# Zip stops at shortest sequence
nums1 = [1, 2, 3, 4, 5]
nums2 = [10, 20, 30]
for a, b in zip(nums1, nums2):
    print(a, b)  # Only 3 iterations

# Use zip_longest for padding
from itertools import zip_longest
for a, b in zip_longest(nums1, nums2, fillvalue=0):
    print(a, b)  # 5 iterations, missing values become 0
```

### The while Loop

Executes as long as a condition is true.

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# User input validation
while True:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        break
    print("Invalid input, try again.")

# Countdown
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast off!")
```

### Infinite Loops

```python
# Be careful with while True
while True:
    command = input("Enter command (quit to exit): ")
    if command == "quit":
        break
    print(f"You entered: {command}")
```

---

## Loop Control Statements

### break

Exits the loop immediately.

```python
# Find first even number
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

# Breaking out of nested loops with a flag
found = False
for i in range(5):
    for j in range(5):
        if i * j == 6:
            print(f"Found: {i} * {j} = 6")
            found = True
            break
    if found:
        break
```

### continue

Skips the rest of the current iteration.

```python
# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# Skip invalid data
data = [1, 2, None, 4, None, 6]
for item in data:
    if item is None:
        continue
    print(f"Processing: {item}")
```

### pass

Does nothing - placeholder for future code.

```python
# Empty function placeholder
def my_function():
    pass  # TODO: implement later

# Empty loop (useful in development)
for i in range(10):
    pass  # Will implement later

# Empty class
class MyClass:
    pass

# Conditional placeholder
x = 10
if x > 5:
    pass  # TODO: handle this case
else:
    print("x is small")
```

### else with Loops

The `else` block executes when the loop completes normally (no break).

```python
# else with for loop
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

# else with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print because of break")

# Practical use: checking if item found
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found")

find_item([1, 2, 3, 4, 5], 3)  # Found 3
find_item([1, 2, 3, 4, 5], 9)  # 9 not found

# else with while loop
n = 5
while n > 0:
    print(n)
    n -= 1
else:
    print("Countdown complete!")
```

---

## Nested Loops

```python
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()  # New line after each row

# Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25

# Pattern printing
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****

# Triangle pattern
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
#     *
#    ***
#   *****
#  *******
# *********

# Processing 2D data
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()
```

---

## Iteration Tools

### Iterating with Index and Value

```python
colors = ["red", "green", "blue"]

# Using enumerate
for i, color in enumerate(colors):
    print(f"{i}: {color}")
```

### Iterating in Reverse

```python
# Reverse a list
for item in reversed([1, 2, 3, 4, 5]):
    print(item)

# Reverse with range
for i in range(5, 0, -1):
    print(i)
```

### Iterating Over Sorted Data

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sorted iteration
for num in sorted(numbers):
    print(num)  # 1, 1, 2, 3, 4, 5, 6, 9

# Reverse sorted
for num in sorted(numbers, reverse=True):
    print(num)  # 9, 6, 5, 4, 3, 2, 1, 1

# Sort by custom key
words = ["banana", "apple", "cherry", "date"]
for word in sorted(words, key=len):
    print(word)  # date, apple, banana, cherry
```

### Iterating Over Unique Values

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Using set (loses order)
for num in set(numbers):
    print(num)

# Preserving order (Python 3.7+)
from dict import fromkeys
for num in dict.fromkeys(numbers):
    print(num)  # 1, 2, 3, 4
```

---

## Practical Examples

### Example 1: FizzBuzz

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Example 2: Prime Number Checker

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find primes up to 50
for num in range(2, 51):
    if is_prime(num):
        print(num, end=" ")
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

### Example 3: Guess the Number Game

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number between 1 and 100!")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
    attempts += 1
    
    if guess == secret:
        print(f"Congratulations! You got it in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Game over! The number was {secret}")
```

### Example 4: Menu System

```python
def show_menu():
    print("\n=== Main Menu ===")
    print("1. View items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

items = []

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            if items:
                for i, item in enumerate(items, 1):
                    print(f"{i}. {item}")
            else:
                print("No items yet.")
        case "2":
            item = input("Enter item name: ")
            items.append(item)
            print(f"Added: {item}")
        case "3":
            if items:
                item = input("Enter item to remove: ")
                if item in items:
                    items.remove(item)
                    print(f"Removed: {item}")
                else:
                    print("Item not found.")
            else:
                print("No items to remove.")
        case "4":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice.")
```

### Example 5: Password Validator

```python
def validate_password(password):
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")
    
    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")
    
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain a digit")
    
    if not any(c in "!@#$%^&*" for c in password):
        errors.append("Password must contain a special character (!@#$%^&*)")
    
    return errors

while True:
    password = input("Enter a password: ")
    errors = validate_password(password)
    
    if errors:
        print("Password is invalid:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Password is valid!")
        break
```

---

## Summary

- **Conditional statements** (`if`, `elif`, `else`) control which code blocks execute
- **Match statement** (Python 3.10+) provides powerful pattern matching
- **for loops** iterate over sequences
- **while loops** repeat while a condition is true
- **break** exits a loop, **continue** skips to the next iteration
- **pass** is a placeholder that does nothing
- **else with loops** executes when a loop completes without breaking
- Use `enumerate()` for index-value pairs, `zip()` for parallel iteration

## Next Steps

Continue to [Data Structures](04-data-structures.md) to learn about Python's built-in data structures.
