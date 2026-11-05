# Module 10 Test Bank: Introduction to Software

Back to: [Main Theory](../Main%20Theory/10_main-theory.md) · [Learner Activities](../Learner%20Activity/10_learner-activities.md)

**Format:** Each question shows its type, difficulty, the learning outcome (LO) and the Main Theory section it tests. Answers and explanations follow the questions.

**Coverage map**

| Group | Questions | Outcomes | Sections |
|---|---|---|---|
| A. What software is | Q1 to Q8 | LO1, LO2 | 4, 5 |
| B. How software is made and runs | Q9 to Q19 | LO3 to LO6 | 6 to 9 |
| C. Software in the real world | Q20 to Q25 | LO7 to LO9 | 10 to 13 |

---

# Group A: What Software Is

**Q1. [Multiple choice · Easy · LO1 · Section 4]**
Which statement best defines software?
- A. The physical parts of a computer
- B. Programs, with their data and settings, that tell hardware what to do
- C. Only the apps installed on a phone
- D. Electricity that powers the computer

**Q2. [Multiple choice · Easy · LO2 · Section 5]**
Which of these is system software?
- A. A word processor
- B. A device driver
- C. A video game
- D. A web page

**Q3. [Multiple choice · Easy · LO2 · Section 5]**
What is firmware?
- A. Hardware that cannot be changed
- B. Software stored inside a device that controls it
- C. A kind of virus
- D. A type of programming language

**Q4. [True or false with correction · Easy · LO2 · Section 5]**
"A web browser is an operating system." If false, correct it.

**Q5. [Matching · Medium · LO2 · Section 5]**
Match each item to a type: (1) a code editor, (2) a spreadsheet program, (3) the control software inside a washing machine, (4) a database connector between a web app and a database.
Types: P = programming software, A = application software, F = firmware / embedded, M = middleware.

**Q6. [Multiple choice · Medium · LO2 · Section 5]**
Which description fits middleware best?
- A. The programs that run directly on the user's screen
- B. Software that sits between other programs so they can work together
- C. Software that translates source code into machine code
- D. The physical memory chips of a device

**Q7. [Short answer · Medium · LO1 · Section 4]**
Explain why software is called "soft". Give one example of how this helps users.

**Q8. [Find the error · Medium · LO1, LO2 · Section 4, 5]**
A student writes: "Firmware is hardware because it is inside the router." Identify the error and write a correct statement.

---

# Group B: How Software Is Made and Runs

**Q9. [Multiple choice · Easy · LO4 · Section 7]**
What is machine code?
- A. Instructions written in English
- B. Binary instructions that a CPU can run directly
- C. A diagram of an algorithm
- D. A list of errors in a program

**Q10. [Calculation · Medium · LO3 · Section 6]**
Convert the decimal number **37** to binary. Show your working.

**Q11. [Calculation · Medium · LO3 · Section 6]**
Convert the binary number **11010** to decimal. Show your working.

**Q12. [Multiple choice · Medium · LO3 · Section 6]**
How many different values can one byte (8 bits) store?
- A. 8
- B. 255
- C. 256
- D. 1024

**Q13. [Calculation · Medium · LO3 · Section 6]**
The letter **A** has the number 65. Write it as an 8-bit binary byte.

**Q14. [Multiple choice · Medium · LO4 · Section 7]**
Which statement describes a compiler?
- A. It runs a program one line at a time without making a file
- B. It translates a whole program into another form before it runs
- C. It finds the largest number in a list
- D. It fixes logic errors automatically

**Q15. [Compare approaches · Medium · LO4 · Section 7]**
Give **one advantage** of a compiled approach and **one advantage** of an interpreted approach.

**Q16. [Predict the output · Medium · LO4, LO6 · Section 7, 9]**
```python
print("Start")
x = 10
print(x / 0)
print("End")
```
What is printed before the program stops, and what kind of error is it?

**Q17. [Trace · Medium · LO5 · Section 8]**
Use the largest-number algorithm from Section 8.2 on the list `[3, 9, 4, 9]`. Show the value of `largest` after each number is checked, and give the output.

**Q18. [Classify errors · Medium · LO6 · Section 9]**
Name the kind of error (syntax, runtime or logic) in each snippet:
- (i) `print("Hello"` (the bracket is never closed)
- (ii) `values = [1, 2, 3]` then `print(values[10])`
- (iii) A program meant to find the average of 4 and 8 uses `a + b / 2` and prints 8.0.

**Q19. [Find the error · Hard · LO5, LO6 · Section 8, 9]**
A student starts the largest-number algorithm with `largest = 0` and runs it on `[-3, -1, -8]`. What does it output? Is that correct? Name the kind of error and give a fix.

---

# Group C: Software in the Real World

**Q20. [Multiple choice · Easy · LO7 · Section 10]**
Open source software is software that:
- A. Always costs nothing
- B. Provides its source code under a licence that grants freedoms to use, study, modify and share
- C. Has no owner
- D. Cannot be used in business

**Q21. [True or false with correction · Medium · LO7 · Section 10]**
"Open source software can never be sold." If false, correct it.

**Q22. [Scenario · Medium · LO7 · Section 10]**
Using the simplified summaries in Section 10.2, answer for each:
- (i) Ana uses an MIT-licensed library in a paid, closed-source app. May she?
- (ii) Ben modifies a GPL program and shares the modified program with others. What must he do?

