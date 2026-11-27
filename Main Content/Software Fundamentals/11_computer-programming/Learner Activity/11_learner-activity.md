# Try it: Bug Hunt: The Broken Leap-Year Checker (2.3)

**Time:** 20 min · **Group:** pairs · **You need:** a browser (online Python) or paper · Study Guide pp. 73–74 · Linked Test Bank question: O4

**Goal:** use test cases to catch a logic error, then fix it.

## Prepare

Open any online Python editor (for example the interactive shell on python.org), or open [leap_year_buggy.py](code/leap_year_buggy.py) if you have Python 3. No internet? Trace it on paper.

## Steps

1. Type the buggy checker:
   ```python
   def is_leap(y): return y % 4 == 0
   ```
2. **Predict** its answer for 2000, 1900, 2024 and 2023. Write your predictions down.
3. Run `print(is_leap(1900))`. Does it match the real rule?
4. Which type of error is this? Fix it using the worked example in the [topic page](../Main%20Theory/11_main-theory.md).
5. Invent one more test year that would catch the bug.

## Record

| Year | Predicted | Buggy output | Correct? |
| --- | --- | --- | --- |
| 2000 | | | |
| 1900 | | | |
| 2024 | | | |
| 2023 | | | |

## Reflect

- Why didn't Python complain about the bug?
- Why are edge cases like 1900 so important to test?

## Check it: expected results

We ran the buggy file to check these outputs.

| Year | Buggy output | Correct? |
| --- | --- | --- |
| 2000 | True | ✓ |
| 1900 | **True** | ✗ (1900 is not a leap year) |
| 2024 | True | ✓ |
| 2023 | False | ✓ |

- It's a **logic error**: the program runs, but the answer is wrong.
- Python checks grammar and crashes, not whether your idea is right. Only tests reveal logic errors.
- The fix is the full checker from [leap_year.py](code/leap_year.py): check 400, then 100, then 4.
- Other years that catch the bug: **1800, 2100** (divisible by 100 but not by 400). Testing 2400 is also useful: it must stay True after your fix.
