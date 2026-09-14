#!/usr/bin/env python3
"""
Activity 3: RPG Character Forge (STARTER)

Week 6: TODOs 1-4 (the Character class)
Week 7: TODOs 5-6 (save/load)

Run the file often to test as you go:
    python code/character_forge_starter.py
"""

SAVE_FILE = "character_save.txt"


class Character:
    def __init__(self, name, hp, level):
        # TODO 1: Set self.name, self.hp, self.max_hp (same as starting hp),
        # self.level, and self.inventory (start as an empty list).
        pass

    def take_damage(self, amount):
        # TODO 2: Reduce self.hp by `amount`. Don't let it go below 0.
        pass

    def level_up(self):
        # TODO 3: Increase self.level by 1 and restore self.hp to self.max_hp.
        pass

    def display_stats(self):
        # TODO 4: Print name, hp/max_hp, level, and inventory.
        pass

    def save_to_file(self, filename):
        # TODO 5: Open `filename` for writing and write self.name, self.hp,
        # and self.level (e.g. one value per line). Use `with open(...)`.
        pass


def load_character(filename):
    """Load a saved character from filename, or return None if not found."""

    # TODO 6: Open `filename` for reading inside a try/except FileNotFoundError
    # block. Read back name, hp, and level, and return a new Character built
    # from those values. Return None if the file doesn't exist yet.
    return None


def main():
    print("=== RPG Character Forge ===\n")

    hero = load_character(SAVE_FILE)

    if hero is None:
        print("No saved character found. Creating a new one!")
        hero = Character("Hero", 100, 1)

    hero.display_stats()

    hero.take_damage(30)
    hero.level_up()
    hero.display_stats()

    hero.save_to_file(SAVE_FILE)
    print(f"\nSaved to {SAVE_FILE}.")


if __name__ == "__main__":
    main()
