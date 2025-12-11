# Exception Handling

Exception handling allows you to gracefully handle errors and unexpected situations in your programs.

---

## What are Exceptions?

Exceptions are events that occur during program execution that disrupt the normal flow. When an error occurs, Python creates an exception object.

```python
# Common exceptions
print(10 / 0)           # ZeroDivisionError
print(int("hello"))     # ValueError
print(undefined_var)    # NameError
print([1, 2, 3][10])    # IndexError
print({'a': 1}['b'])    # KeyError
```

---

## The try-except Block

### Basic Syntax

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the exception
    print("Cannot divide by zero!")
```

### Catching Multiple Exceptions

```python
# Separate except blocks
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input - not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions in one block
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
```

### Catching All Exceptions

```python
# Catch any exception (use sparingly)
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")

# Catch absolutely everything (rarely needed)
try:
    risky_operation()
except BaseException as e:
    print(f"Error: {e}")
```

### Getting Exception Information

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")

# With traceback
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error occurred:")
    traceback.print_exc()
```

---

## The else Clause

The `else` block runs if no exception was raised.

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    # Only runs if no exception occurred
    print(f"Result: {result}")
```

---

## The finally Clause

The `finally` block always runs, whether an exception occurred or not.

```python
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # Always runs - cleanup code
    print("Cleaning up...")
    if 'file' in locals() and not file.closed:
        file.close()

# Common pattern
def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        return file.read()
    except FileNotFoundError:
        return None
    finally:
        if file:
            file.close()
```

### Complete try-except-else-finally

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid types")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Operation complete")

# Test
print(divide(10, 2))   # Division successful, Operation complete, 5.0
print(divide(10, 0))   # Error: Division by zero, Operation complete, None
```

---

## Raising Exceptions

### Basic raise

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(e)  # Age cannot be negative
```

### Re-raising Exceptions

```python
def process_data(data):
    try:
        # Process data
        result = risky_operation(data)
    except Exception as e:
        print(f"Error processing: {e}")
        raise  # Re-raise the same exception

# Add information and re-raise
def process_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {filename}")
```

### Raising from Another Exception

```python
def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise TypeError(f"Cannot convert {value!r} to integer") from e

try:
    convert_to_int("hello")
except TypeError as e:
    print(e)
    print(f"Caused by: {e.__cause__}")
```

---

## Custom Exceptions

### Creating Custom Exception Classes

```python
# Simple custom exception
class ValidationError(Exception):
    """Raised when validation fails."""
    pass

# Custom exception with additional data
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Insufficient funds: balance={balance}, "
            f"required={amount}, deficit={self.deficit}"
        )

# Using custom exceptions
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return amount

# Usage
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)
    print(f"You need ${e.deficit} more")
```

### Exception Hierarchy

```python
# Create a hierarchy of exceptions
class AppError(Exception):
    """Base exception for the application."""
    pass

class ValidationError(AppError):
    """Validation-related errors."""
    pass

class DatabaseError(AppError):
    """Database-related errors."""
    pass

class ConnectionError(DatabaseError):
    """Database connection errors."""
    pass

class QueryError(DatabaseError):
    """Database query errors."""
    pass

# Catch specific or general
try:
    raise ConnectionError("Could not connect to database")
except ConnectionError:
    print("Connection failed")
except DatabaseError:
    print("Database error")
except AppError:
    print("Application error")
```

---

## Built-in Exception Types

### Common Exceptions

| Exception | Description |
|-----------|-------------|
| `Exception` | Base class for most exceptions |
| `ValueError` | Invalid value for operation |
| `TypeError` | Invalid type for operation |
| `KeyError` | Key not found in dictionary |
| `IndexError` | Index out of range |
| `AttributeError` | Attribute not found |
| `NameError` | Name not defined |
| `FileNotFoundError` | File doesn't exist |
| `IOError` | Input/Output operation failed |
| `ZeroDivisionError` | Division by zero |
| `ImportError` | Module import failed |
| `RuntimeError` | Generic runtime error |
| `StopIteration` | Iterator exhausted |
| `KeyboardInterrupt` | User interrupted (Ctrl+C) |

### Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── IsADirectoryError
    │   ├── NotADirectoryError
    │   ├── PermissionError
    │   └── TimeoutError
    ├── RuntimeError
    │   ├── NotImplementedError
    │   └── RecursionError
    ├── SyntaxError
    │   └── IndentationError
    ├── TypeError
    └── ValueError
        └── UnicodeError
```

