"""Course starter GUI for Murach Chapter 18, Exercise 18-2.

Run from this folder:
    python mpg_gui_starter.py
"""

import tkinter as tk
from tkinter import messagebox


class MpgApp:
    def __init__(self, root):
        self.root = root
        root.title("TODO: Set the MPG program title")

        # The textbook starter begins with a single label and entry.
        self.miles_var = tk.StringVar()
        tk.Label(root, text="Miles Driven:").grid(
            row=0, column=0, padx=8, pady=8, sticky="e"
        )
        tk.Entry(root, textvariable=self.miles_var).grid(
            row=0, column=1, padx=8, pady=8
        )

        # TODO 1: Create StringVar objects for the gallons-used and MPG fields.
        # TODO 2: Add the remaining labels, entry fields, and Calculate button.
        # Arrange all seven interface components as directed by the textbook.

    def calculate(self):
        # TODO 3: Get both input values with get_float(). If either value is
        # invalid, stop. Calculate miles divided by gallons, round to two
        # decimal places, and show the result in the MPG field.
        pass

    def get_float(self, value, field_name):
        # TODO 4: Convert value to a float. For invalid text, show an error
        # with messagebox.showerror() and return None. Do not let invalid input
        # close the application.
        pass


def main():
    root = tk.Tk()
    MpgApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
