# Activity 6: The Guild Election Polling Case Study (Student Guide)

Over two class sessions, you'll analyze polling data for a fictional guild leader election between
three candidates: Mira, Doran, and Yusuf. You'll compute weighted averages (Week 12), then chart the
trend over time and write a short report on your findings (Week 13).

## What You're Building

- **Week 12:** Load the polling data and compute a **weighted average** of support for each candidate
  (weighting by how many people each pollster surveyed).
- **Week 13:** Chart how each candidate's support changed over time, and write a short plain-English
  report summarizing who's ahead and who's trending up or down.

## Setup

`pandas`, `numpy`, and `matplotlib` should already be installed from Activity 5. If not:

```
pip install pandas numpy matplotlib
```

## Week 12 — Ingestion & Aggregation

### The TODOs

- **TODO 1:** Load `guild_leader_polls.csv` with `pd.read_csv()`. Parse `poll_date` into real dates
  with `pd.to_datetime(df["poll_date"])`.
- **TODO 2:** Write `weighted_average(df, value_col, weight_col)` — it should return
  `(df[value_col] * df[weight_col]).sum() / df[weight_col].sum()`.
- **TODO 3:** Group by `candidate` and compute each candidate's overall weighted average `percent`
  across all polls (hint: you can use `.groupby("candidate").apply(...)` with your function, or loop
  over each candidate's rows and call `weighted_average` directly — either is fine).
- **TODO 4:** Group by both `poll_date` and `candidate` to get a weighted average **per week** — you'll
  use this in Week 13 to build a trend chart.

## Week 13 — Trends & Reporting

### The TODOs

- **TODO 5:** Using the weekly weighted averages from TODO 4, plot a line chart with one line per
  candidate (x-axis = date, y-axis = weighted average percent).
- **TODO 6:** For each candidate, compute the **swing**: their weighted average in the last week minus
  their weighted average in the first week.
- **TODO 7:** Write `generate_report(...)` — a function that prints 3-5 plain-English sentences
  covering: who's currently leading, by roughly how much, and which candidate has the biggest swing
  (and in which direction). Write it for someone who has never seen the data or a chart.

## Using AI the Right Way

Good use of AI in this activity:

- "How do you compute a weighted average in pandas?" (then verify it matches your own math)
- "What's the difference between correlation and trend?"
- "Review my report summary — is it clear to someone who hasn't seen the data?"

Not the point of this activity:

- Asking AI to write the whole analysis or report for you — the weighting logic and the written
  interpretation are exactly the skills this activity is meant to build.

**Rule of thumb:** use AI to double-check formulas and to get feedback on the clarity of your written
report — do the actual weighting math and interpretation yourself.

## Stretch Goals (if you finish early)

- Check whether any single pollster consistently favors one candidate ("house effect").
- Add a bar chart comparing each candidate's final swing.
- Try weighting recent polls more heavily than older ones and see how the overall average changes.

## Vocabulary Recap

| Term | Meaning |
|---|---|
| Weighted average | An average where some values count more than others |
| Time series | Data points ordered by date/time |
| Trend | The general direction data is moving over time |
| Swing | The change in a value between two points in time |
| `pd.to_datetime()` | Converts text into real date objects pandas can sort/compare |
| Report | A clear, plain-English summary of what the data shows |
