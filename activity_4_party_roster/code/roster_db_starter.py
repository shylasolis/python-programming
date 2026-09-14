#!/usr/bin/env python3
"""
Activity 4, Week 8: Party Roster Manager - Database (STARTER)

Follow the numbered TODOs in order. Run the file often to test as you go:
    python code/roster_db_starter.py
"""

import sqlite3

DB_FILE = "roster.db"


def init_db(conn):
    """Create the characters table if it doesn't already exist."""

    # TODO 1: Run a CREATE TABLE IF NOT EXISTS statement with columns:
    # id (INTEGER PRIMARY KEY AUTOINCREMENT), name (TEXT), hp (INTEGER),
    # level (INTEGER), char_class (TEXT). Then conn.commit().
    pass


def add_character(conn, name, hp, level, char_class):
    """Insert a new character row."""

    # TODO 2: Use a parameterized INSERT (with ? placeholders) to add a row.
    # Never use an f-string to put `name`/`char_class` directly into the SQL.
    # Don't forget conn.commit().
    pass


def list_characters(conn):
    """Return all character rows as a list of tuples."""

    # TODO 3: Run a SELECT statement and return cursor.fetchall().
    return []


def delete_character(conn, character_id):
    """Delete a character row by id."""

    # TODO 4: Use a parameterized DELETE (with a ? placeholder for the id).
    # Don't forget conn.commit().
    pass


def print_roster(rows):
    if not rows:
        print("(roster is empty)")
        return
    for row in rows:
        char_id, name, hp, level, char_class = row
        print(f"  [{char_id}] {name} - {char_class}, Level {level}, HP {hp}")


def main():
    conn = sqlite3.connect(DB_FILE)
    init_db(conn)

    # TODO 5: Finish this menu loop. It should:
    # - print the menu options (add / list / delete / quit)
    # - read the user's choice
    # - call the matching function above
    # - loop until the user chooses "quit"
    print("=== Party Roster Manager (Database) ===")
    print("1) Add character")
    print("2) List roster")
    print("3) Delete character")
    print("4) Quit")

    conn.close()


if __name__ == "__main__":
    main()
