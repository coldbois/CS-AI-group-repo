# Module 10: Introduction to Software

**Software Fundamentals · Study Guide content · V2.0 working draft**

| | |
|---|---|
| **Audience** | Complete beginners (no programming background needed) |
| **Estimated study time** | 4 to 5 hours, including the activities |
| **Author** | [Your name] |
| **Reviewer (not the author)** | [Teammate name, to be completed] |
| **Draft date** | 2026-11-03 |

**Files in this module:**
[Main Theory (this file)](10_main-theory.md) ·
[Learner Activities](../Learner%20Activity/10_learner-activities.md) ·
[Test Bank](../Test%20bank%20Question_Answer/10_test-bank.md) ·
[References and AI Usage](../References%20and%20AI%20Usage/10_references-and-ai-usage.md) ·
[Teammate Review](../Teammate_review/10_teammate-review.md) ·
[Content Status and Mapping](../10_content-status-and-mapping.md)

**Related module:** [Module 09: Where Operating Systems Meet Symbolic AI](../../09_where-operating-systems-meet-symbolic-ai/Main%20Theory/09_main-theory.md) (this module refers to it where the two connect).

---

## 1. Module Overview

Every time you send a message, play a game or watch a video, a computer follows instructions written by people. Those instructions are **software**. This module answers four beginner questions:

1. **What is software**, and how is it different from hardware?
2. **What kinds of software are there?**
3. **How does a written program become something a computer can run?**
4. **What happens to software in the real world**: who owns it, how it is delivered, and why it keeps changing?

**How the module is organised**

| Part | Big question | Sections | Practise with |
|---|---|---|---|
| **A. What software is** | What is software and what types exist? | 4, 5 | Activity 1 |
| **B. How software is made and runs** | How do instructions and data become a running program, and what goes wrong? | 6 to 9 | Activities 2 to 5 |
| **C. Software in the real world** | Who owns software, how is it delivered, and how does it change? | 10 to 13 | Activities 6 to 9 |

**Prerequisite words.** We use a kitchen analogy throughout.

| Word | Meaning | Kitchen analogy |
|---|---|---|
| **Hardware** | The physical parts of a computer | The kitchen: stove, counter, fridge |
| **CPU** | The part that carries out instructions, one small step at a time | The chef |
| **RAM (memory)** | Fast, temporary workspace, emptied when power is off | The counter where you work |
| **Storage (disk)** | Slower, permanent space for files | The pantry |
| **Instruction** | One small command the CPU can carry out | One line of a recipe |
| **Data** | Information the instructions work on | The ingredients |

---

## 2. Learning Outcomes

By the end of this module you should be able to:

| # | Outcome | Sections |
|---|---|---|
| **LO1** | Define software and explain how it differs from hardware | 4 |
| **LO2** | Classify examples into system, application, programming, middleware and firmware/embedded software | 5 |
| **LO3** | Explain why computers use binary and convert small numbers between decimal and binary | 6 |
| **LO4** | Explain how source code becomes a running program, and compare compiled, interpreted and hybrid approaches | 7 |
| **LO5** | Describe an algorithm, trace it step by step, and relate it to a program | 8 |
| **LO6** | Identify and fix syntax, runtime and logic errors | 9 |
| **LO7** | Compare proprietary, open source and other software licences and judge simple scenarios | 10 |
| **LO8** | Explain how software is delivered and updated, and read a version number | 11 |
| **LO9** | Describe the qualities of good software and how this module connects to the others | 12, 13 |

---

# PART A: WHAT SOFTWARE IS

## 3. How Part A is built

Section 4 defines software and separates it from hardware. Section 5 sorts software into types, using one diagram you will reuse for the rest of the module.

---

## 4. Hardware and Software

### 4.1 Definitions

> **Hardware** is the physical equipment of a computer: things you can touch.
> **Software** is the set of programs, together with their data, documentation and settings, that tells hardware what to do.

A **program** is one set of instructions that carries out a task. Software is a broader word: a word processor, for example, is one piece of software made of many programs plus its data files, help pages and settings.

