# Best Practices

This chapter covers Python coding best practices, style guidelines, and techniques for writing clean, maintainable code.

---

## PEP 8 Style Guide

### Naming Conventions

```python
# Variables and functions: snake_case
user_name = "John"
total_count = 42

def calculate_total():
    pass

def get_user_by_id(user_id):
    pass

# Constants: UPPER_SNAKE_CASE
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# Classes: PascalCase
class UserAccount:
    pass

class DatabaseConnection:
    pass

# Private attributes: leading underscore
class MyClass:
    def __init__(self):
        self._internal_value = 42  # Protected
        self.__private_value = 99  # Private (name mangling)
    
    def _helper_method(self):
        """Internal use only."""
        pass

# Module-level "private": leading underscore
_internal_cache = {}

def _helper_function():
    pass
```

### Indentation and Line Length

```python
# Use 4 spaces per indentation level (not tabs)
def my_function():
    if True:
        for i in range(10):
            print(i)

# Maximum line length: 79 characters (72 for docstrings)
# Break long lines using implicit continuation inside parentheses

# Good
result = some_function(
    argument_one,
    argument_two,
    argument_three
)

# Good - hanging indent
result = some_function(argument_one, argument_two,
                       argument_three, argument_four)

# Good - for long if statements
if (condition_one
        and condition_two
        and condition_three):
    do_something()

# Good - for long strings
message = (
    "This is a very long message that would exceed "
    "the line limit if written on a single line."
)
```

### Whitespace

```python
# Good
x = 1
y = 2
long_variable = 3

# Bad - don't align with extra spaces
x             = 1
y             = 2
long_variable = 3

# Spaces around operators
x = 1 + 2
y = x * 3

# No space in keyword arguments
def function(arg1, arg2=None):
    pass

function(1, arg2=2)

# Spaces after commas
my_list = [1, 2, 3, 4]
my_dict = {"a": 1, "b": 2}

# No spaces inside brackets
my_list[0]      # Good
my_list[ 0 ]    # Bad

# No space before colon in slices
my_list[1:3]    # Good
my_list[1 : 3]  # Bad

# Blank lines
# - Two blank lines around top-level definitions
# - One blank line between methods in a class


class MyClass:
    
    def method_one(self):
        pass
    
    def method_two(self):
        pass


def top_level_function():
    pass
```

### Imports

```python
# Standard library imports first
import os
import sys
from datetime import datetime

# Third-party imports second
import requests
import numpy as np
from flask import Flask, request

# Local imports third
from myapp import utils
from myapp.models import User

# Absolute imports preferred over relative
from myapp.utils import helper  # Good
from .utils import helper       # OK for packages

# One import per line (for regular imports)
import os
import sys

# Multiple imports from same module OK
from datetime import datetime, timedelta

# Avoid wildcard imports
from module import *  # Bad - pollutes namespace
```

---

## Documentation

### Docstrings

```python
def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price.
    
    Args:
        price: The original price (float or int).
        discount_percent: The discount percentage (0-100).
    
    Returns:
        The discounted price as a float.
    
    Raises:
        ValueError: If discount_percent is not between 0 and 100.
    
    Examples:
        >>> calculate_discount(100, 20)
        80.0
        >>> calculate_discount(50, 10)
        45.0
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


class ShoppingCart:
    """
    A shopping cart that holds items and calculates totals.
    
    Attributes:
        items: List of items in the cart.
        discount: Applied discount percentage.
    
    Example:
        >>> cart = ShoppingCart()
        >>> cart.add_item("Apple", 1.50)
        >>> cart.total
        1.50
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
        self.discount = 0
    
    def add_item(self, name, price):
        """
        Add an item to the cart.
        
        Args:
            name: Item name.
            price: Item price.
        """
        self.items.append({"name": name, "price": price})
```

### Comments

```python
# Good comments explain WHY, not WHAT
# Bad: Increment counter by 1
# Good: Track failed attempts to implement rate limiting
failed_attempts += 1

# Use comments sparingly - code should be self-documenting
# Bad
# Loop through users
for user in users:
    # Check if user is active
    if user.is_active:
        # Process the user
        process(user)

# Good - code is self-documenting
for user in users:
    if user.is_active:
        process(user)

# Use TODO comments for future work
# TODO: Implement caching to improve performance
# FIXME: This breaks with empty input
# NOTE: This algorithm assumes sorted input
```

