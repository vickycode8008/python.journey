# Week 8: File Handling — Reading, Writing & Managing Data

## Overview
Real applications need to read and write data that persists beyond a single run. This week you'll master text file handling, binary file operations, and build two substantial projects: a Journal Manager and a Library Management System. These projects will tie together everything you've learned so far in a meaningful, practical context.

## Sections Covered
- Section 46: File Handling (text files)
- Section 47: Project — Journal Manager using Files
- Section 48: Sequential & Random Access Binary Files
- Section 49: Project — Library Management System

---

## Daily Plan

### Day 1 — File Handling Basics *(~1–1.5 hrs)*
- [ ] Watch Section 46: File Handling — `open()`, modes (`r`, `w`, `a`, `rb`, `wb`), `read()`, `readline()`, `readlines()`, `write()`, `writelines()`, `close()`, `with` statement (context manager)
- [ ] Understand why `with open(...) as f:` is always preferred over manual `close()`

**Mini-task:** Write a script that:
1. Creates a `notes.txt` file and writes 3 lines to it
2. Appends a 4th line
3. Reads and prints the entire file
4. Counts and prints the number of lines

```python
# Write
with open("notes.txt", "w") as f:
    f.write("Line 1: Python is fun\n")
    f.write("Line 2: File handling is useful\n")
    f.write("Line 3: I'm learning every day\n")

# Append
with open("notes.txt", "a") as f:
    f.write("Line 4: Added later!\n")

# Read
with open("notes.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line, end="")
    print(f"\nTotal lines: {len(lines)}")
```

---

### Day 2 — File Handling Practice & Edge Cases *(~1 hr)*
- [ ] Review file modes thoroughly: difference between `w` (overwrite) and `a` (append)
- [ ] Handle `FileNotFoundError` with `try/except`
- [ ] Use `os.path.exists()` to check if a file exists before opening

**Mini-task:** Write a safe file reader that:
- Takes a filename from the user
- Checks if it exists before opening
- If it doesn't exist, creates it with a welcome message
- Prints the file contents regardless

```python
import os

filename = input("Enter filename: ")

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Welcome! This file was just created.\n")
    print("File created!")

with open(filename, "r") as f:
    print(f.read())
```

---

### Day 3 — Project: Journal Manager *(~1.5 hrs)*
- [ ] Watch Section 47: Project — Journal Manager using Files
- [ ] Build the project alongside the course (pause and code before watching the solution)

**Features to implement:**
- Add a new journal entry (appended with a timestamp)
- View all journal entries
- Search entries by keyword
- Delete a specific entry (requires reading all, filtering, writing back)

> 💡 **Tip:** This project tests your ability to combine file I/O, loops, string methods, and exception handling all at once.

---

### Day 4 — Binary Files *(~1–1.5 hrs)*
- [ ] Watch Section 48: Sequential & Random Access Binary Files — `pickle` module, `struct` module basics, reading/writing binary data
- [ ] Understand when binary files are used (images, compiled data, serialised objects)

**Mini-task:** Use `pickle` to serialise and deserialise a Python dictionary (simulating saving user data).

```python
import pickle

user_data = {"name": "Vignesh", "score": 1500, "level": 7}

# Save
with open("user_data.pkl", "wb") as f:
    pickle.dump(user_data, f)

# Load
with open("user_data.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded)
print(f"Welcome back, {loaded['name']}! Score: {loaded['score']}")
```

---

### Day 5 — Project: Library Management System *(~1.5 hrs)*
- [ ] Watch Section 49: Project — Library Management System
- [ ] Build the project yourself, then compare with the course solution

**Features to implement:**
- Add a new book (title, author, ISBN, available copies)
- Search for a book by title or author
- Borrow a book (reduce available copies by 1)
- Return a book (increase available copies by 1)
- Save/load book data from a file (text or pickle)

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review all file modes and when to use each
- [ ] Make sure both projects (Journal Manager and Library System) run without errors
- [ ] Add one extra feature to one of the projects on your own

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear
- [ ] Clean up and organise your project code
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should have **two working file-based applications** — a Journal Manager and a Library System — and be comfortable reading, writing, appending, and serialising data to disk.

---

## Mini Project / Practice Challenge

> ✅ **This week already has two designated project sections (Sections 47 & 49).** Focus your energy on building those projects to completion with clean, well-commented code. As an extension, try adding CSV export functionality to the Library Management System using Python's built-in `csv` module (a preview of Week 11!).

---

## LinkedIn Post Draft

> 🐍 **Week 8 / Day 56 of learning Python — I built two real apps this week!**
>
> File handling week was a game-changer. For the first time, my Python programs can actually *remember* things between runs:
>
> ✅ Reading and writing text files with `open()` and the `with` statement
> ✅ Binary file serialisation using Python's `pickle` module
> ✅ **Built two full projects**: a Journal Manager and a Library Management System!
>
> The Library Management System was the most satisfying thing I've built so far — you can add books, search by author, borrow and return copies, and all data is saved to a file. It feels like a real application.
>
> The `with` statement for file handling is one of those Python features that makes the language feel so *thoughtful* — automatic resource cleanup with zero extra code.
>
> Have you ever built a file-based app in Python? What was the trickiest part — reading, writing, or keeping the data format consistent?
>
> #Python #FileHandling #ProjectBuilding #100DaysOfCode #CodingJourney

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
