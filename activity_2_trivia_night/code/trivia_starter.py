#!/usr/bin/env python3
"""
Activity 2: AI-Generated Trivia Night (STARTER)

Follow the numbered TODOs in order. Run the file often to test as you go:
    python code/trivia_starter.py
"""

from datetime import datetime


# TODO 1: Build a list of at least 5 dictionaries, each with "question",
# "answer", and "category" keys. Ask AI to help generate content, then
# double-check the answers yourself. Example shape:
# {"question": "What is the capital of France?", "answer": "Paris", "category": "Geography"}
QUESTIONS = [
    {"question": "Fill this in!", "answer": "placeholder", "category": "Practice"},
]


def ask_question(question):
    """Ask one question, check the answer, and return True/False."""

    print(f"\n[{question['category']}] {question['question']}")

    # TODO 4: Wrap this input() call (and the comparison below) in a
    # try/except so a blank or unexpected answer doesn't crash the program.
    # If something goes wrong, print a friendly message and return False.
    answer = input("Your answer: ")

    # TODO 2-3: Compare `answer` to question["answer"]. Use .strip() and
    # .lower() on both sides so extra spaces/capitalization don't count
    # as wrong. Return True if it matches, False otherwise.
    return False


def main():
    print("=== Trivia Night ===\n")

    score = 0

    # TODO 5: Loop over QUESTIONS with a for loop. Call ask_question() for
    # each one, print "Correct!" or "Nope, the answer was ..." and keep a
    # running score.
    for question in QUESTIONS:
        pass

    print(f"\nFinal score: {score}/{len(QUESTIONS)}")


if __name__ == "__main__":
    main()