**Analogy:** A piano is hardware. The sheet music is software. The same piano can play a thousand tunes, but only if someone gives it different sheet music.

### 4.2 Why is it called "soft"?

| Property of software | What it means | Example |
|---|---|---|
| **Intangible** | You cannot touch it | You can hold a phone but not the app inside it |
| **Changeable** | It can be updated without replacing the hardware | A phone gets a new feature after an update |
| **Easy to copy** | Copies cost almost nothing to make | Downloading an app |
| **Does not wear out physically** | But it can become outdated or contain mistakes (bugs) | An old game that no longer works on a new phone |

### 4.3 Instructions and data

Software contains two kinds of things:

- **Instructions:** what to do (for example, "add these two numbers").
- **Data:** what to do it to (for example, the two numbers).

A computer stores *both* as patterns of 0s and 1s (Section 6). This is why one machine can run any software: a different pattern of instructions gives a different behaviour.

### 4.4 Worked example 1: one phone, three behaviours

The phone's hardware never changes. Only the software does.

| Software running | Hardware parts it mainly uses | What the user sees |
|---|---|---|
| Camera app | Camera sensor, CPU, storage | Photos |
| Map app | GPS receiver, screen, network | Your position on a map |
| Music app | Network, speaker, storage | Songs playing |

**Key lesson:** Hardware provides *capabilities*. Software decides *what is done with them*.

> **Common misunderstanding: "Software means apps."**
> Apps are only one type. The operating system, device drivers and the code inside your router are also software (Section 5).

---

## 5. Types of Software

### 5.1 The main types

![Figure 1: Types of software and where they sit. A stack from the user down to the hardware: application software, middleware, system software, firmware, hardware. Programming software sits beside the stack because it is used to build software.](../Diagrams%20and%20Pictures/10_fig1_software-types.svg)

*Figure 1. Types of software. The stack shows layers that run the computer; programming software is the toolbox used to make software.*

| Type | What it does | Examples |
|---|---|---|
| **Application software** | Does tasks for the user | Web browser, word processor, game, messaging app |
| **System software** | Manages the computer and provides a platform for applications | Operating system, device drivers, utilities (such as backup tools) |
| **Programming software** | Helps developers create other software | Code editor, compiler, interpreter, debugger, IDE (integrated development environment), Git |
| **Middleware** | Sits between other programs so they can work together | A database connector; a message queue that passes data between programs |
| **Firmware / embedded software** | Is stored *inside* a device and controls it | Router software, a smart TV's control software, a washing machine controller, a computer's start-up code |

**Other ways to sort software.** The same program can be described in several ways:
- **By licence:** proprietary or open source (Section 10).
- **By delivery:** installed on a device, a mobile app, or a web app (Section 11).

### 5.2 Worked example 2: classify these

| Item | Type | Reasoning |
|---|---|---|
| Windows or Linux | System software | It manages hardware for all other programs |
| A printer driver | System software | It lets the OS control one specific printer |
| Microsoft Excel | Application software | A user does tasks (calculations) with it |
| VS Code | Programming software | Developers use it to write code |
| The Python interpreter | Programming software | It runs code that developers write |
| The control program inside a microwave | Firmware / embedded software | It is stored in the device and controls only that device |
| A tool that lets a web app talk to a database | Middleware | It connects two other pieces of software |
| Google Docs used in a browser | Application software (a web app) | The user does tasks; it is delivered through the browser |

### 5.3 Common misunderstandings

> - *"A web browser is an operating system."* No. A browser is an **application**. It runs on an operating system (although some operating systems, like ChromeOS, are built around a browser).
> - *"Firmware is hardware because it is inside the device."* No. Firmware is **software** that is stored in the device's memory.
> - *"Programming software is what runs my finished program."* Not exactly: programming software is used to **make** software. A finished program runs on the operating system and hardware. (An interpreter is a special case, because it runs your code while you develop it, which is why it counts as programming software.)
> - *"Software types are strict boxes."* Some items fit more than one category (an antivirus tool can be called a utility, so system software, or an application). What matters is giving a reason.

