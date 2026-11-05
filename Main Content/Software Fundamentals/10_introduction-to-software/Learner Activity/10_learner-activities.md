# Module 10 Learner Activities: Introduction to Software

Back to: [Main Theory](../Main%20Theory/10_main-theory.md) · [Test Bank](../Test%20bank%20Question_Answer/10_test-bank.md)

## How to use these activities

- Read the matching section of the Main Theory first, then **try each activity before looking at the answers**. The **Answer Key** is at the end of this file.
- Each activity gives all the information you need. You do not have to look anything up.
- The activities mix skills: classifying, converting, predicting, tracing, finding errors, comparing, and explaining decisions.

| # | Activity | Skill practised | Main Theory section | Outcome |
|---|---|---|---|---|
| 1 | Classify 12 items | Classifying, explaining | 4, 5 | LO1, LO2 |
| 2 | Binary conversions and text encoding | Calculating, finding an error | 6 | LO3 |
| 3 | When do errors appear? Choose an approach | Predicting, comparing, explaining a decision | 7 | LO4 |
| 4 | Trace and improve the largest-number algorithm | Tracing, modifying, finding an error | 8 | LO5 |
| 5 | Classify and fix errors | Error finding | 9 | LO6 |
| 6 | Licensing scenarios | Applying rules, explaining | 10 | LO7 |
| 7 | Version numbers and updates | Calculating, explaining | 11 | LO8 |
| 8 | Web app or installed app? | Comparing, explaining a decision | 11 | LO8 |
| 9 | Map the software behind a task | Applying everything | 4 to 13 | LO1 to LO9 |

---

## Activity 1: Classify 12 items

**Goal:** Sort items into software types and explain your reasons.
**Time:** 15 minutes.

**Categories:** (H) Hardware · (S) System software · (A) Application software · (P) Programming software · (M) Middleware · (F) Firmware / embedded software

**Items**
1. A keyboard
2. Android
3. WhatsApp
4. Git (a tool that tracks changes to code)
5. The built-in control software of a Wi-Fi router
6. A printer driver
7. A tool that lets a web app send queries to a database
8. The Python interpreter
9. An image-editing program such as a photo editor
10. A solid-state drive (SSD)
11. A backup utility that copies your files to another disk
12. The control software inside a smart TV

**Task**
- **(a)** Give each item a category letter with a one-line reason.
- **(b)** Which items could reasonably be placed in two categories, and why?
- **(c) Find the error:** A student says, "Firmware is hardware because it lives inside the device." Explain what is wrong.
- **(d) Explain:** Why is a web browser not an operating system?

---

## Activity 2: Binary conversions and text encoding

**Goal:** Practise place values and see text stored as numbers.
**Time:** 20 minutes.

**Information:** Place values for 8 bits (left to right): 128, 64, 32, 16, 8, 4, 2, 1. A bit of 1 adds its place value; a bit of 0 adds nothing. Character numbers: **H = 72, i = 105, ! = 33**.

**Task**
- **(a)** Convert to binary: **25**, **100**, **255** (give 8-bit answers).
- **(b)** Convert to decimal: **10110**, **1001**, **1111**.
- **(c)** Write the three-character text **Hi!** as three bytes of binary.
- **(d) Find the error:** A student writes, "One byte can store the numbers 1 to 256." Correct it.
- **(e) Predict:** How many different values can 3 bits store, and what is the largest decimal value?

---

## Activity 3: When do errors appear? Choose an approach

**Goal:** Predict what happens, then judge compiled and interpreted approaches.
**Time:** 20 minutes.

**Information:** Python checks the whole file for grammar mistakes before running any line. Division by zero is impossible and stops the program when that line is reached.

**Script A**
```python
print("A")
print(5 / 0)
print("B")
```

**Script B**
```python
print("A")
print("B"
```

**Script C (in the C language):** a program whose third line is missing its closing semicolon, compiled with a standard compiler.

**Task**
- **(a)** For Script A, write exactly what is printed before the program stops. What kind of error is it?
- **(b)** For Script B, what is printed, and why?
- **(c)** For Script C, can you run the program? Why or why not?
- **(d) Explain a decision.** For each situation, choose *compiled* or *interpreted (or hybrid)* and give one reason:
  1. A studio will sell a game to millions of players and wants it to run fast without sharing its source code.
  2. A data analyst wants to try ideas quickly, changing code and re-running many times.
- **(e)** An executable file built for one kind of CPU will not run directly on another kind. Why?

---

## Activity 4: Trace and improve the largest-number algorithm

**Goal:** Use a trace table, modify an algorithm, and find a flaw.
**Time:** 25 minutes.

