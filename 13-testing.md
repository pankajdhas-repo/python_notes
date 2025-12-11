# Testing

This chapter covers testing in Python, from basic unit tests to advanced testing techniques.

---

## Why Testing Matters

- **Catch bugs early** - Find issues before they reach production
- **Enable refactoring** - Change code confidently
- **Document behavior** - Tests show how code should work
- **Improve design** - Testable code is often better designed
- **Save time** - Automated tests are faster than manual testing

---

## unittest (Built-in)

### Basic Test Structure

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_calculator.py
import unittest
from calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

```bash
# Run tests
python -m unittest test_calculator.py
python -m unittest discover  # Find all tests
```

### Assertions

```python
import unittest

class TestAssertions(unittest.TestCase):
    
    def test_equality(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1 + 1, 3)
    
    def test_truthiness(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)
    
    def test_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone("value")
    
    def test_identity(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b)
        self.assertIsNot(a, c)
    
    def test_membership(self):
        self.assertIn(1, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
    
    def test_types(self):
        self.assertIsInstance(1, int)
        self.assertNotIsInstance(1, str)
    
    def test_comparisons(self):
        self.assertGreater(5, 3)
        self.assertGreaterEqual(5, 5)
        self.assertLess(3, 5)
        self.assertLessEqual(5, 5)
    
    def test_approximate(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=5)
    
    def test_regex(self):
        self.assertRegex("hello world", r"hello \w+")
    
    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
        
        with self.assertRaisesRegex(ValueError, "invalid"):
            raise ValueError("invalid literal")
```

### Setup and Teardown

```python
import unittest

class TestWithSetup(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Run once before all tests in the class."""
        print("Setting up class...")
        cls.shared_resource = "shared"
    
    @classmethod
    def tearDownClass(cls):
        """Run once after all tests in the class."""
        print("Tearing down class...")
    
    def setUp(self):
        """Run before each test method."""
        self.test_data = [1, 2, 3]
    
    def tearDown(self):
        """Run after each test method."""
        self.test_data = None
    
    def test_one(self):
        self.assertEqual(len(self.test_data), 3)
        self.assertEqual(self.shared_resource, "shared")
    
    def test_two(self):
        self.test_data.append(4)
        self.assertEqual(len(self.test_data), 4)
```

### Skipping Tests

```python
import unittest
import sys

class TestSkipping(unittest.TestCase):
    
    @unittest.skip("Demonstrating skip")
    def test_skipped(self):
        self.fail("This should be skipped")
    
    @unittest.skipIf(sys.version_info < (3, 10), "Requires Python 3.10+")
    def test_python_310_feature(self):
        # Test that uses Python 3.10+ features
        pass
    
    @unittest.skipUnless(sys.platform.startswith("linux"), "Linux only")
    def test_linux_only(self):
        pass
    
    @unittest.expectedFailure
    def test_known_failure(self):
        self.assertEqual(1, 2)  # Known bug, expected to fail
```

---

## pytest (Recommended)

### Installation

```bash
pip install pytest
```

### Basic Tests

```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_string():
    assert "hello".upper() == "HELLO"

def test_list():
    items = [1, 2, 3]
    assert 1 in items
    assert len(items) == 3
```

```bash
# Run tests
pytest                      # Run all tests
pytest test_example.py      # Run specific file
pytest -v                   # Verbose output
pytest -q                   # Quiet output
pytest -x                   # Stop on first failure
pytest --tb=short           # Shorter traceback
pytest -k "test_add"        # Run tests matching pattern
```

### Fixtures

```python
import pytest

# Simple fixture
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list_sum(sample_list):
    assert sum(sample_list) == 15

def test_list_length(sample_list):
    assert len(sample_list) == 5

# Fixture with setup and teardown
@pytest.fixture
def database():
    # Setup
    db = {"connected": True, "data": []}
    yield db
    # Teardown
    db["connected"] = False
    print("Database closed")

def test_database(database):
    assert database["connected"]
    database["data"].append(1)
    assert len(database["data"]) == 1

# Fixture scopes
@pytest.fixture(scope="module")
def expensive_resource():
    """Created once per module."""
    return {"expensive": "resource"}

@pytest.fixture(scope="session")
def session_resource():
    """Created once per test session."""
    return {"session": "resource"}

# Fixture with parameters
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_is_positive(number):
    assert number > 0
```

