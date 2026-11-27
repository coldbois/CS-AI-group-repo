# 2.3 Test Bank: Computer Programming

T11, M11, M12 and O4 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q2 are extra practice. Answers are at the bottom.

## Questions

**T11 (True or False).** A logic error stops a program from starting.

**M11 (choose ONE).** A program runs, but it gives the wrong answer. What kind of error is this?

- A. Hardware error
- B. Syntax error
- C. Logic error
- D. Runtime error (crash)

**M12 (choose ONE).** Which building block repeats code?

- A. A loop
- B. A comment
- C. A variable
- D. A condition (if)

**O4. Bug hunt: the leap-year checker** (about 100 words, 5 marks)

The real rule: a year divisible by 4 is a leap year, except years divisible by 100, unless they are also divisible by 400. So 1900 is not a leap year. Dandroid wrote this code: `def is_leap(y): return y % 4 == 0`

(1) What does this code say for 1900? Is that right? (2) What kind of error is this? Why did Python not show an error message? (3) Why should programmers test tricky years like 1900?

Use these words: logic error · syntax error · test · edge case

**Q1.** What is `17 % 5` in Python?

**Q2.** Using the correct checker, is 2100 a leap year? Show which check decides it.

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T11 | **False** | A program with a logic error runs, but its answer is wrong. Correct version: a syntax error stops a program from starting; a logic error gives a wrong answer. |
| M11 | **C** | It runs, but the idea in the code is wrong. A syntax error (B) stops it before it runs; a runtime error (D) makes it crash; the computer did what the code said, so it's not hardware (A). |
| M12 | **A** | A loop repeats steps, e.g. `for y in years:`. A comment is a note, a variable stores a value, a condition chooses a path. |
| Q1 | **2** | 17 = 3 × 5 + 2. |
| Q2 | **No** | 2100 % 400 = 100 (not 0), so the first check fails. 2100 % 100 = 0, so the second check returns False. |

**O4 sample answer (122 words).** The code only checks if the year divides by 4. 1900 divides by 4, so the code says True (a leap year). That is wrong, because 1900 also divides by 100 but not by 400, so it is not a leap year. This is a logic error: the program runs without crashing, but it gives a wrong answer. Python did not show an error message because the code follows Python's grammar, so there is no syntax error. Python cannot know that the idea inside the code is wrong. That is why programmers must test their code, especially with tricky edge cases like 1900 or 2100. Easy years like 2024 give the right answer by luck, so they would not show the bug.

**O4 key points (1 mark each):** the code says True for 1900, which is wrong · names it a logic error (runs, wrong answer) · no syntax error, so Python stays silent · testing tricky years (edge cases) finds hidden bugs · gives another tricky year (1800, 2100) or explains why 2024 hides the bug. *Also accept* a correct fixed version of the code as extra evidence.
