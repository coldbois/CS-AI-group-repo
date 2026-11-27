# Starter script for "Be the Librarian" (2.6).
# Builds the Books table from Study Guide p. 93 in memory and runs the activity queries.
# Needs only Python 3: sqlite3 is part of the standard library.
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("""CREATE TABLE Books (
    book_id   INTEGER PRIMARY KEY,
    title     TEXT,
    author    TEXT,
    year      INTEGER,
    available TEXT)""")
db.executemany("INSERT INTO Books VALUES (?, ?, ?, ?, ?)", [
    (10, "Python Basics", "Lee", 2019, "yes"),
    (11, "Intro to AI", "Kumar", 2021, "no"),
    (12, "World History", "Smith", 2015, "yes"),
    (13, "Data Structures", "Lee", 2020, "no"),
    (14, "Cooking 101", "Garcia", 2018, "yes"),
])


def run(sql):
    print(sql)
    for row in db.execute(sql):
        print("   ", row)
    print()


# Predict each result before you run the script!
run("SELECT title FROM Books WHERE author = 'Lee';")
run("SELECT title FROM Books WHERE available = 'yes';")
run("SELECT COUNT(*) FROM Books WHERE year > 2018;")
run("SELECT title, year FROM Books WHERE author = 'Lee' ORDER BY year;")

# Intro to AI was returned:
db.execute("UPDATE Books SET available = 'yes' WHERE book_id = 11;")
run("SELECT book_id, title, available FROM Books WHERE book_id = 11;")

# Try your own queries below this line.
