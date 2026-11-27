# Try it: Be the Librarian (2.6)

**Time:** 25 min · **Group:** solo or pairs · **You need:** pen and paper; Python 3 or SQLite Online (optional) · Study Guide pp. 96–97

**Goal:** read SQL like a database, and spot a badly designed table.

## Prepare

Use the `Books` table from the [topic page](../Main%20Theory/14_main-theory.md):

| book_id | title | author | year | available |
| --- | --- | --- | --- | --- |
| 10 | Python Basics | Lee | 2019 | yes |
| 11 | Intro to AI | Kumar | 2021 | no |
| 12 | World History | Smith | 2015 | yes |
| 13 | Data Structures | Lee | 2020 | no |
| 14 | Cooking 101 | Garcia | 2018 | yes |

Optional: run the queries for real with [books_starter.py](code/books_starter.py) (type `python books_starter.py`), or paste them into SQLite Online.

## Steps

1. **Predict:** `SELECT title FROM Books WHERE author = 'Lee';`
2. **Predict:** `SELECT title FROM Books WHERE available = 'yes';`
3. **Predict:** `SELECT COUNT(*) FROM Books WHERE year > 2018;`
4. **Fill the gaps** (Intro to AI was returned): `UPDATE Books SET available = '___' WHERE book_id = ___;`
5. A `Loans` table repeats Aigerim's name and phone number in two rows:

   | loan_id | member_name | phone | book_id |
   | --- | --- | --- | --- |
   | 1 | Aigerim | 555-0101 | 10 |
   | 2 | Aigerim | 555-0101 | 12 |

   What could go wrong? How would you fix it?

## Record

Write your predicted result for each query, then run it or check the answers.

## Reflect

- Which SQL keyword works like an IF?
- Why do we split data into several linked tables?

## Check it: expected results

We ran queries 1–4 with the starter script to check these answers.

| Query | Result |
| --- | --- |
| 1 | Python Basics, Data Structures |
| 2 | Python Basics, World History, Cooking 101 |
| 3 | **3** (books from 2019, 2020 and 2021) |
| 4 | `UPDATE Books SET available = 'yes' WHERE book_id = 11;` |

5. If Aigerim changes her phone number and someone updates only one row, the table disagrees with itself. **Fix:** a `Members` table that stores each member's phone once, and a `Loans` table that holds only the member's ID. That's **normalisation**.

- `WHERE` works like an IF.
- We split data into linked tables so each fact is stored once and can't contradict itself.