**Information:** The algorithm from Section 8.2:

```python
largest = numbers[0]
for n in numbers[1:]:
    if n > largest:
        largest = n
print(largest)
```

**Task**
- **(a)** Trace it for `numbers = [4, 11, 7, 11, 2]`. Make a table with columns: `n`, `n > largest?`, `largest` afterwards. What is printed?
- **(b)** Change the algorithm so that it finds the **smallest** number. Which single symbol do you change? Test it on the same list.
- **(c) Find the error.** A student rewrites the first line as `largest = 0`. Predict the output for `numbers = [-5, -2, -9]` (the loop now goes over all numbers). Is that correct? What kind of error is it, and how can you fix it?
- **(d) Edge case.** With the original code, what happens if `numbers` is an empty list `[]`, and what kind of error is that?

---

## Activity 5: Classify and fix errors

**Goal:** Recognise the three kinds of error.
**Time:** 20 minutes.

**Code snippets**

**S1**
```python
total = 5
print("Total:" total)
```
**S2**
```python
scores = [70, 85, 90]
print(scores[3])
```
**S3**
```python
a = 4
b = 8
average = a + b / 2
print(average)
```
**S4**
```python
Print("hello")
```

**Task**
- **(a)** For each snippet, say whether the error is **syntax**, **runtime** or **logic**, say what you expect to see, and write the fixed line.
- **(b)** Which snippet gives wrong output with **no error message**? Why is that kind the hardest to find, and how would you find it?
- **(c) Explain:** A student says, "My program ran with no error message, so it must be correct." Give a reply using one of the snippets.

---

## Activity 6: Licensing scenarios

**Goal:** Apply licence rules and explain your reasoning.
**Time:** 20 minutes.

**Information (simplified summaries, not legal advice)**

| Licence type | Summary |
|---|---|
| **Proprietary** | Use under the owner's terms; source usually not shared; usually cannot modify or redistribute |
| **MIT (permissive open source)** | Use, modify and distribute, even in closed commercial products, if you keep the copyright notice and licence text |
| **GPL (copyleft open source)** | If you distribute a modified version or a work based on it, you must provide it under the GPL with source code |
| **SaaS** | You get access to a service, not a copy of the software |
| **No licence stated** | Copyright applies by default: you have no permission to copy or reuse unless the owner says so |

**Scenarios**
1. Mia puts an MIT-licensed library inside a paid app and does not share her own code.
2. Raj modifies a GPL program and sends the modified program to friends.
3. Raj modifies a GPL program only for his own use and gives it to nobody.
4. Lena downloads a photo editor for free. There is no source code available.
5. A company sells copies of a GPL program.
6. A student finds code in a blog post with no licence information and wants to copy it into a class project that will be published.
7. A team uses a web-based spreadsheet on a monthly subscription.

**Task**
- **(a)** For each scenario, say whether the action is allowed and what the person must do.
- **(b) Explain:** "Open source" and "free of charge" are not the same. Use scenario 5 to support your answer.

---

## Activity 7: Version numbers and updates

**Goal:** Read and choose version numbers.
**Time:** 15 minutes.

**Information:** Use `MAJOR.MINOR.PATCH`. Bug fix → PATCH up. New compatible feature → MINOR up, PATCH to 0. Breaking change → MAJOR up, MINOR and PATCH to 0. Current version: **3.2.5**.

**Task**
- **(a)** Choose the new version number for each change: (i) fixed a crash; (ii) added dark mode, nothing else changes; (iii) removed support for an old file format, so old files no longer open; (iv) fixed two bugs.
- **(b)** Which update should you read about most carefully before installing: `3.2.5 → 3.2.6` or `3.2.5 → 4.0.0`? Why?
- **(c) Explain:** Why should you not put off an update labelled as a **security patch**?
- **(d)** A Linux system is named **24.04**. Does that follow MAJOR.MINOR.PATCH? What might the number mean?

---

## Activity 8: Web app or installed app?

**Goal:** Compare two approaches and justify a decision.
**Time:** 15 minutes.

**Scenario:** A student club needs a sign-up form for events. Members have different laptops and phones. The club has no money for software maintenance and wants updates to reach everyone immediately.

**Task**
- **(a)** List **two advantages and two disadvantages** of a **web app** for this club, and the same for an **installed program**.
- **(b)** Recommend one approach and justify it in 2 to 3 sentences, using words from Section 11.
- **(c)** Name one situation in which you would reverse your recommendation.

---

## Activity 9: Map the software behind a task

**Goal:** Apply everything: identify the software involved when you send a photo in a messaging app.
**Time:** 30 minutes.

