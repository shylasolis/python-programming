# Activity 4: Party Roster Manager

Build a roster manager across two class sessions. In Week 8, store RPG characters in SQLite from a
console menu. In Week 9, add a Tkinter interface that uses the same database.

## Skills practiced

- **Relational data and SQL:** define a table and add, list, and delete records. In this project,
  each character is a row with an automatically assigned ID.
- **Safe database access:** use parameterized queries for values supplied by a user, and explain why
  SQL values should not be assembled with string formatting.
- **Event-driven interfaces:** arrange Tkinter widgets and connect button callbacks to database
  operations. Be able to trace an entry from the form to the database and back to the roster.
- **Input validation and testing:** reject missing text and invalid or nonpositive numeric values
  without adding a row or crashing the application.

## Textbook connection

This activity applies *Murach's Python Programming*, Section 4: Chapter 17, “How to work with a
database,” for SQLite operations, followed by Chapter 18, “How to build a GUI program,” for Tkinter
widgets, layout, and event callbacks.

## Textbook homework

Homework is separate from the in-class Party Roster lab and uses the assigned textbook exercises,
not extensions to the RPG project:

- [Chapter 17 homework: Exercise 17-2 (PDF)](homework/Weekly_Homework_04_Chapter_17.pdf)
- [Chapter 18 homework: Exercise 18-2 (PDF)](homework/Weekly_Homework_05_Chapter_18.pdf)

Each assignment has its own course-provided `.py` starting point. Submit completed homework and the
required journal through Canvas; do not publish textbook homework solutions to Git. See the
[homework submission expectations](../course_document_sources/Homework_Submission_Expectations.md)
for the consistent course-wide instructions and rubric. Editable Markdown sources are in the
`homework` folder beside the PDFs.

## Requirements and setup

- Python 3.10 or newer.
- No third-party packages. The standard-library `sqlite3` and `tkinter` modules must be available.
- Credit any outside code/data and meaningful AI assistance in your own project README.
- Open a terminal in this folder (`activity_4_party_roster`), then run the applicable starter. Run
  both sessions from this folder so they use the same `roster.db`:

  ```text
  python code/roster_db_starter.py
  python code/roster_gui_starter.py
  ```

Complete the `# TODO` comments in order. See [student_guide.md](student_guide.md) for the session
tasks, tests, and submission checklist.

The program creates `roster.db` in the current working directory when it runs; no sample data file
is required. Add sample characters through the program. Do not include a database containing
personal or confidential information in a submission.

## Example

The Week 8 console menu includes:

```text
1) Add character
2) List roster
3) Delete character
4) Quit
```

After adding a character, listing the roster shows its generated ID, name, class, level, and HP.
The Week 9 window provides the corresponding form, roster, and delete action.

## Known limitations

The core application supports adding, listing, and deleting one character at a time. It does not
include editing, searching, multiple-user access, or database backups. Document limitations of
your own completed version accurately in its README and journal.

## Credits

This activity uses course-provided starter code. Credit any additional outside code or data and any
meaningful AI assistance in your submitted project README.

## Files

- `code/roster_db_starter.py`: Week 8 SQLite console application
- `code/roster_gui_starter.py`: Week 9 Tkinter application
- `student_guide.md`: detailed activity and submission instructions
- `student_guide.pdf`: printable copy of the student guide
- `homework/`: textbook-only Chapter 17 and Chapter 18 assignments and their Python starters

Use the starter files for your work. Do not submit or publish instructor-only reference solutions.
