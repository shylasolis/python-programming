"""Course starter user interface for Murach Chapter 17, Exercise 17-2.

Run from this folder:
    python ui_starter.py
"""

import db_starter as db


def get_int(prompt):
    """Get an integer from the user, or return None after an invalid entry."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a whole number.")
        return None


def display_movies(movies):
    if not movies:
        print("No movies found.")
        return

    print(f"{'ID':<4} {'Name':<32} {'Year':<6} {'Mins':<6} Category")
    print("-" * 70)
    for movie in movies:
        print(movie)


def delete_movie():
    movie_id = get_int("Movie ID: ")
    if movie_id is None:
        return

    movie = db.get_movie(movie_id)
    if movie is None:
        print("No movie was found with that ID.")
        return

    # TODO 3: Ask the user to confirm deleting this movie. Delete it only
    # when the answer is "y" (case-insensitive); otherwise leave it unchanged.
    db.delete_movie(movie_id)
    print("Movie deleted.")


def display_movies_by_minutes():
    # TODO 4: Use get_int() to ask for the maximum running time, get matching
    # movies from the database, and display them with a helpful heading.
    pass


def display_menu():
    print("\nMovie List")
    print("list - List movies")
    print("del  - Delete a movie")
    # TODO 5: Add the command for the running-time search.
    print("exit - Exit the program")


def main():
    db.init_db()
    while True:
        display_menu()
        command = input("Command: ").strip().lower()
        if command == "list":
            display_movies(db.get_movies())
        elif command == "del":
            delete_movie()
        # TODO 6: Handle the running-time search command.
        elif command == "exit":
            break
        else:
            print("Please choose a listed command.")


if __name__ == "__main__":
    main()
