# Activity 4: Party Roster Manager

Over two sessions, turn RPG character data into a SQLite database, then build a Tkinter interface that lets people manage the roster.

## Textbook Connection

This activity applies *Murach's Python Programming*, Section 4:

- Part A, Database Programming: create a SQLite table and use `INSERT`, `SELECT`, and `DELETE` queries.
- Parameterized queries use `?` placeholders to keep user input separate from SQL commands.
- Part B, GUI Programming: use Tkinter widgets, layouts, and callbacks to build a graphical interface.

This project extends Activity 3. A text file can save one character, but a database makes it practical to store, search, and manage many characters. The GUI then provides a more approachable way to use the database.

## Get Started

1. For the database session, open `code/roster_db_starter.py` and run `python code/roster_db_starter.py`.
2. For the GUI session, open `code/roster_gui_starter.py` and run `python code/roster_gui_starter.py`.
3. Complete the `# TODO` comments in order.
4. Use [student_guide.md](student_guide.md) for the activity instructions.

`sqlite3` and Tkinter are included with standard Python installations. Always use parameterized SQL queries; do not place user input directly inside a SQL f-string.

## Files

- `code/roster_db_starter.py`: SQLite console application
- `code/roster_gui_starter.py`: Tkinter application
- `student_guide.md`: detailed activity instructions
- `README_instructor.md`: instructor facilitation guide
