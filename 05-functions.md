# Functions

Functions are reusable blocks of code that perform specific tasks. They help organize code, improve readability, and reduce repetition.

---

## Defining Functions

### Basic Function Definition

```python
def greet():
    """A simple greeting function."""
    print("Hello, World!")

# Calling the function
greet()  # Hello, World!
```

### Functions with Parameters

```python
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!
```

### Functions with Return Values

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add(3, 5)
print(result)  # 8

# Multiple return values (returns a tuple)
def get_min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9
```

### Return vs Print

```python
# print() displays output, returns None
def print_sum(a, b):
    print(a + b)

result = print_sum(3, 5)  # Prints: 8
print(result)             # None

# return gives back a value to the caller
def return_sum(a, b):
    return a + b

result = return_sum(3, 5)
print(result)  # 8
```

---

## Arguments and Parameters

### Positional Arguments

Arguments are matched to parameters by position.

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe_person("Alice", 25, "New York")
# Alice is 25 years old and lives in New York
```

### Keyword Arguments

Arguments are matched by parameter name.

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

# Using keyword arguments (order doesn't matter)
describe_person(age=25, city="New York", name="Alice")

# Mixing positional and keyword (positional must come first)
describe_person("Alice", city="New York", age=25)
```

### Default Parameter Values

```python
def greet(name, greeting="Hello"):
    """Greet with a customizable greeting."""
    print(f"{greeting}, {name}!")

greet("Alice")                  # Hello, Alice!
greet("Bob", "Hi")              # Hi, Bob!
greet("Charlie", greeting="Hey")  # Hey, Charlie!
```

### Important: Mutable Default Arguments

```python
# WRONG - mutable default is shared between calls
def add_item_wrong(item, items=[]):
    items.append(item)
    return items

print(add_item_wrong("a"))  # ['a']
print(add_item_wrong("b"))  # ['a', 'b']  - Unexpected!

# CORRECT - use None and create new list
def add_item_correct(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_correct("a"))  # ['a']
print(add_item_correct("b"))  # ['b']
```

---

## *args and **kwargs

### *args - Variable Positional Arguments

Collects extra positional arguments into a tuple.

```python
def sum_all(*args):
    """Sum any number of arguments."""
    print(f"args: {args}")  # args is a tuple
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# With regular parameters
def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### **kwargs - Variable Keyword Arguments

Collects extra keyword arguments into a dictionary.

```python
def print_info(**kwargs):
    """Print key-value pairs."""
    print(f"kwargs: {kwargs}")  # kwargs is a dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# kwargs: {'name': 'Alice', 'age': 25, 'city': 'NYC'}
# name: Alice
# age: 25
# city: NYC
```

### Combining *args and **kwargs

```python
def flexible_function(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=25)
# Positional: (1, 2, 3)
# Keyword: {'name': 'Alice', 'age': 25}

# Order matters: regular params, *args, keyword-only, **kwargs
def full_example(a, b, *args, option=True, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"option={option}")
    print(f"kwargs={kwargs}")

full_example(1, 2, 3, 4, option=False, x=10, y=20)
```

### Unpacking Arguments

```python
# Unpack list/tuple with *
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # 6

# Unpack dictionary with **
def greet(name, greeting):
    print(f"{greeting}, {name}!")

data = {"name": "Alice", "greeting": "Hello"}
greet(**data)  # Hello, Alice!
```

---

## Lambda Functions

Anonymous functions defined with the `lambda` keyword.

### Basic Syntax

```python
# Regular function
def add(a, b):
    return a + b

# Equivalent lambda
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Single argument
square = lambda x: x ** 2
print(square(5))  # 25

# No arguments
get_pi = lambda: 3.14159
print(get_pi())  # 3.14159
```

### Common Use Cases

```python
# Sorting with custom key
points = [(1, 2), (3, 1), (2, 4)]
sorted_points = sorted(points, key=lambda p: p[1])
print(sorted_points)  # [(3, 1), (1, 2), (2, 4)]

# Sort by multiple criteria
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 90, "age": 19},
    {"name": "Charlie", "grade": 85, "age": 21}
]
# Sort by grade (descending), then by age (ascending)
sorted_students = sorted(students, key=lambda s: (-s["grade"], s["age"]))

# Filtering with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Transforming with map()
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Reducing with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)  # 120
```

