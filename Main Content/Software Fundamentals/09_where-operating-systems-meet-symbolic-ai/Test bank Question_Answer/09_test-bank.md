# Module 09 Test Bank: Operating Systems Meet Symbolic AI

Back to: [Main Theory](../Main%20Theory/09_main-theory.md) · [Learner Activities](../Learner%20Activity/09_learner-activities.md)

**Format:** Each question shows its type, difficulty, the learning outcome (LO) and the Main Theory section it tests. Answers and explanations follow each question group.

**Coverage map**

| Group | Questions | Outcomes | Sections |
|---|---|---|---|
| A. Operating systems | Q1 to Q13 | LO1 to LO6 | 4 to 9 |
| B. Symbolic AI | Q14 to Q22 | LO7 to LO9 | 10 to 13 |
| C. Where they meet | Q23 to Q25 | LO10 | 14, 15 |

---

# Group A: Operating Systems

**Q1. [Multiple choice · Easy · LO1 · Section 4]**
What is the main role of an operating system?
- A. To create documents and spreadsheets
- B. To manage the hardware and share it among programs
- C. To store all of the user's files permanently
- D. To connect the computer to the internet only

**Q2. [Multiple choice · Easy · LO2 · Section 5]**
A program wants to read a file from disk. What must it do?
- A. Access the disk hardware directly
- B. Ask the kernel through a system call
- C. Switch itself into kernel mode
- D. Ask another application to copy the file

**Q3. [Multiple choice · Easy · LO3 · Section 6]**
Which statement about programs and processes is correct?
- A. A program is a process that is not running
- B. A process is a program being run, and one program can create many processes
- C. A process is a part of a thread
- D. A program and a process always use the same memory

**Q4. [Multiple choice · Medium · LO3 · Section 6]**
A Waiting process's disk read has just finished. Which state does it move to?
- A. Running
- B. Terminated
- C. Ready
- D. New

**Q5. [True or false with correction · Medium · LO3 · Section 6]**
"Threads in the same process each have completely separate memory." If false, correct it.

**Q6. [Calculation · Medium · LO4 · Section 7]**
Three processes arrive at time 0 in the order P1, P2, P3 with burst times 5, 2 and 1. Using **FCFS**, calculate the average waiting time.

**Q7. [Calculation · Hard · LO4 · Section 7]**
Same processes as Q6, but using **Round Robin with a time slice of 2**. Calculate the average waiting time and say which method gives the lower average.

**Q8. [Calculation · Medium · LO5 · Section 8]**
Page size is 4096 bytes. A process's page table is: page 0 → frame 4, page 1 → frame 6, page 2 → frame 3. Translate virtual address **9000** to a physical address. Show your working.

**Q9. [Multiple choice · Medium · LO5 · Section 8]**
What is a page fault?
- A. A hardware failure in RAM
- B. An access to a page that is not currently in RAM
- C. A crash that always stops the program
- D. A virus detected by the OS

**Q10. [Short answer · Medium · LO2 · Section 5]**
Explain why a computer uses both user mode and kernel mode.

**Q11. [Find the error · Medium · LO5 · Section 8]**
A student writes: *"Virtual memory makes a computer faster because it adds extra RAM."* Identify the errors and give a correct statement.

**Q12. [Multiple choice · Medium · LO6 · Section 9]**
A file has permissions `-rw-r-----`. Who can **write** to it?
- A. The owner only
- B. The owner and the group
- C. Everyone
- D. Nobody

**Q13. [Application · Hard · LO6 · Section 9]**
A user, Mia, owns a file whose permissions are `----r-----` and she is also in its group. Can Mia read the file? Explain.

---

# Group B: Symbolic AI

**Q14. [Multiple choice · Easy · LO7 · Section 10]**
In symbolic AI, where does the system's knowledge mainly come from?
- A. Patterns it finds in large datasets
- B. Rules and facts written by people
- C. Random guessing
- D. The operating system's file system

**Q15. [True or false with correction · Easy · LO7 · Section 10]**
"Symbolic AI automatically learns its rules from thousands of examples." If false, correct it.

