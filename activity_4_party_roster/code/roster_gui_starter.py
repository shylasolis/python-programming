#!/usr/bin/env python3
"""
Activity 4, Week 9: Party Roster Manager - GUI (STARTER)

The database functions below are already complete (from Week 8) so you can
focus on the GUI. Follow the numbered TODOs in order. Run the file often:
    python code/roster_gui_starter.py
"""

import sqlite3
import tkinter as tk
from tkinter import ttk

DB_FILE = "roster.db"


# --- Database layer (already complete - reused from Week 8) ---

def init_db(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hp INTEGER NOT NULL,
            level INTEGER NOT NULL,
            char_class TEXT NOT NULL
        )
        """
    )
    conn.commit()


def add_character(conn, name, hp, level, char_class):
    conn.execute(
        "INSERT INTO characters (name, hp, level, char_class) VALUES (?, ?, ?, ?)",
        (name, hp, level, char_class),
    )
    conn.commit()


def list_characters(conn):
    cursor = conn.execute("SELECT id, name, hp, level, char_class FROM characters")
    return cursor.fetchall()


def delete_character(conn, character_id):
    conn.execute("DELETE FROM characters WHERE id = ?", (character_id,))
    conn.commit()


# --- GUI layer (build this part) ---

class RosterApp:
    def __init__(self, root, conn):
        self.conn = conn
        root.title("Party Roster Manager")

        form_frame = tk.Frame(root)
        form_frame.grid(row=0, column=0, padx=10, pady=10)

        # TODO 1: Add labeled Entry widgets for name, hp, level, and class
        # using .grid(row=..., column=...) inside form_frame. Save each Entry
        # widget as self.name_entry, self.hp_entry, self.level_entry,
        # self.class_entry so the other methods can read from them.

        add_button = tk.Button(form_frame, text="Add Character", command=self.on_add_click)
        add_button.grid(row=4, column=0, columnspan=2, pady=5)

        delete_button = tk.Button(root, text="Delete Selected", command=self.on_delete_click)
        delete_button.grid(row=2, column=0, pady=5)

        columns = ("id", "name", "hp", "level", "class")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.title())
        self.tree.grid(row=1, column=0, padx=10, pady=10)

        self.refresh_list()

    def on_add_click(self):
        # TODO 2: Read self.name_entry / self.hp_entry / self.level_entry /
        # self.class_entry values, call add_character(...), clear the
        # entries (e.g. entry.delete(0, tk.END)), and call self.refresh_list().
        pass

    def refresh_list(self):
        # TODO 3: Clear the Treeview (self.tree.delete(*self.tree.get_children()))
        # then loop over list_characters(self.conn) and insert each row with
        # self.tree.insert("", tk.END, values=row).
        pass

    def on_delete_click(self):
        # TODO 4: Get the selected Treeview item (self.tree.selection()),
        # read its "id" value, call delete_character(...), then refresh_list().
        pass


def main():
    conn = sqlite3.connect(DB_FILE)
    init_db(conn)

    root = tk.Tk()
    RosterApp(root, conn)
    root.mainloop()

    conn.close()


if __name__ == "__main__":
    main()