### When to Use Lambdas

- **Use lambdas**: Simple, one-line expressions passed to functions like `sorted`, `map`, `filter`
- **Avoid lambdas**: Complex logic, multiple statements, need for documentation

```python
# Good use of lambda
sorted_words = sorted(words, key=lambda w: len(w))

# Better as regular function (complex logic)
def calculate_score(student):
    """Calculate weighted score with bonus."""
    base = student["grade"]
    bonus = 5 if student["extra_credit"] else 0
    return base + bonus

sorted_students = sorted(students, key=calculate_score)
```

---

## Scope and Namespaces

### Local vs Global Scope

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can read global
    print(local_var)

my_function()
# print(local_var)  # Error: local_var not defined outside function
```

### The global Keyword

```python
counter = 0

def increment():
    global counter  # Declare we're using global variable
    counter += 1

increment()
increment()
print(counter)  # 2
```

### The nonlocal Keyword

```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # Refer to enclosing scope
        count += 1
        return count
    
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### LEGB Rule

Python searches for names in this order:
1. **L**ocal - Inside the current function
2. **E**nclosing - In enclosing functions (for nested functions)
3. **G**lobal - At the module level
4. **B**uilt-in - Python's built-in names

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # local
    
    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

---

## Decorators

Decorators modify or enhance functions without changing their code.

### Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before function call
# Hello!
# After function call
```

### Decorators with Arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))
# Calling add
# Finished add
# 8
```

### Preserving Function Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet a person."""
    print(f"Hello, {name}!")

print(greet.__name__)  # greet (not 'wrapper')
print(greet.__doc__)   # Greet a person.
```

### Practical Decorator Examples

#### Timer Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()  # slow_function took 1.0012 seconds
```

#### Debug Decorator

```python
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(3, 5)
# Calling add(3, 5)
# add returned 8
```

#### Retry Decorator

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"
```

#### Cache Decorator

```python
from functools import wraps

def cache(func):
    """Simple memoization decorator."""
    memo = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Instant! (without cache would be very slow)

# Python has a built-in cache decorator
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Chaining Decorators

```python
@decorator1
@decorator2
@decorator3
def my_function():
    pass

# Equivalent to:
# my_function = decorator1(decorator2(decorator3(my_function)))
```

---

## Generators

Generators are functions that yield values one at a time, saving memory.

### Creating Generators

```python
def count_up_to(n):
    """Generate numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Using the generator
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# In a loop
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5
```

### Generator vs List

```python
# List - stores all values in memory
def get_squares_list(n):
    return [x ** 2 for x in range(n)]

# Generator - generates values on demand
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

# Memory comparison
import sys
list_result = get_squares_list(1000000)
gen_result = get_squares_gen(1000000)

print(sys.getsizeof(list_result))  # ~8697464 bytes
print(sys.getsizeof(gen_result))   # ~112 bytes
```

### Generator Expressions

```python
# List comprehension (creates list in memory)
squares_list = [x ** 2 for x in range(1000000)]

# Generator expression (creates generator)
squares_gen = (x ** 2 for x in range(1000000))

# Using generator expressions
print(sum(x ** 2 for x in range(100)))  # 328350
print(max(x ** 2 for x in range(100)))  # 9801
```

### Practical Generator Examples

#### Reading Large Files

```python
def read_large_file(file_path):
    """Read file line by line without loading entire file."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Process each line without loading entire file
for line in read_large_file('huge_file.txt'):
    process(line)
```

#### Infinite Generator

```python
def infinite_counter(start=0):
    """Generate numbers infinitely."""
    n = start
    while True:
        yield n
        n += 1

# Use with caution - need to break out
counter = infinite_counter()
for i, num in enumerate(counter):
    print(num)
    if i >= 9:
        break
```

#### Generator Pipeline

```python
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    for line in lines:
        if not line.startswith('#'):
            yield line

def parse_csv(lines):
    for line in lines:
        yield line.split(',')

# Pipeline
data = parse_csv(filter_comments(read_lines('data.csv')))
for row in data:
    print(row)
```

### yield from