**▶ Apply it:** Activity 1 (classify 12 items and explain).

---

## Quick Check: Part A

1. Give one difference between hardware and software.
   *Answer: hardware is physical and touchable; software is a set of instructions and data that can be changed and copied.*
2. Which type of software is a printer driver?
   *Answer: system software.*
3. Why is firmware software and not hardware?
   *Answer: it is a set of instructions (code) that happens to be stored in the device.*

---

# PART B: HOW SOFTWARE IS MADE AND RUNS

## 6. How Computers Store Instructions and Data: Binary

### 6.1 Why 0s and 1s?

Computer circuits are built from tiny electronic switches. A switch has two reliable states, off and on. We write them as **0** and **1**. One 0 or 1 is a **bit**. Eight bits make a **byte**.

Everything a computer stores is a pattern of bits: numbers, text, photos, music, and the program's own instructions.

### 6.2 Reading binary

Binary uses **place values** that double each step to the left: 1, 2, 4, 8, 16, 32, 64, 128. A bit that is **1** adds its place value; a bit that is **0** adds nothing.

![Figure 3: The byte 00101101 has place values 128, 64, 32, 16, 8, 4, 2, 1. The bits set to 1 are at 32, 8, 4 and 1, so the value is 32 + 8 + 4 + 1 = 45.](../Diagrams%20and%20Pictures/10_fig3_binary-place-values.svg)

*Figure 3. Reading a byte: add the place values of the bits that are 1.*

### 6.3 Worked example 3: decimal and binary

**Binary to decimal.** Convert `1101`.
Place values (right to left): 1, 2, 4, 8. The bits are 1 (8), 1 (4), 0 (2), 1 (1).
8 + 4 + 0 + 1 = **13**.

**Decimal to binary.** Convert **45**.
1. Find the largest place value that fits: 32 fits (45 − 32 = 13).
2. Next: 16 does not fit (0); 8 fits (13 − 8 = 5); 4 fits (5 − 4 = 1); 2 does not fit (0); 1 fits (1 − 1 = 0).
3. Write the bits from 128 down to 1: 0 0 1 0 1 1 0 1.
4. Result: **00101101**, or **101101** with the leading zeros dropped. This matches Figure 3.

**How many values can a number of bits hold?** *n* bits can make 2ⁿ different patterns. So 3 bits give 2³ = 8 patterns (0 to 7), and 8 bits (one byte) give 2⁸ = 256 patterns, representing 0 to 255.

### 6.4 Worked example 4: text is stored as numbers

Each character is given a number by a standard. For the basic English characters the numbers are the same in **ASCII** and **Unicode**: for example **H = 72**, **i = 105**, **! = 33**.

Encode "Hi" as bytes:
- H = 72 = 64 + 8 → `01001000`
- i = 105 = 64 + 32 + 8 + 1 → `01101001`

So "Hi" is stored as `01001000 01101001`. When the program displays it, the computer looks up the numbers and shows the matching letters.

> **Common misunderstanding: "The computer understands the letter H."**
> The computer stores and moves *numbers*. Software and hardware agree that 72 means H when displaying text.

**▶ Apply it:** Activity 2 (convert numbers, encode text, find the error).

---

## 7. From Source Code to a Running Program

### 7.1 Levels of language

| Level | What it looks like | Who reads it |
|---|---|---|
| **Machine code** | Binary instructions for one kind of CPU | The CPU, directly |
| **Assembly language** | Short readable names for machine instructions | Specialist programmers |
| **High-level language** | Close to human language and mathematics (Python, Java, C) | Most programmers |

People write **source code** in a high-level language because it is easier to read and write. But a CPU understands only its own machine code, so the source code must be **translated**.

**Important:** machine code differs between CPU families (for example, the chips in most PCs and the chips in most phones use different instruction sets). An executable built for one family will not run directly on the other.

### 7.2 A tiny example of what translation means

One line of source code:

