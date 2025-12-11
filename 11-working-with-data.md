# Working with Data

This chapter covers essential libraries for data manipulation, analysis, and visualization in Python.

---

## NumPy Basics

### What is NumPy?

NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides:
- Powerful N-dimensional array objects
- Sophisticated broadcasting functions
- Tools for integrating C/C++ and Fortran code
- Useful linear algebra, Fourier transform, and random number capabilities

### Installing NumPy

```bash
pip install numpy
```

### Creating Arrays

```python
import numpy as np

# From lists
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]]

# Special arrays
zeros = np.zeros((3, 4))       # 3x4 array of zeros
ones = np.ones((2, 3))         # 2x3 array of ones
empty = np.empty((2, 2))       # Uninitialized
full = np.full((2, 2), 7)      # 2x2 filled with 7
identity = np.eye(3)           # 3x3 identity matrix

# Ranges
range_arr = np.arange(0, 10, 2)    # [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)    # [0.   0.25 0.5  0.75 1.  ]
logspace = np.logspace(0, 2, 3)    # [1. 10. 100.]

# Random arrays
random = np.random.rand(3, 3)           # Uniform [0, 1)
normal = np.random.randn(3, 3)          # Standard normal
integers = np.random.randint(0, 10, 5)  # Random integers
```

### Array Attributes

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)     # (2, 3) - dimensions
print(arr.ndim)      # 2 - number of dimensions
print(arr.size)      # 6 - total elements
print(arr.dtype)     # int64 - data type
print(arr.itemsize)  # 8 - bytes per element
print(arr.nbytes)    # 48 - total bytes
```

### Array Indexing and Slicing

```python
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Indexing
print(arr[0, 0])    # 1
print(arr[1, 2])    # 7
print(arr[-1, -1])  # 12

# Slicing
print(arr[0, :])      # [1 2 3 4] - first row
print(arr[:, 0])      # [1 5 9] - first column
print(arr[0:2, 1:3])  # [[2 3] [6 7]] - subarray

# Boolean indexing
print(arr[arr > 5])   # [ 6  7  8  9 10 11 12]

# Fancy indexing
indices = [0, 2]
print(arr[indices])   # [[1 2 3 4] [9 10 11 12]]
```

### Array Operations

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Element-wise operations
print(a + b)      # [ 6  8 10 12]
print(a - b)      # [-4 -4 -4 -4]
print(a * b)      # [ 5 12 21 32]
print(a / b)      # [0.2  0.33 0.43 0.5]
print(a ** 2)     # [ 1  4  9 16]

# Universal functions (ufuncs)
print(np.sqrt(a))     # [1.   1.41 1.73 2.  ]
print(np.exp(a))      # [ 2.72  7.39 20.09 54.6]
print(np.log(a))      # [0.   0.69 1.1  1.39]
print(np.sin(a))      # [0.84 0.91 0.14 -0.76]

# Aggregations
print(np.sum(a))      # 10
print(np.mean(a))     # 2.5
print(np.std(a))      # 1.118
print(np.min(a))      # 1
print(np.max(a))      # 4
print(np.argmax(a))   # 3 (index of max)
```

### Reshaping Arrays

```python
import numpy as np

arr = np.arange(12)

# Reshape
reshaped = arr.reshape(3, 4)
print(reshaped)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Flatten
flat = reshaped.flatten()  # Returns copy
ravel = reshaped.ravel()   # Returns view

# Transpose
transposed = reshaped.T
print(transposed.shape)  # (4, 3)

# Adding dimensions
arr1d = np.array([1, 2, 3])
row = arr1d[np.newaxis, :]    # (1, 3)
col = arr1d[:, np.newaxis]    # (3, 1)
```

### Broadcasting

```python
import numpy as np

# Broadcasting allows operations on arrays of different shapes
a = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
b = np.array([10, 20, 30])             # (3,)

# b is broadcast across rows
print(a + b)
# [[11 22 33]
#  [14 25 36]]

# Scalar broadcasting
print(a * 2)
# [[ 2  4  6]
#  [ 8 10 12]]

# Column broadcast
c = np.array([[100], [200]])  # (2, 1)
print(a + c)
# [[101 102 103]
#  [204 205 206]]
```

