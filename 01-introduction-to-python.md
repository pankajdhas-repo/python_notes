# Introduction to Python

## What is Python?

Python is a high-level, interpreted, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with the use of significant indentation.

### Key Characteristics

- **High-level**: Python abstracts away complex details of the computer, making it easier to learn and use
- **Interpreted**: Code is executed line by line, without the need for compilation
- **Dynamically Typed**: Variable types are determined at runtime
- **Object-Oriented**: Supports OOP concepts like classes, inheritance, and polymorphism
- **Multi-paradigm**: Supports procedural, functional, and object-oriented programming

### Why Python?

1. **Easy to Learn**: Simple, readable syntax that resembles English
2. **Versatile**: Used in web development, data science, AI/ML, automation, and more
3. **Large Community**: Extensive documentation and community support
4. **Rich Ecosystem**: Thousands of libraries and frameworks available
5. **Cross-platform**: Runs on Windows, macOS, Linux, and more

---

## History and Evolution

### Timeline

| Version | Year | Key Features |
|---------|------|--------------|
| Python 1.0 | 1994 | First official release |
| Python 2.0 | 2000 | List comprehensions, garbage collection |
| Python 2.7 | 2010 | Last Python 2 release |
| Python 3.0 | 2008 | Major revision, not backward compatible |
| Python 3.6 | 2016 | f-strings, type hints improvements |
| Python 3.8 | 2019 | Walrus operator (:=), positional-only parameters |
| Python 3.9 | 2020 | Dictionary union operators |
| Python 3.10 | 2021 | Pattern matching (match-case) |
| Python 3.11 | 2022 | Significant performance improvements |
| Python 3.12 | 2023 | Improved error messages, f-string improvements |

### Python 2 vs Python 3

Python 2 reached end-of-life on January 1, 2020. All new projects should use Python 3.

```python
# Python 2
print "Hello, World!"

# Python 3
print("Hello, World!")
```

---

## Installing Python

### Windows

1. Download the installer from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
```bash
python --version
```

### macOS

#### Using Homebrew (Recommended)
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Verify installation
python3 --version
```

#### Using Official Installer
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the .pkg installer
3. Follow the installation wizard

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3
sudo apt install python3 python3-pip

# Verify installation
python3 --version
```

### Verifying Installation

```bash
# Check Python version
python3 --version

# Check pip (package manager) version
pip3 --version

# Start Python interactive shell
python3
```

---

## Running Python Programs

### 1. Interactive Mode (REPL)

The Python REPL (Read-Eval-Print Loop) allows you to execute code line by line.

```bash
$ python3
Python 3.11.0 (main, Oct 24 2022, 18:26:48)
>>> print("Hello, World!")
Hello, World!
>>> 2 + 2
4
>>> exit()
```

### 2. Script Mode

Create a file with `.py` extension and run it:

```python
# hello.py
print("Hello, World!")
print("Welcome to Python!")
```

```bash
python3 hello.py
```

### 3. Using the -c Flag

Run a single command directly:

```bash
python3 -c "print('Hello from command line!')"
```

### 4. Making Scripts Executable (Unix/Linux/macOS)

```python
#!/usr/bin/env python3
# my_script.py

print("This script is executable!")
```

```bash
chmod +x my_script.py
./my_script.py
```

---

## Python IDEs and Editors

### Integrated Development Environments (IDEs)

#### 1. PyCharm
- **Type**: Full-featured IDE
- **Best For**: Large projects, professional development
- **Features**: 
  - Intelligent code completion
  - Debugging tools
  - Version control integration
  - Built-in terminal
- **Editions**: Community (free), Professional (paid)

#### 2. Visual Studio Code
- **Type**: Lightweight editor with extensions
- **Best For**: All levels, versatile development
- **Features**:
  - Python extension for IntelliSense
  - Integrated terminal
  - Git integration
  - Jupyter notebook support
- **Price**: Free

#### 3. Jupyter Notebook
- **Type**: Interactive notebook
- **Best For**: Data science, learning, documentation
- **Features**:
  - Interactive code cells
  - Markdown support
  - Visualization inline
  - Easy sharing
- **Price**: Free

```bash
# Install Jupyter
pip install jupyter

# Start Jupyter Notebook
jupyter notebook
```

#### 4. Spyder
- **Type**: Scientific IDE
- **Best For**: Data science, scientific computing
- **Features**:
  - Variable explorer
  - IPython console
  - Debugging
  - Plots pane
- **Price**: Free (comes with Anaconda)

### Text Editors

#### 1. Sublime Text
- Lightweight and fast
- Multiple selections
- Plugin ecosystem
- Cross-platform

#### 2. Vim/Neovim
- Terminal-based
- Highly customizable
- Steep learning curve
- Very efficient once mastered

#### 3. Atom (Sunset)
- Note: GitHub has sunset Atom; consider VS Code instead

### Online Editors and Environments

1. **Google Colab**: Free Jupyter notebooks with GPU support
2. **Replit**: Online IDE for multiple languages
3. **PythonAnywhere**: Online Python development and hosting
4. **Kaggle Kernels**: For data science competitions

---

## Your First Python Program

Let's create a simple program that demonstrates Python basics:

```python
# my_first_program.py

# This is a comment - Python ignores this line

# Print a welcome message
print("=" * 40)
print("Welcome to Python Programming!")
print("=" * 40)

# Get user input
name = input("What is your name? ")

# Print a personalized greeting
print(f"Hello, {name}! Nice to meet you!")

# Simple calculation
birth_year = int(input("What year were you born? "))
current_year = 2024
age = current_year - birth_year

print(f"You are approximately {age} years old.")

# End message
print("\nThank you for running this program!")
print("Happy coding! 🐍")
```

### Running the Program

```bash
python3 my_first_program.py
```

### Expected Output

```
========================================
Welcome to Python Programming!
========================================
What is your name? Alice
Hello, Alice! Nice to meet you!
What year were you born? 1995
You are approximately 29 years old.

Thank you for running this program!
Happy coding! 🐍
```

---

## Python Zen

Type `import this` in Python to see "The Zen of Python" - guiding principles for writing Python code:

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

---

## Summary

- Python is a versatile, readable, and beginner-friendly programming language
- It's used in web development, data science, AI/ML, automation, and more
- Installation is straightforward on all major operating systems
- You can run Python interactively (REPL) or as scripts
- Many excellent IDEs and editors are available, with VS Code and PyCharm being popular choices
- The Python community is welcoming and has extensive resources for learning

## Next Steps

Now that you have Python installed and understand the basics, proceed to [Python Basics](02-python-basics.md) to learn about variables, data types, and operators.