```python
total = price * quantity
```

At the machine level this becomes a sequence of very small steps. The list below is **an illustration of the idea, not real machine code**:

1. Fetch the number stored as `price` from memory.
2. Fetch the number stored as `quantity` from memory.
3. Multiply the two numbers.
4. Store the result in memory as `total`.

One readable line becomes several tiny instructions, and a translator does that work for the programmer.

### 7.3 Three ways to translate and run

![Figure 2: From source code to a running program. Route 1, compiled: source code, compiler, executable file, CPU. Route 2, interpreted: source code, interpreter, CPU. Route 3, hybrid: source code, compiler to bytecode, bytecode, virtual machine, CPU.](../Diagrams%20and%20Pictures/10_fig2_source-to-running.svg)

*Figure 2. Three routes from source code to execution.*

| | Compiled | Interpreted | Hybrid |
|---|---|---|---|
| **How it works** | A **compiler** translates the whole program into an **executable** file before it runs | An **interpreter** reads the source and carries out each step as it goes | A compiler makes **bytecode**, then a **virtual machine** runs the bytecode |
| **Typical examples** | C, C++ | Many scripting languages in simple form | Java; the standard version of Python |
| **Advantages** | Usually fast to run; you can share the executable without the source | Quick to try and change; helpful for learning | Same bytecode can run on any computer that has the virtual machine |
| **Disadvantages** | Must rebuild after each change; the executable suits one kind of CPU | Often slower to run | Needs the virtual machine installed; extra step |

> **Common misunderstanding: "A language is either compiled or interpreted."**
> It is really about how a language is *usually run*. Real systems mix ideas. The standard Python first compiles your code to bytecode and then runs that bytecode, so it is hybrid.

(Here "virtual machine" means a program that runs bytecode. It is not the same as a virtual machine that pretends to be a whole computer.)

### 7.4 Worked example 5: when do the errors show up?

**Script A (Python): a mistake that appears only when the line runs**

```python
print("Step 1")
print("Step 2")
print(10 / 0)
print("Step 4")
```

Output on a real run:

```
Step 1
Step 2
ZeroDivisionError: division by zero
```

"Step 4" never prints. Python ran line by line until it hit the impossible division. This is a **runtime error**.

**Script B (Python): a mistake in the grammar of the code**

```python
print("Step 1")
print("Step 2"
```

The bracket is never closed. Python reports a `SyntaxError` and **prints nothing at all**, not even "Step 1", because it checks the whole file before running any of it.

**In a compiled language such as C**, a syntax mistake stops the compiler: no executable file is created, so there is nothing to run.

**Lesson:** a *syntax* error is caught **before** the program runs; a *runtime* error is found **while** it runs.

**▶ Apply it:** Activity 3 (predict outputs and choose an approach).

---

## 8. Algorithms and Programs

### 8.1 What is an algorithm?

> An **algorithm** is a finite, step-by-step set of clear instructions for solving a problem.

A good algorithm has clear steps, comes to an end, and produces a result. A recipe is an everyday example.

| Idea | Meaning |
|---|---|
| **Algorithm** | The method (an idea; it exists independently of any language) |
| **Pseudocode** | The method written in plain, structured English |
| **Program** | The method written in a programming language so that a computer can run it |
| **Software** | One or more programs plus data, documentation and settings |

**Input → process → output:** nearly every program takes input (data in), processes it with an algorithm, and produces output (a result).

### 8.2 Worked example 6: find the largest number

**Problem:** given a list of numbers, find the largest.

**Pseudocode**
```
set largest to the first number
for each remaining number:
    if the number is bigger than largest:
        set largest to that number
output largest
```

**Python version**
```python
numbers = [4, 11, 7]
largest = numbers[0]
for n in numbers[1:]:
    if n > largest:
        largest = n
print(largest)
```

![Figure 4: Flowchart of the largest-number algorithm. Start, set largest to the first number, then repeat: if there is another number, take it and if it is larger than largest, replace largest. When no numbers remain, output largest and end.](../Diagrams%20and%20Pictures/10_fig4_largest-number-flowchart.svg)

