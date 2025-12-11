# File Handling

File handling allows you to read from and write to files, enabling data persistence in your programs.

---

## Opening Files

### The open() Function

```python
# Basic syntax
file = open('filename.txt', 'mode')

# Always close files when done
file.close()
```

### File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) - file must exist |
| `'w'` | Write - creates new file or truncates existing |
| `'a'` | Append - creates new file or appends to existing |
| `'x'` | Exclusive create - fails if file exists |
| `'b'` | Binary mode (e.g., `'rb'`, `'wb'`) |
| `'t'` | Text mode (default) |
| `'+'` | Read and write (e.g., `'r+'`, `'w+'`) |

```python
# Examples
f = open('file.txt', 'r')   # Read text
f = open('file.txt', 'w')   # Write text (overwrites)
f = open('file.txt', 'a')   # Append text
f = open('image.png', 'rb') # Read binary
f = open('data.bin', 'wb')  # Write binary
f = open('file.txt', 'r+')  # Read and write
```

---

## Context Managers (with statement)

The `with` statement automatically closes files, even if an error occurs.

```python
# Recommended way - auto-closes file
with open('file.txt', 'r') as f:
    content = f.read()
# File is automatically closed here

# Without with statement - must manually close
f = open('file.txt', 'r')
try:
    content = f.read()
finally:
    f.close()

# Multiple files
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())
```

---

## Reading Files

### read() - Read Entire File

```python
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# Read specific number of characters
with open('file.txt', 'r') as f:
    first_10 = f.read(10)  # Read first 10 characters
    next_10 = f.read(10)   # Read next 10 characters
```

### readline() - Read One Line

```python
with open('file.txt', 'r') as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
    print(line1)
    print(line2)
```

### readlines() - Read All Lines into List

```python
with open('file.txt', 'r') as f:
    lines = f.readlines()  # List of all lines
    
for line in lines:
    print(line.strip())  # Remove trailing newline
```

### Iterating Over Lines (Memory Efficient)

```python
# Best for large files - reads one line at a time
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Process large files without loading entirely into memory
with open('large_file.txt', 'r') as f:
    for line_number, line in enumerate(f, 1):
        if 'error' in line.lower():
            print(f"Line {line_number}: {line.strip()}")
```

---

## Writing Files

### write() - Write String

```python
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('This is line 2.\n')

# write() returns number of characters written
with open('output.txt', 'w') as f:
    chars_written = f.write('Hello!')
    print(chars_written)  # 6
```

### writelines() - Write List of Strings

```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']

with open('output.txt', 'w') as f:
    f.writelines(lines)

# Note: writelines() doesn't add newlines automatically
lines = ['Line 1', 'Line 2', 'Line 3']
with open('output.txt', 'w') as f:
    f.writelines(line + '\n' for line in lines)
```

### print() to File

```python
with open('output.txt', 'w') as f:
    print('Hello, World!', file=f)
    print('Line 2', file=f)
    print('Number:', 42, file=f)
```

---

## Appending to Files

```python
# Append mode - adds to end of file
with open('log.txt', 'a') as f:
    f.write('New log entry\n')

# Append multiple lines
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a') as f:
        f.write(f'[{timestamp}] {message}\n')

log_message('Application started')
log_message('Processing data...')
log_message('Application finished')
```

---

## File Position

```python
with open('file.txt', 'r') as f:
    # Get current position
    print(f.tell())  # 0
    
    f.read(10)
    print(f.tell())  # 10
    
    # Move to position
    f.seek(0)        # Go to beginning
    print(f.tell())  # 0
    
    f.seek(5)        # Go to position 5
    f.seek(0, 2)     # Go to end (0 bytes from end)
```

### seek() Modes

```python
# seek(offset, whence)
# whence: 0 = beginning, 1 = current, 2 = end

with open('file.txt', 'rb') as f:  # Binary mode for whence=1,2
    f.seek(0)       # Beginning of file
    f.seek(10, 0)   # 10 bytes from beginning
    f.seek(5, 1)    # 5 bytes from current position
    f.seek(-10, 2)  # 10 bytes before end
```

---

## Working with Binary Files

```python
# Reading binary files
with open('image.png', 'rb') as f:
    data = f.read()
    print(len(data), 'bytes')
    print(data[:10])  # First 10 bytes

# Writing binary files
with open('copy.png', 'wb') as f:
    f.write(data)

# Copy binary file
def copy_file(source, destination):
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        while chunk := src.read(8192):  # Read in chunks
            dst.write(chunk)

copy_file('original.png', 'copy.png')
```

