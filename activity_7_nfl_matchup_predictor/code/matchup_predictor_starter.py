#!/usr/bin/env python3
"""
Activity 7 (Bonus): NFL Matchup Predictor (STARTER)

nfl_stats.py is already complete - you don't need to edit it. Follow the
numbered TODOs below in order. Run the file often to test as you go:
    python code/matchup_predictor_starter.py
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

import nfl_stats


def power_score(team):
    """Return a single combined rating for a team."""

    # TODO 1: Combine win_pct (scaled up) and point_diff_per_game, e.g.:
    # return team["win_pct"] * 100 + team["point_diff_per_game"]
    return 0.0


def win_probability(team_a, team_b):
    """Return Team A's probability (0.0-1.0) of winning against Team B."""

    # TODO 2: Compute each team's power_score(), then convert the
    # difference into a probability with:
    # return 1 / (1 + 10 ** (-(power_a - power_b) / 10))
    return 0.5


class MatchupApp:
    def __init__(self, root, teams):
        self.teams = {t["team"]: t for t in teams}
        team_names = sorted(self.teams.keys())

        root.title("NFL Matchup Predictor")

        form_frame = tk.Frame(root)
        form_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(form_frame, text="Team A").grid(row=0, column=0)
        tk.Label(form_frame, text="Team B").grid(row=0, column=1)

        # TODO 3: Create two ttk.Combobox widgets (self.team_a_box,
        # self.team_b_box) with values=team_names, placed with .grid()
        # under their labels (row=1, column=0 and row=1, column=1).

        predict_button = tk.Button(form_frame, text="Predict", command=self.on_predict_click)
        predict_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text="Pick two teams and click Predict.")
        self.result_label.grid(row=1, column=0, padx=10, pady=10)

    def on_predict_click(self):
        # TODO 4: Read the selected team names from self.team_a_box.get()
        # and self.team_b_box.get(), look them up in self.teams, call
        # win_probability(), and update self.result_label's text with
        # something like:
        # f"{team_a['team']} have a {prob * 100:.0f}% chance to win"
        #
        # TODO 5: After showing the text result, also plot a bar chart
        # comparing the two teams' win_pct and point_diff_per_game using
        # matplotlib, then plt.show().
        pass


def main():
    teams, used_live = nfl_stats.get_standings()
    print(f"Using {'live' if used_live else 'offline fallback'} data for {len(teams)} teams.")

    root = tk.Tk()
    MatchupApp(root, teams)
    root.mainloop()


if __name__ == "__main__":
    main()
