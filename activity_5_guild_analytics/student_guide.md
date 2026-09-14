# Activity 5: Guild Analytics (Student Guide)

Over two class sessions, you'll analyze a whole spreadsheet of guild members (Week 10), then clean up
a messier version of the same data and make a chart from it (Week 11).

## What You're Building

- **Week 10:** Load `guild_members.csv` into a pandas DataFrame, explore it, filter it, and summarize
  it by group.
- **Week 11:** Clean `messy_guild_members.csv` (missing values, inconsistent text, duplicates) and
  produce a bar chart.

## Setup

Install the needed packages once (ask your instructor if unsure this has been done already):

```
pip install pandas numpy matplotlib
```

## Week 10 — Pandas & NumPy Fast Start

### The TODOs

- **TODO 1:** Load `guild_members.csv` with `pd.read_csv()`. Print `.info()` and `.describe()` to see
  what's in it.
- **TODO 2:** Filter to characters above a level you choose, e.g. `df[df["level"] > 5]`.
- **TODO 3:** Add a new column, `power_score`, calculated as `level * 10 + hp`.
- **TODO 4:** Use `.groupby("char_class")` to find the average `level` and `power_score` per class.

## Week 11 — Data Cleaning & Basic Plots

### The TODOs

- **TODO 5:** Load `messy_guild_members.csv`. Clean the `char_class` column so `"wizard"`, `"WIZARD"`,
  and `"Wizard"` are all treated the same (`.str.strip().str.title()`).
- **TODO 6:** Convert `level` to numeric with `pd.to_numeric(df["level"], errors="coerce")` — this turns
  bad values (like `"N/A"`) into `NaN`. Then decide how to handle the missing values: drop those rows,
  or fill them with the column's median.
- **TODO 7:** Drop duplicate rows with `.drop_duplicates()`.
- **TODO 8:** Make a bar chart of average level per class using
  `df.groupby("char_class")["level"].mean().plot(kind="bar")`, then `plt.show()`.

## Using AI the Right Way

Good use of AI in this activity:

- "What's the difference between a NumPy array and a pandas DataFrame?"
- "What does `.groupby()` do, in plain English?"
- "What are common signs a dataset needs cleaning?"
- "Review my data cleaning steps — am I missing anything?"

Not the point of this activity:

- Asking AI to write your entire cleaning pipeline without you understanding each step — you should be
  able to explain why each cleaning decision (drop vs. fill, for example) was made.

**Rule of thumb:** use AI to explain unfamiliar pandas methods and to sanity-check your cleaning
decisions — write and run the code yourself so you understand what changed and why.

## Stretch Goals (if you finish early)

- Group by `region` instead of (or in addition to) `char_class`.
- Add a histogram of HP values.
- Clean the `region` column too, if it has similar issues.

## Vocabulary Recap

| Term | Meaning |
|---|---|
| DataFrame | A pandas table of rows and columns |
| Series | A single column of a DataFrame |
| Boolean mask | A True/False filter used to select rows |
| `NaN` | Pandas' way of representing a missing value |
| `.groupby()` | Splits data into groups and lets you summarize each group |
| Data cleaning | Fixing missing values, inconsistent text, wrong types, and duplicates |
| Plot | A visual summary of data |