---

## Working with CSV Files

### Using the csv Module

```python
import csv

# Writing CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Writing one row at a time
with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])  # Header
    writer.writerow(['Alice', 25, 'New York'])
    writer.writerow(['Bob', 30, 'Los Angeles'])

# Reading CSV
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Skip header
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    for row in reader:
        name, age, city = row
        print(f'{name} is {age} years old')
```

### CSV with Dictionaries

```python
import csv

# Writing with DictWriter
people = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

with open('people.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people)

# Reading with DictReader
with open('people.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # OrderedDict
        print(f"{row['name']} lives in {row['city']}")
```

### CSV with Different Delimiters

```python
import csv

# Tab-separated values
with open('data.tsv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(data)

# Custom delimiter
with open('data.txt', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='|', quotechar='"')
    writer.writerows(data)
```

---

## Working with JSON Files

```python
import json

# Python object to JSON
data = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'coding'],
    'address': {
        'city': 'New York',
        'zip': '10001'
    }
}

# Write to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Write with formatting
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)

# Read from JSON file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data['name'])

# JSON to string
json_string = json.dumps(data, indent=2)
print(json_string)

# String to Python object
parsed = json.loads(json_string)
```

### Handling Custom Objects

```python
import json
from datetime import datetime

class Person:
    def __init__(self, name, age, birth_date):
        self.name = name
        self.age = age
        self.birth_date = birth_date

# Custom encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {
                '__type__': 'Person',
                'name': obj.name,
                'age': obj.age,
                'birth_date': obj.birth_date.isoformat()
            }
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Custom decoder
def person_decoder(dct):
    if '__type__' in dct and dct['__type__'] == 'Person':
        return Person(
            dct['name'],
            dct['age'],
            datetime.fromisoformat(dct['birth_date'])
        )
    return dct

# Usage
person = Person('Alice', 25, datetime(1999, 5, 15))

# Encode
json_str = json.dumps(person, cls=PersonEncoder, indent=2)
print(json_str)

# Decode
loaded = json.loads(json_str, object_hook=person_decoder)
print(loaded.name)  # Alice
```

---

## Working with Other Formats

### YAML Files

```python
# pip install pyyaml
import yaml

data = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'coding']
}

# Write YAML
with open('data.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)

# Read YAML
with open('data.yaml', 'r') as f:
    loaded = yaml.safe_load(f)
    print(loaded)
```

### INI/Config Files

```python
import configparser

config = configparser.ConfigParser()

# Write config
config['DEFAULT'] = {
    'debug': 'false',
    'log_level': 'INFO'
}
config['database'] = {
    'host': 'localhost',
    'port': '5432',
    'name': 'mydb'
}

with open('config.ini', 'w') as f:
    config.write(f)

# Read config
config.read('config.ini')
print(config['database']['host'])  # localhost
print(config.getboolean('DEFAULT', 'debug'))  # False
```

### Pickle (Python Objects)

```python
import pickle

# Serialize Python objects
data = {
    'name': 'Alice',
    'numbers': [1, 2, 3],
    'nested': {'key': 'value'}
}

# Write pickle
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Read pickle
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)

# Warning: Only unpickle data you trust!
```

---

## Path Operations with pathlib

```python
from pathlib import Path

# Create path objects
p = Path('folder/subfolder/file.txt')
p = Path.home() / 'documents' / 'file.txt'
p = Path.cwd() / 'data'

# Path properties
print(p.name)       # file.txt
print(p.stem)       # file
print(p.suffix)     # .txt
print(p.parent)     # folder/subfolder
print(p.parts)      # ('folder', 'subfolder', 'file.txt')

# Check existence
print(p.exists())
print(p.is_file())
print(p.is_dir())

# Create directories
p = Path('new_folder/subfolder')
p.mkdir(parents=True, exist_ok=True)

# List directory contents
for item in Path('.').iterdir():
    print(item)

# Glob patterns
for py_file in Path('.').glob('**/*.py'):
    print(py_file)

# Read and write with pathlib
p = Path('file.txt')
p.write_text('Hello, World!')
content = p.read_text()

p.write_bytes(b'Binary data')
data = p.read_bytes()

# Delete
p.unlink()  # Delete file
p.rmdir()   # Delete empty directory
```

