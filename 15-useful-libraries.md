# Useful Libraries

This chapter covers essential Python standard library modules and popular third-party libraries that every Python developer should know.

---

## Standard Library Essentials

### os - Operating System Interface

```python
import os

# Working directory
print(os.getcwd())          # Get current directory
os.chdir('/path/to/dir')    # Change directory

# Environment variables
print(os.environ.get('HOME'))
os.environ['MY_VAR'] = 'value'

# Path operations
print(os.path.exists('/path/to/file'))
print(os.path.isfile('/path/to/file'))
print(os.path.isdir('/path/to/dir'))
print(os.path.join('dir', 'subdir', 'file.txt'))
print(os.path.basename('/path/to/file.txt'))  # file.txt
print(os.path.dirname('/path/to/file.txt'))   # /path/to
print(os.path.splitext('file.txt'))           # ('file', '.txt')

# Directory operations
os.mkdir('new_dir')              # Create directory
os.makedirs('path/to/new_dir')   # Create nested directories
os.rmdir('empty_dir')            # Remove empty directory
os.listdir('.')                  # List directory contents

# File operations
os.rename('old.txt', 'new.txt')
os.remove('file.txt')

# Execute commands
os.system('echo "Hello"')        # Run shell command
```

### sys - System-Specific Parameters

```python
import sys

# Python info
print(sys.version)              # Python version
print(sys.version_info)         # Version tuple
print(sys.platform)             # Platform (linux, darwin, win32)
print(sys.executable)           # Python executable path

# Command line arguments
print(sys.argv)                 # List of arguments
# python script.py arg1 arg2
# sys.argv = ['script.py', 'arg1', 'arg2']

# Path
print(sys.path)                 # Module search paths
sys.path.append('/custom/path') # Add custom path

# Exit
sys.exit(0)                     # Exit with code 0 (success)
sys.exit(1)                     # Exit with code 1 (error)

# Standard streams
sys.stdin                       # Standard input
sys.stdout                      # Standard output
sys.stderr                      # Standard error

# Redirect output
original_stdout = sys.stdout
sys.stdout = open('output.txt', 'w')
print("This goes to file")
sys.stdout = original_stdout
```

### pathlib - Modern Path Handling

```python
from pathlib import Path

# Create path objects
p = Path('/home/user/documents')
p = Path.cwd()              # Current directory
p = Path.home()             # Home directory

# Path operations
p = Path('/home/user/file.txt')
print(p.name)               # file.txt
print(p.stem)               # file
print(p.suffix)             # .txt
print(p.parent)             # /home/user
print(p.parts)              # ('/', 'home', 'user', 'file.txt')

# Build paths
new_path = p.parent / 'new_file.txt'
print(new_path)             # /home/user/new_file.txt

# Check existence
print(p.exists())
print(p.is_file())
print(p.is_dir())

# Directory operations
p = Path('.')
for item in p.iterdir():
    print(item)

# Glob patterns
for py_file in Path('.').glob('**/*.py'):
    print(py_file)

# File operations
p = Path('example.txt')
p.write_text('Hello, World!')
content = p.read_text()
p.unlink()                  # Delete file

# Create directories
Path('new/nested/dir').mkdir(parents=True, exist_ok=True)
```

### datetime - Date and Time

```python
from datetime import datetime, date, time, timedelta
import time as time_module

# Current date/time
now = datetime.now()
today = date.today()
utc_now = datetime.utcnow()

print(now)                  # 2024-01-15 10:30:45.123456
print(today)                # 2024-01-15

# Create specific date/time
dt = datetime(2024, 1, 15, 10, 30, 45)
d = date(2024, 1, 15)
t = time(10, 30, 45)

# Access components
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
print(now.weekday())        # 0=Monday, 6=Sunday
print(now.isoweekday())     # 1=Monday, 7=Sunday

# Formatting
print(now.strftime('%Y-%m-%d'))         # 2024-01-15
print(now.strftime('%B %d, %Y'))        # January 15, 2024
print(now.strftime('%H:%M:%S'))         # 10:30:45
print(now.strftime('%I:%M %p'))         # 10:30 AM

# Common format codes:
# %Y - 4-digit year     %y - 2-digit year
# %m - month (01-12)    %B - full month name
# %d - day (01-31)      %A - full weekday name
# %H - hour (00-23)     %I - hour (01-12)
# %M - minute (00-59)   %S - second (00-59)
# %p - AM/PM

# Parsing
dt = datetime.strptime('2024-01-15', '%Y-%m-%d')
dt = datetime.strptime('January 15, 2024', '%B %d, %Y')

# Time arithmetic
tomorrow = today + timedelta(days=1)
next_week = now + timedelta(weeks=1)
two_hours_ago = now - timedelta(hours=2)

# Difference
diff = datetime(2024, 12, 31) - now
print(diff.days)            # Days until New Year

# Timestamps
timestamp = now.timestamp()
dt = datetime.fromtimestamp(timestamp)

# ISO format
iso_string = now.isoformat()
dt = datetime.fromisoformat(iso_string)
```

