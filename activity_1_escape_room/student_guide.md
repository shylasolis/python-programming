# Activity 1: Build-Your-Own Escape Room (Student Guide)

Today you'll build a text-based escape room game in Python. You'll write the game logic yourself
(loops and conditionals), and you'll use AI as a teammate to help brainstorm story text and debug
tricky spots — not to write the whole thing for you.

## What You're Building

A console game where the player:

1. Reads a room description
2. Types a choice (like `go left`, `search desk`, `open door`)
3. Sees what happens based on their choice
4. Keeps playing until they escape (or quit)

## Setup

1. Open `code/escape_room_starter.py` in VS Code.
2. Run it once as-is: `python code/escape_room_starter.py` — it won't do much yet, that's expected.
3. Work through the `# TODO` comments in order.

## The TODOs

- **TODO 1:** Write the description for the starting room (a `print()` statement).
- **TODO 2:** Set up the `while` loop condition so the game keeps running until `playing` is `False`.
- **TODO 3–4:** Write `if` / `elif` / `else` branches for the player's choice in Room 1. At least one
  choice should lead to Room 2, and at least one should be a "wrong choice" that gives a hint and
  loops back.
- **TODO 5:** Copy the Room 1 pattern to build Room 2, with its own choices.
- **TODO 6:** Add an `inventory` list. Use a `for` loop to check whether a required item is in the
  player's inventory before letting them escape.

## Using AI the Right Way

Good use of AI in this activity:

- "I have a `while` loop that never ends — here's my code, what condition am I missing?"
- "Can you suggest a spooky one-sentence description for a locked library room?"
- "Give me 3 riddle ideas for a puzzle where the answer is 'candle'."

Not the point of this activity:

- Pasting the whole assignment and asking AI to write the finished game for you. You won't learn the
  loop/conditional pattern that way, and you'll be lost in Week 4+ when things get harder.

**Rule of thumb:** use AI to get unstuck or add flavor — write the control-flow logic (`while`, `if`,
`elif`, `else`) yourself first, then ask AI to review it.

## Stretch Goals (if you finish early)

- Add a wrong-turn penalty: track `attempts` and end the game if the player runs out.
- Add a third room.
- Print a "map" of rooms visited so far using a `for` loop over a list.

## Vocabulary Recap

| Term | Meaning |
|---|---|
| Variable | A named box that holds a value that can change |
| `while` loop | Repeats code while a condition is `True` |
| `if` / `elif` / `else` | Branches code based on a condition |
| List | An ordered collection of items (used here for inventory) |
| Prompt | The instructions you give an AI assistant — be specific! |