---

## File Operations with shutil

```python
import shutil

# Copy file
shutil.copy('source.txt', 'destination.txt')
shutil.copy2('source.txt', 'dest.txt')  # Preserves metadata

# Copy directory
shutil.copytree('source_dir', 'dest_dir')

# Move/rename
shutil.move('old_name.txt', 'new_name.txt')
shutil.move('file.txt', 'new_folder/file.txt')

# Delete directory and contents
shutil.rmtree('folder_to_delete')

# Get disk usage
total, used, free = shutil.disk_usage('/')
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

# Archive/extract
shutil.make_archive('archive', 'zip', 'folder_to_zip')
shutil.unpack_archive('archive.zip', 'extract_to')
```

---

## Temporary Files

```python
import tempfile

# Temporary file (auto-deleted when closed)
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write('Temporary data')
    temp_path = f.name
print(temp_path)  # Path to temp file

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print(tmpdir)  # Path to temp directory
    # Directory deleted after with block

# Get temp directory path
print(tempfile.gettempdir())  # /tmp or similar
```

---

## Error Handling for Files

```python
from pathlib import Path

# Check before opening
path = Path('file.txt')
if path.exists():
    content = path.read_text()
else:
    print('File not found')

# Try/except approach
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')
except IOError as e:
    print(f'IO error: {e}')

# Multiple exceptions
try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
except json.JSONDecodeError:
    print('Invalid JSON')
    data = {}
```

---

## Practical Examples

### Log File Analyzer

```python
from pathlib import Path
from collections import Counter
from datetime import datetime

def analyze_log(log_path):
    """Analyze a log file and return statistics."""
    error_count = 0
    warning_count = 0
    ip_addresses = Counter()
    
    with open(log_path, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                error_count += 1
            elif 'WARNING' in line:
                warning_count += 1
            
            # Extract IP address (simplified)
            parts = line.split()
            if parts:
                ip_addresses[parts[0]] += 1
    
    return {
        'errors': error_count,
        'warnings': warning_count,
        'top_ips': ip_addresses.most_common(5)
    }

# Usage
stats = analyze_log('access.log')
print(f"Errors: {stats['errors']}")
print(f"Warnings: {stats['warnings']}")
print(f"Top IPs: {stats['top_ips']}")
```

### Configuration Manager

```python
import json
from pathlib import Path

class ConfigManager:
    def __init__(self, config_path='config.json'):
        self.path = Path(config_path)
        self.config = self._load()
    
    def _load(self):
        if self.path.exists():
            return json.loads(self.path.read_text())
        return {}
    
    def save(self):
        self.path.write_text(json.dumps(self.config, indent=2))
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save()
    
    def delete(self, key):
        if key in self.config:
            del self.config[key]
            self.save()

# Usage
config = ConfigManager()
config.set('debug', True)
config.set('database', {'host': 'localhost', 'port': 5432})
print(config.get('debug'))  # True
```

### File Watcher

```python
import time
from pathlib import Path
from datetime import datetime

def watch_file(filepath, interval=1):
    """Watch a file for changes."""
    path = Path(filepath)
    last_modified = None
    
    print(f"Watching {filepath}...")
    
    while True:
        try:
            current_modified = path.stat().st_mtime
            
            if last_modified is None:
                last_modified = current_modified
            elif current_modified != last_modified:
                timestamp = datetime.fromtimestamp(current_modified)
                print(f"File changed at {timestamp}")
                # Do something with the change
                content = path.read_text()
                print(f"New content: {content[:100]}...")
                last_modified = current_modified
            
            time.sleep(interval)
        except FileNotFoundError:
            print("File not found, waiting...")
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopped watching")
            break

# Usage
# watch_file('watched_file.txt')
```

---

## Summary

- Use `with` statement to automatically close files
- **Read methods**: `read()`, `readline()`, `readlines()`, iteration
- **Write methods**: `write()`, `writelines()`, `print(file=f)`
- Use `'r'`, `'w'`, `'a'`, `'rb'`, `'wb'` modes appropriately
- **csv module** for CSV files, **json module** for JSON files
- **pathlib** provides modern path manipulation
- **shutil** for high-level file operations
- Always handle file errors appropriately

## Next Steps

Continue to [Exception Handling](09-exception-handling.md) to learn about handling errors gracefully.
