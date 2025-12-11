# Advanced Topics

This chapter covers advanced Python concepts that will help you write more sophisticated and efficient code.

---

## Iterators and Iterables

### Understanding Iteration

```python
# An iterable is anything you can loop over
# An iterator is an object that yields values one at a time

# Lists, strings, dicts are iterables
for item in [1, 2, 3]:
    print(item)

# Get iterator from iterable
my_list = [1, 2, 3]
my_iter = iter(my_list)

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
# print(next(my_iter))  # StopIteration
```

### Creating Custom Iterators

```python
class CountDown:
    """Iterator that counts down from n to 0."""
    
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

# Usage
for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1, 0

# Creating iterator using __iter__ that returns new iterator
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        # Return a new iterator each time
        return NumberRangeIterator(self.start, self.end)

class NumberRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Can iterate multiple times
nums = NumberRange(1, 4)
print(list(nums))  # [1, 2, 3]
print(list(nums))  # [1, 2, 3]
```

### The itertools Module

```python
import itertools

# Infinite iterators
count = itertools.count(10, 2)  # 10, 12, 14, 16, ...
cycle = itertools.cycle('ABC')  # A, B, C, A, B, C, ...
repeat = itertools.repeat('X', 3)  # X, X, X

# Terminating iterators
# chain - combine iterables
combined = itertools.chain([1, 2], [3, 4], [5])
print(list(combined))  # [1, 2, 3, 4, 5]

# islice - slice an iterator
sliced = itertools.islice(range(100), 5, 10)
print(list(sliced))  # [5, 6, 7, 8, 9]

# takewhile / dropwhile
nums = [1, 3, 5, 7, 4, 6, 8]
taken = itertools.takewhile(lambda x: x < 6, nums)
print(list(taken))  # [1, 3, 5]

dropped = itertools.dropwhile(lambda x: x < 6, nums)
print(list(dropped))  # [7, 4, 6, 8]

# groupby
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('a', 5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3), ('b', 4)]
# a [('a', 5)]

# Combinatoric iterators
# permutations
print(list(itertools.permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations
print(list(itertools.combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# product (Cartesian product)
print(list(itertools.product('AB', '12')))
# [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
```

---

## Context Managers

### Using Context Managers

```python
# Built-in context managers
with open('file.txt', 'r') as f:
    content = f.read()
# File is automatically closed

# Multiple context managers
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read())
```

### Creating Context Managers (Class-based)

```python
class Timer:
    """Context manager for timing code blocks."""
    
    def __init__(self, name="Timer"):
        self.name = name
    
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"{self.name}: {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

# Usage
with Timer("Processing"):
    # Some code
    sum(range(1000000))
# Processing: 0.0234 seconds
```

### Creating Context Managers (contextlib)

```python
from contextlib import contextmanager

@contextmanager
def timer(name="Timer"):
    import time
    start = time.time()
    try:
        yield  # Code in 'with' block runs here
    finally:
        elapsed = time.time() - start
        print(f"{name}: {elapsed:.4f} seconds")

# Usage
with timer("My operation"):
    sum(range(1000000))

# Context manager that yields a value
@contextmanager
def managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with managed_file('test.txt', 'w') as f:
    f.write('Hello!')
```

### Useful contextlib Tools

```python
from contextlib import suppress, redirect_stdout, ExitStack
import io

# suppress - ignore specific exceptions
with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')
# No error raised

# redirect_stdout - capture print output
f = io.StringIO()
with redirect_stdout(f):
    print("This is captured")
output = f.getvalue()
print(f"Captured: {output}")

# ExitStack - dynamic context manager
with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in filenames]
    # All files closed when exiting
```

---

## Regular Expressions

### Basic Patterns

```python
import re

text = "The quick brown fox jumps over the lazy dog"

# Search for pattern
match = re.search(r'quick', text)
if match:
    print(f"Found: {match.group()}")  # quick
    print(f"Position: {match.start()}-{match.end()}")  # 4-9

# Find all matches
text = "cat bat rat hat mat"
matches = re.findall(r'[cbr]at', text)
print(matches)  # ['cat', 'bat', 'rat']

# Replace
new_text = re.sub(r'[cbr]at', 'X', text)
print(new_text)  # X X X hat mat
```

