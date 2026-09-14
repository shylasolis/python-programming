# Activity 4: Party Roster Manager (Student Guide)

Over two class sessions, you'll upgrade your Activity 3 "save to a text file" character system into a
real database (Week 8), then build a graphical interface for it (Week 9).

## What You're Building

- **Week 8:** A SQLite-backed console app that can add, list, and delete RPG characters in a roster.
- **Week 9:** A Tkinter GUI window that lets you do the same thing with buttons and text fields instead
  of a text menu.

## Week 8 — Database Programming

### Setup

1. Open `code/roster_db_starter.py` in VS Code.
2. Run it: `python code/roster_db_starter.py` — the menu will appear even before you finish the TODOs,
   but the add/list/delete options won't work until you do.

### The TODOs

- **TODO 1:** Write `init_db(conn)` — create a `characters` table (columns: id, name, hp, level,
  char_class) if it doesn't already exist.
- **TODO 2:** Write `add_character(conn, name, hp, level, char_class)` — insert a new row using a
  parameterized `INSERT` (use `?` placeholders, never an f-string with user input in the SQL).
- **TODO 3:** Write `list_characters(conn)` — run a `SELECT` and return all rows.
- **TODO 4:** Write `delete_character(conn, character_id)` — delete one row by id using a parameterized
  `DELETE`.
- **TODO 5:** Finish the console menu loop so add/list/delete all work.

### ⚠️ Security note: SQL injection

Never build a SQL query like this:

```python
# DO NOT DO THIS
cursor.execute(f"SELECT * FROM characters WHERE name = '{name}'")
```

If `name` contains something like `' OR '1'='1`, this can let someone see or delete data they
shouldn't. Always use `?` placeholders instead:

```python
cursor.execute("SELECT * FROM characters WHERE name = ?", (name,))
```

Ask AI to review your queries for this pattern before moving on.

## Week 9 — GUI Programming

### Setup

1. Open `code/roster_gui_starter.py` in VS Code. The database functions from Week 8 are already
   provided at the top so you can focus on the GUI.
2. Run it: `python code/roster_gui_starter.py`.

### The TODOs

- **TODO 1:** Lay out `Entry` widgets (with labels) for name, hp, level, and class using `.grid()`.
  This is a great spot to ask AI for layout boilerplate — read through what it gives you before using it.
- **TODO 2:** Write `on_add_click()` — read the entry values, call `add_character(...)`, clear the
  entries, and refresh the list.
- **TODO 3:** Write `refresh_list()` — clear the list widget and repopulate it from
  `list_characters(conn)`.
- **TODO 4:** Write `on_delete_click()` — get the currently selected row, call
  `delete_character(...)`, then refresh.

## Using AI the Right Way

Good use of AI in this activity:

- "Explain SQL injection in simple terms — why is it dangerous?"
- "Lay out a Tkinter form with 4 labeled entry fields and a submit button using `grid()`."
- "My button click isn't doing anything — here's my `command=` line, what's wrong?"

Not the point of this activity:

- Asking AI to write your database queries for you without understanding them — you need to be able
  to explain why `?` placeholders matter.
- Copy-pasting a whole GUI layout without reading it — you should be able to point to which line
  creates which widget.

**Rule of thumb:** use AI heavily for GUI layout boilerplate (it's tedious and low-risk), but write
and understand every SQL query yourself.

## Stretch Goals (if you finish early)

- Add an `update_character` function + an "Update HP" button.
- Add a search/filter entry field that only shows matching characters.
- Color-code rows by character class.

## Vocabulary Recap

| Term | Meaning |
|---|---|
| Database | Organized, persistent storage you can query |
| Table / row / column | A table is like a spreadsheet; a row is one record, a column is one field |
| SQL | The query language used to talk to a database |
| Parameterized query (`?`) | The safe way to put user input into SQL |
| SQL injection | A security risk from building queries with raw string formatting |
| Widget | A GUI element like a `Label`, `Entry`, `Button`, or list |
| Callback (`command=`) | The function that runs when a widget is clicked/used |