### collections - Specialized Containers

```python
from collections import (
    Counter, defaultdict, OrderedDict, 
    namedtuple, deque, ChainMap
)

# Counter - count occurrences
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(counter)                    # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counter.most_common(2))     # [('apple', 3), ('banana', 2)]
counter['orange'] += 1            # Increment count

# defaultdict - dictionary with default values
dd = defaultdict(list)
dd['fruits'].append('apple')      # No KeyError
dd['fruits'].append('banana')
print(dd)                         # {'fruits': ['apple', 'banana']}

dd = defaultdict(int)
dd['count'] += 1                  # Default 0

dd = defaultdict(lambda: 'unknown')
print(dd['missing'])              # 'unknown'

# OrderedDict (maintains insertion order - less needed in Python 3.7+)
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od.move_to_end('first')           # Move to end

# namedtuple - tuple with named fields
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)                   # 3 4
print(p[0], p[1])                 # 3 4
x, y = p                          # Unpacking works

# With defaults
Point = namedtuple('Point', ['x', 'y', 'z'], defaults=[0])
p = Point(1, 2)                   # z defaults to 0

# deque - double-ended queue
dq = deque([1, 2, 3])
dq.append(4)                      # Add right
dq.appendleft(0)                  # Add left
dq.pop()                          # Remove right
dq.popleft()                      # Remove left
dq.rotate(1)                      # Rotate right
dq.rotate(-1)                     # Rotate left

# Fixed-size deque
dq = deque(maxlen=3)
dq.extend([1, 2, 3, 4, 5])        # Only keeps last 3
print(list(dq))                   # [3, 4, 5]

# ChainMap - combine multiple dicts
defaults = {'color': 'red', 'size': 'medium'}
user_settings = {'color': 'blue'}
settings = ChainMap(user_settings, defaults)
print(settings['color'])          # blue (from user_settings)
print(settings['size'])           # medium (from defaults)
```

### itertools - Iterator Functions

```python
import itertools

# Infinite iterators
count = itertools.count(10, 2)    # 10, 12, 14, 16, ...
cycle = itertools.cycle('ABC')    # A, B, C, A, B, C, ...
repeat = itertools.repeat('X', 3) # X, X, X

# Terminating iterators
# chain - combine iterables
result = itertools.chain([1, 2], [3, 4], [5])
print(list(result))               # [1, 2, 3, 4, 5]

# compress - filter based on selectors
data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]
print(list(itertools.compress(data, selectors)))  # ['A', 'C']

# dropwhile / takewhile
nums = [1, 3, 5, 7, 4, 6, 8]
print(list(itertools.dropwhile(lambda x: x < 5, nums)))  # [5, 7, 4, 6, 8]
print(list(itertools.takewhile(lambda x: x < 5, nums)))  # [1, 3]

# groupby
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# islice - slice iterator
print(list(itertools.islice(range(100), 5, 10)))  # [5, 6, 7, 8, 9]

# Combinatoric iterators
# product - Cartesian product
print(list(itertools.product('AB', '12')))
# [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

# permutations
print(list(itertools.permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations
print(list(itertools.combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# combinations_with_replacement
print(list(itertools.combinations_with_replacement('AB', 2)))
# [('A', 'A'), ('A', 'B'), ('B', 'B')]

# accumulate
print(list(itertools.accumulate([1, 2, 3, 4])))  # [1, 3, 6, 10]
```

### functools - Higher-Order Functions

```python
from functools import (
    reduce, partial, lru_cache, 
    wraps, total_ordering, cached_property
)

# reduce - apply function cumulatively
from functools import reduce
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 10
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24

# partial - fix some arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(5))                  # 25
print(cube(3))                    # 27

# lru_cache - memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))             # Fast due to caching
print(fibonacci.cache_info())     # Cache statistics

# wraps - preserve function metadata in decorators
def my_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# total_ordering - complete comparison methods
@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    # __le__, __gt__, __ge__ are auto-generated

# cached_property (Python 3.8+)
class DataProcessor:
    @cached_property
    def expensive_data(self):
        # Only computed once
        return self._load_data()
```

