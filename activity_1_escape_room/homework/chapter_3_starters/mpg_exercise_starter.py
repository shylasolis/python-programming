#!/usr/bin/env python3
"""Starting point for Murach Chapter 3, Exercise 3-1."""

print("The Miles Per Gallon program\n")

miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of gas used: "))

if miles_driven <= 0:
    print("Miles driven must be greater than zero.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero.")
else:
    miles_per_gallon = miles_driven / gallons_used
    print(f"Miles Per Gallon: {miles_per_gallon:.2f}")
