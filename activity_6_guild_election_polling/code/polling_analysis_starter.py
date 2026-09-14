#!/usr/bin/env python3
"""
Activity 6: The Guild Election Polling Case Study (STARTER)

Week 12: TODOs 1-4 (ingestion & weighted aggregation)
Week 13: TODOs 5-7 (trend chart & report)

Run the file often to test as you go:
    python code/polling_analysis_starter.py
"""

import pandas as pd
import matplotlib.pyplot as plt

POLLS_FILE = "guild_leader_polls.csv"


def load_polls():
    # TODO 1: Load POLLS_FILE with pd.read_csv(). Parse "poll_date" into
    # real dates with pd.to_datetime(df["poll_date"]).
    df = None
    return df


def weighted_average(df, value_col, weight_col):
    """Return the weighted average of value_col, weighted by weight_col."""

    # TODO 2: Return (df[value_col] * df[weight_col]).sum() / df[weight_col].sum()
    return 0.0


def overall_candidate_averages(df):
    """Return each candidate's overall weighted average percent."""

    # TODO 3: For each candidate, use weighted_average() on that candidate's
    # rows (df[df["candidate"] == name]) to compute their overall average.
    # Return a dict like {"Mira": 38.5, "Doran": 33.2, "Yusuf": 26.0}.
    return {}


def weekly_candidate_averages(df):
    """Return a DataFrame with one weighted average per (poll_date, candidate)."""

    # TODO 4: Group by ["poll_date", "candidate"] and compute the weighted
    # average per group. A for-loop building a list of rows, then
    # pd.DataFrame(that list), is a perfectly fine approach here.
    return pd.DataFrame(columns=["poll_date", "candidate", "weighted_percent"])


def plot_trend(weekly_df):
    # TODO 5: For each candidate, plot their weekly_percent over poll_date as
    # a line. Add a legend, axis labels, and a title, then plt.show().
    pass


def compute_swing(weekly_df):
    """Return each candidate's change from their first week to their last week."""

    # TODO 6: For each candidate, find their first and last poll_date rows in
    # weekly_df and subtract (last - first). Return a dict of candidate -> swing.
    return {}


def generate_report(overall_averages, swings):
    # TODO 7: Print 3-5 plain-English sentences: who's leading overall, by
    # about how much, and which candidate has the biggest swing (and whether
    # they're rising or falling).
    pass


def main():
    df = load_polls()

    print("=== Week 12: Ingestion & Aggregation ===")
    overall = overall_candidate_averages(df)
    print(overall)

    weekly = weekly_candidate_averages(df)
    print(weekly)

    print("\n=== Week 13: Trends & Report ===")
    plot_trend(weekly)
    swings = compute_swing(weekly)
    print(swings)
    generate_report(overall, swings)


if __name__ == "__main__":
    main()
