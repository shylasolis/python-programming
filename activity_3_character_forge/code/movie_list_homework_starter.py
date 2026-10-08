#!/usr/bin/env python3
"""
Weekly Homework 03: Object-Oriented Movie List (STARTER)

Complete the TODOs to build a console movie list using Movie objects.

Run from the repository root:
    python activity_3_character_forge/code/movie_list_homework_starter.py
"""


class Movie:
    def __init__(self, name, year):
        # TODO 1: Store name and year as attributes on this object.
        pass

    def get_display_text(self):
        # TODO 2: Return text in this format: Movie Name (Year)
        pass


def display_movies(movies):
    """Print each movie with a numbered position."""
    if not movies:
        print("There are no movies in the list.")
        return

    for number, movie in enumerate(movies, start=1):
        # TODO 3: Print the number and the movie's formatted display text.
        pass


def add_movie(movies):
    """Ask for movie details and add a Movie object to the list."""
    name = input("Movie name: ").strip()
    year_text = input("Year: ").strip()

    # TODO 4: Convert year_text to an integer. If it is not a valid integer,
    # print a helpful message and return without crashing.
    # TODO 5: Create a Movie object and append it to movies.
    pass


def delete_movie(movies):
    """Display the list and delete the movie selected by its number."""
    if not movies:
        print("There are no movies to delete.")
        return

    display_movies(movies)
    number_text = input("Enter the number of the movie to delete: ").strip()

    # TODO 6: Convert the selection to an integer and make sure it is between
    # 1 and len(movies). If not, print a helpful message and return.
    # TODO 7: Delete the selected movie from movies. Remember that list indexes
    # start at 0, but the displayed movie numbers start at 1.
    pass


def main():
    movies = [
        Movie("Arrival", 2016),
        Movie("The Princess Bride", 1987),
    ]

    while True:
        print("\n=== Movie List ===")
        print("1. View movies")
        print("2. Add a movie")
        print("3. Delete a movie")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
