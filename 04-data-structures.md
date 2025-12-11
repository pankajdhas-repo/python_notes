# Data Structures

Python has several built-in data structures that allow you to store and organize data efficiently.

---

## Strings

Strings are immutable sequences of characters.

### Creating Strings

```python
# Different ways to create strings
single = 'Hello'
double = "World"
triple_single = '''Multi-line
string with single quotes'''
triple_double = """Multi-line
string with double quotes"""

# Raw strings (ignore escape sequences)
path = r"C:\Users\name\folder"
print(path)  # C:\Users\name\folder

# Byte strings
byte_str = b"Hello"
print(type(byte_str))  # <class 'bytes'>
```

### String Indexing and Slicing

```python
s = "Python Programming"

# Indexing (0-based)
print(s[0])      # P (first character)
print(s[-1])     # g (last character)
print(s[-2])     # n (second to last)

# Slicing [start:stop:step]
print(s[0:6])    # Python
print(s[7:])     # Programming
print(s[:6])     # Python
print(s[::2])    # Pto rgamn (every 2nd char)
print(s[::-1])   # gnimmargorP nohtyP (reversed)
print(s[7:18:2]) # Pormig
```

### String Methods

```python
s = "  Hello, World!  "

# Case methods
print(s.upper())        # "  HELLO, WORLD!  "
print(s.lower())        # "  hello, world!  "
print(s.title())        # "  Hello, World!  "
print(s.capitalize())   # "  hello, world!  "
print(s.swapcase())     # "  hELLO, wORLD!  "

# Whitespace methods
print(s.strip())        # "Hello, World!"
print(s.lstrip())       # "Hello, World!  "
print(s.rstrip())       # "  Hello, World!"

# Search methods
text = "Hello, World!"
print(text.find("World"))      # 7 (index of first occurrence)
print(text.find("Python"))     # -1 (not found)
print(text.index("World"))     # 7 (raises ValueError if not found)
print(text.count("o"))         # 2
print(text.startswith("Hello")) # True
print(text.endswith("!"))      # True

# Replace and split
print(text.replace("World", "Python"))  # "Hello, Python!"
print(text.split(", "))                 # ['Hello', 'World!']
print("a-b-c".split("-"))               # ['a', 'b', 'c']

# Join
words = ["Hello", "World"]
print(" ".join(words))     # "Hello World"
print("-".join(words))     # "Hello-World"
print("".join(words))      # "HelloWorld"

# Check methods
print("hello".isalpha())   # True
print("123".isdigit())     # True
print("hello123".isalnum()) # True
print("   ".isspace())     # True
print("Hello".istitle())   # True
print("HELLO".isupper())   # True
print("hello".islower())   # True

# Alignment
print("hello".center(20, "-"))  # "-------hello--------"
print("hello".ljust(20, "-"))   # "hello---------------"
print("hello".rjust(20, "-"))   # "---------------hello"
print("42".zfill(5))            # "00042"
```

### String Formatting

```python
name = "Alice"
age = 25
price = 49.99

# f-strings (Python 3.6+) - Recommended
print(f"Name: {name}, Age: {age}")
print(f"Price: ${price:.2f}")
print(f"Name: {name!r}")  # Repr: 'Alice'
print(f"{'hello':>10}")   # Right align: "     hello"
print(f"{'hello':<10}")   # Left align: "hello     "
print(f"{'hello':^10}")   # Center: "  hello   "

# Format specifiers
print(f"{42:05d}")        # "00042" (zero-padded)
print(f"{3.14159:.2f}")   # "3.14" (2 decimal places)
print(f"{1000000:,}")     # "1,000,000" (thousands separator)
print(f"{0.25:.0%}")      # "25%" (percentage)
print(f"{255:b}")         # "11111111" (binary)
print(f"{255:x}")         # "ff" (hexadecimal)
print(f"{255:o}")         # "377" (octal)

# str.format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# % formatting (older style)
print("Name: %s, Age: %d" % (name, age))
print("Price: %.2f" % price)
```

---

## Lists

Lists are mutable, ordered sequences that can contain mixed types.

### Creating Lists

