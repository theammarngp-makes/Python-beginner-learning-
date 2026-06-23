# Python & Pandas Refresher — Core DA Functions

One pass through this should bring back most of what's gone fuzzy. Run it alongside Kaggle Learn's Python/Pandas tracks if you want guided drills.

---

## 1. Python Core (the stuff you forget fastest)

```python
# f-strings — always use these, not .format() or %
name = "Mohammad"
print(f"Hello {name}, score: {95.456:.2f}")  # Hello Mohammad, score: 95.46

# List comprehension — your bread and butter
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Dict comprehension
sales = {emp: amt for emp, amt in zip(["Amit", "Neha"], [4000, 5200])}

# enumerate — index + value together
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# zip — pair up two lists
names = ["Amit", "Neha"]
scores = [88, 92]
for n, s in zip(names, scores):
    print(n, s)

# Unpacking
a, *rest = [1, 2, 3, 4]   # a=1, rest=[2,3,4]

# Lambda + sorting
data = [("Amit", 88), ("Neha", 92)]
data.sort(key=lambda x: x[1], reverse=True)

# Try/except (you'll need this in the OE labs too)
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

---

## 2. Pandas — Reading & Inspecting

```python
import pandas as pd

df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

df.head()        # first 5 rows
df.tail(3)        # last 3 rows
df.shape          # (rows, cols)
df.info()         # dtypes + nulls
df.describe()     # stats summary (numeric cols)
df.columns        # column names
df.dtypes
df.isnull().sum() # null count per column
```

---

## 3. Selecting & Filtering

```python
df["column"]                      # single column -> Series
df[["col1", "col2"]]              # multiple columns -> DataFrame

df.loc[0]                          # row by label/index
df.iloc[0]                         # row by position
df.loc[df["sales"] > 1000]         # filter rows

# Multiple conditions — use & / | with parentheses, NOT and/or
df[(df["sales"] > 1000) & (df["region"] == "Nagpur")]

df.query("sales > 1000 and region == 'Nagpur'")  # readable alternative
```

---

## 4. Cleaning Data

```python
df.dropna()                        # drop rows with any null
df.dropna(subset=["sales"])        # drop nulls in specific column
df.fillna(0)                       # fill nulls with 0
df.fillna(df["sales"].mean())      # fill with mean

df.drop_duplicates()
df.rename(columns={"old": "new"})
df["col"] = df["col"].astype(int)  # type conversion

df["col"] = df["col"].str.strip().str.lower()  # clean strings
```

---

## 5. GroupBy & Aggregation (this is where DA work lives)

```python
df.groupby("region")["sales"].sum()
df.groupby("region")["sales"].agg(["sum", "mean", "count"])

df.groupby(["region", "month"]).agg(
    total_sales=("sales", "sum"),
    avg_sales=("sales", "mean")
).reset_index()

df["sales"].value_counts()         # frequency count
```

---

## 6. New Columns & Apply

```python
df["profit"] = df["revenue"] - df["cost"]

df["category"] = df["sales"].apply(lambda x: "High" if x > 1000 else "Low")

df["growth_pct"] = df["sales"].pct_change() * 100
```

---

## 7. Merging & Joining (maps directly to your SQL JOINs)

```python
pd.merge(df1, df2, on="id", how="inner")   # = SQL INNER JOIN
pd.merge(df1, df2, on="id", how="left")    # = SQL LEFT JOIN
pd.concat([df1, df2], axis=0)              # stack rows
pd.concat([df1, df2], axis=1)              # stack columns
```

---

## 8. Sorting & Exporting

```python
df.sort_values("sales", ascending=False)
df.sort_values(["region", "sales"], ascending=[True, False])

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

---

## Quick Mental Map: SQL → Pandas

| SQL | Pandas |
|---|---|
| `SELECT col FROM t` | `df["col"]` |
| `WHERE x > 5` | `df[df["x"] > 5]` |
| `GROUP BY x` | `df.groupby("x")` |
| `HAVING` | `.filter()` on grouped object |
| `JOIN` | `pd.merge()` |
| `ORDER BY` | `df.sort_values()` |
| `CASE WHEN` | `.apply(lambda...)` or `np.select()` |

You already know this logic from SQL — Pandas is mostly a syntax wrapper around concepts you've drilled for 5 days straight.

---

**Weekend plan:** Run this against any small CSV (even your NagpurLens locality dataset) for ~2 hours. By Sunday night it'll feel native again.