### json - JSON Encoding/Decoding

```python
import json

# Python to JSON
data = {
    'name': 'Alice',
    'age': 30,
    'active': True,
    'scores': [95, 87, 92]
}

json_string = json.dumps(data)
print(json_string)

# Pretty print
json_pretty = json.dumps(data, indent=2, sort_keys=True)
print(json_pretty)

# JSON to Python
data = json.loads(json_string)
print(data['name'])

# File operations
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('data.json', 'r') as f:
    data = json.load(f)

# Custom encoder
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps({'date': datetime.now()}, cls=DateEncoder)

# Custom decoder
def date_decoder(dct):
    for key, value in dct.items():
        try:
            dct[key] = datetime.fromisoformat(value)
        except (ValueError, TypeError):
            pass
    return dct

data = json.loads(json_string, object_hook=date_decoder)
```

### re - Regular Expressions

```python
import re

text = "Contact: john@example.com or jane@test.org"

# Search - find first match
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group())          # john@example.com
    print(match.start(), match.end())

# Find all matches
emails = re.findall(r'\w+@\w+\.\w+', text)
print(emails)                     # ['john@example.com', 'jane@test.org']

# Substitution
new_text = re.sub(r'\w+@\w+\.\w+', '[EMAIL]', text)
print(new_text)

# Split
parts = re.split(r'[,;:\s]+', "a, b; c: d e")
print(parts)                      # ['a', 'b', 'c', 'd', 'e']

# Compile for reuse
email_pattern = re.compile(r'''
    [\w.-]+     # username
    @           # @ symbol
    [\w.-]+     # domain
    \.          # dot
    \w+         # TLD
''', re.VERBOSE)

matches = email_pattern.findall(text)

# Groups
pattern = r'(\w+)@(\w+)\.(\w+)'
match = re.search(pattern, text)
if match:
    print(match.groups())         # ('john', 'example', 'com')
    print(match.group(1))         # john

# Named groups
pattern = r'(?P<user>\w+)@(?P<domain>\w+)\.(?P<tld>\w+)'
match = re.search(pattern, text)
if match:
    print(match.group('user'))    # john
    print(match.groupdict())      # {'user': 'john', 'domain': 'example', 'tld': 'com'}
```

### argparse - Command Line Arguments

```python
import argparse

parser = argparse.ArgumentParser(
    description='Process some files.'
)

# Positional argument
parser.add_argument('filename', help='File to process')

# Optional arguments
parser.add_argument('-v', '--verbose', 
                    action='store_true',
                    help='Enable verbose output')

parser.add_argument('-n', '--number',
                    type=int,
                    default=10,
                    help='Number of items (default: 10)')

parser.add_argument('-o', '--output',
                    required=True,
                    help='Output file')

parser.add_argument('--mode',
                    choices=['fast', 'slow', 'normal'],
                    default='normal',
                    help='Processing mode')

parser.add_argument('--files',
                    nargs='+',
                    help='Multiple files')

# Parse arguments
args = parser.parse_args()

print(f"Processing: {args.filename}")
print(f"Verbose: {args.verbose}")
print(f"Number: {args.number}")
print(f"Output: {args.output}")
print(f"Mode: {args.mode}")

# Usage: python script.py input.txt -o output.txt -v -n 20
```

### subprocess - Run External Commands

```python
import subprocess

# Simple command
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)

# With shell
result = subprocess.run('echo "Hello World"', shell=True, capture_output=True, text=True)

# Check for errors
try:
    result = subprocess.run(['ls', '/nonexistent'], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with code {e.returncode}")

# Pipe input
result = subprocess.run(
    ['grep', 'python'],
    input='python is great\njava is ok\npython rules',
    capture_output=True,
    text=True
)
print(result.stdout)

# Streaming output
process = subprocess.Popen(
    ['ping', '-c', '3', 'google.com'],
    stdout=subprocess.PIPE,
    text=True
)

for line in process.stdout:
    print(line, end='')

process.wait()
```

### shutil - High-Level File Operations