### Conftest.py

```python
# conftest.py - shared fixtures across multiple test files

import pytest

@pytest.fixture
def app():
    """Create application for testing."""
    from myapp import create_app
    app = create_app("testing")
    return app

@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()

@pytest.fixture(autouse=True)
def cleanup():
    """Automatically run cleanup after each test."""
    yield
    # Cleanup code here
```

### Parametrized Tests

```python
import pytest

# Test with multiple inputs
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (0, 0),
    (-1, -2),
])
def test_double(input, expected):
    assert input * 2 == expected

# Multiple parameters
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (10, 20, 30),
])
def test_add(a, b, expected):
    assert a + b == expected

# Combining parametrize decorators
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_multiply(x, y):
    # Runs for: (1,3), (1,4), (2,3), (2,4)
    assert x * y > 0
```

### Testing Exceptions

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_by_zero_detailed():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert "zero" in str(exc_info.value)
```

### Markers

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(2)
    assert True

@pytest.mark.integration
def test_database_connection():
    # Integration test
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 1 == 2
```

```bash
# Run specific markers
pytest -m slow
pytest -m "not slow"
pytest -m "slow or integration"
```

### pytest.ini Configuration

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
```

---

## Mocking

### unittest.mock

```python
from unittest.mock import Mock, patch, MagicMock
import unittest

# Basic Mock
def test_mock_basic():
    mock = Mock()
    mock.method.return_value = 42
    
    result = mock.method()
    
    assert result == 42
    mock.method.assert_called_once()

# Mock with return values
def test_mock_return_value():
    mock = Mock()
    mock.return_value = "mocked"
    
    assert mock() == "mocked"
    
    # Side effect for multiple calls
    mock.side_effect = [1, 2, 3]
    assert mock() == 1
    assert mock() == 2
    assert mock() == 3

# Mock raising exceptions
def test_mock_exception():
    mock = Mock()
    mock.side_effect = ValueError("error")
    
    try:
        mock()
    except ValueError as e:
        assert str(e) == "error"
```

### Patching

```python
from unittest.mock import patch
import requests

# Function to test
def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# Patching with decorator
@patch('requests.get')
def test_get_user_data(mock_get):
    mock_get.return_value.json.return_value = {"id": 1, "name": "John"}
    
    result = get_user_data(1)
    
    assert result["name"] == "John"
    mock_get.assert_called_once_with("https://api.example.com/users/1")

# Patching with context manager
def test_get_user_data_context():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"id": 1, "name": "John"}
        
        result = get_user_data(1)
        
        assert result["name"] == "John"

# Patching object attributes
class MyClass:
    def method(self):
        return "original"

def test_patch_object():
    obj = MyClass()
    
    with patch.object(obj, 'method', return_value="mocked"):
        assert obj.method() == "mocked"
```

### pytest-mock

```bash
pip install pytest-mock
```

```python
# Using mocker fixture
def test_with_mocker(mocker):
    mock_request = mocker.patch('requests.get')
    mock_request.return_value.json.return_value = {"data": "test"}
    
    # Your test code
    import requests
    response = requests.get("https://example.com")
    
    assert response.json() == {"data": "test"}

# Spy on real objects
def test_spy(mocker):
    my_list = [1, 2, 3]
    spy = mocker.spy(my_list, 'append')
    
    my_list.append(4)
    
    spy.assert_called_once_with(4)
    assert my_list == [1, 2, 3, 4]  # Real method was called
```

---

## Test-Driven Development (TDD)

### TDD Cycle

```
1. RED   - Write a failing test
2. GREEN - Write minimum code to pass
3. REFACTOR - Improve the code
```

### TDD Example

```python
# Step 1: Write failing test
# test_shopping_cart.py
from shopping_cart import ShoppingCart

def test_cart_starts_empty():
    cart = ShoppingCart()
    assert cart.total == 0
    assert len(cart.items) == 0

# Step 2: Write minimum code to pass
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

# Step 3: Write next failing test
def test_add_item():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    assert len(cart.items) == 1
    assert cart.total == 1.50

# Step 4: Implement to pass
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        self.total += price

