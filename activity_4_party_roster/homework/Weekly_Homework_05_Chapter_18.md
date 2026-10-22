# Weekly Homework 05: GUI Practice

**Course:** Python Programming  
**Textbook:** *Murach's Python Programming*, 2nd edition  
**Required work:** Chapter 18, Exercise 18-2, page 534  
**Submission:** Canvas; due date is posted in Canvas  
**Python:** 3.10 or newer; standard-library `tkinter`  
**Total:** 100 points

## Purpose

Complete the assigned Chapter 18 textbook exercise to practice building and validating a graphical
user interface. This is individual textbook homework, separate from the Party Roster in-class lab.
Do not add RPG features or other requirements that are not part of the assigned exercise.

## Read first (part of the homework)

Before you start the exercise, read these pages of your textbook. Page numbers are the printed
numbers at the bottom of each page. Reading is part of the assignment, and you should refer back to
these pages while you work.

| Pages | What to read | How it helps with the exercise |
|---|---|---|
| 512-517 | Creating a GUI that handles an event | The root window, frames, buttons, and how a button click runs your function. |
| 518-521 | Labels, text entry fields, and grid layout | Placing labels and entry fields, and using `StringVar` objects with `get()` and `set()`. |
| 522-523 | A frame defined by a class | How the window's code is organized, which the MPG starter follows. |
| 524-525 | Message boxes | Showing an error message when the input is not valid. |
| 526-531 | The Future Value program | A complete worked example with a `calculate()` method, number conversion with `float()`, and error handling. It is very close to what you build. |

Optional warm-up: Exercise 18-1 on page 533 modifies the Future Value program.

In your journal, add a short **Reading notes** section before your step-by-step entries. In your own
words, write two or three sentences about what you learned from the reading and one question or
unclear point you had. Do not copy text from the book.

## Read and complete

Complete **Exercise 18-2, steps 1-11**, using the directions in your textbook. The exercise starts
from the MPG program and has you build its window, connect the calculation to a button, and handle
invalid numeric input.

Use one of these starting points:

- The course-provided `activity_4_party_roster/homework/chapter_18/mpg_gui_starter.py` file (open
  a terminal in that folder and run `python mpg_gui_starter.py`).
- A copy of the textbook's Chapter 18 MPG exercise starter, if you have downloaded it.

Choose one starting point and work on a copy. Do not combine the two starting points or use
instructor solutions. The course starter is original course scaffolding for the textbook exercise;
it does not replace the textbook directions.

## What to submit

Submit through Canvas:

1. **Completed Python source file** for the assigned exercise.
2. **One exercise journal**, organized by the assigned numbered steps. For each step, briefly record
   what you changed or tried, what happened when you ran or checked it, and how you responded to any
   problem. If it worked, describe what you observed.
3. **Run information in the journal:** identify the exercise and filename, your Python version,
   any dependencies, and how to run the program.
4. **Testing evidence in the journal:** record the actions or inputs and the results you observed.
   Include an ordinary calculation and relevant invalid or boundary cases.
5. **AI-use note in the journal:** name any tool you used, describe what you asked, identify a
   suggestion you accepted, changed, or rejected, and explain how you checked it. If you did not use
   AI, say so.

AI may be used to explain an error, review a small part of your own code, or suggest a test. Do not
ask AI to complete the textbook exercise for you or submit code you cannot explain. Check suggestions
by running your program and record meaningful assistance in the journal.

The journal may be Canvas text or an uploaded document when Canvas accepts that file type. If
uploads are limited to `.py`, put the journal in the Canvas text entry or submission comments.
Screenshots are optional; clear written observations are enough.

**No README is required. Do not publish textbook homework to Git.** Keep run information, testing
notes, takeaways, and the AI-use note together in the journal. Do not submit the textbook PDF,
instructor solutions, classmates' work, passwords, or other private information.

## Checks to record

Run your completed program and record what you observed when you:

- Open the window and check that its title, labels, entry fields, button, and result field are
  present.
- Enter an ordinary miles-and-gallons pair and calculate the result.
- Enter text that is not a number in either input and verify that the program reports the problem
  without crashing.
- If a relevant boundary case applies to your implementation, record what you tested and observed.

Use the textbook's instructions for the expected program behavior. Do not report a test as passed
unless you actually tried it.

## Rubric: 100 points

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Exercise 18-2: window and variables | 20 | The window has the required title and components, with the required text variables connected to their entries. |
| Exercise 18-2: calculation event | 20 | The button calls the calculation, computes miles per gallon, and displays the result to two decimal places. |
| Exercise 18-2: input validation | 20 | The helper handles invalid numeric text and communicates errors with a message box; valid calculations continue to work. |
| Exercise journal | 25 | Assigned-step coverage and actions (10); observations and learning (10); problem/fix or successful-check explanation and AI-use/non-use note (5). |
| Testing evidence | 10 | Ordinary and relevant invalid/boundary checks are recorded with actual results. |
| File organization and run information | 5 | The source file is identified (2); Python version and usable run/dependency information are in the journal (3). |
| **Total** | **100** | |

Partial credit is available for documented attempts and demonstrated understanding. The journal,
testing, and run details can all be in the same journal; no separate README or testing document is
required. Follow the course-wide
[Homework Submission Expectations](../../course_document_sources/Homework_Submission_Expectations.md).
