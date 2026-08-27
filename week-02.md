# Week 2: Controlling the Flow — Decisions & Loops

## Overview
This week you move from simple sequential code to code that *thinks* and *repeats*. Conditional statements let your programs make decisions, while loops let them do repetitive work efficiently. These are arguably the two most important building blocks in all of programming, and Python makes both feel intuitive.

## Sections Covered
- Section 10: Conditional Statements (`if`, `elif`, `else`)
- Section 11: Challenges
- Section 12: Nested `if`
- Section 13: Short Circuit Evaluation & Chaining Comparisons
- Section 14: Loops (`while` loop)
- Section 15: `for` Loop
- Section 16: Nested Loop & `match` Case

---

## Daily Plan

### Day 1 — Conditional Statements *(~1–1.5 hrs)*
- [x] Watch Section 10: `if`, `elif`, `else` — syntax, indentation rules, boolean conditions
- [ ] Understand how Python evaluates `True`/`False` expressions

**Mini-task:** Write a grade classifier:
- Score ≥ 90 → "A"
- Score ≥ 75 → "B"
- Score ≥ 60 → "C"
- Below 60 → "Fail"

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")
```

---

### Day 2 — Nested `if` & Short Circuit Evaluation *(~1–1.5 hrs)*
- [ ] Watch Section 12: Nested `if` — conditions inside conditions
- [ ] Watch Section 13: Short Circuit (`and`, `or`, `not`) & Chaining (`1 < x < 10`)

**Mini-task:** Write a login validator. Check if a username is "admin" **and** a password is "1234". Use short circuit evaluation — only check the password if the username is correct.

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Access granted!")
else:
    print("Access denied.")
```

Also try: `10 < 50 < 100` — explain to yourself why Python allows this chaining.

---

### Day 3 — Challenges *(~1 hr)*
- [ ] Watch Section 11: Challenges — solve all conditional challenges from the course
- [ ] Re-attempt any you got wrong, without looking at solutions

**Mini-task:** Build a BMI calculator:
- Take weight (kg) and height (m) as input
- Calculate BMI = weight / height²
- Print category: Underweight / Normal / Overweight / Obese

---

### Day 4 — `while` Loop *(~1–1.5 hrs)*
- [ ] Watch Section 14: `while` loop — condition-driven repetition, `break`, `continue`, `else` on loops
- [ ] Understand infinite loops and how to avoid them

**Mini-task:** Write a number guessing game using a `while` loop — the program picks a secret number (hardcode it), and the user keeps guessing until they get it right. Print "Too high", "Too low", or "Correct!" each attempt.

```python
secret = 42
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Correct! 🎉")
```

---

### Day 5 — `for` Loop, Nested Loops & `match` *(~1–1.5 hrs)*
- [ ] Watch Section 15: `for` loop — iterating over ranges and sequences, `range()`
- [ ] Watch Section 16: Nested loops & `match` case (Python 3.10+ structural pattern matching)

**Mini-task 1:** Print a multiplication table for any number the user inputs using a `for` loop.

**Mini-task 2:** Print a right-angled triangle pattern of stars with nested loops (5 rows).

```python
for i in range(1, 6):
    print("* " * i)
```

**Mini-task 3:** Use a `match` statement to print the day type (Weekday/Weekend) based on a day name input.

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review all control flow concepts from the week
- [ ] Redo the grade classifier and guessing game from memory
- [ ] Make sure you understand the difference between `break` and `continue`

**Mini-task:** Write a script that prints all even numbers between 1 and 50 using both a `for` loop and a `while` loop.

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear
- [ ] Write a 3–5 bullet summary of the week
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **write programs that make decisions and repeat actions** — including nested conditions, looping with `for` and `while`, and using `match` for clean branching logic.
