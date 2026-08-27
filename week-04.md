# Week 4: Lists — Python's Swiss Army Knife

## Overview
Lists are one of the most frequently used data structures in Python — ordered, mutable, and incredibly flexible. This week you'll master creating and manipulating lists, using Python's rich set of list functions, and writing elegant list comprehensions that compress loops into single, readable lines.

## Sections Covered
- Section 23: List Introduction
- Section 24: Challenges
- Section 25: List Functions
- Section 26: Challenges
- Section 27: List Comprehensions & Nested Lists
- Section 28: Challenges

---

## Daily Plan

### Day 1 — List Basics *(~1–1.5 hrs)*
- [ ] Watch Section 23: List Introduction — creating lists, indexing, slicing, updating elements, nested lists, `len()`
- [ ] Understand that lists are mutable (unlike strings)

**Mini-task:** Create a list of your 5 favourite movies. Then:
- Print the first and last movie
- Change the second movie to a new title
- Add a 6th movie at the end
- Print the full list and its length

```python
movies = ["Interstellar", "3 Idiots", "Inception", "The Matrix", "Parasite"]
print("First:", movies[0])
print("Last:", movies[-1])
movies[1] = "Taare Zameen Par"
movies.append("Dune")
print("All movies:", movies)
print("Count:", len(movies))
```

---

### Day 2 — List Functions & Methods *(~1–1.5 hrs)*
- [ ] Watch Section 25: List Functions — `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `index()`, `count()`, `extend()`, `copy()`, `clear()`
- [ ] Understand the difference between `sort()` (in-place) and `sorted()` (returns new list)

**Mini-task:** Given a list of random numbers `[42, 7, 19, 3, 88, 55, 21]`:
- Sort ascending and descending
- Find the max, min, and sum without built-in functions (use a loop)
- Remove duplicates manually

---

### Day 3 — Challenges *(~1 hr)*
- [ ] Watch Section 24 & 26: Challenges
- [ ] Solve all challenge problems on your own first, then compare

**Mini-task:** Write a script that:
1. Takes 5 numbers from the user (using a `for` loop with `input()`)
2. Stores them in a list
3. Prints the average, the maximum, and the minimum

```python
numbers = []
for i in range(5):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

print("Average:", sum(numbers) / len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
```

---

### Day 4 — List Comprehensions *(~1–1.5 hrs)*
- [ ] Watch Section 27: List Comprehensions & Nested Lists — `[expr for item in iterable if condition]`, 2D lists (matrix)

**Mini-task 1:** Use list comprehensions to:
- Generate squares of numbers 1–10
- Filter only even numbers from 1–20
- Convert a list of strings to uppercase in one line

```python
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
```

**Mini-task 2:** Create a 3×3 matrix using a nested list comprehension and print it row by row.

```python
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in matrix:
    print(row)
```

---

### Day 5 — Nested Lists & More Challenges *(~1–1.5 hrs)*
- [ ] Watch Section 28: Challenges (list comprehension challenges)
- [ ] Practice writing comprehensions for at least 5 problems

**Mini-task:** Write a program to flatten a 2D list into a 1D list using a list comprehension:

```python
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in nested for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review list methods and comprehension syntax
- [ ] Re-solve 2–3 challenges without notes
- [ ] Compare `list.sort()` vs `sorted(list)` — write an example showing the difference

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear
- [ ] Write your weekly summary bullets
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **build, manipulate, and transform lists** confidently — including sorting, filtering, using comprehensions, and working with 2D nested lists.

---

## Mini Project / Practice Challenge

**"Student Grade Manager"**

Build a script that:
1. Stores student names and their scores in a list of lists: `[["Alice", 88], ["Bob", 72], ...]`
2. Calculates and prints the class average
3. Identifies the top scorer and lowest scorer
4. Prints all students who passed (score ≥ 60), sorted by score descending
5. Uses a list comprehension to extract just the names of failed students

This combines list creation, sorting, filtering, and comprehensions in one real-world scenario.

---

## LinkedIn Post Draft

> 🐍 **Week 4 / Day 28 of learning Python — lists are my new best friends!**
>
> This week I went deep on one of Python's most versatile data structures: **Lists**. Here's what clicked:
>
> ✅ Creating and manipulating lists — indexing, slicing, updating, nesting
> ✅ 10+ list methods: `append()`, `sort()`, `pop()`, `extend()`, and more
> ✅ **List comprehensions** — one of Python's most elegant features!
>
> That moment when I wrote `[x**2 for x in range(1, 11)]` and got the first 10 squares in a single line? That's when Python started feeling genuinely *fun*.
>
> My mini project this week was a Student Grade Manager — collecting scores, computing averages, ranking students, and filtering pass/fail using comprehensions.
>
> What Python feature surprised you the most when you first learned it? For me, it's definitely list comprehensions. 🤩
>
> #Python #LearnToCode #ListComprehension #100DaysOfCode #PythonBeginners

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
