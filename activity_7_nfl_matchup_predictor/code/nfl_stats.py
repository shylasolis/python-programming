#!/usr/bin/env python3
"""
Activity 7: NFL Matchup Predictor - data layer (COMPLETE, provided to students)

This module fetches real NFL standings from ESPN's public API. If the
network request fails (no internet, API down, school firewall), it falls
back to a bundled CSV snapshot so the activity still works offline.

Nothing in this file needs to be edited - it's the "plumbing" so students
can focus on the prediction formula and the GUI in matchup_predictor_starter.py.
"""

import csv
import json
import urllib.request

STANDINGS_URL = "https://site.api.espn.com/apis/v2/sports/football/nfl/standings"
FALLBACK_FILE = "nfl_standings_fallback.csv"
REQUEST_TIMEOUT_SECONDS = 5


def fetch_standings_live():
    """Fetch current NFL standings from ESPN's public API.

    Returns a list of team stat dicts, or raises an exception if the
    request fails (no internet, timeout, unexpected response shape, etc).
    """

    with urllib.request.urlopen(STANDINGS_URL, timeout=REQUEST_TIMEOUT_SECONDS) as response:
        data = json.loads(response.read())

    teams = []
    for conference in data["children"]:
        for entry in conference["standings"]["entries"]:
            team = entry["team"]
            stats = {s["name"]: s.get("value") for s in entry["stats"]}
            wins = int(stats.get("wins") or 0)
            losses = int(stats.get("losses") or 0)
            points_for = int(stats.get("pointsFor") or 0)
            points_against = int(stats.get("pointsAgainst") or 0)
            teams.append(_build_team_record(team["displayName"], team["abbreviation"], wins, losses, points_for, points_against))

    if not teams:
        raise ValueError("ESPN API returned no team data (maybe the season hasn't started yet)")

    if all(t["games_played"] == 0 for t in teams):
        raise ValueError("ESPN API returned no games played yet this season (too early in the season)")

    return teams


def _build_team_record(team_name, abbreviation, wins, losses, points_for, points_against):
    """Build a team stat dict with derived fields (games_played, win_pct, point_diff)."""

    games_played = wins + losses
    win_pct = wins / games_played if games_played > 0 else 0.0
    point_diff_per_game = (points_for - points_against) / games_played if games_played > 0 else 0.0

    return {
        "team": team_name,
        "abbreviation": abbreviation,
        "wins": wins,
        "losses": losses,
        "points_for": points_for,
        "points_against": points_against,
        "games_played": games_played,
        "win_pct": win_pct,
        "point_diff_per_game": point_diff_per_game,
    }


def load_standings_fallback():
    """Load the bundled offline snapshot of NFL standings from a CSV file."""

    teams = []
    with open(FALLBACK_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            teams.append(
                _build_team_record(
                    row["team"],
                    row["abbreviation"],
                    int(row["wins"]),
                    int(row["losses"]),
                    int(row["points_for"]),
                    int(row["points_against"]),
                )
            )
    return teams


def get_standings():
    """Return (teams, used_live_data). Tries the live API first, falls
    back to the offline CSV snapshot if the live request fails."""

    try:
        return fetch_standings_live(), True
    except Exception:
        return load_standings_fallback(), False
