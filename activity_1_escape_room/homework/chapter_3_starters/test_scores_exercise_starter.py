#!/usr/bin/env python3
"""Starting point for Murach Chapter 3, Exercise 3-2."""

print("The Test Scores program")
print("Enter test scores from 0 through 100.")
print("Enter 999 when you are finished.\n")

total_score = 0
score_count = 0
score = int(input("Enter test score: "))

while score != 999:
    if score < 0 or score > 100:
        print("Test score must be from 0 through 100. Try again.")
    else:
        total_score += score
        score_count += 1

    score = int(input("Enter test score: "))

if score_count > 0:
    average_score = round(total_score / score_count)
    print(f"\nTotal Score: {total_score}")
    print(f"Average Score: {average_score}")
else:
    print("\nNo test scores were entered.")
