# 2.2 Introduction to Software

![Dandroid standing still, confused](../../../assets/dandroid/dandroid-confused.png)

**Chapter 2 · Dandroid's Instructions** · Study Guide pp. 62–67 · Slide 21 · Test Bank T10, M10

> **Mission.** Dandroid has a perfect robot body... but it just stands there doing nothing. What is missing?

**You will learn to**

- explain the difference between hardware and software
- sort software into four types
- describe how source code becomes a running program

**Key words:** hardware, software, source code, machine code, compiler, interpreter, open source

---

## Hardware and software

**Hardware** is the physical part of a computer: anything you can touch. **Software** is the set of instructions that tells the hardware what to do.

Think of a piano and sheet music. The piano (hardware) can make every note, but on its own it plays nothing. The music (software) says which notes to play and when. Dandroid's body from Chapter 1 is the piano. This chapter writes the music.

## Four types of software

![Figure 2.2a](../Diagrams%20and%20Pictures/2-2_software-types.png)

*Figure 2.2a. Four types of software (Study Guide p. 63).*

| Type | What it does | Examples |
| --- | --- | --- |
| **System** | runs the computer itself | the OS, drivers, utilities |
| **Application** | helps *you* do a task | browser, Word, games, WhatsApp |
| **Programming** | helps developers build software | code editors, compilers, debuggers |
| **Middleware** | glue that lets programs talk to each other | database connectors, messaging tools |

A few more words you'll meet:

- **Firmware** is software built into a device, such as a router, a TV remote or the UEFI chip from [1.2](../../../Operating%20Systems%20%E2%80%94%20Essential%20Foundations/02_Boot%20Process%20and%20the%20Motherboard/Main%20Theory/02_main-theory.md).
- **Open source** means anyone can read and change the code (Firefox, VLC, LibreOffice, Linux, Python). **Proprietary** software is owned and restricted by a company. A **licence** sets the rules for using it.

## From idea to running program

![Figure 2.2b](../Diagrams%20and%20Pictures/2-2_idea-to-program.png)

*Figure 2.2b. From idea to running program (Study Guide p. 64; the same steps are on slide 21).*

1. **Source code.** A person writes instructions in a language people can read, such as Python or C.
2. **Translate.** The CPU can't read Python or C, so the code must be translated:
   - a **compiler** translates the *whole* program into machine code *before* it runs (C works this way, see [1.8](../../../Operating%20Systems%20%E2%80%94%20Essential%20Foundations/08_Basic%20C%20for%20Operating%20System%20Ideas/Main%20Theory/08_main-theory.md));
   - an **interpreter** translates and runs it *line by line* (Python works this way).
3. **Machine code.** The 0s and 1s the CPU actually understands.
4. **Run.** The OS loads it into memory as a **process** (remember [1.3](../../../Operating%20Systems%20%E2%80%94%20Essential%20Foundations/03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md)).

> **Bug alert.** A **bug** is a mistake that makes software behave wrongly. The word is older than computers, but a famous 1947 logbook from the Harvard Mark II team has a real moth taped into it, found stuck inside the machine.

## What makes software good?

When we judge software we look at six qualities:

| Quality | Question to ask |
| --- | --- |
| Correct | Does it give the right answers? |
| Reliable | Does it keep working without crashing? |
| Usable | Can people work out how to use it? |
| Efficient | Does it use little time, memory and battery? |
| Maintainable | Can other developers understand and update the code? |
| Secure | Does it protect data from people who shouldn't see or change it? |

## Try it

**Software Safari** (15 min, solo): sort the software on your own phone or laptop into the four types and rate your favourite app on the six qualities. Instructions and answers: [10_learner-activity.md](../Learner%20Activity/10_learner-activity.md).

## Going further (optional)

- **Machine code is binary.** Each binary digit (bit) is a place value that doubles from right to left: 128, 64, 32, 16, 8, 4, 2, 1. So `00001101` = 8 + 4 + 1 = 13. Eight bits make a byte.
- **Version numbers.** Many projects use *semantic versioning*, `MAJOR.MINOR.PATCH`. Going from 2.4.1 to 2.4.2 is a bug fix, 2.5.0 adds features, and 3.0.0 may break older things.

## Check yourself

1. Is a USB driver system or application software?
2. What does a compiler do?
3. Give two qualities of good software.

**Answers (try first, then peek)**
1. System software.
2. Translates a whole program into machine code before it runs.
3. Any two: correct, reliable, usable, efficient, maintainable, secure.


More questions: [10_test-bank.md](../Test%20bank%20Question_Answer/10_test-bank.md)

## Remember

- Hardware = the piano; software = the music.
- Four types: system, application, programming, middleware.
- Source code → compiler or interpreter → machine code → running process.

## Watch and explore

**Crash Course Computer Science #11: The First Programming Languages** (PBS, YouTube). Shows why we moved from machine code to readable languages. Write down one reason compilers made programming easier. It is history-heavy; skip the assembly details if they confuse you.

## References

- Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson. Chapter 1.
- Smithsonian National Museum of American History. (n.d.). *Log book with computer bug*. https://americanhistory.si.edu/collections/object/nmah_334663

---

Previous: [2.1 OS meets Symbolic AI](../../09_where-operating-systems-meet-symbolic-ai/Main%20Theory/09_main-theory.md) · Next: [2.3 Computer Programming](../../11_computer-programming/Main%20Theory/11_main-theory.md) · Up: [Chapter 2 overview](../../README.md)
