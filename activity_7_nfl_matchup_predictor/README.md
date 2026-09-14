# Activity 7: NFL Matchup Predictor

Build a Tkinter application that compares two NFL teams and estimates a win probability from current-season statistics. The activity uses live ESPN data when available and a bundled CSV fallback when it is not.

## Textbook Connection

This is a bonus activity that applies and extends ideas from *Murach's Python Programming* and *Murach's Python for Data Science*:

- Python data structures and JSON parsing organize data returned by a public API.
- A derived metric, `power_score`, turns team statistics into a simple, explainable model.
- A logistic-style formula turns the score difference into a probability.
- Tkinter widgets and callbacks build an interactive interface.
- Matplotlib charts compare the teams visually.
- The fallback CSV demonstrates a practical software-design principle: programs that depend on a network service need a backup plan.

This is not a production prediction model. Its purpose is to make data, formulas, and GUI programming visible and understandable.

## Get Started

1. Ensure matplotlib is installed: `pip install matplotlib`.
2. Read `code/nfl_stats.py`; it is provided and does not need changes.
3. Open `code/matchup_predictor_starter.py`.
4. Run it with `python code/matchup_predictor_starter.py`.
5. Complete the `# TODO` comments in order and use [student_guide.md](student_guide.md) for details.

## Files

- `code/matchup_predictor_starter.py`: your starting point
- `code/nfl_stats.py`: provided live-data and fallback module
- `code/nfl_standings_fallback.csv`: offline standings snapshot
- `student_guide.md`: detailed activity instructions
- `README_instructor.md`: instructor facilitation guide
