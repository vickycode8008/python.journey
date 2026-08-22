# Week 1: Python Foundations — Getting Started.

## Overview
This week lays the absolute groundwork for your Python journey. You'll set up your environment, understand how Python thinks about data through variables and datatypes, and start writing your first real expressions. These fundamentals are the backbone of everything you'll build in the coming weeks.

## Sections Covered
- Section 1: Introduction to Python
- Section 2: Setup & Installation (Python + IDE)
- Section 3: Variables
- Section 4: Datatypes
- Section 5: Literals & Constants
- Section 6: Base Conversion & Type Conversion
- Section 7: Operators & Expressions
- Section 8: Challenges
- Section 9: Arithmetic & Assignment Operators

---

## Daily Plan

### Day 1 — Introduction & Setup *(~1 hr)*
- [x] Watch Section 1: Introduction to Python — understand what Python is, where it's used, and why it's beginner-friendly
- [x] Watch Section 2: Setup & Installation — install Python and your IDE (VS Code or PyCharm)
- [x] Write and run your very first `print("Hello, World!")` script

**Mini-task:** Write a script that prints your name, your city, and why you want to learn Python — one `print()` per line.

---

### Day 2 — Variables & Datatypes *(~1 hr)*
- [x] Watch Section 3: Variables — naming rules, assignment, re-assignment
- [x] Watch Section 4: Datatypes — `int`, `float`, `str`, `bool`, `NoneType`
- [x] Experiment with `type()` to inspect different variables

**Mini-task:** Create variables for your name (str), age (int), height in metres (float), and whether you've coded before (bool). Print each one with a descriptive label.

```python
name = "Vignesh"
age = 25
height = 1.75
has_coded_before = False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Coded before?", has_coded_before)
```

---

### Day 3 — Literals, Constants & Type Conversion *(~1–1.5 hrs)*
- [ ] Watch Section 5: Literals & Constants — numeric, string, boolean literals; using `UPPER_CASE` for constants
- [ ] Watch Section 6: Base Conversion & Type Conversion — `int()`, `float()`, `str()`, `bin()`, `hex()`, `oct()`

**Mini-task:** Convert the number `255` to binary, octal, and hexadecimal. Then take a string `"42"` and add it to an integer `8` after converting it correctly.

```python
num = 255
print(bin(num))   # binary
print(oct(num))   # octal
print(hex(num))   # hexadecimal

result = int("42") + 8
print(result)     # should print 50
```

---

### Day 4 — Operators & Expressions *(~1–1.5 hrs)*
- [ ] Watch Section 7: Operators & Expressions — arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), comparison, logical operators
- [ ] Watch Section 9: Arithmetic & Assignment Operators — `+=`, `-=`, `*=`, `/=`, `//=`, `**=`

**Mini-task:** Write a mini calculator script. Given two numbers, print their sum, difference, product, quotient (regular and floor), remainder, and power.

```python
a = 17
b = 5

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
```

---

### Day 5 — Challenges *(~1–1.5 hrs)*
- [ ] Watch Section 8: Challenges — work through the practice problems
- [ ] Re-attempt any challenges that felt tricky without looking at the solution first

**Mini-task:** Solve these on your own:
1. Swap two variables without using a third variable.
2. Calculate the area and perimeter of a rectangle given its length and width.
3. Convert a temperature from Celsius to Fahrenheit using the formula: `F = (C × 9/5) + 32`

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review your notes from Days 1–5
- [ ] Re-read the official Python docs on [Built-in Types](https://docs.python.org/3/library/stdtypes.html) for 10 minutes
- [ ] Redo 2–3 challenges from scratch without notes

**Mini-task:** Write a script that asks (via `input()`) for a user's birth year and prints their approximate age.

```python
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print("You are approximately", age, "years old.")
```

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything you missed or felt shaky on
- [ ] Write a short summary (3–5 bullet points) of what you learned this week
- [ ] Draft and post your LinkedIn update (see below)

---

## Week Goal
By Sunday, you should be able to **write a Python script from scratch** that uses variables of different types, performs arithmetic and type conversions, and prints formatted output — all without referring to notes.

---

## Mini Project / Practice Challenge

**"Personal Info Card Generator"**

Write a Python script that stores your name, age, height (in cm), favourite programming language, and a fun fact about yourself in variables. Then print a neatly formatted info card like:

```
===========================
       MY INFO CARD
===========================
Name    : Vignesh
Age     : 25
Height  : 175 cm
Lang    : Python
Fun Fact: I once read a book in one sitting.
===========================
```

Use string concatenation and type conversion where needed.

---

## LinkedIn Post Draft

> 🐍 **Week 1 / Day 7 of learning Python — and I'm officially hooked!**
>
> I just wrapped up my first week studying Python through Abdulbari's course on Udemy, and here's what I covered:
>
> ✅ Setting up Python and my IDE from scratch
> ✅ Variables, datatypes (int, float, str, bool), and type conversion
> ✅ Arithmetic, comparison, and assignment operators
>
> My biggest takeaway? Python's syntax is refreshingly readable — it almost feels like writing plain English. The `//` floor division and `%` modulus operators were new to me and I can already see how useful they'll be.
>
> I built a mini "Personal Info Card" script by the end of the week — small, but it felt great to see something I wrote actually run! 🎉
>
> If you're also learning Python or have been through Abdulbari's course, I'd love to hear your tips. What concept tripped you up the most at the start?
>
> #Python #LearnToCode #100DaysOfCode #PythonBeginners #CodingJourney

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