### Linear Algebra

```python
import numpy as np

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)        # Matrix multiplication
print(np.dot(A, B)) # Same as above
print(A * B)        # Element-wise (NOT matrix multiplication)

# Linear algebra operations
print(np.linalg.det(A))       # Determinant: -2
print(np.linalg.inv(A))       # Inverse
print(np.linalg.eig(A))       # Eigenvalues and eigenvectors
print(np.linalg.norm(A))      # Frobenius norm

# Solving linear equations (Ax = b)
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)  # [2. 3.]
```

---

## Pandas Basics

### What is Pandas?

Pandas is a powerful data manipulation library that provides:
- DataFrame and Series data structures
- Tools for reading/writing data
- Data cleaning and transformation
- Grouping and aggregation
- Time series functionality

### Installing Pandas

```bash
pip install pandas
```

### Series

```python
import pandas as pd

# Creating a Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# With custom index
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s['b'])  # 2

# From dictionary
d = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(d)

# Operations
print(s * 2)      # Element-wise multiplication
print(s.mean())   # Mean
print(s.sum())    # Sum
```

### DataFrame

```python
import pandas as pd

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
#       Name  Age     City
# 0    Alice   25      NYC
# 1      Bob   30       LA
# 2  Charlie   35  Chicago

# From list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30}
]
df = pd.DataFrame(data)

# With custom index
df = pd.DataFrame(data, index=['first', 'second'])
```

### Reading and Writing Data

```python
import pandas as pd

# CSV
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df.to_excel('output.xlsx', index=False)

# JSON
df = pd.read_json('data.json')
df.to_json('output.json', orient='records')

# SQL
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table_name', conn)
df.to_sql('table_name', conn, if_exists='replace', index=False)

# HTML tables
# tables = pd.read_html('https://example.com')

# Parquet (efficient columnar storage)
df = pd.read_parquet('data.parquet')
df.to_parquet('output.parquet')
```

### Basic Operations

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 70000, 55000],
    'Department': ['HR', 'IT', 'IT', 'HR']
})

# View data
print(df.head(2))      # First 2 rows
print(df.tail(2))      # Last 2 rows
print(df.info())       # Data types and memory
print(df.describe())   # Statistical summary

# Shape and columns
print(df.shape)        # (4, 4)
print(df.columns)      # ['Name', 'Age', 'Salary', 'Department']
print(df.dtypes)       # Data types

# Selecting columns
print(df['Name'])           # Single column (Series)
print(df[['Name', 'Age']])  # Multiple columns (DataFrame)

# Selecting rows
print(df.loc[0])            # By label
print(df.iloc[0])           # By position
print(df.loc[0:2])          # Rows 0-2 by label
print(df.iloc[0:2])         # Rows 0-1 by position

# Selecting rows and columns
print(df.loc[0:2, ['Name', 'Age']])
print(df.iloc[0:2, 0:2])
```

### Filtering Data

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 70000, 55000],
    'Department': ['HR', 'IT', 'IT', 'HR']
})

# Boolean filtering
print(df[df['Age'] > 28])
print(df[df['Department'] == 'IT'])

# Multiple conditions
print(df[(df['Age'] > 25) & (df['Salary'] > 55000)])
print(df[(df['Department'] == 'HR') | (df['Age'] > 30)])

# isin
print(df[df['Name'].isin(['Alice', 'Bob'])])

# Query method
print(df.query('Age > 28 and Department == "IT"'))

# String methods
# df[df['Name'].str.contains('a', case=False)]
# df[df['Name'].str.startswith('A')]
```

### Data Manipulation

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
})

# Add column
df['Bonus'] = df['Salary'] * 0.1
df['Department'] = 'IT'

# Rename columns
df = df.rename(columns={'Name': 'Employee', 'Salary': 'BaseSalary'})

# Drop columns
df = df.drop(columns=['Bonus'])

# Drop rows
df = df.drop(index=[0])

# Apply function
df['Age'] = df['Age'].apply(lambda x: x + 1)