```python
import shutil

# Copy files
shutil.copy('source.txt', 'dest.txt')           # Copy file
shutil.copy2('source.txt', 'dest.txt')          # Copy with metadata
shutil.copyfile('source.txt', 'dest.txt')       # Copy content only

# Copy directory
shutil.copytree('source_dir', 'dest_dir')

# Move/rename
shutil.move('old_name', 'new_name')

# Remove directory tree
shutil.rmtree('directory')

# Disk usage
total, used, free = shutil.disk_usage('/')
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

# Archive operations
shutil.make_archive('archive', 'zip', 'directory')
shutil.unpack_archive('archive.zip', 'extract_dir')

# Find executables
python_path = shutil.which('python')
print(python_path)
```

### secrets - Cryptographically Secure Random

```python
import secrets

# Generate secure tokens
token = secrets.token_hex(32)         # 64-char hex string
token = secrets.token_urlsafe(32)     # URL-safe base64 string
token = secrets.token_bytes(32)       # 32 random bytes

# Secure random numbers
num = secrets.randbelow(100)          # Random int 0-99
bit = secrets.randbits(8)             # Random 8-bit int

# Secure choice
password_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%'
password = ''.join(secrets.choice(password_chars) for _ in range(16))

# Compare strings securely (constant time)
secrets.compare_digest(token1, token2)
```

---

## Popular Third-Party Libraries

### HTTP Requests

```bash
pip install requests httpx
```

```python
# requests - synchronous HTTP
import requests

response = requests.get('https://api.github.com')
response = requests.post('https://api.example.com', json={'key': 'value'})
response = requests.get('https://api.example.com', headers={'Authorization': 'Bearer token'})

# httpx - async HTTP
import httpx
import asyncio

async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.github.com')
        return response.json()

result = asyncio.run(fetch())
```

### Data Validation

```bash
pip install pydantic
```

```python
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None
    tags: List[str] = []
    created_at: datetime = datetime.now()
    
    @validator('age')
    def age_must_be_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError('Age must be positive')
        return v

# Validation
user = User(id=1, name='Alice', email='alice@example.com')
print(user.json())
print(user.dict())

# From JSON
user = User.parse_raw('{"id": 1, "name": "Bob", "email": "bob@example.com"}')
```

### CLI Tools

```bash
pip install click typer rich
```

```python
# click
import click

@click.command()
@click.option('--name', prompt='Your name', help='Name to greet')
@click.option('--count', default=1, help='Number of greetings')
def hello(name, count):
    for _ in range(count):
        click.echo(f'Hello, {name}!')

# typer (modern, type-hint based)
import typer

app = typer.Typer()

@app.command()
def hello(name: str, count: int = 1):
    for _ in range(count):
        typer.echo(f'Hello, {name}!')

# rich (beautiful terminal output)
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()
console.print("[bold red]Error![/bold red] Something went wrong.")

table = Table(title="Users")
table.add_column("Name")
table.add_column("Email")
table.add_row("Alice", "alice@example.com")
console.print(table)
```

### Database

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)

# Setup
engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# CRUD
user = User(name='Alice', email='alice@example.com')
session.add(user)
session.commit()

users = session.query(User).filter(User.name.like('%Alice%')).all()
```

### Environment Variables

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file

DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
```

---

## Summary

### Standard Library Quick Reference

| Module | Purpose |
|--------|---------|
| os | Operating system interface |
| sys | System-specific parameters |
| pathlib | Modern path handling |
| datetime | Date and time operations |
| collections | Specialized containers |
| itertools | Iterator functions |
| functools | Higher-order functions |
| json | JSON encoding/decoding |
| re | Regular expressions |
| argparse | Command line parsing |
| subprocess | Run external commands |
| shutil | High-level file operations |
| secrets | Secure random generation |

### Popular Third-Party Libraries

| Library | Purpose |
|---------|---------|
| requests/httpx | HTTP requests |
| pydantic | Data validation |
| click/typer | CLI applications |
| rich | Beautiful terminal output |
| sqlalchemy | Database ORM |
| python-dotenv | Environment variables |

## Conclusion

Congratulations! You've completed this Python learning resource. You now have a solid foundation in Python programming, from basics to advanced topics. Keep practicing and building projects to reinforce your knowledge.

### What's Next?

1. **Build projects** - Apply what you've learned
2. **Contribute to open source** - Learn from real codebases
3. **Explore specializations** - Web dev, data science, ML, automation
4. **Read the official docs** - [docs.python.org](https://docs.python.org)
5. **Join communities** - Python Discord, Reddit r/learnpython

Happy coding! 🐍