*Figure 4. The same algorithm as a flowchart.*

**Trace table** for `[4, 11, 7]`:

| Step | `n` | Is `n > largest`? | `largest` afterwards |
|---|---|---|---|
| Start | (none) | (none) | 4 |
| 1 | 11 | yes (11 > 4) | **11** |
| 2 | 7 | no (7 > 11 is false) | 11 |
| End | | | Output: **11** |

**Same algorithm, different languages.** The steps stay the same whether you write Python, Java or C; only the grammar changes. You will study the details of programming in Module 11 and of algorithms in Module 12.

**▶ Apply it:** Activity 4 (trace, modify, and find the flaw).

---

## 9. Bugs and Errors

A **bug** is a mistake in software that makes it behave wrongly. There are three main kinds of error.

| Kind | What is wrong | When it appears | Example |
|---|---|---|---|
| **Syntax error** | Breaks the grammar rules of the language | Before the program runs (when the code is translated) | A missing bracket or comma |
| **Runtime error** | The instructions are legal but something impossible happens while running | During the run, often with an error message | Dividing by zero; using the 5th item of a 3-item list |
| **Logic error** | The program runs without complaint but gives the **wrong result** | During or after the run; often no message | Using the wrong formula |

### 9.1 Worked example 7: one of each

Python is case-sensitive and follows normal arithmetic order (division before addition).

| Code | What happens (checked by running it) | Kind | Fix |
|---|---|---|---|
| `print("Total:" total)` | `SyntaxError: invalid syntax` (a comma is missing) | Syntax | `print("Total:", total)` |
| `scores = [70, 85, 90]` then `print(scores[3])` | `IndexError: list index out of range` (positions start at 0, so valid positions are 0, 1, 2) | Runtime | Use `scores[2]` for the last item |
| `Print("hello")` | `NameError: name 'Print' is not defined` (the built-in is spelled `print`) | Runtime | `print("hello")` |
| `a = 4`, `b = 8`, `average = a + b / 2` | Prints **8.0**, but the average of 4 and 8 should be **6.0** | Logic | `average = (a + b) / 2` |

**Why logic errors are hardest:** the computer reports nothing. You only find them by **testing** with inputs whose correct answers you already know (here, 4 and 8 should give 6).

### 9.2 A simple debugging routine

1. **Reproduce** the problem reliably.
2. **Locate** where it happens (read the error message; check the line it points to).
3. **Understand** why (trace the values step by step, as in a trace table).
4. **Fix** one thing at a time.
5. **Retest**, including the cases that used to work.

> **Common misunderstandings**
> - *"A bug is a computer virus."* No. A bug is a programmer's mistake; a virus is malicious software.
> - *"If there is no error message, the program is correct."* No. Logic errors give no message.
> - *"Testing once proves it works."* No. Testing shows the program works for the cases tested.

**▶ Apply it:** Activity 5 (classify and fix errors).

---

## Quick Check: Part B

1. Write 1010 in decimal. *Answer: 8 + 2 = 10.*
2. A program has a missing bracket. Is that a syntax, runtime or logic error? *Answer: syntax.*
3. Which approach produces an executable file before the program runs: compiled or interpreted? *Answer: compiled.*

---

# PART C: SOFTWARE IN THE REAL WORLD

## 10. Ownership and Licensing

### 10.1 Software is protected by copyright

By default, the person or company that creates software owns the copyright. You may use it only as far as a **licence** (a set of permissions) allows. Even free-to-download software can have strict rules.

### 10.2 Common models

| Model | What you receive | Typical permissions | Typical example |
|---|---|---|---|
| **Proprietary (closed source)** | Usually only the finished program | Use it under the licence terms; cannot normally modify or redistribute; source code usually not shared | Windows |
| **Freeware** | Free to use, but still proprietary | Use at no cost; source code not shared | Many free utilities |
| **Trial / shareware** | Try now, pay to keep using | Limited time or features | Trial versions |
| **Open source** | The program **and** its source code | The licence lets you use, study, modify and share | Linux |
| **Software as a service (SaaS)** | Access to a running service, not the program itself | Use it while you subscribe; you do not get a copy | A web-based spreadsheet on subscription |
| **Public domain** | No copyright restrictions | Anyone can use it for any purpose | Works that are deliberately dedicated to the public domain |

