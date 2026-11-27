# 1.4 Test Bank: Memory Management

T4, M4 and O2 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T4 (True or False).** RAM keeps your files safe when the power is off.

**M4 (choose TWO).** Which two sentences about RAM are true?

- A. It keeps your photos forever
- B. It is the same as the hard drive
- C. It is fast working memory
- D. It is cleared when the power is off

**O2. Why is my laptop so slow?** (about 100 words, 5 marks)

Dandroid opened 40 browser tabs. Now the laptop is very slow, and the drive light keeps flashing.

(1) What is RAM, and what is storage? Use the desk and bookshelf idea. (2) Why does the laptop become slow when RAM is full? (3) Give two things Dandroid could do to make it faster.

Use these words: RAM · storage · desk · bookshelf · swap · slow

**Q1 (True or False).** A page fault always means the program has crashed. *(Chapter 1 quick quiz)*

**Q2.** With 3 frames and the requests 1, 2, 3, 4, 1, 2, how many page faults does FIFO make?

**Q3.** Why does the OS give each program its own virtual addresses instead of letting it use real RAM addresses?

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T4 | **False** | RAM is like a desk: it is cleared when you leave. Correct version: RAM is cleared when the power is off; storage (SSD or hard drive) keeps your files. |
| M4 | **C, D** | RAM is the fast "desk" and is temporary. Storage keeps photos (A), and the hard drive is storage, a different part (B). |
| Q1 | **False** | Most page faults are normal: the OS just fetches the page from storage. |
| Q2 | **6** | 1, 2, 3 are faults; 4 is a fault (out: 1); 1 is a fault (out: 2); 2 is a fault (out: 3). Every request misses. |
| Q3 | Protection | Each program can only reach its own memory, so one buggy or harmful program cannot read or overwrite another's data. |

**O2 sample answer (127 words).** RAM is like a small desk. It is very fast, but it only holds what you are working on now, and it is cleared when the power goes off. Storage (an SSD or hard drive) is like a big bookshelf: it is much bigger and keeps files when the power is off, but it is slower. With 40 tabs open, the desk is full. The OS has to move some pages from RAM to the bookshelf (this is called swap) and bring them back when they are needed. Fetching from storage is much slower than using RAM, so everything feels slow and the drive is busy. To make it faster, Dandroid could close tabs and apps it is not using, restart the browser, or add more RAM.

**O2 key points (1 mark each):** RAM = fast, small, temporary (the desk) · storage = big, slower, keeps files (the bookshelf) · when RAM is full the OS swaps pages to storage · storage is slower, so the laptop slows down · two sensible fixes. *Also accept* "virtual memory" or "page faults" instead of "swap" if explained correctly.