**Q23. [Multiple choice · Medium · LO8 · Section 11]**
Version **4.2.9** is updated to **4.3.0**. What does this most likely mean under semantic versioning?
- A. A bug fix only
- B. New features that do not break existing use
- C. A breaking change
- D. The software was deleted

**Q24. [Short answer · Medium · LO8 · Section 11]**
Give **two reasons** to install software updates and **one risk** of updating.

**Q25. [Scenario · Hard · LO2, LO7, LO8, LO9 · Sections 5, 10, 11, 13]**
You send a message with a phone app. Name **at least four** pieces of software involved, state the **type** of each, and say **one** way a software update could matter.

---

# Answer Key with Explanations

## Group A

**Q1: B.** Software is programs together with their data and settings. A describes hardware; C is too narrow; D is not software.

**Q2: B.** A device driver lets the OS control a hardware device, so it is system software. A and C are applications; D is not software in this sense.

**Q3: B.** Firmware is software stored in a device that controls it.

**Q4: False.** A browser is **application software** that runs on an operating system.

**Q5:** (1) **P**, (2) **A**, (3) **F**, (4) **M**.

**Q6: B.** Middleware connects other programs. A describes application software, C a compiler or interpreter, and D hardware.

**Q7: Model answer.** Software is "soft" because it can be **changed**, for example through updates, without replacing the hardware. Example: a phone gains a new feature after an app update, with no new phone needed. *(Award marks for "changeable/updatable" plus a valid example.)*

**Q8: Error.** Firmware is not hardware. **Correct statement:** "Firmware is software (instructions) that is stored inside the router's memory and controls it."

## Group B

**Q9: B.** Machine code is binary instructions that a CPU can run directly.

**Q10: 100101.** 37 = 32 + 4 + 1. Place values: 32 (1), 16 (0), 8 (0), 4 (1), 2 (0), 1 (1) → **100101**.

**Q11: 26.** `11010`: 16 (1) + 8 (1) + 4 (0) + 2 (1) + 1 (0) = 16 + 8 + 2 = **26**.

**Q12: C. 256.** Eight bits give 2⁸ = 256 patterns (0 to 255).

**Q13: 01000001.** 65 = 64 + 1 → bits for 128, 64, 32, 16, 8, 4, 2, 1 are 0, 1, 0, 0, 0, 0, 0, 1.

**Q14: B.** A compiler translates the program before it runs. A describes an interpreter.

**Q15: Examples (any valid pair).**
- *Compiled:* usually faster to run; you can share the executable without the source.
- *Interpreted:* quick to test and change because there is no separate build step.

**Q16: It prints `Start`, then stops with `ZeroDivisionError: division by zero`.** `End` is never printed. It is a **runtime error**.

**Q17:** `largest` starts at 3.

| Number checked | Is it larger? | `largest` afterwards |
|---|---|---|
| 9 | yes | 9 |
| 4 | no | 9 |
| 9 | no (9 > 9 is false) | 9 |

Output: **9**.

**Q18:** (i) **Syntax**. (ii) **Runtime** (`IndexError`). (iii) **Logic** (the program runs but gives the wrong result; `b / 2` is calculated first, giving 8.0 instead of 6.0).

**Q19: It outputs 0, which is wrong.** None of −3, −1 or −8 is larger than 0, so `largest` stays 0, but 0 is not in the list. The correct answer is −1. It is a **logic error**. **Fix:** start with the first number in the list (`largest = numbers[0]`).

## Group C

**Q20: B.** Open source gives access to the source code under a licence with freedoms. It is not necessarily free of charge (A), it has an owner (C), and it can be used commercially (D).

**Q21: False.** Open source software **can** be sold. The licence is about freedoms (use, study, modify, share), not price. Under the GPL, for example, a company may sell copies provided it also supplies the source and the same freedoms.

**Q22:** (i) **Yes**, as long as she keeps the copyright notice and licence text (MIT is permissive). (ii) Ben must **provide the source code and license his modified version under the GPL** to the people he gives it to (GPL is copyleft and applies when you distribute).

**Q23: B.** Under semantic versioning, an increase in the MINOR number (with PATCH reset to 0) signals new features that do not break existing use.

**Q24: Model answer.**
*Reasons (any two):* fix bugs; close security vulnerabilities; add features; support new hardware.
*Risk (any one):* the update may introduce new bugs or break compatibility with files or add-ons.

**Q25: Model answer (any four with correct types).** Example:

| Software | Type |
|---|---|
| Start-up code stored in the phone | Firmware |
| The phone's operating system | System software |
| The messaging app | Application software |
| Server software at the messaging company | Application software on a remote computer |
| A connector between the app server and its database | Middleware |
| The code editor or compiler used to build the app | Programming software |

*Update example:* a security patch to the app or operating system closes a vulnerability so attackers cannot misuse the app. *(Award marks for four correct items with matching types plus a valid update reason.)*

---

## Review status

| Check | Done by | Result |
|---|---|---|
| Calculations (Q10, Q11, Q13, Q17) recomputed independently | [Teammate name] | [To be completed] |
| Python snippets (Q16, Q18) run and outputs confirmed | [Teammate name] | [To be completed] |
| Questions match the Main Theory wording and terminology | [Teammate name] | [To be completed] |
| Each multiple-choice question has exactly one defensible answer | [Teammate name] | [To be completed] |