### Pattern Syntax

```python
import re

# Metacharacters
# .   - Any character except newline
# ^   - Start of string
# $   - End of string
# *   - 0 or more repetitions
# +   - 1 or more repetitions
# ?   - 0 or 1 repetition
# []  - Character class
# |   - Alternation (or)
# ()  - Grouping

# Character classes
r'\d'  # Digit [0-9]
r'\D'  # Non-digit
r'\w'  # Word character [a-zA-Z0-9_]
r'\W'  # Non-word character
r'\s'  # Whitespace
r'\S'  # Non-whitespace
r'\b'  # Word boundary

# Quantifiers
r'a*'      # 0 or more 'a'
r'a+'      # 1 or more 'a'
r'a?'      # 0 or 1 'a'
r'a{3}'    # Exactly 3 'a'
r'a{2,4}'  # 2 to 4 'a'
r'a{2,}'   # 2 or more 'a'

# Examples
email_pattern = r'[\w.-]+@[\w.-]+'
phone_pattern = r'\d{3}-\d{3}-\d{4}'
url_pattern = r'https?://[\w./]+'
```

### Groups and Capturing

```python
import re

text = "John: 30, Jane: 25, Bob: 35"

# Groups
pattern = r'(\w+): (\d+)'
for match in re.finditer(pattern, text):
    name = match.group(1)
    age = match.group(2)
    print(f"{name} is {age} years old")

# Named groups
pattern = r'(?P<name>\w+): (?P<age>\d+)'
for match in re.finditer(pattern, text):
    print(match.group('name'), match.group('age'))
    print(match.groupdict())  # {'name': 'John', 'age': '30'}

# Non-capturing groups
pattern = r'(?:Mr|Ms|Dr)\. (\w+)'
match = re.search(pattern, "Dr. Smith")
print(match.group(1))  # Smith (not Dr.)
```

### Compiled Patterns

```python
import re

# Compile for reuse
email_regex = re.compile(r'''
    [\w.-]+     # Username
    @           # @ symbol
    [\w.-]+     # Domain
    \.          # Dot
    [a-z]{2,}   # TLD
''', re.VERBOSE | re.IGNORECASE)

emails = email_regex.findall("Contact: john@example.com, jane@test.org")
print(emails)  # ['john@example.com', 'jane@test.org']

# Flags
re.IGNORECASE  # Case-insensitive
re.MULTILINE   # ^ and $ match line starts/ends
re.DOTALL      # . matches newline
re.VERBOSE     # Allow whitespace and comments
```

---

## Multithreading

### Basic Threading

```python
import threading
import time

def worker(name, seconds):
    print(f"{name} starting")
    time.sleep(seconds)
    print(f"{name} finished")

# Create and start threads
thread1 = threading.Thread(target=worker, args=("Thread-1", 2))
thread2 = threading.Thread(target=worker, args=("Thread-2", 3))

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads finished")
```

### Thread Synchronization

```python
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        with self.lock:  # Thread-safe
            self.value += 1

counter = Counter()

def worker():
    for _ in range(10000):
        counter.increment()

threads = [threading.Thread(target=worker) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter.value)  # 100000 (correctly synchronized)
```

### Thread Pool

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process_item(item):
    time.sleep(1)
    return item * 2

items = [1, 2, 3, 4, 5]

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # map - preserves order
    results = list(executor.map(process_item, items))
    print(results)  # [2, 4, 6, 8, 10]
    
    # submit - returns futures
    futures = [executor.submit(process_item, item) for item in items]
    for future in futures:
        print(future.result())
```

---

## Multiprocessing

### Basic Multiprocessing

```python
from multiprocessing import Process
import os

def worker(name):
    print(f"{name} running in process {os.getpid()}")

if __name__ == '__main__':
    processes = []
    for i in range(4):
        p = Process(target=worker, args=(f"Worker-{i}",))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
```

### Process Pool

```python
from multiprocessing import Pool
import time

def cpu_intensive(n):
    """Simulate CPU-intensive work."""
    return sum(i * i for i in range(n))

