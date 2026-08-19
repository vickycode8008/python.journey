# Week 11: The Final Frontier — CSV, GUIs, Threads, DSA & NumPy.

## Overview
You've made it to the final week! This week is a power-packed survey of Python's broader ecosystem — practical topics that professional Python developers use daily. You'll process CSV data, build a desktop GUI with Tkinter, explore multithreading for concurrent tasks, review essential data structure modules, work with dates and times, and get your first taste of NumPy for numerical computing.

## Sections Covered
- Section 60: CSV Files
- Section 61: Tkinter (GUI programming)
- Section 62: MultiThreading
- Section 63: Data Structure Modules (`collections`, `heapq`, `queue`)
- Section 64: Date and Time (`datetime` module)
- Section 65: NumPy Arrays

---

## Daily Plan

### Day 1 — CSV Files *(~1–1.5 hrs)*
- [ ] Watch Section 60: CSV Files — `import csv`, `csv.reader()`, `csv.writer()`, `csv.DictReader()`, `csv.DictWriter()`, reading/writing headers and rows

**Mini-task:** Create a `students.csv` file with columns `name,age,grade`. Write 5 student records, then read them back and print only students with grade ≥ 80.

```python
import csv

# Write
with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "grade"])
    writer.writeheader()
    writer.writerows([
        {"name": "Alice", "age": 20, "grade": 88},
        {"name": "Bob", "age": 22, "grade": 72},
        {"name": "Charlie", "age": 21, "grade": 95},
        {"name": "Diana", "age": 23, "grade": 67},
        {"name": "Eve", "age": 20, "grade": 91},
    ])

# Read & filter
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    top_students = [row for row in reader if int(row["grade"]) >= 80]
    for s in top_students:
        print(f"{s['name']}: {s['grade']}")
```

---

### Day 2 — Tkinter GUI *(~1.5 hrs)*
- [ ] Watch Section 61: Tkinter — `Tk()`, `Label`, `Button`, `Entry`, `Frame`, `pack()` / `grid()`, event handling with `command=`, `mainloop()`
- [ ] Understand the event-driven programming model

**Mini-task:** Build a **simple temperature converter GUI** — the user types a Celsius value, clicks "Convert", and the Fahrenheit result appears in a label.

```python
import tkinter as tk

def convert():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{fahrenheit:.1f} °F")
    except ValueError:
        result_label.config(text="Invalid input!")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x150")

tk.Label(root, text="Celsius:").pack(pady=5)
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Convert to °F", command=convert).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

root.mainloop()
```

---

### Day 3 — MultiThreading *(~1–1.5 hrs)*
- [ ] Watch Section 62: MultiThreading — `import threading`, `Thread(target=func)`, `start()`, `join()`, thread safety, `Lock`, the GIL (Global Interpreter Lock)
- [ ] Understand when to use threads (I/O-bound tasks) vs `multiprocessing` (CPU-bound tasks)

**Mini-task:** Write a script that downloads (simulate with `time.sleep`) 3 "files" concurrently using threads and prints how long it took vs doing it sequentially.

```python
import threading
import time

def download(name, duration):
    print(f"Starting download: {name}")
    time.sleep(duration)
    print(f"Finished: {name}")

files = [("file1.mp4", 2), ("file2.zip", 3), ("file3.pdf", 1)]

# Sequential
start = time.time()
for name, duration in files:
    download(name, duration)
print(f"Sequential time: {time.time() - start:.2f}s\n")

# Concurrent
start = time.time()
threads = [threading.Thread(target=download, args=(n, d)) for n, d in files]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Concurrent time: {time.time() - start:.2f}s")
```

---

### Day 4 — Data Structure Modules & Dates *(~1–1.5 hrs)*
- [ ] Watch Section 63: Data Structure Modules — `collections.Counter`, `collections.defaultdict`, `collections.deque`, `heapq` (min-heap), `queue.Queue`
- [ ] Watch Section 64: Date and Time — `datetime.date`, `datetime.datetime`, `datetime.timedelta`, `strftime()`, `strptime()`

**Mini-task 1 (collections):**

