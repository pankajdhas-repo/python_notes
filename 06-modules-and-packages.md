# Modules and Packages

Modules and packages help organize code into reusable, maintainable units.

---

## What are Modules?

A module is a Python file (`.py`) containing functions, classes, and variables that can be imported and used in other files.

### Creating a Module

```python
# mymodule.py

"""A simple example module."""

PI = 3.14159

def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

class Calculator:
    """A simple calculator class."""
    
    def multiply(self, a, b):
        return a * b
```

### Using a Module

```python
# main.py

# Import the entire module
import mymodule

print(mymodule.PI)              # 3.14159
print(mymodule.greet("Alice"))  # Hello, Alice!
print(mymodule.add(3, 5))       # 8

calc = mymodule.Calculator()
print(calc.multiply(4, 5))      # 20
```

---

## Import Statements

### Import Variations

```python
# Import entire module
import math
print(math.sqrt(16))  # 4.0

# Import with alias
import numpy as np
print(np.array([1, 2, 3]))

# Import specific items
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793

# Import with alias
from math import sqrt as square_root
print(square_root(16))  # 4.0

# Import all (not recommended)
from math import *
print(sin(0))  # 0.0
print(cos(0))  # 1.0
```

### Why Avoid `from module import *`?

```python
# Problem: Namespace pollution
from module1 import *
from module2 import *
# If both have function 'process', which one are we using?

# Problem: Unclear origins
result = mysterious_function()  # Where does this come from?

# Better:
import module1
import module2
result = module1.process(data)  # Clear origin
```

---

## Module Search Path

When you import a module, Python searches in this order:

1. **Current directory**
2. **PYTHONPATH** environment variable directories
3. **Standard library** directories
4. **Site-packages** (installed packages)

```python
import sys

# View search path
for path in sys.path:
    print(path)

# Add to search path (temporary)
sys.path.append('/path/to/my/modules')
```

---

## The `__name__` Variable

Every module has a `__name__` attribute:
- If the module is run directly: `__name__ == "__main__"`
- If the module is imported: `__name__ == "module_name"`

```python
# mymodule.py

def main():
    print("Running main function")

def helper():
    print("Helper function")

# Only runs when executed directly, not when imported
if __name__ == "__main__":
    print("Running as main script")
    main()
```

```bash
python mymodule.py      # Prints: Running as main script
                        #         Running main function
```

```python
import mymodule         # Nothing printed
mymodule.main()         # Running main function
```

---

## Packages

A package is a directory containing Python modules and a special `__init__.py` file.

### Package Structure

```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

### Creating a Package

```python
# mypackage/__init__.py
"""My package initialization."""

from .module1 import function1
from .module2 import function2

__version__ = "1.0.0"
__all__ = ['function1', 'function2']
```

```python
# mypackage/module1.py
def function1():
    return "Function 1"

def helper():
    return "Helper"
```

```python
# mypackage/module2.py
def function2():
    return "Function 2"
```

### Using a Package

```python
# Import entire package
import mypackage
print(mypackage.function1())

# Import specific module
from mypackage import module1
print(module1.function1())

# Import specific function
from mypackage.module1 import function1
print(function1())

# Import from subpackage
from mypackage.subpackage import module3
from mypackage.subpackage.module3 import some_function
```

### Relative Imports (Within a Package)

```python
# mypackage/module2.py

# Absolute import
from mypackage.module1 import function1

# Relative import (preferred within packages)
from .module1 import function1       # Same directory
from ..module1 import function1      # Parent directory
from .subpackage import module3      # Subpackage
```

---

## Python Standard Library

Python comes with a rich standard library. Here are some commonly used modules:

### Math Operations

```python
import math

# Constants
print(math.pi)        # 3.141592653589793
print(math.e)         # 2.718281828459045

# Functions
print(math.sqrt(16))  # 4.0
print(math.pow(2, 3)) # 8.0
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4
print(math.factorial(5))  # 120
print(math.gcd(48, 18))   # 6

# Trigonometry
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))            # 1.0
print(math.degrees(math.pi))  # 180.0
print(math.radians(180))      # 3.14159...
```

### Random Numbers

```python
import random

# Random float [0.0, 1.0)
print(random.random())

# Random integer
print(random.randint(1, 10))  # 1 to 10 inclusive
print(random.randrange(1, 10))  # 1 to 9

# Random choice
colors = ['red', 'green', 'blue']
print(random.choice(colors))

# Random sample (without replacement)
print(random.sample(range(100), 5))

# Shuffle list in place
cards = list(range(1, 14))
random.shuffle(cards)
print(cards)

# Reproducible randomness
random.seed(42)
print(random.random())  # Always the same value
```

### Date and Time

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# Specific date
d = date(2024, 1, 15)
print(d)  # 2024-01-15

# Specific time
t = time(14, 30, 45)
print(t)  # 14:30:45

# Formatting
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-01-15 14:30:45
print(now.strftime("%B %d, %Y"))          # January 15, 2024

# Parsing
date_str = "2024-01-15"
parsed = datetime.strptime(date_str, "%Y-%m-%d")

# Date arithmetic
tomorrow = date.today() + timedelta(days=1)
next_week = datetime.now() + timedelta(weeks=1)
difference = date(2024, 12, 31) - date.today()
print(difference.days)  # Days until New Year
```

### Operating System

