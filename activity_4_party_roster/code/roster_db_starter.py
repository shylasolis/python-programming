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

    # TODO 1: Run CREATE TABLE IF NOT EXISTS with an auto-generated integer id
    # and required name (TEXT), hp (INTEGER), level (INTEGER), and
    # char_class (TEXT) columns. Then conn.commit().
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
    # Commit, then return True if a row was deleted or False if the ID was
    # not found.
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

    # TODO 5: Finish this menu loop. Validate nonblank name/class and
    # positive integer HP, level, and delete ID inputs. Handle non-integer
    # values with a helpful message and return to the menu without crashing.
    # Call the matching function and report when a delete ID is not found.
    print("=== Party Roster Manager (Database) ===")
    print("1) Add character")
    print("2) List roster")
    print("3) Delete character")
    print("4) Quit")

    conn.close()


if __name__ == "__main__":
    main()