```python
from collections import Counter, defaultdict, deque

# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(Counter(words))  # most common words

# defaultdict
word_lengths = defaultdict(list)
for word in words:
    word_lengths[len(word)].append(word)
print(dict(word_lengths))

# deque (efficient queue)
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d)
```

**Mini-task 2 (datetime):**

```python
from datetime import datetime, timedelta

now = datetime.now()
print("Now:", now.strftime("%d %B %Y, %H:%M"))

birthday = datetime(1999, 8, 19)
age_days = (now - birthday).days
print(f"Days since birth: {age_days}")

deadline = now + timedelta(days=30)
print("Deadline:", deadline.strftime("%d %B %Y"))
```

---

### Day 5 — NumPy Arrays *(~1–1.5 hrs)*
- [ ] Watch Section 65: NumPy Arrays — `import numpy as np`, `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, array shape/reshape, broadcasting, vectorised operations, `np.sum()`, `np.mean()`, `np.std()`, `np.dot()`
- [ ] Install if needed: `pip install numpy`

**Mini-task:** Perform basic data analysis on a sales dataset using NumPy:

```python
import numpy as np

sales = np.array([1500, 2300, 1800, 3100, 2750, 980, 4200])

print("Total sales:  ₹", np.sum(sales))
print("Average:      ₹", np.mean(sales))
print("Std Dev:      ₹", round(np.std(sales), 2))
print("Best day:     ₹", np.max(sales))
print("Worst day:    ₹", np.min(sales))
print("Above avg:", sales[sales > np.mean(sales)])

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A × B =\n", np.dot(A, B))
```

---

### Day 6 — Review & Course Retrospective *(~1 hr)*
- [ ] Review all Week 11 topics — which ones excited you most?
- [ ] Write down 3 Python areas you want to explore further after this course (e.g., web dev with Flask/Django, data science with Pandas, automation with Selenium)
- [ ] Revisit your very first Week 1 script — notice how much more you can do now!
- [ ] Make sure all mini-projects from all 11 weeks run without errors

---

### Day 7 — Celebration & Wrap-Up *(~1 hr)*
- [ ] 🎉 Celebrate completing Abdulbari's Python course!
- [ ] Organise your project folder — clean up your code files
- [ ] Write your final LinkedIn post
- [ ] Plan your next learning goal: a Python framework, a personal project, or a certification

---

## Week Goal
By Sunday, you should be able to **read and write CSV files, build a basic Tkinter GUI, run tasks concurrently with threads, use `collections` and `datetime` confidently, and perform vectorised computations with NumPy** — demonstrating broad Python fluency across the ecosystem.

---

## Mini Project / Practice Challenge

**"Student Analytics Dashboard (CLI)"**

Pull together everything from Week 11:

1. Read student data from a `students.csv` file
2. Use `datetime` to add a "days until graduation" column based on a target date
3. Use `Counter` to find the most common grade bucket (A/B/C/F)
4. Use NumPy to compute mean, median, and standard deviation of grades
5. Display results in a formatted Tkinter window with labels
6. (Optional) Use a thread to simulate a "live refresh" every 5 seconds

This capstone challenge ties together CSV, datetime, collections, NumPy, and Tkinter!

---

## LinkedIn Post Draft

> 🐍 **Week 11 / Day 77 — I just completed Abdulbari's Python course on Udemy! 🎉**
>
> 11 weeks. 65 sections. Countless hours of coding. Here's what I covered in the final week:
>
> ✅ **CSV files** — reading/writing structured data with `csv.DictReader` and `DictWriter`
> ✅ **Tkinter** — building a real desktop GUI (Temperature Converter!) with event handling
> ✅ **MultiThreading** — running tasks concurrently; cut "download" time from 6s to 3s
> ✅ **NumPy** — vectorised array operations that make data analysis feel effortless
>
> Looking back at Week 1 where I typed `print("Hello, World!")` — and comparing it to this week's threaded GUI with CSV and NumPy — is genuinely surreal.
>
> My next steps: dive into Pandas & Matplotlib, and start building a personal project. The course gave me the foundation; now it's time to build.
>
> To everyone who followed along — THANK YOU for the encouragement! 🙏 What should I build first?
>
> #Python #CourseComplete #100DaysOfCode #NumPy #Tkinter #LearningJourney

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