```python
# Empty list
empty = []
empty = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

# From other iterables
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
nums = list(range(5))  # [0, 1, 2, 3, 4]
```

### List Operations

```python
fruits = ["apple", "banana", "cherry"]

# Indexing and slicing (same as strings)
print(fruits[0])      # apple
print(fruits[-1])     # cherry
print(fruits[1:3])    # ['banana', 'cherry']

# Length
print(len(fruits))    # 3

# Concatenation
more = fruits + ["date", "elderberry"]
print(more)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Repetition
print([0] * 5)  # [0, 0, 0, 0, 0]

# Membership
print("apple" in fruits)  # True
print("grape" in fruits)  # False
```

### List Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Adding elements
numbers.append(7)           # Add to end: [3, 1, 4, 1, 5, 9, 2, 6, 7]
numbers.insert(0, 0)        # Insert at index: [0, 3, 1, 4, 1, 5, 9, 2, 6, 7]
numbers.extend([8, 9])      # Add multiple: [..., 7, 8, 9]

# Removing elements
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")     # Remove first occurrence: ['apple', 'cherry', 'banana']
popped = fruits.pop()       # Remove and return last: 'banana'
popped = fruits.pop(0)      # Remove and return at index: 'apple'
fruits.clear()              # Remove all: []

# Finding elements
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(numbers.index(4))     # 2 (first index of 4)
print(numbers.count(1))     # 2 (count of 1s)

# Sorting
numbers.sort()              # Sort in place: [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # Descending: [9, 6, 5, 4, 3, 2, 1, 1]
numbers.reverse()           # Reverse in place

# sorted() returns a new list
original = [3, 1, 4, 1, 5]
sorted_nums = sorted(original)  # original unchanged
print(sorted_nums)              # [1, 1, 3, 4, 5]

# Sort with key
words = ["banana", "apple", "Cherry"]
words.sort()                    # ['Cherry', 'apple', 'banana']
words.sort(key=str.lower)       # ['apple', 'banana', 'Cherry']
words.sort(key=len)             # ['apple', 'Cherry', 'banana']

# Copy
original = [1, 2, 3]
shallow_copy = original.copy()
shallow_copy = original[:]
shallow_copy = list(original)

# Deep copy (for nested lists)
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
```

### List as Stack and Queue

```python
# Stack (LIFO - Last In First Out)
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(stack.pop())  # 3 (Pop)
print(stack.pop())  # 2

# Queue (FIFO - First In First Out)
from collections import deque
queue = deque()
queue.append(1)    # Enqueue
queue.append(2)
queue.append(3)
print(queue.popleft())  # 1 (Dequeue)
print(queue.popleft())  # 2
```

---

## Tuples

Tuples are immutable, ordered sequences.

### Creating Tuples

```python
# Empty tuple
empty = ()
empty = tuple()

# Single element tuple (note the comma)
single = (1,)
not_tuple = (1)  # This is just an integer!

# Multiple elements
point = (3, 4)
mixed = (1, "hello", 3.14)
nested = ((1, 2), (3, 4))

# Without parentheses (tuple packing)
coordinates = 10, 20, 30
```

### Tuple Operations

```python
t = (1, 2, 3, 4, 5)

# Indexing and slicing
print(t[0])      # 1
print(t[-1])     # 5
print(t[1:4])    # (2, 3, 4)

# Length
print(len(t))    # 5

# Concatenation
print(t + (6, 7))  # (1, 2, 3, 4, 5, 6, 7)

# Repetition
print((0,) * 5)  # (0, 0, 0, 0, 0)

# Membership
print(3 in t)    # True

# Methods
print(t.count(2))  # 1
print(t.index(3))  # 2

# Tuple unpacking
x, y, z = (1, 2, 3)
print(x, y, z)  # 1 2 3

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

first, *middle, last = (1, 2, 3, 4, 5)
print(middle)  # [2, 3, 4]
```

### Why Use Tuples?

1. **Immutability**: Data that shouldn't change
2. **Hashable**: Can be used as dictionary keys
3. **Performance**: Slightly faster than lists
4. **Multiple return values**: Functions can return tuples

```python
# As dictionary keys
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")

