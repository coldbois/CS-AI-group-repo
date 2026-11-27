# 2.3 Computer Programming

![Dandroid ready to code](../../../assets/dandroid/dandroid-confident.png)

**Chapter 2 · Dandroid's Instructions** · Study Guide pp. 68–75 · Slides 22–24 · Test Bank T11, M11, M12, O4

> **Mission.** Teach Dandroid to answer one question: "Is this year a leap year?" Sounds easy... until you meet the year 1900.

**You will learn to**

- follow the program development cycle
- spot variables, decisions, loops and functions
- tell syntax, runtime and logic errors apart

**Key words:** variable, condition, loop, function, syntax, debugging, test case

---

## How programmers work

Programming is not just typing code. Most of the work happens before and after.

![Figure 2.3a](../Diagrams%20and%20Pictures/2-3_how-programmers-work.png)

*Figure 2.3a. The program development cycle (Study Guide p. 69).*

Applied to our mission:

1. **Understand.** Input: a year. Output: True or False. The rule: *divisible by 4, except years divisible by 100, unless they are also divisible by 400.*
2. **Plan.** Check 400 first, then 100, then 4. (The order matters, as you'll see.)
3. **Code** it in Python.
4. **Test** with normal years (2024, 2023) *and* tricky ones (2000, 1900).
5. **Improve:** fix anything that fails, then test again.

> **Dandroid's tip.** Break big problems into small functions. Small pieces are easier to test and fix. Use meaningful names (`is_leap`, not `x`), tidy indentation and comments for the tricky parts.

## The building blocks of every program

| Block | What it does | Python example |
| --- | --- | --- |
| **Variable** | a named box holding a value | `year = 2024` |
| **Condition** | chooses a path | `if ... else` |
| **Loop** | repeats work | `for y in years:` |
| **Function** | a reusable mini-program | `is_leap(year)` |

Every variable has a **type**: a whole number (`2024`), text (`"hello"`) or True/False. An **expression** calculates a result, for example `year % 4`, which gives the remainder after dividing by 4. If the remainder is 0, the year divides evenly.

## Worked example: a leap-year checker

![Figure 2.3b](../Diagrams%20and%20Pictures/2-3_leap-year-example.png)

*Figure 2.3b. The leap-year checker (Study Guide p. 71; also slide 22). The file is [leap_year.py](../Learner%20Activity/code/leap_year.py).*

```python
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

for y in [2000, 1900, 2024, 2023]:
    print(y, is_leap(y))
```

Output (we ran it to check):

```
2000 True
1900 False
2024 True
2023 False
```

- `def` creates a **function** called `is_leap`.
- `%` gives the remainder, so `year % 400 == 0` means "divides evenly by 400".
- The checks run **in order**: 400 first, then 100, then 4. 2000 stops at the first check (True). 1900 fails the first check and stops at the second (False).
- The `for` **loop** tests four years, including the tricky **edge case** 1900.

## Three kinds of bugs

![Figure 2.3c](../Diagrams%20and%20Pictures/2-3_three-bugs.png)

*Figure 2.3c. Three kinds of bugs (Study Guide p. 72).*

| Bug | What happens | Example |
| --- | --- | --- |
| **Syntax error** | breaks the language's grammar; the program won't even start | `print("hi"` (missing bracket) |
| **Runtime error** | crashes while running | dividing by zero; opening a file that doesn't exist |
| **Logic error** | runs fine but gives the **wrong answer** | the leap-year bug below |

Logic errors are the sneakiest kind. Python checks the *grammar* of your code, not whether your *idea* is right, so only tests catch them.

Try changing the checker to the short version `return year % 4 == 0`. It runs with no error message, and it is right for 2000, 2024 and 2023. Only 1900 shows that it is wrong. That's why we always test edge cases.

**Debugging** means finding and fixing bugs. Read the error message (it usually gives a line number), add `print` lines to see what your variables hold, and change one thing at a time.

## Try it

**Bug Hunt: The Broken Leap-Year Checker** (20 min, pairs): predict, run and fix the buggy checker. Instructions and answers: [11_learner-activity.md](../Learner%20Activity/11_learner-activity.md). The buggy file is [leap_year_buggy.py](../Learner%20Activity/code/leap_year_buggy.py).

## Check yourself

1. What is the difference between a syntax error and a logic error?
2. Which building block repeats work?
3. Why test 1900 as well as 2024?

**Answers (try first, then peek)**
1. A syntax error breaks the language rules; a logic error runs but gives a wrong answer.
2. A loop.
3. It's an edge case: divisible by 4 and by 100, but not by 400.


More questions: [11_test-bank.md](../Test%20bank%20Question_Answer/11_test-bank.md)

## Remember

- Understand → plan → code → test → improve.
- Variables, conditions, loops and functions build every program.
- Tests catch the bugs a computer can't see.

## Watch and explore

**Crash Course Computer Science #12: Programming Basics: Statements & Functions** (PBS, YouTube). A visual introduction to variables, if-statements, loops and functions. Pause at each code example and predict its result. It uses pseudo-code, not exact Python.

## References

- Python Software Foundation. (n.d.). *The Python Tutorial*. https://docs.python.org/3/tutorial/
- Downey, A. B. (2015). *Think Python* (2nd ed.). O'Reilly. Chapters 1–6. Free online at https://greenteapress.com/wp/think-python-2e/

---

Previous: [2.2 Introduction to Software](../../10_introduction-to-software/Main%20Theory/10_main-theory.md) · Next: [2.4 Algorithms](../../12_algorithms/Main%20Theory/12_main-theory.md) · Up: [Chapter 2 overview](../../README.md)
