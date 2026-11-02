# Part 14 — Learner Activity: Run a Tiny Library Database

**Time:** about 30 minutes · **You need:** pen and paper. Optional: Python 3 (no install needed beyond Python itself) or any online SQLite playground.

You are the librarian of a small university library. The database has three tables:

**`Members`**

| member_id | name | faculty |
|---|---|---|
| 1 | Aigerim | Science |
| 2 | Ben | Arts |
| 3 | Chen | Science |

**`Books`**

| book_id | title | author | year |
|---|---|---|---|
| 10 | Python Basics | Lee | 2019 |
| 11 | Intro to AI | Kumar | 2021 |
| 12 | World History | Smith | 2015 |
| 13 | Data Structures | Lee | 2020 |

**`Loans`**

| member_id | book_id | returned |
|---|---|---|
| 1 | 10 | yes |
| 1 | 11 | no |
| 3 | 13 | no |
| 2 | 12 | yes |

---

## Part A — Understand the design

1. What is the **primary key** of `Books`?
2. Which columns in `Loans` are **foreign keys**, and which tables do they point to?
3. Why is it better to store `member_id` in `Loans` instead of the member's full name and faculty?

## Part B — Write the SQL

Write a query for each question, then predict the result.

4. Show the titles of all books written by `Lee`.
5. Show all books published **after 2018**, newest first.
6. Count how many members are in the `Science` faculty.
7. A new member, `Dana` (Arts), joins with `member_id` 4. Add her.
8. Show the **names of members** and the **titles** of books they have **not returned yet**. *(Hint: you need a JOIN across all three tables.)*

## Part C — Think about it

9. The library computer crashes halfway through recording a loan, *after* the book is marked "borrowed" but *before* the loan row is saved. Which ACID property protects against this, and how?

---

## Try it in Python (optional)

Copy this into a file called `library.py` and run `python library.py`. Then replace the query at the bottom with your own answers.

```python
import sqlite3

db = sqlite3.connect(":memory:")   # a temporary database that lives in memory
db.executescript("""
CREATE TABLE Members (member_id INTEGER PRIMARY KEY, name TEXT, faculty TEXT);
CREATE TABLE Books   (book_id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER);
CREATE TABLE Loans   (member_id INTEGER REFERENCES Members(member_id),
                      book_id   INTEGER REFERENCES Books(book_id),
                      returned  TEXT);

INSERT INTO Members VALUES (1, 'Aigerim', 'Science'), (2, 'Ben', 'Arts'), (3, 'Chen', 'Science');
INSERT INTO Books VALUES (10, 'Python Basics', 'Lee', 2019), (11, 'Intro to AI', 'Kumar', 2021),
                         (12, 'World History', 'Smith', 2015), (13, 'Data Structures', 'Lee', 2020);
INSERT INTO Loans VALUES (1, 10, 'yes'), (1, 11, 'no'), (3, 13, 'no'), (2, 12, 'yes');
""")

query = "SELECT title FROM Books WHERE author = 'Lee';"   # <- change me
for row in db.execute(query):
    print(row)
```

---

## ✅ Answers / expected outcomes

1. `book_id`, because it is unique for every book.
2. `member_id` → `Members`, and `book_id` → `Books`.
3. Each fact is then stored once (normalisation). If a member changes faculty, only one row in `Members` changes; storing names in `Loans` would repeat data and risk an **update anomaly**. Two members could also share a name, but never an ID.

4.
```sql
SELECT title FROM Books WHERE author = 'Lee';
```
Result: `Python Basics`, `Data Structures`.

5.
```sql
SELECT title, year FROM Books WHERE year > 2018 ORDER BY year DESC;
```
Result: `Intro to AI` (2021), `Data Structures` (2020), `Python Basics` (2019).

6.
```sql
SELECT COUNT(*) FROM Members WHERE faculty = 'Science';
```
Result: `2`.

7.
```sql
INSERT INTO Members VALUES (4, 'Dana', 'Arts');
```

8.
```sql
SELECT Members.name, Books.title
FROM Loans
JOIN Members ON Loans.member_id = Members.member_id
JOIN Books   ON Loans.book_id   = Books.book_id
WHERE Loans.returned = 'no';
```
Result: `Aigerim | Intro to AI` and `Chen | Data Structures`.

9. **Atomicity.** Marking the book and saving the loan are wrapped in one **transaction**. If the crash happens before `COMMIT`, the DBMS rolls back the half-finished work, so the database never shows a book as borrowed with no loan record. (Durability then guarantees that a *committed* loan is not lost.)
