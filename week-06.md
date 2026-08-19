# Week 6: Functions — Writing Reusable, Elegant Code.

## Overview
Functions transform you from someone who writes scripts into someone who writes *programs*. This week covers everything from defining basic functions to advanced concepts like variable-length arguments, multiple return values, iterators, generators, and recursion. Writing good functions is the single biggest leap in code quality you can make as a beginner.

## Sections Covered
- Section 34: Functions
- Section 35: Challenges
- Section 36: Variable Length Arguments & Multiple Return
- Section 37: Challenges
- Section 38: Iterators / Generators / Recursion
- Section 39: Challenges

---

## Daily Plan

### Day 1 — Function Fundamentals *(~1–1.5 hrs)*
- [ ] Watch Section 34: Functions — `def`, parameters vs arguments, default parameters, keyword arguments, `return` statement, scope (local vs global)
- [ ] Understand the difference between a function that *prints* and one that *returns*

**Mini-task:** Write three functions:
1. `greet(name)` — returns a greeting string
2. `circle_area(radius)` — returns the area (use `import math`)
3. `is_even(n)` — returns `True` or `False`

```python
import math

def greet(name="World"):
    return f"Hello, {name}!"

def circle_area(radius):
    return math.pi * radius ** 2

def is_even(n):
    return n % 2 == 0

print(greet("Vignesh"))
print(f"Area: {circle_area(5):.2f}")
print(is_even(7))
```

---

### Day 2 — Challenges & Scope *(~1 hr)*
- [ ] Watch Section 35: Challenges — implement all challenge functions
- [ ] Experiment with `global` keyword — understand when (and why not) to use it

**Mini-task:** Write a `factorial(n)` function and a `fibonacci(n)` function using only loops (no recursion yet). Test with several inputs.

---

### Day 3 — Variable Length Arguments & Multiple Return *(~1–1.5 hrs)*
- [ ] Watch Section 36: `*args` (positional), `**kwargs` (keyword), returning multiple values (tuples)
- [ ] Understand how to unpack `*args` and iterate `**kwargs`

**Mini-task 1:** Write a `total(*prices)` function that accepts any number of prices and returns the sum.

**Mini-task 2:** Write a `stats(numbers)` function that returns `(min, max, avg)` as a tuple, then unpack it on call.

```python
def total(*prices):
    return sum(prices)

def stats(*numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = stats(10, 25, 7, 42, 3)
print(f"Min: {lo}, Max: {hi}, Avg: {avg:.2f}")
```

**Mini-task 3:** Write a `display_info(**kwargs)` function that prints each key-value pair on a new line.

---

### Day 4 — More Challenges *(~1 hr)*
- [ ] Watch Section 37: Challenges — solve all problems using `*args` and `**kwargs`
- [ ] Write a function that accepts a mix of positional and keyword arguments

**Mini-task:** Write `make_sentence(*words, separator=" ")` that joins words with the given separator (default: space).

---

### Day 5 — Iterators, Generators & Recursion *(~1–1.5 hrs)*
- [ ] Watch Section 38: Iterators / Generators / Recursion
  - **Iterator**: `__iter__()` and `__next__()`, `iter()`, `next()`
  - **Generator**: `yield` keyword — lazy evaluation
  - **Recursion**: base case + recursive case

**Mini-task 1 (Recursion):** Write recursive versions of `factorial(n)` and `fibonacci(n)`. Compare with your loop versions.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Mini-task 2 (Generator):** Write a generator `count_up(start, end)` that yields numbers one at a time. Consume it with a `for` loop.

```python
def count_up(start, end):
    while start <= end:
        yield start
        start += 1

for num in count_up(1, 5):
    print(num)
```

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review: when to use `*args` vs `**kwargs` vs default parameters
- [ ] Trace through a recursive function call by hand (draw the call stack)
- [ ] Explain to yourself (or write down) the difference between a generator and a list comprehension

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear
- [ ] Write your weekly summary bullets
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **write clean, reusable functions** with default/variable-length arguments, multiple return values, and understand the concept of recursion and generators well enough to use them in simple scenarios.

---

## Mini Project / Practice Challenge

**"Function Library"**

Build a Python module (single `.py` file) containing at least 6 utility functions:

1. `is_prime(n)` — returns True if n is prime
2. `celsius_to_fahrenheit(c)` — temperature converter
3. `count_vowels(s)` — counts vowels in a string
4. `flatten(*lists)` — flattens multiple lists into one using `*args`
5. `describe(**person)` — prints a person's profile from keyword arguments
6. `fibonacci_gen(n)` — a generator that yields the first n Fibonacci numbers

Then write a `main()` function that demonstrates all of them.

---

## LinkedIn Post Draft

> 🐍 **Week 6 / Day 42 of learning Python — functions changed everything!**
>
> This week I went from writing scripts to writing *programs* — and it all comes down to functions:
>
> ✅ `def`, parameters, default values, and `return` — the foundation
> ✅ `*args` and `**kwargs` — writing flexible functions that accept any input
> ✅ **Recursion** and **Generators** — two mind-bending but powerful concepts
>
> Recursion was the biggest challenge this week. Tracing through `factorial(5)` by hand — watching it unwind back to the base case — was one of those genuine "oohhh!" moments.
>
> Generators are also fascinating: instead of building a whole list in memory, you can `yield` values one at a time. Perfect for large datasets.
>
> I built a personal "function library" this week — a reusable set of utilities I can import into future projects. Feels great to produce something actually useful!
>
> What's your most-used custom Python function? Share it below! 👇
>
> #Python #Functions #LearnToCode #100DaysOfCode #CodingJourney

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