**Task**
1. List **at least six** pieces of software involved, from switching on the phone to the friend seeing the photo. Include at least one of each: firmware, system software, application software, middleware (or a connector between programs), and programming software (used earlier, to build the app).
2. Label each with its **type** from Figure 1.
3. Name **one piece** that is proprietary and one that could be open source, and say why you think so (you may be uncertain; give reasons).
4. Say where **updates** matter (name one kind of update and why it is needed).
5. Name one type of error that might occur on the phone and which kind (syntax, runtime or logic) a developer could find *before* release.

---

# Answer Key

## Answer 1
**(a)**

| # | Item | Category | Reason |
|---|---|---|---|
| 1 | Keyboard | **H** | Physical equipment |
| 2 | Android | **S** | An operating system |
| 3 | WhatsApp | **A** | The user does a task (messaging) |
| 4 | Git | **P** | Developers use it to manage code |
| 5 | Router control software | **F** | Stored in the router and controls it |
| 6 | Printer driver | **S** | Lets the OS control a specific printer |
| 7 | Database connector | **M** | Connects a web app and a database |
| 8 | Python interpreter | **P** | Runs code that developers write |
| 9 | Photo editor | **A** | The user edits photos |
| 10 | SSD | **H** | Physical storage device |
| 11 | Backup utility | **S** (utility) or **A** | A utility that serves the computer's upkeep; many sources call it system software |
| 12 | Smart TV control software | **F** | Embedded in the TV |

**(b)** Item 11 (the backup utility) could be called system software (a utility that looks after the computer) or application software (a program the user runs). Item 4 (Git) is a program a user runs, so it could also be called an application, but its purpose is to help build software, so **P** is the better fit. A clear reason matters more than a single "correct" box.

**(c)** Firmware is **software** (a set of instructions) that is stored in the device's memory. Being inside the device does not make it hardware.

**(d)** A browser is an **application** that runs on top of an operating system. The OS manages the hardware and provides the services that the browser asks for.

## Answer 2
**(a)**
- 25 = 16 + 8 + 1 → `00011001`
- 100 = 64 + 32 + 4 → `01100100`
- 255 = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 → `11111111`

**(b)**
- `10110` = 16 + 4 + 2 = **22**
- `1001` = 8 + 1 = **9**
- `1111` = 8 + 4 + 2 + 1 = **15**

**(c)**
- H = 72 = 64 + 8 → `01001000`
- i = 105 = 64 + 32 + 8 + 1 → `01101001`
- ! = 33 = 32 + 1 → `00100001`

So **Hi!** is `01001000 01101001 00100001`.

**(d)** A byte (8 bits) has 2⁸ = 256 patterns, but they start at 0, so the range is **0 to 255**, not 1 to 256.

**(e)** 2³ = **8** different values, from 000 (0) to 111 (7). The largest decimal value is **7**.

## Answer 3
**(a)** It prints `A`, then stops with `ZeroDivisionError: division by zero`. `B` is never printed. It is a **runtime error**.

**(b)** **Nothing** is printed. The line `print("B"` has an unclosed bracket (a **syntax error**), and Python checks the whole file for grammar mistakes before running any line, so even `A` is not printed.

**(c)** **No.** A syntax error stops the compiler, so no executable file is created and there is nothing to run until the mistake is fixed.

**(d)**
1. **Compiled.** It is usually faster to run, and the studio can ship the executable without revealing the source. *(A hybrid answer with a good reason is also acceptable.)*
2. **Interpreted (or hybrid).** The analyst can change a line and run again immediately, without a separate build step.

**(e)** Machine code is made for one **kind of CPU** (its instruction set). A different kind of CPU has different instructions, so the same executable file cannot be understood directly.

## Answer 4
**(a)** Start: `largest = 4`.

| `n` | `n > largest?` | `largest` afterwards |
|---|---|---|
| 11 | yes (11 > 4) | 11 |
| 7 | no | 11 |
| 11 | no (11 > 11 is false) | 11 |
| 2 | no | 11 |

Output: **11**.

**(b)** Change `>` to `<` (so the test is `if n < smallest:`, with the variable renamed `smallest`). Test: start 4; 11 no; 7 no; 11 no; 2 yes (2 < 4) → smallest = 2. Output: **2**.

**(c)** With `largest = 0`, none of −5, −2, −9 is greater than 0, so it prints **0**. That is **wrong**, because 0 is not in the list; the largest value is −2. This is a **logic error** (no error message). Fix: start from the **first number in the list** (`largest = numbers[0]`).

**(d)** `numbers[0]` does not exist for an empty list, so Python raises `IndexError: list index out of range`. This is a **runtime error**. A better algorithm checks for an empty list first and decides what to do (for example, report "no numbers").