Open source licences come in two main families:

| Family | Idea | Example licence | Simplified summary |
|---|---|---|---|
| **Permissive** | Few conditions | MIT | You may use, modify and distribute the software, even inside a closed commercial product, as long as you keep the copyright notice and licence text |
| **Copyleft** | Keeps the freedom going | GNU GPL | If you **distribute** a modified version or a work based on it, you must make it available under the same licence, with its source code |

*These are simplified summaries to help learning. They are not legal advice; always read the actual licence text.*

### 10.3 Worked example 8: what are you allowed to do?

| Scenario | Answer | Reason |
|---|---|---|
| Mia uses an MIT-licensed library in an app she sells without sharing her source | **Allowed** | MIT is permissive; she must keep the notice and licence text |
| Raj changes a GPL program and gives the modified program to friends | **He must share the source** and licence his version under the GPL | GPL is copyleft and applies when you distribute |
| Raj changes a GPL program only for himself and shares it with nobody | Generally **no obligation to publish** | The GPL conditions are triggered by distributing copies |
| Lena finds a free photo editor with no source code | **Not open source** | Free of cost is not the same as open source; it is freeware or proprietary |
| A company sells copies of a GPL program | **Allowed**, if it also provides the source and the same freedoms | Open source can be sold; it is about freedoms, not price |

> **Common misunderstandings**
> - *"Open source means free of charge."* Not necessarily. It means the source is available under a licence that grants freedoms.
> - *"Free download means open source."* No.
> - *"If I can see the code online, I can copy it."* Without a licence, copyright still applies. Check the licence first.

**▶ Apply it:** Activity 6 (judge licensing scenarios).

---

## 11. Delivering and Updating Software

### 11.1 How software reaches users

| Method | How it works | Advantages | Disadvantages |
|---|---|---|---|
| **Installed program** | Files are copied to your computer and registered with the OS | Works without internet; can use all device features | You must update it yourself or allow auto-update |
| **Mobile app (app store)** | Downloaded from a store that checks and updates apps | Easy install and update | Tied to one platform's store rules |
| **Web app / SaaS** | Runs on a server; you use it in a browser | No install; always current; works on many devices | Needs internet; fewer device features |
| **Firmware update** | New software is written into a device | Fixes the device without replacing it | Must be done carefully; a failed update can disable the device |

**Dependencies.** Most software relies on **libraries** (reusable code written by others). The other software it needs in order to work is its **dependencies**. If a dependency is missing or too old, the program may not run. (The operating system is the biggest dependency; see Module 09.)

### 11.2 Why software is updated

- **Bug fixes:** correct mistakes.
- **Security patches:** close a **vulnerability** (a weakness attackers can exploit).
- **New features and support for new hardware.**

**Risk:** updates can introduce new bugs or break compatibility, which is why developers test them and why users may read what changed before updating major versions.

### 11.3 Version numbers

Many projects use **semantic versioning**: `MAJOR.MINOR.PATCH`.

![Figure 5: Reading a version number. In 2.4.1 the MAJOR part changes for breaking changes, the MINOR part for new features that do not break old ones, and the PATCH part for bug fixes only. Examples: 2.4.1 to 2.4.2 is a bug fix; 2.4.2 to 2.5.0 is a new feature; 2.5.0 to 3.0.0 is a breaking change.](../Diagrams%20and%20Pictures/10_fig5_version-numbers.svg)

*Figure 5. The parts of a version number and what changes them.*

| Change made | Increase | Reset |
|---|---|---|
| Bug fix only | PATCH | nothing |
| New feature, old things still work | MINOR | PATCH goes to 0 |
| Breaking change | MAJOR | MINOR and PATCH go to 0 |