```python
import os

# Current directory
print(os.getcwd())

# Change directory
os.chdir('/path/to/directory')

# List directory
print(os.listdir('.'))

# Create directory
os.mkdir('new_folder')
os.makedirs('path/to/nested/folder')  # Create parents too

# Remove
os.remove('file.txt')
os.rmdir('empty_folder')

# Path operations
print(os.path.exists('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('folder'))
print(os.path.join('folder', 'subfolder', 'file.txt'))
print(os.path.basename('/path/to/file.txt'))  # file.txt
print(os.path.dirname('/path/to/file.txt'))   # /path/to

# Environment variables
print(os.environ.get('HOME'))
os.environ['MY_VAR'] = 'value'
```

### Path Operations (Modern Way)

```python
from pathlib import Path

# Create path object
p = Path('/home/user/documents')
p = Path.home() / 'documents'  # User's home + documents

# Path operations
print(p.exists())
print(p.is_file())
print(p.is_dir())
print(p.name)      # documents
print(p.parent)    # /home/user
print(p.suffix)    # File extension

# Iterate directory
for item in p.iterdir():
    print(item)

# Glob patterns
for py_file in Path('.').glob('**/*.py'):
    print(py_file)

# Read/write files
content = p.read_text()
p.write_text('content')
```

### JSON

```python
import json

# Python to JSON
data = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'coding']
}

# To JSON string
json_str = json.dumps(data)
print(json_str)

# Pretty print
json_str = json.dumps(data, indent=2)
print(json_str)

# JSON to Python
parsed = json.loads(json_str)
print(parsed['name'])

# File operations
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('data.json', 'r') as f:
    loaded = json.load(f)
```

### Regular Expressions

```python
import re

text = "My email is john@example.com and phone is 123-456-7890"

# Search
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
if match:
    print(match.group())  # 123-456-7890

# Find all
emails = re.findall(r'[\w.-]+@[\w.-]+', text)
print(emails)  # ['john@example.com']

# Replace
new_text = re.sub(r'\d', 'X', text)
print(new_text)  # Phone becomes XXX-XXX-XXXX

# Split
parts = re.split(r'\s+', "Hello   World")
print(parts)  # ['Hello', 'World']

# Compile pattern (for reuse)
pattern = re.compile(r'\d+')
matches = pattern.findall("abc 123 def 456")
print(matches)  # ['123', '456']
```

---

## Installing Packages with pip

pip is Python's package installer.

### Basic Commands

```bash
# Install package
pip install package_name
pip install numpy pandas matplotlib

# Install specific version
pip install package_name==1.2.3
pip install "package_name>=1.0,<2.0"

# Upgrade package
pip install --upgrade package_name

# Uninstall
pip uninstall package_name

# List installed packages
pip list

# Show package info
pip show package_name

# Search packages (deprecated in recent pip)
pip search package_name

# Install from requirements file
pip install -r requirements.txt

# Generate requirements file
pip freeze > requirements.txt
```

### requirements.txt

```text
# requirements.txt
numpy==1.21.0
pandas>=1.3.0
requests~=2.26.0
matplotlib
flask>=2.0,<3.0
```

---

## Virtual Environments

Virtual environments isolate project dependencies.

### Creating and Using venv

```bash
# Create virtual environment
python -m venv myenv

# Activate (macOS/Linux)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Deactivate
deactivate

# Install packages (in activated env)
pip install numpy pandas
```

### Project Structure with venv

```
my_project/
├── venv/                  # Virtual environment (don't commit)
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### .gitignore for Python

```gitignore
# Virtual environments
venv/
.venv/
env/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Distribution
dist/
build/
*.egg-info/

# IDE
.vscode/
.idea/

# Environment variables
.env
```

---

## Package Management with Poetry

Poetry is a modern dependency management tool.

```bash
# Install poetry
pip install poetry

# Create new project
poetry new myproject

# Initialize in existing project
poetry init

# Add dependencies
poetry add numpy pandas
poetry add pytest --dev

# Install dependencies
poetry install

# Run scripts
poetry run python script.py

# Activate shell
poetry shell
```

### pyproject.toml

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My awesome project"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
numpy = "^1.21.0"
pandas = "^1.3.0"

[tool.poetry.dev-dependencies]
pytest = "^7.0"
black = "^22.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

## Creating Distributable Packages

### Package Structure

```
mypackage/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
└── tests/
    ├── __init__.py
    └── test_module1.py
```

### pyproject.toml (Modern)

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A sample Python package"
readme = "README.md"
license = {file = "LICENSE"}
authors = [
    {name = "Your Name", email = "you@example.com"}
]
requires-python = ">=3.8"
dependencies = [
    "requests>=2.25.0",
    "numpy>=1.20.0",
]

[project.optional-dependencies]
dev = ["pytest", "black", "mypy"]

[project.scripts]
mycommand = "mypackage.cli:main"
```

### Building and Publishing

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*

# Upload to PyPI (need account)
twine upload dist/*

# Upload to TestPyPI first
twine upload --repository testpypi dist/*
```

---

## Common Third-Party Packages

### Data Science

```python
# NumPy - Numerical computing
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())

# Pandas - Data analysis
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.describe())

# Matplotlib - Visualization
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### Web Development

```python
# Requests - HTTP library
import requests
response = requests.get('https://api.github.com')
data = response.json()

# Flask - Web framework
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
```

### Testing

```python
# pytest
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

---

## Summary

- **Modules** are Python files that can be imported
- **Packages** are directories containing modules and `__init__.py`
- Use `import` statements to bring in code from modules
- The **standard library** provides many useful built-in modules
- **pip** installs third-party packages from PyPI
- **Virtual environments** isolate project dependencies
- Use `requirements.txt` or `pyproject.toml` for dependency management

## Next Steps

Continue to [Object-Oriented Programming](07-object-oriented-programming.md) to learn about classes and OOP concepts.
