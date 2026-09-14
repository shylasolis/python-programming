#!/usr/bin/env python3
"""
Activity 1: Build-Your-Own Escape Room (STARTER)

Follow the numbered TODOs in order. Run the file often to test as you go:
    python code/escape_room_starter.py
"""


def room_one(inventory):
    """Room 1: the player arrives here first."""

    # TODO 1: Print a short description of the starting room.
    # Example: "You wake up in a dusty library. There is a door to the LEFT
    # and a desk in front of you."

    choice = input("What do you do? ").lower()

    # TODO 3: Write if/elif/else branches for this room's choices.
    # - one branch should print(...) and return "room_two"
    # - one branch should search the desk, maybe add an item to inventory,
    #   and return "room_one" again (stay in this room)
    # - an else branch should give a hint and return "room_one" again
    #
    # Example shape:
    # if choice == "go left":
    #     print("You step through the door into a dark hallway.")
    #     return "room_two"
    # elif choice == "search desk":
    #     print("You find a rusty key!")
    #     inventory.append("rusty key")
    #     return "room_one"
    # else:
    #     print("Hmm, try 'go left' or 'search desk'.")
    #     return "room_one"

    # TODO 4: replace this placeholder return once your branches are written
    return "room_one"


def room_two(inventory):
    """Room 2: reached after leaving room one."""

    # TODO 5: Copy the room_one pattern here. Give this room its own
    # description and its own choices. One choice should require an item
    # from `inventory` (use a for loop, see TODO 6) to "escape".

    print("You are in room two. (Fill this in!)")
    choice = input("What do you do? ").lower()

    return "room_two"


def has_item(inventory, item_name):
    """Return True if item_name is in the player's inventory."""

    # TODO 6: Use a for loop to check each item in `inventory`.
    # If it matches item_name, return True. If the loop finishes without
    # finding it, return False.
    for item in inventory:
        pass

    return False


def main():
    print("=== Escape Room ===")
    print("Type 'quit' at any time to give up.\n")

    inventory = []
    current_room = "room_one"

    # TODO 2: Set the loop condition so the game keeps running until the
    # player escapes or quits. Hint: use a `playing` boolean flag.
    playing = True
    while playing:
        if current_room == "room_one":
            current_room = room_one(inventory)
        elif current_room == "room_two":
            current_room = room_two(inventory)
        elif current_room == "escaped":
            print("\nYou escaped! Congratulations!")
            playing = False
        elif current_room == "quit":
            print("\nMaybe next time!")
            playing = False


if __name__ == "__main__":
    main()