if __name__ == '__main__':
    numbers = [10**6, 10**6, 10**6, 10**6]
    
    # Sequential
    start = time.time()
    results = [cpu_intensive(n) for n in numbers]
    print(f"Sequential: {time.time() - start:.2f}s")
    
    # Parallel
    start = time.time()
    with Pool(4) as pool:
        results = pool.map(cpu_intensive, numbers)
    print(f"Parallel: {time.time() - start:.2f}s")
```

### Sharing Data Between Processes

```python
from multiprocessing import Process, Value, Array, Manager

# Shared Value and Array
def increment_value(shared_val, shared_arr):
    shared_val.value += 1
    for i in range(len(shared_arr)):
        shared_arr[i] += 1

if __name__ == '__main__':
    val = Value('i', 0)  # Shared integer
    arr = Array('i', [0, 0, 0])  # Shared array
    
    p = Process(target=increment_value, args=(val, arr))
    p.start()
    p.join()
    
    print(val.value)  # 1
    print(list(arr))  # [1, 1, 1]

# Using Manager for complex objects
def worker(shared_dict, shared_list):
    shared_dict['key'] = 'value'
    shared_list.append(42)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list()
        
        p = Process(target=worker, args=(d, l))
        p.start()
        p.join()
        
        print(dict(d))  # {'key': 'value'}
        print(list(l))  # [42]
```

---

## Async/Await (Asyncio)

### Basic Async Programming

```python
import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    # Sequential
    await say_hello("Alice", 1)
    await say_hello("Bob", 1)
    # Total: ~2 seconds

# Run async function
asyncio.run(main())

async def main_concurrent():
    # Concurrent
    await asyncio.gather(
        say_hello("Alice", 1),
        say_hello("Bob", 1)
    )
    # Total: ~1 second

asyncio.run(main_concurrent())
```

### Tasks and Gathering Results

```python
import asyncio

async def fetch_data(url, delay):
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def main():
    # Create tasks
    task1 = asyncio.create_task(fetch_data("url1", 2))
    task2 = asyncio.create_task(fetch_data("url2", 1))
    task3 = asyncio.create_task(fetch_data("url3", 3))
    
    # Wait for all
    results = await asyncio.gather(task1, task2, task3)
    print(results)
    
    # Or with timeout
    try:
        results = await asyncio.wait_for(
            asyncio.gather(task1, task2, task3),
            timeout=2.5
        )
    except asyncio.TimeoutError:
        print("Timeout!")

asyncio.run(main())
```

### Async Context Managers and Iterators

```python
import asyncio

# Async context manager
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(0.5)
        return False

async def main():
    async with AsyncResource() as resource:
        print("Using resource")

# Async iterator
class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.count >= self.limit:
            raise StopAsyncIteration
        self.count += 1
        await asyncio.sleep(0.1)
        return self.count

async def main():
    async for num in AsyncCounter(5):
        print(num)

asyncio.run(main())
```

### Async HTTP Requests (aiohttp)

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        "https://api.github.com",
        "https://api.github.com/users",
        "https://api.github.com/repos"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        for url, result in zip(urls, results):
            print(f"{url}: {len(result)} bytes")

# asyncio.run(main())
```

---

## Descriptors

### Understanding Descriptors

```python
class Validator:
    """Descriptor for validating attribute values."""
    
    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)
    
    def validate(self, value):
        pass  # Override in subclasses

class PositiveNumber(Validator):
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'{self.name} must be a number')
        if value <= 0:
            raise ValueError(f'{self.name} must be positive')

class NonEmptyString(Validator):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'{self.name} must be a string')
        if not value.strip():
            raise ValueError(f'{self.name} cannot be empty')

# Usage
class Product:
    name = NonEmptyString()
    price = PositiveNumber()
    quantity = PositiveNumber()
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product = Product("Widget", 9.99, 100)
print(product.name)   # Widget
print(product.price)  # 9.99

# Validation
# product.price = -5  # ValueError: price must be positive
```

---

## Metaclasses

### Understanding Metaclasses

```python
# Classes are objects created by metaclasses
# type is the default metaclass

class MyClass:
    pass

# Equivalent to:
MyClass = type('MyClass', (), {})

print(type(MyClass))  # <class 'type'>
print(type(type))     # <class 'type'>
```