Not every product follows this. Some use dates or plain counting, for example the version `24.04` means April 2024 for a well-known Linux distribution.

### 11.4 Worked example 9: choosing the next version

Current version: **2.4.1**.

| Change | New version | Why |
|---|---|---|
| Fixed a crash | **2.4.2** | Bug fix → PATCH |
| Added a new export option; nothing else changed | **2.5.0** | New, compatible feature → MINOR (PATCH resets) |
| Removed an old file format, so old files no longer open | **3.0.0** | Breaking change → MAJOR (MINOR, PATCH reset) |

**▶ Apply it:** Activity 7 (versions and updates) and Activity 8 (choose a delivery method).

---

## 12. What Makes Software Good?

Working once is not enough. Software is judged by several qualities:

| Quality | Meaning |
|---|---|
| **Correct** | Gives the right results |
| **Reliable** | Keeps working and recovers from problems |
| **Usable** | People can learn and use it easily |
| **Efficient** | Does not waste time or memory |
| **Secure** | Protects data and resists misuse |
| **Maintainable** | Others can understand and change it later |

These qualities often pull against each other (for example, very high security can reduce ease of use), so developers make trade-offs. How teams plan, build, test and maintain software to reach these qualities is the topic of **Module 15: Software Engineering**.

**How this module connects to the others**

| Module | What it adds to this one |
|---|---|
| 09 Operating systems and symbolic AI | The system software that every program runs on |
| 11 Computer programming | The detail of writing programs |
| 12 Algorithms | Judging how good an algorithm is |
| 13 Data structures | Organising data for algorithms |
| 14 Databases | Storing large amounts of data safely |
| 15 Software engineering | Building software well in teams |

---

## 13. Putting It All Together

### 13.1 Worked example 10: you open a news website

Which software is involved, from switching on to reading the page? (Use Figure 1 as a map.)

| Step | What happens | Software type |
|---|---|---|
| 1 | You press the power button; the start-up code stored on the computer begins loading the system | **Firmware** |
| 2 | The operating system loads and manages memory, files and the network card | **System software** (with **device drivers** controlling the hardware) |
| 3 | You start the browser; the OS creates a process for it | **Application software** |
| 4 | The browser asks the network for the page | Network drivers (**system software**) |
| 5 | A web server program on a remote computer receives the request | **Application software** running on another computer's operating system |
| 6 | The server fetches the article from a database, using a connector | **Middleware** and database software |
| 7 | The page returns; the browser displays it and runs the page's script code | The browser's engine translates and runs the code (Section 7) |

Every one of these programs was written by people using **programming software**: editors, compilers or interpreters, and version control. It follows a **licence** and has a **version number**, and it is updated over time.

**▶ Apply it:** Activity 9 (map the software behind a task).

---

## 14. Common Misconceptions: Summary Table

| # | Misconception | Correct idea | Section |
|---|---|---|---|
| 1 | "Software means apps." | Apps are one type; operating systems, drivers and firmware are software too. | 4, 5 |
| 2 | "A web browser is an operating system." | A browser is an application that runs on an OS. | 5 |
| 3 | "Firmware is hardware." | Firmware is software stored in a device. | 5 |
| 4 | "The computer understands letters." | It stores numbers; a standard maps numbers to characters. | 6 |
| 5 | "A language is either compiled or interpreted." | It depends on how it is usually run; many are hybrid. | 7 |
| 6 | "All errors show up before the program runs." | Syntax errors do; runtime and logic errors appear later. | 7, 9 |
| 7 | "No error message means no bug." | Logic errors give no message. | 9 |
| 8 | "A bug is a virus." | A bug is a mistake; a virus is malicious software. | 9 |
| 9 | "Algorithm and program are the same thing." | The algorithm is the method; the program is it written in a language. | 8 |
| 10 | "Open source means free of charge." | It means the source is available under a licence with freedoms. | 10 |
| 11 | "A free download is open source." | Free of cost does not mean the source is shared. | 10 |
| 12 | "Updates only add features." | Many updates fix bugs and security problems. | 11 |

