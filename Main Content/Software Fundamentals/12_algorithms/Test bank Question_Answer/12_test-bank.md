# 2.4 Test Bank: Algorithms

T12, T13 and M13 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T12 (True or False).** Binary search only works on a sorted list.

**T13 (True or False).** An algorithm is a list of clear steps that solves a problem.

**M13 (choose ONE).** You guess a number from 1 to 100, and you always guess the middle. What is the most guesses you need?

- A. 7
- B. 25
- C. 50
- D. 100

**Q1.** Using binary search on `[3, 8, 12, 15, 20, 24, 29, 33, 37, 41, 46, 52, 58, 63, 70]`, which number is checked first when looking for 12? Which is checked second?

**Q2.** An algorithm is O(n²). It takes 1 second for 1,000 items. Roughly how long for 2,000 items?

**Q3 (True or False).** Binary search works on any list, sorted or not. *(Chapter 2 quick quiz)*

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T12 | **True** | Binary search checks the middle and throws away half. That only works if the items are in order. |
| T13 | **True** | Like a recipe: clear steps, an input, an output, and it finishes. |
| M13 | **A** | Each guess cuts the list in half: 100 → 50 → 25 → 13 → 7 → 4 → 2 → 1. 25 and 50 are much slower; 100 is checking one by one. |
| Q1 | 33, then 15 | 33 is the middle; 12 < 33 so keep the left half (3 ... 29), whose middle is 15. (Third check: 8, fourth: 12.) |
| Q2 | About 4 seconds | Doubling n quadruples the work for O(n²). |
| Q3 | **False** | The list must be sorted. |
