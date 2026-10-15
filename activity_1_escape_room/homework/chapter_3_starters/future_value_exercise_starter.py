#!/usr/bin/env python3
"""Starting point for Murach Chapter 3, Exercise 3-3."""

print("Welcome to the Future Value Calculator\n")

choice = "y"
while choice.lower() == "y":
    monthly_investment = float(input("Enter monthly investment: "))
    yearly_interest_rate = float(input("Enter yearly interest rate: "))
    years = int(input("Enter number of years: "))

    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    future_value = 0

    for _ in range(months):
        future_value += monthly_investment
        future_value += future_value * monthly_interest_rate

    print(f"\nFuture value: ${future_value:,.2f}\n")
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
