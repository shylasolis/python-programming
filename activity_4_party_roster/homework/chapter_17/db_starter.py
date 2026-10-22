"""Course starter database layer for Murach Chapter 17, Exercise 17-2.

The small local database is created on first run. It is test data for this
starter and is not part of the textbook's movie database.
"""

from contextlib import closing
from pathlib import Path
import sqlite3

from objects_starter import Movie

DB_FILE = Path(__file__).with_name("movies_homework.db")

SAMPLE_MOVIES = (
    ("Moon Harbor", 2021, 94, "Adventure"),
    ("The Paper Kingdom", 2018, 88, "Drama"),
    ("Lanterns at Noon", 2022, 103, "Drama"),
    ("The Clockwork Picnic", 2019, 79, "Comedy"),
    ("River of Stars", 2020, 96, "Adventure"),
)


def _connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    with closing(_connect()) as conn, conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Category (
                categoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Movie (
                movieID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year INTEGER NOT NULL,
                minutes INTEGER NOT NULL,
                categoryID INTEGER NOT NULL,
                FOREIGN KEY (categoryID) REFERENCES Category(categoryID)
            )
            """
        )

        category_count = conn.execute("SELECT COUNT(*) FROM Category").fetchone()[0]
        movie_count = conn.execute("SELECT COUNT(*) FROM Movie").fetchone()[0]
        if category_count == 0 and movie_count == 0:
            for name, year, minutes, category in SAMPLE_MOVIES:
                conn.execute(
                    "INSERT OR IGNORE INTO Category (name) VALUES (?)",
                    (category,),
                )
                category_row = conn.execute(
                    "SELECT categoryID FROM Category WHERE name = ?",
                    (category,),
                ).fetchone()
                conn.execute(
                    """
                    INSERT INTO Movie (name, year, minutes, categoryID)
                    VALUES (?, ?, ?, ?)
                    """,
                    (name, year, minutes, category_row["categoryID"]),
                )


def _movie_from_row(row):
    if row is None:
        return None
    return Movie(
        row["movieID"],
        row["name"],
        row["year"],
        row["minutes"],
        row["category"],
    )


def get_movies():
    """Return all movies, in database ID order."""
    with closing(_connect()) as conn:
        rows = conn.execute(
            """
            SELECT Movie.movieID, Movie.name, Movie.year, Movie.minutes, Category.name AS category
            FROM Movie
            INNER JOIN Category ON Movie.categoryID = Category.categoryID
            ORDER BY Movie.movieID
            """
        ).fetchall()
    return [_movie_from_row(row) for row in rows]


def get_movie(movie_id):
    """Return the movie with this ID, or None if there is no match."""
    # TODO 1: Select one movie by movie_id, join its category, and return a
    # Movie object using _movie_from_row(). Use a ? placeholder for the ID.
    # Select the category name AS category, as get_movies() does above.
    pass


def delete_movie(movie_id):
    """Delete one movie by ID and report whether a row was removed."""
    with closing(_connect()) as conn, conn:
        cursor = conn.execute("DELETE FROM Movie WHERE movieID = ?", (movie_id,))
    return cursor.rowcount > 0


def get_movies_by_minutes(max_minutes):
    """Return movies shorter than max_minutes, sorted by running time."""
    # TODO 2: Select matching movies and their category. Use a ? placeholder
    # for max_minutes, sort minutes from lowest to highest, and return Movie
    # objects by passing each row to _movie_from_row(). As in get_movies(),
    # select the category name AS category.
    pass


if __name__ == "__main__":
    init_db()
    print("Database ready:", DB_FILE.name)
