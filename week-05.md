# Week 5: Collections — Tuples, Sets & Dictionaries.

## Overview
Python gives you four core collection types, and this week you complete the set. Tuples offer immutable, ordered storage; sets give you unique, unordered collections perfect for membership testing; and dictionaries are the key-value powerhouses behind almost every real-world Python application. Understanding when to use which structure is a crucial developer skill.

## Sections Covered
- Section 29: Tuple
- Section 30: Sets
- Section 31: Challenges Using Sets
- Section 32: Dictionary
- Section 33: Challenges Using Dictionary

---

## Daily Plan

### Day 1 — Tuples *(~1–1.5 hrs)*
- [ ] Watch Section 29: Tuple — creation, indexing, slicing, packing/unpacking, `count()`, `index()`, `len()`
- [ ] Understand why tuples are immutable and when to prefer them over lists (e.g., fixed data, dictionary keys, function returns)

**Mini-task:** Store a person's record as a tuple `(name, age, city)`. Unpack it into separate variables and print each one. Try to modify an element and observe the `TypeError`.

```python
person = ("Vignesh", 25, "Chennai")
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")

# Swap two variables using tuple unpacking
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

---

### Day 2 — Sets *(~1–1.5 hrs)*
- [ ] Watch Section 30: Sets — `set()`, `add()`, `remove()`, `discard()`, union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`), `issubset()`, `issuperset()`
- [ ] Key insight: sets automatically eliminate duplicates

**Mini-task:** Given two lists of students who attended Monday's class and Tuesday's class, use sets to find:
- Students who attended **both** days
- Students who attended **only** Monday
- Students who attended **at least one** day

```python
monday = {"Alice", "Bob", "Charlie", "Diana"}
tuesday = {"Bob", "Diana", "Eve", "Frank"}

both = monday & tuesday
only_monday = monday - tuesday
either_day = monday | tuesday

print("Both days:", both)
print("Only Monday:", only_monday)
print("At least one day:", either_day)
```

---

### Day 3 — Set Challenges *(~1 hr)*
- [ ] Watch Section 31: Challenges Using Sets
- [ ] Solve all challenges on your own first

**Mini-task:** Write a duplicate remover — take a list with repeated numbers, convert to a set to get unique values, then convert back to a sorted list.

```python
numbers = [4, 2, 7, 2, 4, 9, 1, 7, 3]
unique_sorted = sorted(set(numbers))
print(unique_sorted)  # [1, 2, 3, 4, 7, 9]
```

---

### Day 4 — Dictionaries *(~1–1.5 hrs)*
- [ ] Watch Section 32: Dictionary — `{key: value}`, `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `setdefault()`, nested dicts, dict comprehensions

**Mini-task:** Build a contact book as a dictionary. Add 3 contacts, look one up by name, update a phone number, and delete an entry. Then iterate over all contacts and print them neatly.

```python
contacts = {
    "Alice": {"phone": "9876543210", "email": "alice@email.com"},
    "Bob": {"phone": "9123456789", "email": "bob@email.com"},
    "Charlie": {"phone": "9000000001", "email": "charlie@email.com"},
}

# Lookup
print(contacts.get("Alice"))

# Update
contacts["Alice"]["phone"] = "9999999999"

# Delete
del contacts["Charlie"]

# Print all
for name, info in contacts.items():
    print(f"{name}: {info['phone']} | {info['email']}")
```

---

### Day 5 — Dictionary Challenges *(~1–1.5 hrs)*
- [ ] Watch Section 33: Challenges Using Dictionary
- [ ] Solve all challenges on your own first

**Mini-task:** Write a word frequency counter — take a sentence, split it into words, and count how many times each word appears using a dictionary.

```python
sentence = "the cat sat on the mat and the cat wore a hat"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Sort by frequency
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")
```

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review the difference between list, tuple, set, and dict — when to use each
- [ ] Write one example of each from memory
- [ ] Try a dict comprehension: `{word: len(word) for word in ["apple", "banana", "cherry"]}`

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear
- [ ] Write your weekly summary bullets
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **choose the right collection type** for any situation, and confidently use tuples for fixed data, sets for unique/membership operations, and dicts for key-value lookups.

---

## Mini Project / Practice Challenge

**"Inventory Manager"**

Build a simple inventory system using a dictionary where:
- Keys are product names (strings)
- Values are another dict with `price` and `quantity`

Implement these operations:
1. Add a new product
2. Update quantity when a sale is made
3. Print all products with total value (price × quantity)
4. Find the most expensive product
5. Remove out-of-stock items (quantity = 0)

```python
inventory = {
    "Apple": {"price": 0.5, "quantity": 100},
    "Banana": {"price": 0.2, "quantity": 0},
    "Cherry": {"price": 1.5, "quantity": 50},
}
# Your code here...
```

---

## LinkedIn Post Draft

> 🐍 **Week 5 / Day 35 of learning Python — unlocking the full collection toolkit!**
>
> Halfway through the course, and this week was a deep dive into Python's collection types:
>
> ✅ **Tuples** — immutable sequences, perfect for data that shouldn't change
> ✅ **Sets** — lightning-fast for checking membership and finding unique values
> ✅ **Dictionaries** — the workhorse of Python; key-value pairs that power everything from APIs to databases
>
> The "aha!" moment this week? Using set operations (`|`, `&`, `-`) to compare two groups of data in a single line — what would have taken a nested loop now takes just one character. Elegant.
>
> My mini project was an Inventory Manager that uses nested dictionaries to track products, prices, quantities, and total stock value.
>
> Curious: do you have a go-to trick for working with Python dicts? Drop it in the comments! 🔑
>
> #Python #LearnToCode #DataStructures #100DaysOfCode #PythonBeginners

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
