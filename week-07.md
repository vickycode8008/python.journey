# Week 7: Advanced Functions — Built-ins, Lambdas, Decorators & Error Handling

## Overview
This week fills in the remaining "advanced function" toolkit and introduces one of the most important topics in production Python: exception handling. You'll learn to use Python's powerful built-in functions, write compact lambda expressions, build decorators, and write code that fails *gracefully* — a mark of a professional developer.

## Sections Covered
- Section 40: Built-in Functions & Modules
- Section 41: Certification Style Practice Test
- Section 42: Lambda / Nested Functions / Decorators
- Section 43: Exception Handling (`try`, `except`, `raise`)
- Section 44: User-Defined Exceptions / `else` / `finally`
- Section 45: Challenges

---

## Daily Plan

### Day 1 — Built-in Functions & Modules *(~1–1.5 hrs)*
- [ ] Watch Section 40: Built-in Functions & Modules — `map()`, `filter()`, `zip()`, `enumerate()`, `sorted()`, `any()`, `all()`, `abs()`, `round()`, `min()`, `max()`, `sum()`, `range()`; importing standard library modules (`math`, `random`, `os`, `sys`)

**Mini-task:** Use built-in functions to solve these in one line each:
1. Square all numbers in a list using `map()`
2. Filter only positive numbers from a list using `filter()`
3. Pair two lists together using `zip()`
4. Loop with index using `enumerate()`

```python
nums = [-3, 1, -7, 4, 9, -2, 6]

squared = list(map(lambda x: x**2, nums))
positives = list(filter(lambda x: x > 0, nums))

names = ["Alice", "Bob", "Charlie"]
scores = [88, 72, 95]
paired = list(zip(names, scores))

for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
```

---

### Day 2 — Certification Practice Test *(~1 hr)*
- [ ] Watch Section 41: Certification Style Practice Test
- [ ] Treat it as a real test — attempt every question before checking answers
- [ ] Note every question you got wrong and review the concept behind it

**Mini-task:** Write a one-page cheat sheet of every built-in function you've learned so far, with a one-line description of each.

---

### Day 3 — Lambda, Nested Functions & Decorators *(~1–1.5 hrs)*
- [ ] Watch Section 42: Lambda / Nested Functions / Decorators
  - **Lambda**: `lambda args: expression` — anonymous one-liner functions
  - **Nested functions**: functions defined inside other functions (closures)
  - **Decorators**: functions that wrap other functions with extra behaviour

**Mini-task 1:** Use `lambda` with `sorted()` to sort a list of tuples by the second element:

```python
students = [("Alice", 88), ("Bob", 72), ("Charlie", 95)]
ranked = sorted(students, key=lambda s: s[1], reverse=True)
print(ranked)
```

**Mini-task 2:** Write a `timer` decorator that measures how long a function takes to run using `import time`.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(10_000_000)
```

---

### Day 4 — Exception Handling *(~1–1.5 hrs)*
- [ ] Watch Section 43: Exception Handling — `try`, `except`, `raise`, catching specific exceptions (`ValueError`, `ZeroDivisionError`, `TypeError`, `FileNotFoundError`, `IndexError`, `KeyError`)
- [ ] Understand the exception hierarchy

**Mini-task:** Write a robust division calculator that handles:
- Division by zero
- Non-numeric input

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return f"Result: {result:.2f}"
    finally:
        print("Division attempted.")  # always runs

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))
```

---

### Day 5 — User-Defined Exceptions & Challenges *(~1–1.5 hrs)*
- [ ] Watch Section 44: User-Defined Exceptions / `else` / `finally` — creating custom exception classes with `class MyError(Exception)`
- [ ] Watch Section 45: Challenges — solve all exception-handling challenges

**Mini-task:** Create a custom `AgeError` exception that is raised if a user's age is negative or greater than 150.

```python
class AgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Must be between 0 and 150.")

def validate_age(age):
    if age < 0 or age > 150:
        raise AgeError(age)
    return f"Valid age: {age}"

try:
    print(validate_age(200))
except AgeError as e:
    print(e)
```

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review: `map()` vs list comprehension — when to use each
- [ ] Review: `try/except/else/finally` flow — draw a flowchart
- [ ] Re-implement the `timer` decorator from memory

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear
- [ ] Write your weekly summary bullets
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **write decorators, use built-in functions fluently, and handle errors gracefully** — your code should never crash unexpectedly, and you should know how to create meaningful custom exceptions.

---

## Mini Project / Practice Challenge

**"Robust Calculator App"**

Build a command-line calculator that:
1. Uses a `while` loop to keep running until the user types `quit`
2. Supports `+`, `-`, `*`, `/`, `**`, and `%`
3. Handles all edge cases with `try/except`: invalid input, division by zero, unknown operators
4. Has a `@log` decorator on the calculation function that prints the inputs and result
5. Defines a custom `InvalidOperatorError` exception

---

## LinkedIn Post Draft

> 🐍 **Week 7 / Day 49 of learning Python — decorators, lambdas, and error handling!**
>
> This week felt like levelling up from "beginner" to "intermediate" Python:
>
> ✅ **Decorators** — wrapping functions with extra behaviour using `@decorator` syntax (it's like middleware for your functions!)
> ✅ **Lambda functions** — compact, anonymous one-liners perfect for `map()`, `filter()`, and `sorted()`
> ✅ **Exception handling** — `try/except/else/finally` and even creating custom exceptions
>
> The decorator concept was the trickiest this week — functions that take functions and return functions. But once I built a `@timer` decorator that measures execution time, it clicked completely.
>
> Writing code that *fails gracefully* also feels like a superpower. Professional software doesn't crash — it handles errors and communicates them clearly.
>
> What's your favourite Python decorator — built-in or custom? I'm especially curious about `@property` and `@staticmethod` (coming soon in OOP week!).
>
> #Python #Decorators #ExceptionHandling #100DaysOfCode #CodingJourney

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
