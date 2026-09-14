# Python Programming Class Repo

This repository contains beginner Python practice programs and instructor materials.

## Skills You Will Build

By working through these files, students will practice:

- Using the terminal to run Python programs
- Reading and understanding beginner Python code
- Variables, data types, and user input
- Numeric conversion with `int()` and `float()`
- `while` loops and `for` loops
- Basic function design and program structure
- Conditional logic with `if`, `elif`, and `else`
- Simple debugging by finding and fixing code mistakes
- Building a basic desktop GUI with Tkinter

## What Is In This Repo

- `code/future_value.py`
  - Console app that calculates future value with repeated user runs
- `code/future_value_errors.py`
  - Similar app with intentional bug(s) for debugging practice
- `code/future_value_gui.py`
  - Tkinter GUI version of the future value calculator
- `code/guess_the_number.py`
  - Number guessing game with loop and conditionals
- `instructor/`
  - Exam materials and answer key

## Do Students Need A Virtual Environment?

Short answer: not required for this repo right now.

Why:

- The current code uses only Python standard library modules (`random`, `locale`, `tkinter`), which are included with Python.

Recommended anyway:

- Yes, it is still good beginner practice to use a virtual environment.
- It helps students build habits they will need in future projects with external packages.

## First-Time Setup (Windows)

### 1) Install Python

1. Go to https://www.python.org/downloads/
2. Download and install Python 3.12+ (or newest stable version).
3. During install, check the box: **Add Python to PATH**.

### 2) Open Command Prompt

1. Press the Windows key.
2. Type: `cmd`
3. Press Enter.

### 3) Go to the folder where you want your class work

Example:

```bat
cd C:\Users\YourName\Documents
mkdir class-work
cd class-work
```

### 4) Clone (copy) the GitHub repository to your computer

1. In GitHub, open this repo.
2. Click the green **Code** button.
3. Copy the HTTPS URL.
4. In Command Prompt, run:

```bat
git clone https://github.com/shylasolis/python-programming.git
cd python-programming
```

### 5) Create and activate a virtual environment (recommended)

```bat
python -m venv .venv
.venv\Scripts\activate
```

If activation worked, you should see `(.venv)` at the start of your command line.

### 6) Install dependencies

```bat
pip install -r code\requirements.txt
```

Note: this file currently has no third-party packages, so install may finish quickly.

### 7) Run a program

```bat
python code\guess_the_number.py
```

Other examples:

```bat
python code\future_value.py
python code\future_value_errors.py
python code\future_value_gui.py
```

### 8) Deactivate virtual environment when done

```bat
deactivate
```

## First-Time Setup (macOS)

### 1) Install Python

Option A (official installer):

1. Go to https://www.python.org/downloads/
2. Install Python 3.12+ (or newest stable version).

Option B (Homebrew):

```bash
brew install python
```

### 2) Open Terminal

1. Press Command + Space to open Spotlight.
2. Type: `Terminal`
3. Press Return.

### 3) Go to the folder where you want your class work

Example:

```bash
cd ~/Documents
mkdir -p class-work
cd class-work
```

### 4) Clone (copy) the GitHub repository to your computer

1. In GitHub, open this repo.
2. Click the green **Code** button.
3. Copy the HTTPS URL.
4. In Terminal, run:

```bash
git clone https://github.com/shylasolis/python-programming.git
cd python-programming
```

### 5) Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If activation worked, you should see `(.venv)` at the start of your command line.

### 6) Install dependencies

```bash
pip install -r code/requirements.txt
```

### 7) Run a program

```bash
python3 code/guess_the_number.py
```

Other examples:

```bash
python3 code/future_value.py
python3 code/future_value_errors.py
python3 code/future_value_gui.py
```

### 8) Deactivate virtual environment when done

```bash
deactivate
```

## Daily Student Workflow (After Setup)

From the project folder:

### Windows

```bat
.venv\Scripts\activate
python code\guess_the_number.py
deactivate
```

### macOS

```bash
source .venv/bin/activate
python3 code/guess_the_number.py
deactivate
```

## How To Push Your Work To GitHub

Use these commands after making changes.

### Windows or macOS

```bash
git status
git add .
git commit -m "Complete beginner Python exercises"
git push
```

What each command does:

- `git status`: shows changed files
- `git add .`: stages your changes
- `git commit -m "..."`: saves a snapshot with a message
- `git push`: uploads your commit to GitHub

## Troubleshooting

- `python` command not found:
  - Windows: reinstall Python and make sure **Add Python to PATH** is checked.
  - macOS: try `python3` instead of `python`.
- `git` command not found:
  - Install Git from https://git-scm.com/downloads
- Virtual environment activation blocked on Windows:
  - In PowerShell, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Instructor Note

The file `code/future_value_errors.py` intentionally includes a bug for debugging practice. Students should run it, read the error, and fix it as a guided exercise.