---

## Type Hints

### Basic Type Hints

```python
from typing import List, Dict, Optional, Union, Tuple, Any

# Variable annotations
name: str = "Alice"
age: int = 30
balance: float = 100.50
is_active: bool = True

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Collections
def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    # Returns str or None
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Union (multiple possible types)
def process(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode()
    return data

# Tuple
def get_coordinates() -> Tuple[float, float]:
    return (40.7128, -74.0060)
```

### Advanced Type Hints

```python
from typing import (
    Callable, TypeVar, Generic, 
    Iterator, Iterable, Sequence
)

# Callable
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

# TypeVar for generics
T = TypeVar('T')

def first(items: List[T]) -> Optional[T]:
    return items[0] if items else None

# Generic classes
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()

# Usage
int_stack: Stack[int] = Stack()
int_stack.push(1)

# Type aliases
UserId = int
UserDict = Dict[str, Union[str, int]]

def get_user(user_id: UserId) -> UserDict:
    return {"id": user_id, "name": "Alice"}
```

### Python 3.10+ Type Hints

```python
# Union with | operator (Python 3.10+)
def process(data: str | bytes) -> str:
    if isinstance(data, bytes):
        return data.decode()
    return data

# Optional with | None
def find_user(user_id: int) -> str | None:
    return None

# Built-in generics (no need to import)
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

---

## Logging

### Basic Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log levels
logger.debug("Debug message - detailed info for debugging")
logger.info("Info message - general information")
logger.warning("Warning message - something unexpected")
logger.error("Error message - serious problem")
logger.critical("Critical message - program may crash")

# With exception info
try:
    result = 1 / 0
except ZeroDivisionError:
    logger.exception("Division failed")  # Includes traceback
```

### Logging Configuration

```python
import logging
import logging.config

# Dict configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5
        }
    },
    'loggers': {
        '': {  # Root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'myapp': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('myapp')
```

### Best Practices

```python
import logging

logger = logging.getLogger(__name__)

# Use lazy formatting (don't format if not logged)
# Bad - always formats string
logger.debug("Processing user: %s" % user_id)

# Good - only formats if debug level is enabled
logger.debug("Processing user: %s", user_id)

# Use structured logging for complex data
logger.info("User action", extra={
    'user_id': user_id,
    'action': 'login',
    'ip': ip_address
})

# Don't log sensitive data
# Bad
logger.info(f"User logged in with password: {password}")

# Good
logger.info(f"User {user_id} logged in successfully")
```

---

## Debugging

### Using pdb

```python
import pdb

def calculate(a, b):
    result = a + b
    pdb.set_trace()  # Breakpoint
    return result * 2

# Or use breakpoint() in Python 3.7+
def calculate(a, b):
    result = a + b
    breakpoint()  # Built-in breakpoint
    return result * 2

# pdb commands:
# n (next) - execute next line
# s (step) - step into function
# c (continue) - continue execution
# p variable - print variable
# l (list) - show source code
# q (quit) - quit debugger
# h (help) - show help
```

### Debugging Techniques

```python
# Print debugging (simple but effective)
def process_data(data):
    print(f"DEBUG: Input data type: {type(data)}")
    print(f"DEBUG: Input data: {data}")
    
    result = transform(data)
    print(f"DEBUG: Result: {result}")
    
    return result

# Assert for debugging assumptions
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    assert isinstance(a, (int, float)), f"Expected number, got {type(a)}"
    return a / b

# Using __debug__ (disabled with -O flag)
if __debug__:
    print("Debug mode is enabled")

# Inspect objects
import inspect

def debug_function(func):
    print(f"Function: {func.__name__}")
    print(f"Signature: {inspect.signature(func)}")
    print(f"Source file: {inspect.getfile(func)}")
    print(f"Docstring: {func.__doc__}")
```

---

## Code Organization

### Project Structure

```
my_project/
├── README.md
├── LICENSE
├── pyproject.toml          # Modern Python packaging
├── requirements.txt        # Dependencies
├── setup.py               # Legacy packaging (optional)
├── .gitignore
├── .env                   # Environment variables (not in git)
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── user_service.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main.py
│   └── test_user_service.py
└── docs/
    └── index.md
```

### Configuration Management