# Named tuples (better readability)
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # 3 4
print(p[0], p[1])  # 3 4
```

---

## Sets

Sets are mutable, unordered collections of unique elements.

### Creating Sets

```python
# Empty set (NOT {} - that's an empty dict)
empty = set()

# Set with elements
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}  # No duplicates, unordered

# From other iterables
chars = set("hello")  # {'h', 'e', 'l', 'o'}
nums = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Frozen set (immutable)
frozen = frozenset([1, 2, 3])
```

### Set Operations

```python
s = {1, 2, 3, 4, 5}

# Adding elements
s.add(6)         # {1, 2, 3, 4, 5, 6}
s.update([7, 8]) # {1, 2, 3, 4, 5, 6, 7, 8}

# Removing elements
s.remove(8)      # Raises KeyError if not found
s.discard(7)     # No error if not found
popped = s.pop() # Remove and return arbitrary element
s.clear()        # Remove all

# Length and membership
s = {1, 2, 3}
print(len(s))    # 3
print(2 in s)    # True
```

### Set Mathematical Operations

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union (elements in either set)
print(a | b)           # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))      # Same

# Intersection (elements in both sets)
print(a & b)           # {4, 5}
print(a.intersection(b))

# Difference (elements in a but not in b)
print(a - b)           # {1, 2, 3}
print(a.difference(b))

# Symmetric difference (elements in either but not both)
print(a ^ b)           # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))

# Subset and superset
print({1, 2}.issubset({1, 2, 3}))      # True
print({1, 2, 3}.issuperset({1, 2}))    # True
print({1, 2}.isdisjoint({3, 4}))       # True (no common elements)
```

### Practical Uses of Sets

```python
# Remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))  # [1, 2, 3, 4]

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)  # {4, 5}

# Check membership efficiently
valid_users = {"alice", "bob", "charlie"}
user = "alice"
if user in valid_users:  # O(1) lookup
    print("Valid user")
```

---

## Dictionaries

Dictionaries are mutable, unordered (ordered in Python 3.7+) collections of key-value pairs.

### Creating Dictionaries

```python
# Empty dictionary
empty = {}
empty = dict()

# With elements
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict()
person = dict(name="Alice", age=25, city="New York")

# From list of tuples
items = [("a", 1), ("b", 2), ("c", 3)]
d = dict(items)  # {'a': 1, 'b': 2, 'c': 3}

# Using dict.fromkeys()
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

# Dictionary with different value types
mixed = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "nested": {"key": "value"}
}
```

### Dictionary Operations

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Accessing values
print(person["name"])       # Alice
print(person.get("name"))   # Alice
print(person.get("country", "Unknown"))  # Unknown (default)

# Modifying values
person["age"] = 26
person["country"] = "USA"  # Add new key

# Removing elements
del person["city"]
age = person.pop("age")          # Remove and return value
item = person.popitem()          # Remove and return last item (3.7+)
person.clear()                   # Remove all

# Length and membership
person = {"name": "Alice", "age": 25}
print(len(person))               # 2
print("name" in person)          # True (checks keys)
print("Alice" in person.values()) # True (checks values)
```

### Dictionary Methods

```python
person = {"name": "Alice", "age": 25}

# Get keys, values, items
print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 25])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 25)])

# Iterating
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Update (merge dictionaries)
person.update({"city": "NYC", "age": 26})
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'NYC'}

# Merge operators (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2       # {'a': 1, 'b': 3, 'c': 4}
d1 |= d2               # Update d1 in place

# setdefault
person = {"name": "Alice"}
person.setdefault("age", 25)  # Only sets if key doesn't exist
print(person)  # {'name': 'Alice', 'age': 25}

# Copy
shallow = person.copy()
```

### Nested Dictionaries

```python
users = {
    "alice": {
        "age": 25,
        "email": "alice@example.com",
        "hobbies": ["reading", "coding"]
    },
    "bob": {
        "age": 30,
        "email": "bob@example.com",
        "hobbies": ["gaming", "music"]
    }
}

# Accessing nested values
print(users["alice"]["email"])           # alice@example.com
print(users["alice"]["hobbies"][0])      # reading