---

## Assertions

Assertions are debugging aids that test conditions and raise `AssertionError` if false.

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)

# Usage
print(calculate_average([1, 2, 3]))  # 2.0
# print(calculate_average([]))      # AssertionError: List cannot be empty

# Assertions can be disabled with -O flag
# python -O script.py
# Don't use assertions for data validation in production!
```

### When to Use Assertions

```python
# Good: Internal consistency checks
def _internal_function(data):
    assert isinstance(data, list), "Internal error: expected list"
    # ...

# Bad: User input validation (use exceptions instead)
def get_user_age(age):
    # Don't do this:
    # assert age >= 0, "Age must be positive"
    
    # Do this instead:
    if age < 0:
        raise ValueError("Age must be positive")
```

---

## Context Managers for Exception Handling

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    try:
        yield name
    except Exception as e:
        print(f"Error with {name}: {e}")
        raise
    finally:
        print(f"Releasing {name}")

# Usage
try:
    with managed_resource("database") as db:
        print(f"Using {db}")
        raise ValueError("Something went wrong")
except ValueError:
    print("Handled the error")

# Output:
# Acquiring database
# Using database
# Error with database: Something went wrong
# Releasing database
# Handled the error
```

---

## Exception Chaining

```python
# Implicit chaining (during handling of another exception)
try:
    try:
        raise ValueError("Original error")
    except ValueError:
        raise TypeError("New error")  # Original is in __context__
except TypeError as e:
    print(f"Error: {e}")
    print(f"Context: {e.__context__}")

# Explicit chaining with 'from'
try:
    try:
        raise ValueError("Original error")
    except ValueError as e:
        raise TypeError("New error") from e  # Original is in __cause__
except TypeError as e:
    print(f"Error: {e}")
    print(f"Cause: {e.__cause__}")

# Suppress chaining
try:
    try:
        raise ValueError("Original error")
    except ValueError:
        raise TypeError("New error") from None  # No chain shown
except TypeError as e:
    print(f"Error: {e}")
    print(f"Cause: {e.__cause__}")  # None
```

---

## Exception Groups (Python 3.11+)

```python
# Raise multiple exceptions at once
def process_items(items):
    errors = []
    results = []
    
    for i, item in enumerate(items):
        try:
            results.append(process(item))
        except Exception as e:
            errors.append(e)
    
    if errors:
        raise ExceptionGroup("Processing failed", errors)
    
    return results

# Handle exception groups
try:
    process_items([1, "invalid", 3, None])
except* ValueError as e:
    print(f"Value errors: {e.exceptions}")
except* TypeError as e:
    print(f"Type errors: {e.exceptions}")
```

---

## Best Practices

### 1. Be Specific with Exceptions

```python
# Bad - too broad
try:
    do_something()
except Exception:
    pass

# Good - catch specific exceptions
try:
    do_something()
except ValueError:
    handle_value_error()
except KeyError:
    handle_key_error()
```

### 2. Don't Silence Exceptions

```python
# Bad - swallows all errors
try:
    do_something()
except Exception:
    pass

# Good - at least log it
import logging

try:
    do_something()
except Exception:
    logging.exception("Error in do_something")
```

### 3. Use finally for Cleanup

```python
# Ensure cleanup happens
resource = acquire_resource()
try:
    use_resource(resource)
finally:
    release_resource(resource)

# Or use context managers
with acquire_resource() as resource:
    use_resource(resource)
```