**Q16. [Multiple choice · Easy · LO9 · Section 13]**
In an expert system, which part stores the domain rules?
- A. Inference engine
- B. Working memory
- C. Knowledge base
- D. Explanation facility

**Q17. [Trace · Medium · LO8 · Section 12]**
Rules:
- R1: IF A AND B THEN C
- R2: IF C THEN D
- R3: IF E THEN F
- R4: IF D AND B THEN G

Known facts: A, B. Using **forward chaining**, list every new fact derived, in order, and say which rule(s) never fire.

**Q18. [Trace · Medium · LO8 · Section 12]**
Using the rules from Q17 and the facts A and B, use **backward chaining** to show that the goal **G** can be proven. List the sub-goals.

**Q19. [Short answer · Medium · LO9 · Section 13]**
Explain the difference between a knowledge base and an inference engine. Why does that difference matter?

**Q20. [Short answer · Medium · LO9 · Section 13]**
Give **two** limitations of expert systems, each with a brief explanation.

**Q21. [Find the error · Medium · LO8 · Section 12]**
A student says: *"Rule R2: IF memory_full AND disk_activity_high THEN suspect_thrashing fires as soon as memory_full is true."* Find the error and correct the statement.

**Q22. [Compare approaches · Hard · LO7 · Section 10]**
A company wants to (i) detect fraudulent card payments from millions of past transactions, and (ii) guide customers through a fixed refund policy with clear reasons. Which task better fits machine learning, and which better fits symbolic rules? Justify each choice in one or two sentences.

---

# Group C: Where They Meet

**Q23. [Multiple choice · Medium · LO10 · Section 14]**
Which statement best describes how an expert system relates to the operating system?
- A. The expert system replaces the OS
- B. The expert system is an application that runs as a process on the OS
- C. The OS is itself an expert system
- D. They have no connection

**Q24. [Explain and evaluate · Hard · LO10 · Section 14]**
Is a Unix file-permission check an example of symbolic AI? Give **one similarity** and **two differences** to a rule-based expert system.

**Q25. [Scenario · Hard · LO10 · Sections 6, 8, 14]**
An expert system has a faulty rule set that makes it repeat the same reasoning forever and fill memory. (a) What can the operating system do about it? (b) What can the OS *not* do? Use at least two OS concepts from Part A.

---

# Answer Key with Explanations

## Group A

**Q1: B.** The OS manages hardware and shares it. A is application software, C is only one part (files), and D is too narrow.

**Q2: B.** User-mode programs must ask the kernel through a system call. A and C are not allowed in user mode, and D is not how file access works.

**Q3: B.** A process is a running program, and starting a program twice makes two processes. A is wrong because a program file is not a "non-running process"; it is simply instructions on disk.

**Q4: C. Ready.** After I/O completes, the process becomes Ready, and the scheduler later decides when it runs.

**Q5: False.** Threads in the same process **share** the process's memory (they each have their own execution position).

**Q6: 4.0.** FCFS: P1 runs 0 to 5, P2 5 to 7, P3 7 to 8. Waiting times: P1 = 0, P2 = 5, P3 = 7. Average = 12 ÷ 3 = **4.0**.

**Q7: 3.0, so Round Robin is lower.**
Timeline (slice 2): P1 0 to 2 (3 left), P2 2 to 4 (done at 4), P3 4 to 5 (done at 5), P1 5 to 7 (1 left), P1 7 to 8 (done at 8).
Waiting = completion − burst: P1 = 8 − 5 = 3, P2 = 4 − 2 = 2, P3 = 5 − 1 = 4. Average = 9 ÷ 3 = **3.0**. RR (3.0) beats FCFS (4.0) here.

**Q8: 13096.**
Page = 9000 ÷ 4096 = 2 remainder 808 (2 × 4096 = 8192; 9000 − 8192 = 808). Page 2 is in frame 3. Physical address = 3 × 4096 + 808 = 12288 + 808 = **13096**.

**Q9: B.** A page fault is an access to a page that is not currently in RAM. Most are handled normally; only illegal access ends the program.

