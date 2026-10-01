
def room_one(inventory):
    """Room 1: the player arrives here first."""

    # TODO 1: Print a short description of the starting room.
        # Example: "You wake up in a dusty library. There is a door to the LEFT
        # and a desk in front of you."
    
    choice = input("What do you do? ").lower()


#MY new file
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
       



if __name__ == "__main__":
    main()