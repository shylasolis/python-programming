# Activity 3: RPG Character Forge (Student Guide)

Over two class sessions you'll build a `Character` class for a simple RPG, then make it so your
character is saved to a file and can be loaded back later. This is your first time writing your own
class, so take it slow — ask AI to explain any term you don't recognize, but write the class yourself.

## What You're Building

- **Week 6:** A `Character` class with attributes (name, hp, level, inventory) and methods (take
  damage, level up, display stats).
- **Week 7:** The ability to save your character to a file and load it back later, so it isn't lost
  when the program closes.

## Setup

1. Open `code/character_forge_starter.py` in VS Code.
2. Run it once as-is: `python code/character_forge_starter.py` — it won't do much yet, that's expected.
3. Work through the `# TODO` comments in order (TODOs 1–4 in Week 6, TODOs 5–6 in Week 7).

## Week 6 TODOs

- **TODO 1:** Write `__init__(self, name, hp, level)` to set `self.name`, `self.hp`, `self.level`, and
  `self.inventory = []`.
- **TODO 2:** Write `take_damage(self, amount)` — reduce `self.hp`, but don't let it go below 0.
- **TODO 3:** Write `level_up(self)` — increase `self.level` by 1 and restore `self.hp` to its max.
- **TODO 4:** Write `display_stats(self)` — print the character's name, hp, level, and inventory.

## Week 7 TODOs

- **TODO 5:** Write `save_to_file(self, filename)` — a method on `Character` that writes `name`, `hp`,
  and `level` to a text file (one per line works fine).
- **TODO 6:** Write `load_character(filename)` — a standalone function that reads the file back and
  returns a new `Character` built from those values. Use `try`/`except FileNotFoundError` so it doesn't
  crash if no save file exists yet.

## Using AI the Right Way

Good use of AI in this activity:

- "Explain the difference between a class and an object using a real-world analogy."
- "Explain the difference between a function and a method."
- "I keep getting `NameError: name 'self' is not defined` — what does `self` mean and why do I need it?"
- "What's the difference between file mode `'w'` and `'a'`?"

Not the point of this activity:

- Asking AI to write your whole `Character` class. This is your first class ever — the point is to
  build the mental model of "attributes + methods" yourself, with AI as a tutor for concepts you get
  stuck on, not a code generator for the whole thing.

**Rule of thumb:** if you don't understand a term (class, object, attribute, method, constructor,
`self`), ask AI to explain *the concept* before you ask it to help with *your code*.

## Stretch Goals (if you finish early)

- Save/load your `inventory` list too, not just name/hp/level.
- Create a `Wizard(Character)` or `Warrior(Character)` subclass with one special method.
- Support saving more than one character to the same file.

## Vocabulary Recap

| Term | Meaning |
|---|---|
| Class | A blueprint for creating objects (defines attributes and methods) |
| Object / instance | A specific thing created from a class |
| Attribute | A piece of data stored on an object (e.g. `self.hp`) |
| Method | A function that belongs to a class |
| `__init__` | The constructor — runs automatically when you create a new object |
| File I/O | Reading from and writing to files on disk |
| `with open(...)` | The standard way to open a file so it closes automatically |