---

## Summary

- **Software** is instructions and data (plus documentation and settings) that tell hardware what to do. It is **changeable**, **intangible** and **easy to copy**.
- Main types: **application**, **system**, **programming**, **middleware**, and **firmware/embedded** software.
- Computers store everything as **binary**. Source code is **translated** (compiled, interpreted or hybrid) into instructions a CPU can run.
- An **algorithm** is the method; a **program** is the method written in a language. Errors are **syntax**, **runtime** or **logic**, and logic errors need **testing** to find.
- Software has **owners and licences** (proprietary, open source, permissive, copyleft), is **delivered** in different ways, and is **updated**, with **version numbers** that signal what changed.

---

## Glossary (terms used consistently in this module)

| Term | Meaning |
|---|---|
| **Hardware** | Physical parts of a computer |
| **Software** | Programs plus their data, documentation and settings |
| **Program** | A set of instructions that performs a task |
| **Instruction / Data** | A command for the CPU / the information it works on |
| **Application software** | Software that does tasks for users |
| **System software** | Software that manages the computer (OS, drivers, utilities) |
| **Programming software** | Tools used to create software |
| **Middleware** | Software that connects other software |
| **Firmware / Embedded software** | Software stored inside a device that controls it |
| **IDE** | Integrated development environment: an editor plus tools in one program |
| **Bit / Byte** | One 0 or 1 / eight bits |
| **Binary** | Number system using only 0 and 1 |
| **ASCII / Unicode** | Standards that give characters their numbers |
| **Source code** | Program text written by people |
| **Machine code** | Binary instructions a CPU can run |
| **Assembly language** | Readable names for machine instructions |
| **High-level language** | A language close to human language (Python, Java, C) |
| **Compiler** | Translates a whole program before it runs |
| **Interpreter** | Reads and runs a program step by step |
| **Executable** | A file of machine code ready to run |
| **Bytecode** | Intermediate code run by a virtual machine |
| **Virtual machine (bytecode)** | A program that runs bytecode |
| **Algorithm** | Step-by-step method for solving a problem |
| **Pseudocode** | An algorithm written in structured plain English |
| **Flowchart** | A diagram of an algorithm's steps |
| **Trace table** | A table of values step by step |
| **Bug** | A mistake that makes software behave wrongly |
| **Syntax / Runtime / Logic error** | Grammar mistake / impossible action while running / wrong result without a message |
| **Debugging** | Finding and fixing bugs |
| **Copyright / Licence** | Legal ownership of software / permissions granted to users |
| **Proprietary / Open source** | Source not shared / source available under a licence with freedoms |
| **Permissive / Copyleft** | Few conditions (MIT) / share-alike when distributing (GPL) |
| **SaaS** | Software delivered as an online service |
| **Library / Dependency** | Reusable code written by others / other software a program needs |
| **Patch / Update** | A fix / a new version of software |
| **Vulnerability** | A weakness attackers can exploit |
| **Semantic versioning** | MAJOR.MINOR.PATCH numbering |

---

## Scope Note and Honest Gaps

**Covered (core):** everything above.
**Not covered in this version (optional extensions):**
- The history of software and programming languages
- Cloud computing details and app store rules
- Cybersecurity beyond the idea of vulnerabilities and patches
- Detailed programming syntax (Module 11), algorithm efficiency (Module 12), data structures (Module 13), databases (Module 14) and the software development life cycle and testing (Module 15)

These gaps and the next steps are recorded in the [Content Status and Mapping](../10_content-status-and-mapping.md) file.

**Where to practise:** [Learner Activities](../Learner%20Activity/10_learner-activities.md) (with answers) and the [Test Bank](../Test%20bank%20Question_Answer/10_test-bank.md).

**References:** see [References and AI Usage](../References%20and%20AI%20Usage/10_references-and-ai-usage.md). All diagrams (Figures 1 to 5) are original drawings made for this module.
