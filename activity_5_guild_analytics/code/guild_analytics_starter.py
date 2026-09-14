#!/usr/bin/env python3
"""
Activity 5: Guild Analytics (STARTER)

Week 10: TODOs 1-4 (using guild_members.csv)
Week 11: TODOs 5-8 (using messy_guild_members.csv)

Run the file often to test as you go:
    python code/guild_analytics_starter.py
"""

import pandas as pd
import matplotlib.pyplot as plt

CLEAN_FILE = "guild_members.csv"
MESSY_FILE = "messy_guild_members.csv"


def explore_clean_data():
    # TODO 1: Load CLEAN_FILE into a DataFrame with pd.read_csv().
    # Print df.info() and df.describe() to see what's in it.
    df = None

    # TODO 2: Filter to characters above a level you choose (e.g. > 5) and
    # print the result.

    # TODO 3: Add a "power_score" column: level * 10 + hp.

    # TODO 4: Group by "char_class" and print the average level and
    # power_score per class using .groupby("char_class").mean(numeric_only=True).

    return df


def clean_messy_data():
    # TODO 5: Load MESSY_FILE into a DataFrame. Clean the char_class column
    # with .str.strip().str.title() so casing is consistent.
    df = None

    # TODO 6: Convert the "level" column to numeric with
    # pd.to_numeric(df["level"], errors="coerce"). Decide how to handle the
    # resulting missing values (drop those rows, or fill with the median).

    # TODO 7: Drop duplicate rows with df.drop_duplicates().

    # TODO 8: Plot average level per class as a bar chart:
    # df.groupby("char_class")["level"].mean().plot(kind="bar")
    # plt.ylabel("Average Level")
    # plt.title("Average Level by Class")
    # plt.tight_layout()
    # plt.show()

    return df


def main():
    print("=== Week 10: Clean Data Exploration ===")
    explore_clean_data()

    print("\n=== Week 11: Data Cleaning ===")
    clean_messy_data()


if __name__ == "__main__":
    main()
