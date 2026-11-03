# Part 14 — Learner Activity: Be the Librarian

**Time:** about 25 minutes · **You need:** pen and paper · **No coding needed**

You look after a small library. All the books are stored in one database table called `Books`:

| book_id | title | author | year | available |
|---|---|---|---|---|
| 10 | Python Basics | Lee | 2019 | yes |
| 11 | Intro to AI | Kumar | 2021 | no |
| 12 | World History | Smith | 2015 | yes |
| 13 | Data Structures | Lee | 2020 | no |
| 14 | Cooking 101 | Garcia | 2018 | yes |

---

## Activity 1 — Name the parts

1. How many **rows** does the table have? What does one row describe?
2. How many **columns** does it have? Name two of them.
3. Which column is the **primary key**? How do you know?
4. Why would `author` be a bad primary key?

---

## Activity 2 — Read the query, guess the answer

You don't have to write SQL yet. Just read each query and write down what the database would show.

> 💡 **Remember:** `SELECT` = which columns, `FROM` = which table, `WHERE` = which rows, `ORDER BY` = how to sort.

**a)**
```sql
SELECT title FROM Books WHERE author = 'Lee';
```

**b)**
```sql
SELECT title FROM Books WHERE available = 'yes';
```

**c)**
```sql
SELECT title, year FROM Books ORDER BY year;
```

**d)**
```sql
SELECT COUNT(*) FROM Books WHERE year > 2018;
```

---

## Activity 3 — Fill in the blanks

Fill in each `____` with the right word or value.

**a)** Show the titles of all books written by Kumar.
```sql
SELECT title ____ Books ____ author = 'Kumar';
```

**b)** A new book arrives: *Space Facts* by Ito, 2022, available. Add it with book_id 15.
```sql
____ INTO Books VALUES (15, 'Space Facts', 'Ito', 2022, 'yes');
```

**c)** *Intro to AI* has just been returned. Mark it as available.
```sql
UPDATE Books SET available = '____' WHERE book_id = ____;
```

---

## Activity 4 — Spot the problem

A classmate stored loans in one table like this:

| member_name | member_phone | book_title |
|---|---|---|
| Aigerim | 555-0101 | Intro to AI |
| Aigerim | 555-0101 | Data Structures |
| Ben | 555-0199 | World History |

1. What information is **repeated**?
2. Aigerim gets a new phone number. What could go wrong?
3. How would you fix the design? *(Hint: think about how Part 14 split students and courses into separate tables.)*

---

## ⭐ Bonus challenge (optional) — Join two tables

The library adds a second table, `Loans`, that records who borrowed which book:

| member | book_id |
|---|---|
| Aigerim | 11 |
| Chen | 13 |

What does this query show?

```sql
SELECT Loans.member, Books.title
FROM Loans
JOIN Books ON Loans.book_id = Books.book_id;
```

> 💡 **Hint:** for each row in `Loans`, find the row in `Books` with the same `book_id`.

**Want to try it for real?** Paste this into a file called `library.py` and run it with Python. Change the query on the last lines to test your other answers.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE Books (book_id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, available TEXT);
INSERT INTO Books VALUES
  (10, 'Python Basics', 'Lee', 2019, 'yes'), (11, 'Intro to AI', 'Kumar', 2021, 'no'),
  (12, 'World History', 'Smith', 2015, 'yes'), (13, 'Data Structures', 'Lee', 2020, 'no'),
  (14, 'Cooking 101', 'Garcia', 2018, 'yes');
CREATE TABLE Loans (member TEXT, book_id INTEGER);
INSERT INTO Loans VALUES ('Aigerim', 11), ('Chen', 13);
""")

query = "SELECT title FROM Books WHERE author = 'Lee'"   # <- change me
for row in db.execute(query):
    print(row)
```

---

## ✅ Answers

### Activity 1

1. **5 rows.** Each row describes one book.
2. **5 columns:** `book_id`, `title`, `author`, `year`, `available` (any two).
3. **`book_id`.** Every book has a different number, so it identifies exactly one book.
4. Two books can share an author. Lee wrote both *Python Basics* and *Data Structures*, so `author` is not unique.

### Activity 2

| Query | Result |
|---|---|
| a) | Python Basics, Data Structures |
| b) | Python Basics, World History, Cooking 101 |
| c) | World History 2015, Cooking 101 2018, Python Basics 2019, Data Structures 2020, Intro to AI 2021 |
| d) | **3** (the 2019, 2020 and 2021 books) |

### Activity 3

- **a)** `SELECT title FROM Books WHERE author = 'Kumar';` → shows *Intro to AI*
- **b)** `INSERT INTO Books VALUES (15, 'Space Facts', 'Ito', 2022, 'yes');`
- **c)** `UPDATE Books SET available = 'yes' WHERE book_id = 11;`

### Activity 4

1. Aigerim's name and phone number appear **twice**.
2. If only one row is updated, the table will show **two different phone numbers** for Aigerim, and nobody knows which one is right.
3. Split it into a `Members` table (each member and their phone stored **once**, with a member ID) and a `Loans` table that stores only the member ID and the book ID. This is called **normalisation**.

### ⭐ Bonus

| member | title |
|---|---|
| Aigerim | Intro to AI |
| Chen | Data Structures |

Book 11 is *Intro to AI* and book 13 is *Data Structures*, so the JOIN swaps each book ID for its title.
