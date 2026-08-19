# Week 3: Mastering Strings — Text Processing & Pattern Matching.

## Overview
Strings are everywhere — user inputs, file contents, APIs, web pages. This week you'll go deep into Python's powerful string capabilities, from basic operations to built-in methods, formatted output, and even regular expressions for pattern matching. By the end, you'll be able to manipulate and format text like a pro.

## Sections Covered
- Section 17: String Introduction
- Section 18: Projects Using Strings
- Section 19: String Class & Methods
- Section 20: Projects Using String Methods
- Section 21: Formatted Printing (`f-strings`, `format()`, `%`)
- Section 22: Regular Expressions (`re` module)

---

## Daily Plan

### Day 1 — String Basics *(~1–1.5 hrs)*
- [ ] Watch Section 17: String Introduction — string literals, indexing (`s[0]`), slicing (`s[1:4]`), negative indexing, `len()`
- [ ] Understand that strings are immutable in Python

**Mini-task:** Given the string `"PythonProgramming"`, extract:
- First 6 characters
- Last 11 characters
- Every other character
- The string reversed

```python
s = "PythonProgramming"
print(s[:6])       # Python
print(s[6:])       # Programming
print(s[::2])      # every other character
print(s[::-1])     # reversed
```

---

### Day 2 — String Methods *(~1–1.5 hrs)*
- [ ] Watch Section 19: String Class & Methods — `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`, `find()`, `count()`, `startswith()`, `endswith()`, `isdigit()`, `isalpha()`, etc.

**Mini-task:** Write a "string analyzer" that takes a sentence as input and prints:
- Word count
- Character count (no spaces)
- The sentence in UPPER case
- Whether it starts with a capital letter
- All occurrences of the word "the" (case-insensitive)

```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))
print("Characters (no spaces):", len(sentence.replace(" ", "")))
print("Uppercase:", sentence.upper())
print("Starts with capital:", sentence[0].isupper())
print('"the" count:', sentence.lower().count("the"))
```

---

### Day 3 — Projects Using Strings *(~1–1.5 hrs)*
- [ ] Watch Section 18: Projects Using Strings
- [ ] Watch Section 20: Projects Using String Methods
- [ ] Implement the projects from the course yourself before watching the solution

**Mini-task:** Build a simple **Palindrome Checker** — strip spaces, lowercase, then compare the string to its reverse.

```python
word = input("Enter a word: ").strip().lower().replace(" ", "")
if word == word[::-1]:
    print(f'"{word}" is a palindrome! 🔁')
else:
    print(f'"{word}" is NOT a palindrome.')
```

---

### Day 4 — Formatted Printing *(~1 hr)*
- [ ] Watch Section 21: Formatted Printing — `f-strings` (preferred), `str.format()`, `%` formatting, alignment and padding

**Mini-task:** Display a nicely formatted receipt using f-strings with aligned columns:

```python
items = [("Apple", 3, 0.99), ("Bread", 1, 2.49), ("Milk", 2, 1.75)]
print(f"{'Item':<10} {'Qty':>5} {'Price':>8} {'Total':>8}")
print("-" * 35)
grand_total = 0
for name, qty, price in items:
    total = qty * price
    grand_total += total
    print(f"{name:<10} {qty:>5} {price:>8.2f} {total:>8.2f}")
print("-" * 35)
print(f"{'GRAND TOTAL':>24} {grand_total:>8.2f}")
```

---

### Day 5 — Regular Expressions *(~1–1.5 hrs)*
- [ ] Watch Section 22: Regular Expressions — `re` module, `re.match()`, `re.search()`, `re.findall()`, `re.sub()`, common patterns (`\d`, `\w`, `\s`, `+`, `*`, `?`, `^`, `$`)

**Mini-task:** Write a script that validates a simple email address using regex — must have characters, an `@`, a domain, and a `.com` / `.org` / `.net` ending.

```python
import re

email = input("Enter an email: ")
pattern = r'^[\w.-]+@[\w.-]+\.(com|org|net)$'
if re.match(pattern, email):
    print("✅ Valid email!")
else:
    print("❌ Invalid email.")
```

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review string slicing and the 5 most useful string methods
- [ ] Re-do the palindrome checker and receipt formatter from memory
- [ ] Try to write a regex pattern that extracts all phone numbers from a block of text

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear from the week
- [ ] Write your weekly summary bullets
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **slice, search, transform, and format strings** confidently, and write a basic regular expression to validate or extract patterns from text.

---

## Mini Project / Practice Challenge

**"Text Statistics Tool"**

Write a script that accepts a multi-line paragraph (hard-code it or paste it in) and outputs:
- Total word count
- Total character count (with and without spaces)
- Most common word (use a loop and a dictionary to count)
- Count of sentences (split by `.`, `!`, `?`)
- Whether any word appears more than 3 times

This is a great preview of real-world text processing!

---

## LinkedIn Post Draft

> 🐍 **Week 3 / Day 21 of learning Python — strings are more powerful than I expected!**
>
> This week was all about text — and Python's string handling blew me away:
>
> ✅ Slicing and indexing strings (including reversal with `[::-1]`)
> ✅ 15+ built-in string methods: `split()`, `join()`, `strip()`, `replace()`, `find()`, and more
> ✅ Beautiful formatted output with f-strings and alignment padding
>
> The wild card this week? **Regular expressions.** Writing a pattern like `r'^[\w.-]+@[\w.-]+'` to validate emails felt like learning a secret language — frustrating for 20 minutes, then *incredibly* satisfying.
>
> My mini project was a "Text Statistics Tool" that counts words, sentences, and the most repeated word in a paragraph. Surprisingly fun to build!
>
> Have you ever used regex in a real project? What was the most useful pattern you wrote? 👇
>
> #Python #LearnToCode #RegularExpressions #100DaysOfCode #PythonBeginners

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