## Answer 5
**(a)**

| Snippet | Kind | What you see | Fix |
|---|---|---|---|
| S1 | **Syntax** | `SyntaxError: invalid syntax` (a comma is missing) | `print("Total:", total)` |
| S2 | **Runtime** | `IndexError: list index out of range` (valid positions are 0, 1, 2) | `print(scores[2])` |
| S3 | **Logic** | Prints `8.0` with no error; correct average is `6.0` | `average = (a + b) / 2` |
| S4 | **Runtime** | `NameError: name 'Print' is not defined` | `print("hello")` |

**(b)** **S3.** Nothing tells you something is wrong. You find it by **testing** with inputs whose correct answer you know (4 and 8 should average to 6) and by tracing: `b / 2` is done first (4.0), then `a + 4.0` gives 8.0.

**(c)** "No error message" only means no syntax or runtime error. In S3 the program ran fine and still gave the wrong answer, so only testing shows correctness.

## Answer 6
**(a)**
1. **Allowed.** She must keep the copyright notice and MIT licence text.
2. **Allowed, but he must provide the source and license his version under the GPL** to the friends who receive it.
3. Generally **no obligation to publish**, because the GPL conditions apply when you distribute.
4. It is **not open source** (no source code). It is freeware or proprietary software that happens to cost nothing.
5. **Allowed**, provided the company also supplies the source code and the same GPL freedoms.
6. **Not allowed to copy by default.** With no licence, copyright applies. Ask the author, find the licence, or write your own code.
7. They have **access to a service**, not a copy of the program, under the service's terms.

**(b)** In scenario 5 the program is open source **and** sold, so "open source" does not mean "free of charge". Open source is about the **freedoms** granted by the licence (use, study, modify, share), not about the price.

## Answer 7
**(a)**
- (i) **3.2.6** (bug fix → PATCH)
- (ii) **3.3.0** (new compatible feature → MINOR; PATCH resets)
- (iii) **4.0.0** (breaking change → MAJOR; MINOR and PATCH reset)
- (iv) **3.2.6** (one patch release can include several bug fixes; each change here is judged separately from the current version 3.2.5)

**(b)** **3.2.5 → 4.0.0.** A MAJOR change may break old files, add-ons or settings, so check what changed. A PATCH is expected to be a safe bug fix.

**(c)** A security patch closes a **vulnerability** that attackers may already be exploiting. Delaying leaves you exposed.

**(d)** **No.** `24.04` is not MAJOR.MINOR.PATCH. It follows a **date-based** scheme: year 2024, month April.

## Answer 8
**(a)** *(Model answer)*

| | Advantages | Disadvantages |
|---|---|---|
| **Web app** | 1. Nothing to install on members' devices. 2. Updates reach everyone immediately. | 1. Needs internet. 2. Fewer device features. |
| **Installed program** | 1. Can work offline. 2. Can use more device features. | 1. Must be installed and updated on every device. 2. Different versions for different laptops and phones. |

**(b)** *(Model answer)* Recommend a **web app**. Members use different devices, nobody has to install or update anything, and the club's single version is always current. This matches the club's low-maintenance needs.

**(c)** For example: if sign-ups had to work at an event with **no internet**, an installed or offline-capable app might be better.

## Answer 9 (model answer and marking guide)

| # | Software | Type |
|---|---|---|
| 1 | Start-up code stored in the phone | **Firmware** |
| 2 | The phone's operating system (for example Android or iOS) | **System software** |
| 3 | Camera driver and network drivers | **System software** |
| 4 | The messaging app | **Application software** |
| 5 | A library or connector the app uses to store messages | **Middleware** (or a library dependency) |
| 6 | Server software at the messaging company that passes the photo on | **Application software** on a remote computer |
| 7 | The editor, compiler or interpreter, and Git used to build the app | **Programming software** |

- **Licences (example):** the phone operating system or the messaging app may be proprietary; part of the system or a library could be open source (for example, Android is built on open source parts). *Your answer should show reasoning, and it is fine to say you are not certain.*
- **Updates:** a security patch to the messaging app closes a weakness; an OS update keeps the app compatible.
- **Errors:** a developer can find a **syntax** error before release because the code will not translate; a logic error (for example, sending the wrong photo size) needs **testing**.

**Marking guide (self-check):** ☐ At least six items ☐ At least one of each required type ☐ Types match Figure 1 ☐ Licence reasoning given ☐ Update reason makes sense ☐ Error type correctly named.

---

*Answers have been calculated twice and the code snippets were run to confirm their behaviour. A teammate who is not the author should re-check them and record the result in the [Teammate Review](../Teammate_review/10_teammate-review.md).*
