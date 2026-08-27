# Week 10: Databases — Python Meets SQL

## Overview
Almost every real-world application needs a database. This week you'll learn to connect Python to SQLite (a lightweight, file-based database that requires zero setup), write SQL queries from Python, build a full bank database project, and get an introduction to SQLAlchemy — the industry-standard ORM that lets you interact with databases using pure Python objects instead of raw SQL.

## Sections Covered
- Section 56: Introduction to Databases & SQL
- Section 57: Database Programming in Python (`sqlite3`)
- Section 58: Project — Bank Database using SQLite
- Section 59: SQLAlchemy (ORM basics)

---

## Daily Plan

### Day 1 — SQL Fundamentals *(~1–1.5 hrs)*
- [ ] Watch Section 56: Introduction to Databases & SQL — relational databases, tables, rows, columns, primary keys, foreign keys, `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `WHERE`, `ORDER BY`, `GROUP BY`
- [ ] No code today — focus on understanding the SQL language itself

**Mini-task:** On paper (or in a text file), design a database schema for a simple bookstore:
- `books` table: `id`, `title`, `author`, `price`, `stock`
- `customers` table: `id`, `name`, `email`
- `orders` table: `id`, `customer_id`, `book_id`, `quantity`, `date`

Write out the SQL `CREATE TABLE` statements and 3 `INSERT` statements for each table.

---

### Day 2 — SQLite3 in Python *(~1–1.5 hrs)*
- [ ] Watch Section 57: Database Programming in Python — `import sqlite3`, `connect()`, `cursor()`, `execute()`, `executemany()`, `fetchone()`, `fetchall()`, `commit()`, `close()`, parameterised queries (preventing SQL injection)

**Mini-task:** Create a `students.db` database with a `students` table. Insert 5 students, then query and print all of them.

```python
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL
    )
""")

students = [
    ("Alice", 20, 88.5),
    ("Bob", 22, 72.0),
    ("Charlie", 21, 95.0),
    ("Diana", 23, 67.5),
    ("Eve", 20, 91.0),
]
cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students)
conn.commit()

cursor.execute("SELECT * FROM students ORDER BY grade DESC")
for row in cursor.fetchall():
    print(row)

conn.close()
```

---

### Day 3 — More SQLite Operations *(~1 hr)*
- [ ] Practice `UPDATE` and `DELETE` with `WHERE` clauses
- [ ] Use parameterised queries (always use `?` placeholders — never f-strings in SQL!)
- [ ] Learn to use `sqlite3.Row` for named column access

**Mini-task:** Extend your student database:
- Update Bob's grade to 80.0
- Delete Eve's record
- Select only students with grade ≥ 85 and print their names
- Count total students using `SELECT COUNT(*)`

```python
# Update
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (80.0, "Bob"))

# Delete
cursor.execute("DELETE FROM students WHERE name = ?", ("Eve",))

# Filter
cursor.execute("SELECT name, grade FROM students WHERE grade >= 85")
print(cursor.fetchall())

# Count
cursor.execute("SELECT COUNT(*) FROM students")
print("Total students:", cursor.fetchone()[0])
conn.commit()
```

---

### Day 4 — Project: Bank Database *(~1.5 hrs)*
- [ ] Watch Section 58: Project — Bank Database using SQLite
- [ ] Build the project yourself, then compare with the solution

**Features to implement:**
- `accounts` table: account number, owner name, account type, balance
- `transactions` table: transaction ID, account number, type (credit/debit), amount, timestamp
- Functions: `create_account()`, `deposit()`, `withdraw()`, `get_balance()`, `transaction_history()`
- Use a `try/except` block around all database operations; always `commit()` or `rollback()` appropriately

---

### Day 5 — SQLAlchemy Introduction *(~1–1.5 hrs)*
- [ ] Watch Section 59: SQLAlchemy — ORM concept, installing (`pip install sqlalchemy`), `create_engine()`, `declarative_base()`, defining models, `Session`, `session.add()`, `session.commit()`, `session.query()`

**Mini-task:** Re-create the `students` table using SQLAlchemy models instead of raw SQL:

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Student(Base):
    __tablename__ = "students_orm"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    grade = Column(Float)

    def __repr__(self):
        return f"<Student(name={self.name}, grade={self.grade})>"

engine = create_engine("sqlite:///students_orm.db", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        Student(name="Alice", age=20, grade=88.5),
        Student(name="Bob", age=22, grade=72.0),
    ])
    session.commit()

    students = session.query(Student).order_by(Student.grade.desc()).all()
    for s in students:
        print(s)
```

---

### Day 6 — Review & Light Practice *(~45 min)*
- [ ] Review: raw `sqlite3` vs SQLAlchemy — when would you use each?
- [ ] Review: why parameterised queries prevent SQL injection
- [ ] Re-create a simple table with CRUD operations from memory using `sqlite3`

---

### Day 7 — Buffer & Catch-Up Day *(~30–45 min)*
- [ ] Finish the Bank Database project if not done
- [ ] Write your weekly summary bullets
- [ ] Draft and post your LinkedIn update

---

## Week Goal
By Sunday, you should be able to **design a relational database schema, perform full CRUD operations from Python using `sqlite3`**, and define at least one SQLAlchemy ORM model — demonstrating that your Python programs can now persist structured, queryable data.

---

## Mini Project / Practice Challenge

> ✅ **This week already has a designated project (Section 58 — Bank Database using SQLite).** As an extension challenge, try converting the Bank Database from raw `sqlite3` to SQLAlchemy ORM models. This will solidify your understanding of both approaches and give you a direct comparison.

---

## LinkedIn Post Draft

> 🐍 **Week 10 / Day 70 of learning Python — connecting Python to databases!**
>
> This week, my Python programs learned to *remember things permanently* using databases:
>
> ✅ **SQL fundamentals** — `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `WHERE`, `JOIN`
> ✅ **Python's `sqlite3` module** — running SQL queries directly from Python code
> ✅ **SQLAlchemy ORM** — defining database tables as Python classes (no SQL required!)
>
> The Bank Database project was the highlight — a full system where you can create accounts, deposit/withdraw funds, and view transaction history, all stored in a persistent SQLite database.
>
> The shift from raw SQL to SQLAlchemy ORM felt like going from assembly to high-level code. You define a Python class, and SQLAlchemy handles the table creation, queries, and relationships.
>
> For anyone working with databases: do you prefer writing raw SQL or using an ORM like SQLAlchemy/Django ORM? I'd love to hear the trade-offs from experience!
>
> #Python #SQL #SQLAlchemy #DatabaseProgramming #100DaysOfCode

---

## Notes / Resources

### My Notes
*(Fill this in as you go through the week)*

---

### Questions to Revisit
*(Jot down anything that confused you or that you want to dig deeper into)*
