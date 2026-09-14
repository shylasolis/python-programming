# Activity 7 (Bonus): NFL Matchup Predictor (Student Guide)

Today you'll build a GUI that predicts the outcome of an NFL matchup using **real, current season
stats** pulled from a live API — with an automatic offline backup in case the API isn't reachable.

## What You're Building

A Tkinter window where you:

1. Pick two NFL teams from dropdowns
2. Click "Predict"
3. See a win-probability estimate and a bar chart comparing the two teams' stats

## Setup

1. `code/nfl_stats.py` is already complete — **you don't need to edit it.** It fetches real standings
   data from ESPN's API, and automatically falls back to a bundled CSV snapshot if the API can't be
   reached. Open it and read through `get_standings()` so you understand what data you're working with.
2. Open `code/matchup_predictor_starter.py` and work through the `# TODO`s in order.
3. Run it often: `python code/matchup_predictor_starter.py`.

## The TODOs

- **TODO 1:** Write `power_score(team)`. It should combine two things: win percentage (scaled up so it
  matters as much as point differential) and average point differential per game:
  ```python
  team["win_pct"] * 100 + team["point_diff_per_game"]
  ```
- **TODO 2:** Write `win_probability(team_a, team_b)`. Compute each team's `power_score`, then convert
  the difference into a probability:
  ```python
  1 / (1 + 10 ** (-(power_a - power_b) / 10))
  ```
  This returns Team A's probability of winning (a number between 0 and 1). If both teams have the same
  power score, this should give exactly 0.5 — check that it does!
- **TODO 3:** Add two `ttk.Combobox` dropdowns populated with team names, so the user can pick Team A
  and Team B.
- **TODO 4:** Write `on_predict_click()` — read the two selected teams, call your functions, and display
  the resulting probability as text (e.g., "Buffalo Bills have a 63% chance to win").
- **TODO 5:** Add a `matplotlib` bar chart comparing the two teams' `win_pct` and `point_diff_per_game`.

## Using AI the Right Way

Good use of AI in this activity:

- "What's a simple way to turn a stat difference into a win probability?"
- "Explain what a sigmoid/logistic function does in plain English."
- "Help me lay out two dropdown menus and a button in Tkinter using `grid()`."

Not the point of this activity:

- Asking AI for a "real" machine learning model to predict games — the goal here is understanding a
  simple, explainable formula, not building the most accurate predictor possible.

**Rule of thumb:** you should be able to explain, in one sentence, what your `power_score` formula
means and why a bigger gap between two teams' scores leads to a more lopsided prediction.

## Why Is There a Fallback CSV?

`nfl_stats.py` tries to fetch live data first. If that fails (no internet, API down, a school firewall
blocking it), it automatically uses `nfl_standings_fallback.csv` instead — real, production software
almost always needs a "what if this fails?" plan for anything that depends on the internet.

## Stretch Goals (if you finish early)

- Add a "confidence" label: "Toss-up" (45-55%), "Likely" (55-70% or 30-45%), "Highly Favored" (>70% or
  <30%).
- Rank every team by `power_score` and print a top-10 list.
- Try changing the `/10` divisor in the probability formula — what happens to the predictions if you
  make it bigger or smaller?

## Vocabulary Recap

| Term | Meaning |
|---|---|
| API | A way for your program to request data from another service over the internet |
| JSON | The text format most web APIs use to send structured data |
| Fallback | A backup plan for when a primary data source is unavailable |
| Derived metric | A new value calculated from existing data |
| Sigmoid / logistic formula | A formula that squishes any difference into a probability between 0 and 1 |
| `ttk.Combobox` | A dropdown selector widget in Tkinter |
