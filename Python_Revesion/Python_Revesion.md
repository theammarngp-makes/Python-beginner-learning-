# Python & Pandas — Complete Revision Guide
### Mohammad Ammar | DA/DS Career  | ACET Nagpur

---

## PART 1 — PYTHON CORE

---

### Unit I — Data Types & I/O

```python
# Core types
x = 42          # int
y = 3.14        # float
name = "Ammar"  # str
flag = True     # bool

# Type casting
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False  — 0, "", [], None are all falsy

# Input always returns str — always cast it
age = int(input("Enter age: "))

# f-strings — always use these, never % or .format()
print(f"Name: {name}, score: {95.456:.2f}")   # 95.46
print(f"{'hello':>10}")                        # right-align in 10 chars
print(f"{1000000:,}")                          # 1,000,000
```

---

### Unit I — Operators & Expressions

```python
# Arithmetic
10 // 3    # 3   floor division
10 % 3     # 1   modulo — key for prime checks, even/odd
2 ** 8     # 256 power

# Comparison & logical
x = 5
x > 3 and x < 10    # True
x == 5 or x == 6    # True
not (x > 10)        # True

# Chained comparison (Pythonic)
1 < x < 10          # True — cleaner than x > 1 and x < 10

# Walrus operator (Python 3.8+)
if (n := len("hello")) > 3:
    print(f"Long string: {n} chars")
```

---

### Unit II — Conditionals & Loops

```python
# if/elif/else
grade = 85
if grade >= 90:
    print("O")
elif grade >= 75:
    print("A")
elif grade >= 60:
    print("B")
else:
    print("Fail")

# while
i = 0
while i < 5:
    print(i)
    i += 1

# for + range
for i in range(5):          # 0 to 4
    print(i)
for i in range(1, 6):       # 1 to 5
    print(i)
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8

# Loop control
for i in range(10):
    if i == 3: continue     # skip 3
    if i == 7: break        # stop at 7
    print(i)

# for/else — often forgotten, examiners love it
for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")          # runs only if loop completed without break
```

---

### Unit II+ — Comprehensions

```python
# List comprehension — replaces most for loops
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
upper   = [w.upper() for w in ["hello", "world"]]

# Dict comprehension
sales   = {"Amit": 4000, "Neha": 5200}
doubled = {k: v*2 for k, v in sales.items()}
high    = {k: v for k, v in sales.items() if v > 4500}

# Set comprehension (unique values only)
nums      = [1, 2, 2, 3, 3, 4]
unique_sq = {x**2 for x in nums}     # {1, 4, 9, 16}

# Nested list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat   = [val for row in matrix for val in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### Unit III — Strings

```python
s = "Hello Nagpur"

# Slicing
s[0]       # "H"
s[-1]      # "r"
s[0:5]     # "Hello"
s[::-1]    # reverse: "rupgaN olleH"

# Common methods
s.lower()
s.upper()
s.strip()                     # remove whitespace
s.replace("Hello", "Hi")
s.split(" ")                  # ["Hello", "Nagpur"]
" ".join(["Hello", "Nagpur"]) # "Hello Nagpur"
s.startswith("He")            # True
s.find("Nagpur")              # 6 (index)
s.count("l")                  # 2

# String formatting
name = "Ammar"
print(f"Hello {name}!")
print(f"{3.14159:.2f}")       # 3.14
print(f"{1000000:,}")         # 1,000,000
```

---

### Unit III — Data Structures

```python
# LIST — mutable, ordered
lst = [1, 2, 3]
lst.append(4)        # add to end
lst.insert(0, 0)     # insert at index
lst.pop()            # remove last
lst.pop(0)           # remove at index
lst.remove(2)        # remove by value
lst.sort()
lst.reverse()
len(lst)
3 in lst             # True

# TUPLE — immutable, ordered
t = (1, 2, 3)
a, b, c = t          # unpacking
a, *rest = t         # a=1, rest=[2,3]

# DICT — key-value
d = {"name": "Ammar", "city": "Nagpur"}
d["age"] = 22
d.get("age", 0)      # safe get — no KeyError
d.keys()
d.values()
d.items()            # [(key, val), ...]
del d["age"]

# SET — unique, unordered
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 | s2   # union        {1,2,3,4}
s1 & s2   # intersection {2,3}
s1 - s2   # difference   {1}
```

---

### Unit IV — Functions

```python
# Basic
def greet(name):
    return f"Hello {name}"

# Default argument
def power(base, exp=2):
    return base ** exp

power(3)      # 9
power(3, 3)   # 27

# *args — variable positional
def total(*nums):
    return sum(nums)
total(1, 2, 3, 4)   # 10

# **kwargs — variable keyword
def profile(**info):
    for k, v in info.items():
        print(f"{k}: {v}")
profile(name="Ammar", city="Nagpur")

# Lambda
square = lambda x: x**2
nums = [3, 1, 4, 1, 5]
nums.sort(key=lambda x: -x)   # sort descending

# Scope
x = 10
def fn():
    global x
    x = 20
fn()
```

---

### Unit IV — Exception Handling

```python
try:
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Always runs")       # cleanup goes here

# Multiple exceptions in one line
# except (ValueError, TypeError) as e:

# Raising errors
def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age
```

---

### Unit IV — File Handling

```python
# Read
with open("data.txt", "r") as f:
    content = f.read()         # whole file as string
    lines   = f.readlines()    # list of lines
    for line in f:             # line by line
        print(line.strip())

# Write
with open("output.txt", "w") as f:
    f.write("Hello Nagpur\n")

# Append
with open("log.txt", "a") as f:
    f.write("New entry\n")

# CSV — use Pandas for real DA work
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["sales"])

# Better: just use Pandas
import pandas as pd
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)
```

---

### Beyond OE — OOP Basics

```python
class DataAnalyst:
    tools = ["Python", "SQL", "Pandas"]   # class variable

    def __init__(self, name, city):
        self.name     = name              # instance variable
        self.city     = city
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def __str__(self):
        return f"{self.name} from {self.city}"

analyst = DataAnalyst("Ammar", "Nagpur")
analyst.add_project("NagpurLens")
print(analyst)

# Inheritance
class DataScientist(DataAnalyst):
    def __init__(self, name, city, ml_stack):
        super().__init__(name, city)
        self.ml_stack = ml_stack
```

---

---