### Creating Custom Metaclasses

```python
class SingletonMeta(type):
    """Metaclass that makes classes singletons."""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "connected"

# Usage
db1 = Database()
db2 = Database()
print(db1 is db2)  # True (same instance)
```

### Practical Metaclass Example

```python
class AutoReprMeta(type):
    """Metaclass that auto-generates __repr__ for classes."""
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Get __init__ parameters
        import inspect
        if '__init__' in namespace:
            sig = inspect.signature(namespace['__init__'])
            params = [p for p in sig.parameters.keys() if p != 'self']
            
            def __repr__(self):
                attrs = ', '.join(f'{p}={getattr(self, p)!r}' for p in params)
                return f'{name}({attrs})'
            
            cls.__repr__ = __repr__
        
        return cls

class Person(metaclass=AutoReprMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person)  # Person(name='Alice', age=25)
```

---

## Slots

### Using __slots__

```python
# Without __slots__ - uses __dict__
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# With __slots__ - no __dict__, less memory
class SlottedClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison
import sys

regular = RegularClass(1, 2)
slotted = SlottedClass(1, 2)

print(sys.getsizeof(regular.__dict__))  # 104 bytes
# print(slotted.__dict__)  # AttributeError - no __dict__

# Can't add new attributes with __slots__
regular.z = 3  # Works
# slotted.z = 3  # AttributeError
```

### Slots with Inheritance

```python
class Base:
    __slots__ = ['x']

class Derived(Base):
    __slots__ = ['y']  # Add more slots
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = Derived(1, 2)
print(obj.x, obj.y)  # 1 2
```

---

## Weak References

```python
import weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"{self.name} being deleted")

# Strong reference
obj = MyClass("Strong")
# obj is kept alive

# Weak reference
obj = MyClass("Weak")
weak_ref = weakref.ref(obj)

print(weak_ref())  # <MyClass object>
del obj
print(weak_ref())  # None (object was deleted)

# Weak reference with callback
def callback(ref):
    print(f"Object was garbage collected")

obj = MyClass("Callback")
weak_ref = weakref.ref(obj, callback)
del obj  # "Callback being deleted" then "Object was garbage collected"

# WeakValueDictionary
cache = weakref.WeakValueDictionary()
obj = MyClass("Cached")
cache['key'] = obj
print('key' in cache)  # True
del obj
print('key' in cache)  # False (auto-removed when obj deleted)
```

---

## Memory Management

### Understanding Memory

```python
import sys

# Object size
x = 42
print(sys.getsizeof(x))  # 28 bytes

lst = [1, 2, 3, 4, 5]
print(sys.getsizeof(lst))  # 96 bytes (list overhead, not element sizes)

# Reference counting
x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 (x + function argument)

y = x
print(sys.getrefcount(x))  # 3

# Garbage collection
import gc

# Force garbage collection
gc.collect()

# Get garbage collection stats
print(gc.get_stats())

# Disable/enable GC (use carefully)
gc.disable()
gc.enable()
```

### Memory Profiling

```python
# Using memory_profiler (pip install memory_profiler)
# @profile
def my_function():
    big_list = [x ** 2 for x in range(1000000)]
    return sum(big_list)

# Run with: python -m memory_profiler script.py

# Using tracemalloc
import tracemalloc

tracemalloc.start()

# Your code here
data = [x ** 2 for x in range(100000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 1024:.2f} KB")
print(f"Peak memory: {peak / 1024:.2f} KB")

tracemalloc.stop()
```

---

## Summary

- **Iterators** yield values one at a time; use `__iter__` and `__next__`
- **Context managers** handle setup/cleanup with `__enter__` and `__exit__`
- **Regular expressions** provide powerful pattern matching
- **Threading** is good for I/O-bound tasks
- **Multiprocessing** bypasses GIL for CPU-bound tasks
- **Asyncio** enables efficient concurrent I/O operations
- **Descriptors** customize attribute access
- **Metaclasses** customize class creation
- **Slots** reduce memory usage for many instances
- **Weak references** allow garbage collection of referenced objects

## Next Steps

Continue to [Working with Data](11-working-with-data.md) to learn about data manipulation with NumPy and Pandas.