```python
# config.py
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    """Application configuration."""
    
    # Database
    database_url: str = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    
    # API
    api_key: Optional[str] = os.getenv('API_KEY')
    api_timeout: int = int(os.getenv('API_TIMEOUT', '30'))
    
    # Application
    debug: bool = os.getenv('DEBUG', 'false').lower() == 'true'
    log_level: str = os.getenv('LOG_LEVEL', 'INFO')
    
    def validate(self):
        """Validate required configuration."""
        if not self.api_key:
            raise ValueError("API_KEY is required")

# Usage
config = Config()
config.validate()

# Or use pydantic for validation
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = 'sqlite:///app.db'
    api_key: str
    debug: bool = False
    
    class Config:
        env_file = '.env'

settings = Settings()
```

### Dependency Injection

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Abstract interface
class EmailService(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, body: str) -> bool:
        pass

# Concrete implementations
class SMTPEmailService(EmailService):
    def send(self, to: str, subject: str, body: str) -> bool:
        # Real email sending
        print(f"Sending email to {to}")
        return True

class MockEmailService(EmailService):
    def send(self, to: str, subject: str, body: str) -> bool:
        # For testing
        print(f"Mock: would send to {to}")
        return True

# Service that depends on EmailService
@dataclass
class UserService:
    email_service: EmailService
    
    def register(self, email: str, name: str):
        # Create user...
        self.email_service.send(
            to=email,
            subject="Welcome!",
            body=f"Hello {name}"
        )

# Usage
email_service = SMTPEmailService()  # or MockEmailService() for tests
user_service = UserService(email_service)
user_service.register("user@example.com", "Alice")
```

---

## Performance Tips

### Profiling

```python
import cProfile
import pstats

# Profile a function
def slow_function():
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

# Using cProfile
cProfile.run('slow_function()', 'output.prof')

# Analyze results
stats = pstats.Stats('output.prof')
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10

# Line profiler (pip install line_profiler)
# @profile
# def slow_function():
#     ...
# Run with: kernprof -l -v script.py
```

### Optimization Tips

```python
# Use generators for large datasets
# Bad - loads all into memory
def get_squares(n):
    return [x ** 2 for x in range(n)]

# Good - generates on demand
def get_squares(n):
    for x in range(n):
        yield x ** 2

# Use appropriate data structures
# O(1) lookup with set/dict vs O(n) with list
items = {1, 2, 3, 4, 5}  # set for membership testing
5 in items  # O(1)

# Use local variables (faster than global)
def process():
    local_func = some_function  # Cache lookup
    for i in range(1000):
        local_func(i)

# Use built-in functions (implemented in C)
# Bad
total = 0
for x in numbers:
    total += x

# Good
total = sum(numbers)

# String concatenation
# Bad - creates new string each iteration
result = ""
for s in strings:
    result += s

# Good - single allocation
result = "".join(strings)

# Use slots for memory efficiency
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## Security Best Practices

```python
# Never hardcode secrets
# Bad
API_KEY = "secret123"

# Good - use environment variables
import os
API_KEY = os.environ.get('API_KEY')

# Validate and sanitize input
from html import escape

user_input = "<script>alert('xss')</script>"
safe_input = escape(user_input)

# Use parameterized queries (prevent SQL injection)
# Bad
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# Good
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# Hash passwords properly
import hashlib
import secrets

# Bad - simple hash
password_hash = hashlib.md5(password.encode()).hexdigest()

# Good - use bcrypt or similar
import bcrypt
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Generate secure random tokens
token = secrets.token_urlsafe(32)

# Use HTTPS for all external requests
import requests
response = requests.get('https://api.example.com', verify=True)
```

---

## Summary

### Key Principles

1. **Readability counts** - Code is read more than written
2. **Explicit is better than implicit** - Be clear about intent
3. **Simple is better than complex** - Don't over-engineer
4. **Errors should never pass silently** - Handle exceptions properly
5. **There should be one obvious way** - Follow conventions

### Checklist

- [ ] Follow PEP 8 style guide
- [ ] Write meaningful docstrings
- [ ] Use type hints
- [ ] Implement proper logging
- [ ] Write tests
- [ ] Handle errors gracefully
- [ ] Keep functions small and focused
- [ ] Don't repeat yourself (DRY)
- [ ] Use version control
- [ ] Document your code

## Next Steps

Continue to [Useful Libraries](15-useful-libraries.md) to explore essential Python libraries.