```python
def chain(*iterables):
    """Yield from multiple iterables."""
    for iterable in iterables:
        yield from iterable

# Usage
result = list(chain([1, 2], [3, 4], [5, 6]))
print(result)  # [1, 2, 3, 4, 5, 6]

# Flattening nested structures
def flatten(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Recursion

Functions that call themselves.

### Basic Recursion

```python
def factorial(n):
    """Calculate n! using recursion."""
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # 120 (5 * 4 * 3 * 2 * 1)

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Recursion Limit

```python
import sys
print(sys.getrecursionlimit())  # 1000 (default)

# Can be increased (carefully!)
sys.setrecursionlimit(2000)
```

### Tail Recursion (Optimization)

Python doesn't optimize tail recursion, but you can convert to iteration:

```python
# Recursive (not tail-optimized)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Tail-recursive style
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# Iterative (recommended for Python)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

---

## Higher-Order Functions

Functions that take functions as arguments or return functions.

### map()

```python
numbers = [1, 2, 3, 4, 5]

# Apply function to each element
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# With regular function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)  # [11, 22, 33]
```

### filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter with None removes falsy values
mixed = [0, 1, '', 'hello', None, True, False, [], [1, 2]]
truthy = list(filter(None, mixed))
print(truthy)  # [1, 'hello', True, [1, 2]]
```

### reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Reduce to single value
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# With initial value
total = reduce(lambda x, y: x + y, numbers, 100)
print(total)  # 115

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

### sorted() with key

```python
# Sort with custom key function
words = ["banana", "apple", "Cherry", "date"]

# Sort by length
print(sorted(words, key=len))
# ['date', 'apple', 'banana', 'Cherry']

# Sort case-insensitive
print(sorted(words, key=str.lower))
# ['apple', 'banana', 'Cherry', 'date']

# Sort by last character
print(sorted(words, key=lambda w: w[-1]))
# ['banana', 'apple', 'date', 'Cherry']

# Sort complex objects
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 90},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print([s["name"] for s in by_grade])  # ['Bob', 'Alice', 'Charlie']
```

---

## Type Hints

Type hints document expected types (not enforced at runtime).

### Basic Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_adult(age: int) -> bool:
    return age >= 18
```

### Common Types

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable

# Collections
def process_items(items: List[str]) -> List[str]:
    return [item.upper() for item in items]

def get_user(users: Dict[str, int]) -> None:
    for name, age in users.items():
        print(f"{name}: {age}")

def get_coordinates() -> Tuple[float, float]:
    return (40.7128, -74.0060)

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Union (multiple possible types)
def process(value: Union[int, str]) -> str:
    return str(value)

# Python 3.10+ uses | instead of Union
def process(value: int | str) -> str:
    return str(value)

# Callable
def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)

# Any (accepts any type)
def log(message: Any) -> None:
    print(message)
```

### Type Aliases

```python
from typing import List, Tuple

# Type aliases
Coordinates = Tuple[float, float]
PointList = List[Coordinates]

def calculate_distance(p1: Coordinates, p2: Coordinates) -> float:
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

def process_points(points: PointList) -> None:
    for point in points:
        print(point)
```

---

## Docstrings

Document functions with docstrings.

### Google Style

```python
def divide(a: float, b: float) -> float:
    """Divide two numbers.
    
    Args:
        a: The dividend.
        b: The divisor.
    
    Returns:
        The quotient of a divided by b.
    
    Raises:
        ZeroDivisionError: If b is zero.
    
    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

### NumPy Style

```python
def divide(a, b):
    """
    Divide two numbers.
    
    Parameters
    ----------
    a : float
        The dividend.
    b : float
        The divisor.
    
    Returns
    -------
    float
        The quotient of a divided by b.
    
    Raises
    ------
    ZeroDivisionError
        If b is zero.
    
    Examples
    --------
    >>> divide(10, 2)
    5.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

---

## Summary

- Functions are defined with `def` and can have parameters and return values
- Use `*args` for variable positional arguments, `**kwargs` for keyword arguments
- Lambda functions are anonymous, single-expression functions
- Decorators modify functions without changing their code
- Generators yield values one at a time, saving memory
- Higher-order functions take or return other functions
- Type hints document expected types
- Docstrings document function purpose and usage

## Next Steps

Continue to [Modules and Packages](06-modules-and-packages.md) to learn about organizing code into modules.