# Safe nested access
def safe_get(d, *keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d

print(safe_get(users, "alice", "email"))  # alice@example.com
print(safe_get(users, "charlie", "email"))  # None
```

### DefaultDict

```python
from collections import defaultdict

# Regular dict raises KeyError
# d = {}
# d["key"] += 1  # KeyError

# defaultdict provides default value
counter = defaultdict(int)
counter["a"] += 1
counter["b"] += 1
counter["a"] += 1
print(dict(counter))  # {'a': 2, 'b': 1}

# List as default
groups = defaultdict(list)
for item in [("fruit", "apple"), ("fruit", "banana"), ("veggie", "carrot")]:
    groups[item[0]].append(item[1])
print(dict(groups))  # {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}
```

### Counter

```python
from collections import Counter

# Count elements
text = "hello world"
char_count = Counter(text)
print(char_count)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Most common
print(char_count.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]

# Count words
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(word_count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Arithmetic
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Counter({'a': 4, 'b': 3})
print(c1 - c2)  # Counter({'a': 2})
```

---

## List Comprehensions

A concise way to create lists.

### Basic Syntax

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With Conditions

```python
# Filter even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# if-else in comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
```

### Nested Comprehensions

```python
# Flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a matrix
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Transpose a matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
```

### Practical Examples

```python
# Extract data from objects
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
names = [user["name"] for user in users]
adults = [user for user in users if user["age"] >= 30]

# Process strings
words = ["  hello  ", "  world  ", "  python  "]
cleaned = [word.strip().upper() for word in words]
print(cleaned)  # ['HELLO', 'WORLD', 'PYTHON']

# Filter and transform
numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_squares = [x ** 2 for x in numbers if x > 0]
print(positive_squares)  # [1, 4, 9]
```

---

## Dictionary Comprehensions

```python
# Basic dictionary comprehension
squares = {x: x ** 2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Filter dictionary
data = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in data.items() if v > 2}
print(filtered)  # {'c': 3, 'd': 4}
```

---

## Set Comprehensions

```python
# Basic set comprehension
squares = {x ** 2 for x in range(-5, 6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# Extract unique first letters
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
first_letters = {word[0] for word in words}
print(first_letters)  # {'a', 'b', 'c'}
```

---

## Generator Expressions

Memory-efficient alternative to list comprehensions.

```python
# Generator expression (uses parentheses)
squares_gen = (x ** 2 for x in range(1000000))
print(type(squares_gen))  # <class 'generator'>

# Memory efficient - doesn't store all values at once
for i, square in enumerate(squares_gen):
    if i >= 5:
        break
    print(square)

# Use with functions
print(sum(x ** 2 for x in range(10)))  # 285
print(max(x ** 2 for x in range(10)))  # 81
print(any(x > 100 for x in range(50)))  # False
print(all(x < 100 for x in range(50)))  # True
```

---

## Choosing the Right Data Structure

| Data Structure | Use Case |
|---------------|----------|
| **List** | Ordered, mutable collection; frequent additions/removals |
| **Tuple** | Ordered, immutable collection; function returns; dict keys |
| **Set** | Unique elements; membership testing; mathematical operations |
| **Dictionary** | Key-value pairs; fast lookup by key |
| **String** | Text data; immutable character sequence |

### Performance Comparison

```python
# List vs Set for membership testing
import time

large_list = list(range(1000000))
large_set = set(range(1000000))

# List: O(n) - slow for large collections
start = time.time()
999999 in large_list
print(f"List: {time.time() - start:.6f}s")

# Set: O(1) - fast for any size
start = time.time()
999999 in large_set
print(f"Set: {time.time() - start:.6f}s")
```

---

## Summary

- **Strings**: Immutable sequences of characters with rich methods
- **Lists**: Mutable, ordered sequences; most versatile collection
- **Tuples**: Immutable, ordered sequences; faster than lists
- **Sets**: Unordered collections of unique elements
- **Dictionaries**: Key-value pairs with fast lookup
- **Comprehensions**: Concise syntax for creating lists, dicts, and sets

## Next Steps

Continue to [Functions](05-functions.md) to learn about defining and using functions.