**Q10: Model answer.** User mode limits ordinary programs so a faulty or malicious program cannot damage the hardware or other programs' data. Kernel mode gives the OS full control to manage everything safely. Programs request privileged work through system calls. *(Award marks for protection plus the idea of controlled access.)*

**Q11: Errors.** (1) Virtual memory does not add RAM; it is a technique that uses disk space to extend what appears available. (2) It does not make the computer faster. It lets larger programs run, and heavy use can slow things down (thrashing). **Correct statement:** "Virtual memory lets programs use more memory than RAM provides by moving pages between RAM and disk, at the cost of speed when pages must be fetched."

**Q12: A.** Owner `rw-` can write; group `r--` can only read; others `---`.

**Q13: No.** Mia is the **owner**, so only the owner class applies, and it is `---`. The group's read permission is never checked for the owner. (Mia could change the permissions herself as the owner.)

## Group B

**Q14: B.** Knowledge is written by people as rules and facts. A describes machine learning.

**Q15: False.** In symbolic AI people write the rules. Learning rules from large datasets describes **machine learning**.

**Q16: C. Knowledge base.** The inference engine applies rules; working memory stores current facts; the explanation facility shows why.

**Q17: New facts in order: C (R1), D (R2), G (R4). R3 never fires.**
Cycle 1: R1 (A and B true) → C. Cycle 2: R2 (C) → D. Cycle 3: R4 (D and B) → G. R3 needs E, which is not known. Cycle 4: nothing new → stop.

**Q18: Goal G proven.**
G ← R4 needs D and B. D ← R2 needs C. C ← R1 needs A and B. A and B are known facts. Sub-goals in order: D, B, C, A, B. All proven.

**Q19: Model answer.** The **knowledge base** holds the domain rules (what is known); the **inference engine** is the general procedure that applies rules to facts (how to reason). It matters because you can change the topic by changing the knowledge base while keeping the same engine, and because errors in knowledge and errors in reasoning are fixed in different places.

**Q20: Examples (any two with explanation).**
- *Knowledge acquisition bottleneck:* turning an expert's know-how into rules is slow and expensive.
- *Brittleness:* the system fails badly on cases the rules did not anticipate.
- *Maintenance:* with many rules, adding one can interact unexpectedly with others.
- *Uncertainty/common sense:* basic rule systems handle vague or noisy situations poorly.

**Q21: Error.** The rule has an **AND**. It fires only when **both** `memory_full` and `disk_activity_high` are true. Correct statement: "R2 fires only when memory is full **and** disk activity is high."

**Q22: Model answer.** (i) Fraud detection fits **machine learning**: there are millions of examples and subtle patterns that humans could not list as rules. (ii) A fixed refund policy fits **symbolic rules**: the policy is already explicit, and the rule trace gives clear reasons for each decision.

## Group C

**Q23: B.** An expert system is application software that runs as a process on the OS and uses the OS for memory, files and CPU time.

**Q24: Model answer.**
- *Similarity:* both use an IF-THEN style of decision from facts and written policy (for example, "if the user is in the group and group has read, allow").
- *Differences (any two):* the OS check enforces a fixed policy rather than reasoning from knowledge; it usually makes a single check instead of chains of inference; it has no knowledge base built by a knowledge engineer; it cannot explain itself beyond allow or deny.
- *Conclusion:* it is a rule-shaped OS mechanism, not usually classified as AI.

**Q25: Model answer.** (a) The OS can **terminate** the process (the process moves to Terminated and its memory is reclaimed), and its memory management (limits and virtual memory) and scheduler can stop the process from taking over the whole machine, though heavy paging could cause thrashing first. (b) The OS **cannot repair the faulty logic**. The loop is in the rules. Only a person fixing the knowledge base can solve that. *(Award marks for naming at least two of: process termination/states, memory management or paging/thrashing, scheduling.)*

---

## Review status

| Check | Done by | Result |
|---|---|---|
| Calculations (Q6, Q7, Q8, Q17, Q18) recomputed independently | [Teammate name] | [To be completed] |
| Questions match the Main Theory wording and terminology | [Teammate name] | [To be completed] |
| Each question has exactly one defensible answer (for MCQ) | [Teammate name] | [To be completed] |
