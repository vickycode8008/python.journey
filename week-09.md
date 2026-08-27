# Week 9: Object-Oriented Programming — Thinking in Objects

## Overview
OOP is the paradigm shift that makes large software manageable. This week you'll learn to model the world as objects with attributes and behaviours — then extend those models through inheritance and polymorphism. These concepts are the foundation of virtually every major Python framework: Django, Flask, SQLAlchemy, and more.

## Sections Covered
- Section 50: OOP Introduction (`class`, `__init__`, instance vs class attributes, methods)
- Section 51: Challenges
- Section 52: Inheritance
- Section 53: Challenges using Inheritance & Inner Class
- Section 54: Polymorphism
- Section 55: Challenges using Polymorphism and Operator Overloading

---

## Daily Plan

### Day 1 — Classes & Objects *(~1–1.5 hrs)*
- [ ] Watch Section 50: OOP Introduction — `class` keyword, `__init__` constructor, `self`, instance attributes vs class attributes, instance methods
- [ ] Key insight: a class is a *blueprint*, an object is an *instance* of that blueprint

**Mini-task:** Design a `BankAccount` class with:
- Attributes: `owner`, `balance`
- Methods: `deposit(amount)`, `withdraw(amount)`, `get_balance()`
- Validation: prevent withdrawals exceeding the balance

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining: ₹{self.balance}")

    def get_balance(self):
        return self.balance

acc = BankAccount("Vignesh", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)
```

---

### Day 2 — OOP Challenges & Special Methods *(~1 hr)*
- [ ] Watch Section 51: Challenges
- [ ] Explore dunder (magic) methods: `__str__`, `__repr__`, `__len__`

**Mini-task:** Add a `__str__` method to your `BankAccount` class so that `print(acc)` shows: `"Account[Vignesh]: ₹1300"`.

```python
def __str__(self):
    return f"Account[{self.owner}]: ₹{self.balance}"
```

**Extra challenge:** Create a `Student` class with name, age, and a list of grades. Add a `gpa()` method and a `__str__` method.

---

### Day 3 — Inheritance *(~1–1.5 hrs)*
- [ ] Watch Section 52: Inheritance — single inheritance, `super()`, method overriding, `isinstance()`, `issubclass()`
- [ ] Understand the "is-a" relationship: `SavingsAccount` **is-a** `BankAccount`

**Mini-task:** Extend your `BankAccount` to create:
- `SavingsAccount` — adds an `interest_rate` attribute and an `add_interest()` method
- `CheckingAccount` — adds an `overdraft_limit` attribute (allows negative balance up to limit)

```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ₹{interest:.2f}")

savings = SavingsAccount("Vignesh", 10000)
savings.add_interest()
```

---

### Day 4 — Inheritance Challenges & Inner Classes *(~1–1.5 hrs)*
- [ ] Watch Section 53: Challenges using Inheritance & Inner Class
- [ ] Understand inner (nested) classes — a class defined inside another class

**Mini-task:** Build a `School` class that contains an inner `Student` class. The `School` class manages a list of `Student` objects.

```python
class School:
    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade
        def __str__(self):
            return f"{self.name} (Grade {self.grade})"

    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll(self, name, grade):
        self.students.append(School.Student(name, grade))

    def list_students(self):
        for s in self.students:
            print(s)
```

---

### Day 5 — Polymorphism & Operator Overloading *(~1–1.5 hrs)*
- [ ] Watch Section 54: Polymorphism — same method name, different behaviour in subclasses; `@abstractmethod` from `abc`
- [ ] Watch Section 55: Challenges — operator overloading with `__add__`, `__sub__`, `__eq__`, `__lt__`

**Mini-task 1 (Polymorphism):** Create a `Shape` base class with an `area()` method, then subclass `Circle`, `Rectangle`, and `Triangle`. Call `area()` on a list of mixed shapes.

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"{type(shape).__name__}: area = {shape.area():.2f}")
```

**Mini-task 2 (Operator Overloading):** Add `__add__` to a `Vector` class so that `v1 + v2` returns a new `Vector`.

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review: Class → Object → Inheritance → Polymorphism (draw a class hierarchy diagram)
- [ ] Re-implement the `BankAccount` hierarchy from memory
- [ ] Explain to yourself: what does `super()` do, and why is it important?

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Catch up on anything unclear
- [ ] Write your weekly summary bullets
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **design a class hierarchy from scratch** — with a base class, subclasses, method overriding, and polymorphic behaviour — and explain the four pillars of OOP: encapsulation, abstraction, inheritance, and polymorphism.

---

## Mini Project / Practice Challenge

**"Animal Kingdom Simulator"**

Build a hierarchy:
- Base class: `Animal` — attributes: `name`, `sound`; methods: `speak()`, `__str__()`
- Subclasses: `Dog`, `Cat`, `Bird` — each overrides `speak()` with their own sound
- `Bird` has an extra method `fly()`
- Create a `Zoo` class that holds a list of animals and has a `roll_call()` method that calls `speak()` on each

Add operator overloading: `zoo1 + zoo2` should merge two zoos into one.

---

## LinkedIn Post Draft

> 🐍 **Week 9 / Day 63 of learning Python — Object-Oriented Programming clicked this week!**
>
> OOP was the concept I feared most as a beginner. This week, it finally made sense:
>
> ✅ **Classes & Objects** — blueprints and instances; `__init__`, `self`, methods
> ✅ **Inheritance** — reusing and extending code with `super()` and method overriding
> ✅ **Polymorphism** — the same method name doing different things depending on the object
>
> The most satisfying exercise? Building a `Shape` hierarchy where `Circle`, `Rectangle`, and `Triangle` all have an `area()` method — and calling it on a mixed list *just works*.
>
> OOP feels like the difference between a pile of bricks and a blueprint — suddenly your code has *structure*.
>
> If you've used OOP in Python, what's one real-world design pattern (Strategy, Factory, Singleton...) you'd recommend a beginner try next?
>
> #Python #OOP #ObjectOrientedProgramming #100DaysOfCode #CodingJourney

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
