# 2.6 Databases

![Dandroid running the school library](../../../assets/dandroid/dandroid-proud.png)

**Chapter 2 · Dandroid's Instructions** · Study Guide pp. 91–98 · Slide 30 · Test Bank T15, M15

> **Mission.** Dandroid now runs the school library: 5,000 books, 800 students, and everyone borrowing at once. A notebook won't cut it. What will?

**You will learn to**

- explain why databases beat plain files
- read tables, primary keys and foreign keys
- read and write simple SQL queries

**Key words:** database, DBMS, table, primary key, foreign key, SQL, transaction

---

## Why not just use a file?

A **database** is an organised store of data that many people and programs can use at the same time, safely. A plain file (or one shared spreadsheet) starts to break when the data grows and lots of people use it.

![Figure 2.6a](../Diagrams%20and%20Pictures/2-6_file-vs-database.svg)

*Figure 2.6a. Many people + one file = trouble (team diagram, used on Study Guide p. 91).*

| Problem with a plain file | What goes wrong | What a database does |
| --- | --- | --- |
| Slow search | reading 1,000,000 lines one by one | indexes jump straight to the row |
| Two people edit at once | one change overwrites the other | handles many users safely |
| Bad data | someone types a grade as "A+++" | checks rules and data types |
| Repeated data | an email updated in 1 place, but not the other 9 | stores each fact once |
| Crashes | a power cut leaves a half-saved file | transactions and recovery |

> **Dandroid's tip.** A **DBMS** (Database Management System) is the software that guards the data: MySQL, PostgreSQL, SQLite, MongoDB... Users send it requests called **queries**; they never touch the files directly.

## Inside a table

Most databases store data in **tables**. This is Dandroid's `Books` table, the same one used in the Study Guide, on slide 30 and in the activity:

| book_id | title | author | year | available |
| --- | --- | --- | --- | --- |
| 10 | Python Basics | Lee | 2019 | yes |
| 11 | Intro to AI | Kumar | 2021 | no |
| 12 | World History | Smith | 2015 | yes |
| 13 | Data Structures | Lee | 2020 | no |
| 14 | Cooking 101 | Garcia | 2018 | yes |

- **Row (record):** one thing, here one book.
- **Column (field):** one property every row has.
- **Primary key:** a column that is **unique** for every row and never empty: `book_id`.
- **Foreign key:** a column that points to another table's primary key. A `Loans` table would have a `book_id` column that points to `Books.book_id`, so each loan knows which book it is.

Why not use `author` as the key? Lee wrote two books, so `author` doesn't identify one row.

Tables that are linked by keys are called **relational**. This is why the most common kind of database is a *relational database*.

## Talking to the database: SQL

**SQL** (Structured Query Language) is the language for asking a database questions and changing its data.

![Figure 2.6b](../Diagrams%20and%20Pictures/2-6_sql.png)

*Figure 2.6b. Talking to the database (Study Guide p. 94).*

```sql
SELECT title, year      -- which columns
FROM Books              -- which table
WHERE author = 'Lee'    -- which rows
ORDER BY year;          -- sort the result
```

Result: `Python Basics 2019` and `Data Structures 2020`.

- `SELECT` chooses the columns. `WHERE` chooses the rows: it is a condition, just like an IF.
- `--` starts a comment in SQL.
- The four basic jobs are called **CRUD**: Create (`INSERT`), Read (`SELECT`), Update (`UPDATE`), Delete (`DELETE`).

```sql
INSERT INTO Books VALUES (15, 'Space Facts', 'Ito', 2022, 'yes');
UPDATE Books SET available = 'yes' WHERE book_id = 11;
DELETE FROM Books WHERE book_id = 14;
```

> **Bug alert.** Always use `WHERE` with `UPDATE` and `DELETE`. `DELETE FROM Books;` deletes *every* book!

## Keeping data clean and safe

![Figure 2.6c](../Diagrams%20and%20Pictures/2-6_clean-and-safe.png)

*Figure 2.6c. Keeping data clean and safe (Study Guide p. 95).*

**Normalisation: store each fact once.** If Ana's email is copied into many rows and you change only one copy, the database disagrees with itself (an *update anomaly*). The fix is to split the data into separate tables (Students, Courses, Enrolments) and link them with keys, so Ana's email is stored in exactly one place.

**Transactions: all or nothing.** Moving 100 from Ana's account to Ben's takes two steps: take 100 from Ana, add 100 to Ben. If the power cuts out between them, 100 vanishes. A **transaction** wraps both steps so that either both happen (`COMMIT`) or neither does (`ROLLBACK`). Databases promise four properties, called **ACID**: Atomicity (all or nothing), Consistency (rules always hold), Isolation (users don't see each other's half-finished work) and Durability (once committed, it survives a crash).

> **Dandroid's tip.** SQL or NoSQL? SQL tables suit banking and grades. NoSQL databases (documents, key-value, graphs) suit huge, fast-changing, varied data such as social feeds. Either way, **indexes** make searches fast.

## Try it

**Be the Librarian** (25 min, solo or pairs): predict the results of SQL queries on the Books table, then spot a badly designed table. Instructions and answers: [14_learner-activity.md](../Learner%20Activity/14_learner-activity.md). To run the queries for real, use [books_starter.py](../Learner%20Activity/code/books_starter.py) (Python 3 only, nothing to install) or SQLite Online.

## Going further (optional)

![Figure 2.6d](../Diagrams%20and%20Pictures/2-6_relationship-types.svg)

*Figure 2.6d. Three kinds of relationship (team diagram, mentioned on Study Guide p. 93).*

- A **many-to-many** relationship (students and courses) always needs a linking table, here `Enrolments`, with two foreign keys.
- `COUNT(*)`, `AVG(year)` and `MAX(year)` are *aggregate functions*: they turn many rows into one number.
- `JOIN` combines rows from two tables using their keys, for example every loan together with the title of the borrowed book.

## Check yourself

1. What makes a good primary key?
2. What does a foreign key do?
3. A bank transfer fails halfway. Which ACID property protects your money?

**Answers (try first, then peek)**
1. It is unique for every row and never empty (e.g. an ID number).
2. It links a row to a row in another table, using that table's primary key.
3. Atomicity: all steps happen, or none do.


More questions: [14_test-bank.md](../Test%20bank%20Question_Answer/14_test-bank.md)

## Remember

- Databases keep data permanent, shared and safe.
- Tables + primary keys + foreign keys.
- SQL: `SELECT ... FROM ... WHERE`; transactions are all-or-nothing.

## Watch and explore

**SQLite Online** (sqliteonline.com). Write real SQL in your browser with no installation. Create the Books table and run all the queries from the activity. It is a public playground: never type personal data.

## References

- Codd, E. F. (1970). A relational model of data for large shared data banks. *Communications of the ACM, 13*(6), 377–387.
- Silberschatz, A., Korth, H. F., & Sudarshan, S. (2019). *Database System Concepts* (7th ed.). McGraw-Hill. Chapters 1–3.
- SQLite. (n.d.). *SQL As Understood By SQLite*. https://www.sqlite.org/lang.html

---

Previous: [2.5 Data Structures](../../13_data-structures/Main%20Theory/13_main-theory.md) · Next: [2.7 Software Engineering](../../15_software-engineering/Main%20Theory/15_main-theory.md) · Up: [Chapter 2 overview](../../README.md)