# Map values
mapping = {'IT': 'Information Technology', 'HR': 'Human Resources'}
df['Department'] = df['Department'].map(mapping)

# Replace values
df['Age'] = df['Age'].replace({26: 25})

# Sort
df = df.sort_values('Age', ascending=False)
df = df.sort_values(['Department', 'Age'])

# Reset index
df = df.reset_index(drop=True)
```

### Handling Missing Data

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, 2, 3, np.nan]
})

# Check for missing values
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())

# Drop missing values
df_clean = df.dropna()           # Drop rows with any NaN
df_clean = df.dropna(how='all')  # Drop rows where all NaN
df_clean = df.dropna(subset=['A', 'B'])  # Check specific columns

# Fill missing values
df_filled = df.fillna(0)                    # Fill with 0
df_filled = df.fillna(df.mean())            # Fill with column means
df_filled = df.fillna(method='ffill')       # Forward fill
df_filled = df.fillna(method='bfill')       # Backward fill
df_filled = df.fillna({'A': 0, 'B': 99})    # Different values per column

# Interpolate
df_interp = df.interpolate()
```

### Grouping and Aggregation

```python
import pandas as pd

df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 55000, 65000, 70000],
    'Age': [25, 30, 35, 28, 40]
})

# Basic groupby
grouped = df.groupby('Department')

# Aggregation
print(grouped['Salary'].mean())
print(grouped['Salary'].sum())
print(grouped['Salary'].agg(['mean', 'sum', 'count']))

# Multiple columns
print(grouped[['Salary', 'Age']].mean())

# Multiple aggregations
print(grouped.agg({
    'Salary': ['mean', 'sum'],
    'Age': 'mean'
}))

# Custom aggregation
print(grouped['Salary'].agg(lambda x: x.max() - x.min()))

# Group by multiple columns
print(df.groupby(['Department', 'Age']).mean())
```

### Merging and Joining

```python
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Department': ['HR', 'IT', 'Finance', 'Marketing']
})

# Merge (SQL-like join)
merged = pd.merge(df1, df2, on='ID')               # Inner join (default)
merged = pd.merge(df1, df2, on='ID', how='left')   # Left join
merged = pd.merge(df1, df2, on='ID', how='right')  # Right join
merged = pd.merge(df1, df2, on='ID', how='outer')  # Outer join

# Merge on different column names
df3 = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Salary': [50000, 60000, 70000]
})
merged = pd.merge(df1, df3, left_on='ID', right_on='EmpID')

# Concatenate
df_concat = pd.concat([df1, df1])          # Vertical stack
df_concat = pd.concat([df1, df2], axis=1)  # Horizontal stack
```

### Pivot Tables

```python
import pandas as pd

df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Region': ['East', 'East', 'West', 'West'],
    'Sales': [100, 150, 200, 250]
})

# Pivot table
pivot = df.pivot_table(
    values='Sales',
    index='Date',
    columns='Product',
    aggfunc='sum'
)
print(pivot)

# Multiple aggregations
pivot = df.pivot_table(
    values='Sales',
    index='Date',
    columns='Product',
    aggfunc=['sum', 'mean', 'count']
)

# Multiple indices
pivot = df.pivot_table(
    values='Sales',
    index=['Date', 'Region'],
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
```

---

## Data Visualization

### Matplotlib Basics

```python
import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True)
plt.savefig('plot.png', dpi=300)
plt.show()

# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='steelblue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = np.random.rand(50) * 500

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()

# Histogram
data = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
```

### Subplots

```python
import matplotlib.pyplot as plt
import numpy as np

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

x = np.linspace(0, 10, 100)

# Plot 1
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine')

# Plot 2
axes[0, 1].plot(x, np.cos(x), color='orange')
axes[0, 1].set_title('Cosine')

# Plot 3
axes[1, 0].plot(x, np.exp(-x/5))
axes[1, 0].set_title('Exponential Decay')

# Plot 4
axes[1, 1].plot(x, np.log(x + 1))
axes[1, 1].set_title('Logarithm')

plt.tight_layout()
plt.show()
```

### Pandas Plotting

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 1, 5, 3],
    'C': [3, 1, 4, 2, 5]
})

