# Part 14 — Test Bank: Databases

## Multiple choice

**1.** What is a DBMS?
A) A type of spreadsheet  B) Software that stores and manages a database  C) A programming language  D) A computer network

**2.** In a relational table, one **row** represents…
A) One property of every item  B) One item / record  C) The whole database  D) A query

**3.** Which column is the best primary key for a `Students` table?
A) name  B) year  C) student_id  D) email domain

**4.** What does this query return?
```sql
SELECT name FROM Students WHERE year = 2;
```
A) All columns of every student  B) Names of students in year 2  C) The number of year-2 students  D) It deletes year-2 students

**5.** A column in one table that stores the primary key of another table is a…
A) Foreign key  B) Index  C) Transaction  D) Schema

**6.** "All steps of a transaction happen, or none do" describes which ACID property?
A) Atomicity  B) Consistency  C) Isolation  D) Durability

**7.** Which is the most dangerous statement?
A) `SELECT * FROM Students;`  B) `DELETE FROM Students;`  C) `SELECT COUNT(*) FROM Students;`  D) `DELETE FROM Students WHERE student_id = 9;`

## Short answer

**8.** Give two problems with storing a large shop's orders in one shared text file instead of a database.

**9.** What is an *update anomaly*? Give an example.

**10.** Name one situation where a NoSQL database could be a better choice than a relational one, and explain why.

---

## Answers

1. **B**
2. **B**
3. **C** — it is guaranteed unique; names and years can repeat.
4. **B**
5. **A**
6. **A**
7. **B** — with no `WHERE`, it deletes every row.
8. Any two of: searching is slow; two people editing at once can overwrite each other; no checks stop invalid data; repeated data gets out of sync; a crash during saving can corrupt the file.
9. When the same fact is stored in several places and only some copies are changed, so the data contradicts itself. Example: a customer's address is stored on every order; it is updated on one order but not the others.
10. Example: a social media app storing posts that each have different fields (text, photos, polls) and huge volumes of data, so a flexible document database like MongoDB fits better than fixed table columns.