# Continue the cycle...
def test_add_multiple_items():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    assert len(cart.items) == 2
    assert cart.total == 2.25

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    cart.remove_item("Apple")
    assert len(cart.items) == 0
    assert cart.total == 0
```

---

## Testing Best Practices

### Test Organization

```
project/
├── src/
│   └── myapp/
│       ├── __init__.py
│       ├── models.py
│       └── services.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   └── test_services.py
│   └── integration/
│       ├── __init__.py
│       └── test_api.py
├── pytest.ini
└── requirements.txt
```

### FIRST Principles

```python
# F - Fast: Tests should run quickly
def test_fast():
    result = add(1, 2)  # No I/O, no sleep
    assert result == 3

# I - Independent: Tests shouldn't depend on each other
def test_independent_a():
    user = create_user("Alice")
    assert user.name == "Alice"

def test_independent_b():
    user = create_user("Bob")  # Doesn't depend on test_a
    assert user.name == "Bob"

# R - Repeatable: Same result every time
@pytest.fixture
def fixed_time(mocker):
    mocker.patch('time.time', return_value=1234567890)
    return 1234567890

# S - Self-validating: Pass or fail, no manual checking
def test_self_validating():
    result = process_data([1, 2, 3])
    assert result == [2, 4, 6]  # Clear pass/fail

# T - Timely: Write tests at the right time (TDD)
```

### AAA Pattern

```python
def test_aaa_pattern():
    # Arrange - Set up test data
    user = User(name="John", age=30)
    
    # Act - Perform the action
    greeting = user.greet()
    
    # Assert - Verify the result
    assert greeting == "Hello, I'm John!"
```

### Good Test Names

```python
# Bad names
def test_1():
    pass

def test_user():
    pass

# Good names - describe what is being tested
def test_user_with_empty_name_raises_validation_error():
    pass

def test_login_with_valid_credentials_returns_token():
    pass

def test_calculate_total_with_discount_applies_percentage():
    pass
```

---

## Code Coverage

### Using pytest-cov

```bash
pip install pytest-cov
```

```bash
# Run with coverage
pytest --cov=myapp tests/

# Generate HTML report
pytest --cov=myapp --cov-report=html tests/

# Show missing lines
pytest --cov=myapp --cov-report=term-missing tests/

# Minimum coverage threshold
pytest --cov=myapp --cov-fail-under=80 tests/
```

### Coverage Configuration

```ini
# .coveragerc
[run]
source = myapp
omit = 
    */tests/*
    */migrations/*
    */__init__.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
    if __name__ == .__main__.:
```

---

## Testing Web Applications

### Testing Flask

```python
import pytest
from myapp import create_app

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_api_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_api_create_user(client):
    response = client.post('/api/users', json={
        'name': 'John',
        'email': 'john@example.com'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'John'
```

### Testing FastAPI

```python
from fastapi.testclient import TestClient
from myapp import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Widget", "price": 9.99}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Widget"

# Async testing
import pytest

@pytest.mark.anyio
async def test_async_endpoint():
    from httpx import AsyncClient
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/async-endpoint")
    assert response.status_code == 200
```

### Testing Django

```python
from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class UserTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )
    
    def test_user_list_view(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")
    
    def test_user_create(self):
        response = self.client.post(reverse('user-create'), {
            'name': 'New User',
            'email': 'new@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(User.objects.filter(email='new@example.com').exists())
```

---

## Summary

| Tool | Purpose | When to Use |
|------|---------|-------------|
| unittest | Built-in testing | Simple projects, no deps needed |
| pytest | Full-featured testing | Most projects, recommended |
| mock | Isolate dependencies | When testing with external deps |
| coverage | Measure test coverage | All projects |

### Testing Pyramid

```
         /\
        /E2E\         <- Few end-to-end tests
       /------\
      / Integr \      <- Some integration tests
     /----------\
    /   Unit     \    <- Many unit tests
   /--------------\
```

### Key Takeaways

1. **Write tests first** (TDD) when possible
2. **Keep tests simple** - one assertion per test ideally
3. **Use descriptive names** - tests are documentation
4. **Mock external dependencies** - tests should be reliable
5. **Aim for high coverage** - but don't obsess over 100%
6. **Run tests automatically** - CI/CD integration

## Next Steps

Continue to [Best Practices](14-best-practices.md) to learn about writing clean, maintainable Python code.