# Line plot
df.plot(figsize=(10, 6))
plt.title('Line Plot')
plt.show()

# Bar plot
df.plot(kind='bar', figsize=(10, 6))
plt.title('Bar Plot')
plt.show()

# Horizontal bar
df.plot(kind='barh', figsize=(10, 6))
plt.show()

# Area plot
df.plot(kind='area', alpha=0.5, figsize=(10, 6))
plt.show()

# Pie chart
df['A'].plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.show()

# Box plot
df.plot(kind='box', figsize=(10, 6))
plt.show()
```

### Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set style
sns.set_style('whitegrid')
sns.set_palette('husl')

# Sample data
tips = sns.load_dataset('tips')

# Distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(tips['total_bill'], kde=True)
plt.title('Distribution of Total Bill')
plt.show()

# Count plot
plt.figure(figsize=(10, 6))
sns.countplot(data=tips, x='day', hue='sex')
plt.title('Count by Day and Sex')
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Total Bill by Day and Sex')
plt.show()

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill')
plt.title('Violin Plot')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', size='size')
plt.title('Total Bill vs Tip')
plt.show()

# Regression plot
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title('Regression: Total Bill vs Tip')
plt.show()

# Pair plot
sns.pairplot(tips, hue='sex')
plt.show()

# Heatmap
plt.figure(figsize=(10, 8))
correlation = tips.select_dtypes(include='number').corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# FacetGrid
g = sns.FacetGrid(tips, col='time', row='sex')
g.map(sns.histplot, 'total_bill')
plt.show()
```

---

## Practical Example: Data Analysis Project

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
# df = pd.read_csv('sales_data.csv')

# Sample data creation
np.random.seed(42)
df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['A', 'B', 'C'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Sales': np.random.randint(100, 1000, 100),
    'Quantity': np.random.randint(1, 50, 100)
})

# 1. Data exploration
print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe())
print("\nMissing values:")
print(df.isnull().sum())

# 2. Data cleaning
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()

# 3. Aggregation
monthly_sales = df.groupby('Month')['Sales'].sum()
product_sales = df.groupby('Product')['Sales'].sum()
region_sales = df.groupby(['Region', 'Product'])['Sales'].sum().unstack()

# 4. Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Monthly trend
axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker='o')
axes[0, 0].set_title('Monthly Sales Trend')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Sales')

# Product comparison
product_sales.plot(kind='bar', ax=axes[0, 1], color=['#1f77b4', '#ff7f0e', '#2ca02c'])
axes[0, 1].set_title('Sales by Product')
axes[0, 1].set_ylabel('Total Sales')

# Regional heatmap
sns.heatmap(region_sales, annot=True, fmt='.0f', cmap='YlOrRd', ax=axes[1, 0])
axes[1, 0].set_title('Sales by Region and Product')

# Distribution
axes[1, 1].hist(df['Sales'], bins=20, edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Sales Distribution')
axes[1, 1].set_xlabel('Sales')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('analysis_report.png', dpi=300)
plt.show()

# 5. Export results
summary = df.groupby('Product').agg({
    'Sales': ['sum', 'mean', 'std'],
    'Quantity': ['sum', 'mean']
}).round(2)
summary.to_csv('sales_summary.csv')
print("\nSummary exported to sales_summary.csv")
```

---

## Summary

| Library | Purpose | Key Features |
|---------|---------|--------------|
| NumPy | Numerical computing | N-dimensional arrays, math operations |
| Pandas | Data manipulation | DataFrame, data cleaning, aggregation |
| Matplotlib | Basic visualization | Line, bar, scatter, histogram plots |
| Seaborn | Statistical visualization | Beautiful statistical plots, heatmaps |

### Best Practices

1. **Always explore your data first** - Use `head()`, `info()`, `describe()`
2. **Handle missing data early** - Check with `isnull()`, decide strategy
3. **Use vectorized operations** - Avoid loops with Pandas/NumPy
4. **Choose appropriate visualizations** - Match chart type to data
5. **Label your plots** - Always add titles, axis labels, legends

## Next Steps

Continue to [Web Development](12-web-development.md) to learn about building web applications with Python.
