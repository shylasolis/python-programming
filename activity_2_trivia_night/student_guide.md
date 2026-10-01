# Activity 2: AI-Generated Trivia Night (Student Guide)

Today you'll build a trivia game powered by a question bank you help generate with AI. You'll write
the functions and error handling yourself — AI's job is to help you brainstorm question *content*, not
write your game logic.

## What You're Building

A console trivia game that:

1. Stores questions as a list of dictionaries (question, answer, category)
2. Asks each question with a function, checks the answer, and tracks a score
3. Doesn't crash if the player types something unexpected
4. Prints a final score (and, if you do the stretch goal, a timestamp)

## Setup

1. Open `code/trivia_starter.py` in VS Code.
2. Run it once as-is: `python code/trivia_starter.py` — it will error out until you fill in TODOs 1-2,
   that's expected.
3. Work through the `# TODO` comments in order.

## The TODOs

- **TODO 1:** Build a `QUESTIONS` list with at least 5 dictionaries, each with `"question"`, `"answer"`,
  and `"category"` keys. Ask AI to help generate the content, then double-check the answers are actually
  correct.
- **TODO 2–3:** Write the `ask_question(question)` function. It should print the question, get the
  player's input, compare it (case-insensitively, with extra whitespace stripped) to the correct answer,
  and return `True` or `False`.
- **TODO 4:** Check for a blank answer with an `if` statement, and use `try`/`except` to handle an input
  exception such as `EOFError` without crashing the program.
- **TODO 5:** Write the main game loop: use a `for` loop over `QUESTIONS`, call `ask_question()` for
  each one, keep a running score, and print the final score with an f-string.

## Run-Time Errors and Exceptions

A **run-time error** is a problem that happens after Python has started running your program. For example, dividing by zero raises an exception while the program runs:

```python
result = 10 / 0  # raises ZeroDivisionError when this line runs
```

A **syntax error** is different: Python cannot understand how the code is written, so that code cannot start running. An **exception** is a signal Python raises for a problem during execution. If an exception is not handled, the program usually stops and Python displays an error message. `try` and `except` let your program handle a specific exception and decide what to do next.

Blank input is not an exception. Pressing Enter without typing gives `input()` an empty string, so check it with `if`. When the input stream closes, `input()` raises `EOFError`, which you can handle with `try`/`except`. An unanswered question should not earn a point.

```python
try:
  answer = input("Your answer: ")
except EOFError:
  print("No input received. This answer will count as incorrect.")
  answer = ""

if answer.strip() == "":
  print("A blank answer will count as incorrect.")
```

## Using AI the Right Way

Good use of AI in this activity:

- "Generate 5 trivia questions about [topic] as a Python list of dictionaries with `question`,
  `answer`, and `category` keys." (Then **check the answers yourself** — AI can be wrong!)
- "What edge cases am I missing in this `try`/`except` block?"
- "Explain the difference between a list and a tuple in one sentence."

Not the point of this activity:

- Asking AI to write the whole `ask_question()` function or the full game loop for you. Write the
  function and exception handling yourself first — that's the part you're here to practice.

**Rule of thumb:** use AI to generate the *data* (questions) and to review your logic — write the
functions and `try`/`except` yourself.

## Stretch Goals (if you finish early)

- Store multiple-choice options for each question as a `tuple` (since they shouldn't change).
- Let the player pick a category before playing (filter the list).
- Use `datetime.now()` to print a timestamp with the final score.

`datetime` is Python's standard date-and-time tool. The starter already imports `datetime` for you. `datetime.now()` gets the current date and time from the computer's clock. To make a shorter timestamp, use `strftime()` to format it as text:

```python
finished_at = datetime.now()
timestamp = finished_at.strftime("%Y-%m-%d %H:%M")
print(f"Game finished at: {timestamp}")
```

In this format, `%Y` is the four-digit year, `%m` the month, `%d` the day, `%H` the hour on a 24-hour clock, and `%M` the minute. The time depends on the computer's clock and time zone. This is optional; finish the main game first.

## Vocabulary Recap

| Term | Meaning |
|---|---|
| Function | Reusable code block that can take inputs and return a result |
| List | An ordered, changeable collection (`[]`) |
| Dictionary | A collection of key/value pairs (`{}`) |
| Tuple | An ordered, unchangeable collection (`()`) |
| Run-time error | A problem that happens while a program is running |
| Exception | A signal Python raises for a problem during execution; `try` / `except` can handle it |
| `try` / `except` | Runs code that might raise an exception and handles a specific exception |
| String method | A built-in function for text, like `.strip()` or `.lower()` |
| `datetime` | Python's date-and-time tools; `datetime.now()` gets the current date and time |
