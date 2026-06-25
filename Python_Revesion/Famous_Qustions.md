
## PART 3 — FAMOUS PROBLEMS

---

### 1. Fibonacci Sequence

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
# 0 1 1 2 3 5 8 13 21 34

# Key insight: a, b = b, a+b swaps simultaneously — no temp variable needed
```

---

### 2. Prime Number Check

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# All primes up to 50
primes = [x for x in range(2, 51) if is_prime(x)]

# Key insight: only check up to √n
```

---

### 3. Reverse String / Palindrome

```python
s = "racecar"

# Pythonic
rev = s[::-1]
is_palindrome = s == s[::-1]

# Manual (OE wants this too)
def reverse_manual(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
```

---

### 4. FizzBuzz

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Key insight: check % 15 first — if you check % 3 first you miss FizzBuzz
```

---

### 5. Anagram Check

```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

print(is_anagram("listen", "silent"))   # True
```

---

### 6. Find Duplicates in a List

```python
from collections import Counter

nums = [1, 2, 3, 2, 4, 3, 5]
dupes = [k for k, v in Counter(nums).items() if v > 1]
print(dupes)   # [2, 3]
```

---

### 7. Star & Number Patterns

```python
n = 5

# Right triangle
for i in range(1, n+1):
    print("* " * i)

# Number pyramid
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Key: outer loop = rows, inner loop = what prints per row
```

---

### 8. Word Frequency Counter

```python
text  = "nagpur is great nagpur has oranges"
words = text.lower().split()

# Pure Python
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# Pandas version
import pandas as pd
s = pd.Series(words)
print(s.value_counts())

# Key: dict.get(key, 0) avoids KeyError — cleaner than if/else
```

---

### 9. Sales Aggregation (DA-style)

```python
data = [
    {"region": "Nagpur", "sales": 4000},
    {"region": "Mumbai", "sales": 8000},
    {"region": "Nagpur", "sales": 6000},
    {"region": "Mumbai", "sales": 3000},
]

# Pure Python
from collections import defaultdict
totals = defaultdict(int)
counts = defaultdict(int)
for row in data:
    totals[row["region"]] += row["sales"]
    counts[row["region"]] += 1

for r in totals:
    avg = totals[r] / counts[r]
    print(f"{r}: total={totals[r]}, avg={avg:.0f}")

# Pandas version (1 liner)
import pandas as pd
df = pd.DataFrame(data)
print(df.groupby("region")["sales"].agg(["sum", "mean"]))

# Always show both in interviews — pure Python shows logic, Pandas shows tool fluency
```