### 4. Provide Meaningful Error Messages

```python
# Bad
raise ValueError("Invalid")

# Good
raise ValueError(f"Age must be between 0 and 150, got {age}")
```

### 5. Document Exceptions

```python
def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    
    Args:
        a: The dividend.
        b: The divisor.
    
    Returns:
        The quotient.
    
    Raises:
        ZeroDivisionError: If b is zero.
        TypeError: If a or b are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

---

## Practical Examples

### Example 1: Retry with Exponential Backoff

```python
import time
import random

def retry_with_backoff(func, max_retries=3, base_delay=1):
    """Retry a function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise  # Re-raise on last attempt
            
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed: {e}")
            print(f"Retrying in {delay:.2f} seconds...")
            time.sleep(delay)

# Usage
def unreliable_operation():
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success!"

try:
    result = retry_with_backoff(unreliable_operation)
    print(result)
except ConnectionError:
    print("All retries failed")
```

### Example 2: Validation Framework

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class ValidationErrors(Exception):
    def __init__(self, errors):
        self.errors = errors
        messages = [str(e) for e in errors]
        super().__init__("Validation failed:\n" + "\n".join(messages))

def validate_user(data):
    errors = []
    
    if not data.get('name'):
        errors.append(ValidationError('name', 'Name is required'))
    elif len(data['name']) < 2:
        errors.append(ValidationError('name', 'Name must be at least 2 characters'))
    
    if not data.get('email'):
        errors.append(ValidationError('email', 'Email is required'))
    elif '@' not in data['email']:
        errors.append(ValidationError('email', 'Invalid email format'))
    
    if data.get('age') is not None:
        if not isinstance(data['age'], int):
            errors.append(ValidationError('age', 'Age must be an integer'))
        elif data['age'] < 0 or data['age'] > 150:
            errors.append(ValidationError('age', 'Age must be between 0 and 150'))
    
    if errors:
        raise ValidationErrors(errors)
    
    return True

# Usage
try:
    validate_user({'name': 'A', 'email': 'invalid', 'age': -5})
except ValidationErrors as e:
    print(e)
    for error in e.errors:
        print(f"  - {error.field}: {error.message}")
```

### Example 3: Safe Dictionary Access

```python
from functools import wraps

def safe_get(data, *keys, default=None):
    """Safely get nested dictionary values."""
    result = data
    for key in keys:
        try:
            result = result[key]
        except (KeyError, TypeError, IndexError):
            return default
    return result

# Usage
data = {
    'user': {
        'profile': {
            'name': 'Alice',
            'settings': {
                'theme': 'dark'
            }
        }
    }
}

print(safe_get(data, 'user', 'profile', 'name'))  # Alice
print(safe_get(data, 'user', 'profile', 'age'))   # None
print(safe_get(data, 'user', 'missing', 'key', default='N/A'))  # N/A
```

### Example 4: Error Handler Decorator

```python
from functools import wraps
import logging

logging.basicConfig(level=logging.ERROR)

def handle_errors(default=None, log=True, reraise=False):
    """Decorator to handle exceptions in functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if log:
                    logging.exception(f"Error in {func.__name__}")
                if reraise:
                    raise
                return default
        return wrapper
    return decorator

@handle_errors(default=0, log=True)
def risky_calculation(a, b):
    return a / b

print(risky_calculation(10, 2))  # 5.0
print(risky_calculation(10, 0))  # 0 (logged error)
```

---

## Summary

- Use `try-except` to catch and handle exceptions
- Use `else` for code that should run only if no exception occurred
- Use `finally` for cleanup code that must always run
- Raise exceptions with `raise` to signal errors
- Create custom exceptions for domain-specific errors
- Be specific about which exceptions you catch
- Don't silence exceptions - at least log them
- Use context managers for resource management
- Document the exceptions your functions can raise

## Next Steps

Continue to [Advanced Topics](10-advanced-topics.md) to explore more advanced Python concepts.
