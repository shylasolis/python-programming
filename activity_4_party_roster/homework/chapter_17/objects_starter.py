"""Course starter objects for Murach Chapter 17, Exercise 17-2."""


class Movie:
    """One movie row returned by the database."""

    def __init__(self, movie_id, name, year, minutes, category):
        self.movie_id = movie_id
        self.name = name
        self.year = year
        self.minutes = minutes
        self.category = category

    def __str__(self):
        return (
            f"{self.movie_id:<4} {self.name:<32} "
            f"{self.year:<6} {self.minutes:<6} {self.category}"
        )
