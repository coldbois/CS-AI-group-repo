# 2.6 Test Bank: Databases

T15 and M15 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice (they use the Books table on the [topic page](../Main%20Theory/14_main-theory.md)). Answers are at the bottom.

## Questions

**T15 (True or False).** Two rows in a table can have the same primary key.

**M15 (choose TWO).** Which two are true about a database table?

- A. You cannot search a table
- B. Each row is one record, e.g. one book
- C. The primary key is different for every row
- D. All rows must be the same

**Q1.** What does `SELECT title FROM Books WHERE year < 2019;` return?

**Q2.** Write an SQL query that lists the titles of all books by Kumar.

**Q3.** Why is `DELETE FROM Books;` dangerous?

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T15 | **False** | The primary key is how the database tells rows apart. Correct version: every row must have a different primary key, like a student ID number. |
| M15 | **B, C** | One row = one thing, and the primary key is how rows are told apart. SQL searches tables with SELECT (not A); rows hold different data (not D). |
| Q1 | World History, Cooking 101 | Their years are 2015 and 2018. |
| Q2 | `SELECT title FROM Books WHERE author = 'Kumar';` | Result: Intro to AI. |
| Q3 | No `WHERE` | Without a condition it deletes every row in the table. |
