
## PART 2 — PANDAS

---

### Step 1 — Reading & Inspecting

```python
import pandas as pd

df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

df.head()          # first 5 rows
df.tail(3)         # last 3 rows
df.shape           # (rows, cols)
df.info()          # dtypes + null counts
df.describe()      # stats: mean, std, min, max
df.columns         # column names
df.dtypes
df.isnull().sum()  # null count per column
df.nunique()       # unique values per column
```

---

### Step 2 — Selecting & Filtering

```python
df["col"]                      # single column -> Series
df[["col1", "col2"]]           # multiple -> DataFrame

df.loc[0]                      # row by label
df.iloc[0]                     # row by position
df.loc[0:3, "col"]             # rows 0-3, one column

# Boolean filters
df[df["sales"] > 1000]
df[df["city"] == "Nagpur"]

# Multiple conditions — use & and | with ()
df[(df["sales"] > 1000) & (df["city"] == "Nagpur")]
df[(df["city"] == "Nagpur") | (df["city"] == "Mumbai")]

# query() — most readable
df.query("sales > 1000 and city == 'Nagpur'")

# isin() and NOT with ~
df[df["city"].isin(["Nagpur", "Mumbai"])]
df[~df["city"].isin(["Delhi"])]
```

---

### Step 3 — Cleaning Data

```python
df.isnull().sum()             # count nulls
df.dropna()                   # drop rows with any null
df.dropna(subset=["sales"])   # drop nulls in specific col
df.fillna(0)
df.fillna(df["sales"].mean())
df["col"].fillna(method="ffill")   # forward fill

df.duplicated().sum()
df.drop_duplicates()
df.drop_duplicates(subset=["id"])

df.rename(columns={"old_name": "new_name"})
df["sales"] = df["sales"].astype(int)
df["date"]  = pd.to_datetime(df["date"])

# String cleaning
df["city"] = df["city"].str.strip().str.lower()
df.drop(columns=["useless_col"])
```

---

### Step 4 — GroupBy & Aggregation

```python
df.groupby("city")["sales"].sum()
df.groupby("city")["sales"].agg(["sum", "mean", "count"])

# Named aggregation — cleanest pattern
df.groupby("city").agg(
    total_sales = ("sales", "sum"),
    avg_sales   = ("sales", "mean"),
    num_orders  = ("order_id", "count")
).reset_index()

# Group by multiple columns
df.groupby(["city", "month"])["sales"].sum()

# value_counts — frequency of categorical
df["city"].value_counts()
df["city"].value_counts(normalize=True)   # as %
```

---

### Step 5 — New Columns & Apply

```python
df["profit"]     = df["revenue"] - df["cost"]
df["margin_pct"] = (df["profit"] / df["revenue"]) * 100

# apply + lambda
df["size"] = df["sales"].apply(lambda x: "High" if x > 1000 else "Low")

# apply with custom function (row-wise)
def classify(row):
    if row["sales"] > 1000 and row["city"] == "Nagpur":
        return "Priority"
    return "Standard"
df["segment"] = df.apply(classify, axis=1)

# Built-in operations
df["growth"]  = df["sales"].pct_change() * 100
df["rank"]    = df["sales"].rank(ascending=False)
df["cumsum"]  = df["sales"].cumsum()

# np.where — vectorized if/else (faster than apply)
import numpy as np
df["flag"] = np.where(df["sales"] > 1000, "High", "Low")
```

---

### Step 6 — Merging & Joining

```python
# Maps directly to your SQL JOIN knowledge
pd.merge(df1, df2, on="id", how="inner")   # INNER JOIN
pd.merge(df1, df2, on="id", how="left")    # LEFT JOIN
pd.merge(df1, df2, on="id", how="right")   # RIGHT JOIN
pd.merge(df1, df2, on="id", how="outer")   # FULL OUTER JOIN

# Different column names
pd.merge(df1, df2, left_on="emp_id", right_on="id")

# Multiple keys
pd.merge(df1, df2, on=["city", "month"])

# concat — stack DataFrames
pd.concat([df1, df2], axis=0)   # stack rows
pd.concat([df1, df2], axis=1)   # stack columns
```

---

### Step 7 — Sorting & Exporting

```python
df.sort_values("sales", ascending=False)
df.sort_values(["city", "sales"], ascending=[True, False])
df.sort_values("sales").reset_index(drop=True)

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False, sheet_name="Data")
df[["city","sales","profit"]].to_csv("summary.csv", index=False)

df.sample(100)          # random 100 rows
df.sample(frac=0.1)     # random 10%
df.nlargest(10, "sales")
df.nsmallest(5, "cost")
```

---

### Advanced — Pivot Tables

```python
df.pivot_table(
    values  = "sales",
    index   = "city",
    columns = "month",
    aggfunc = "sum",
    fill_value = 0
)

pd.crosstab(df["city"], df["segment"])

# melt — wide to long
pd.melt(df, id_vars=["city"], value_vars=["jan","feb","mar"])
```

---

### SQL → Pandas Quick Map

| SQL | Pandas |
|---|---|
| `SELECT col FROM t` | `df["col"]` |
| `WHERE x > 5` | `df[df["x"] > 5]` |
| `GROUP BY x` | `df.groupby("x")` |
| `HAVING count > 2` | `.filter()` on grouped |
| `JOIN` | `pd.merge()` |
| `ORDER BY` | `df.sort_values()` |
| `CASE WHEN` | `np.where()` or `.apply(lambda...)` |
| `DISTINCT` | `df.drop_duplicates()` |
| `COUNT(*)` | `df.shape[0]` or `.count()` |

---
