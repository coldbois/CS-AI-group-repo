# Module 09: Where Operating Systems Meet Symbolic AI

**Software Fundamentals · Study Guide content · V2.0 working draft**

| | |
|---|---|
| **Audience** | Complete beginners (no programming or AI background needed) |
| **Estimated study time** | 4 to 5 hours, including the activities |
| **Author** | [Your name] |
| **Reviewer (not the author)** | [Teammate name, to be completed] |
| **Draft date** | 2026-11-03 |

**Files in this module:**
[Main Theory (this file)](09_main-theory.md) ·
[Learner Activities](../Learner%20Activity/09_learner-activities.md) ·
[Test Bank](../Test%20bank%20Question_Answer/09_test-bank.md) ·
[References and AI Usage](../References%20and%20AI%20Usage/09_references-and-ai-usage.md) ·
[Teammate Review](../Teammate_review/09_teammate-review.md) ·
[Content Status and Mapping](../09_content-status-and-mapping.md)

---

## 1. Module Overview

A computer is useful only when two things work together: **hardware** that does the work, and **software** that tells it what to do. In this module you will meet two kinds of software that look very different but share an interesting connection.

- The **operating system (OS)** is the manager of the computer. It decides which program runs, where programs keep their data, and what each user is allowed to touch.
- **Symbolic AI** is an approach to artificial intelligence in which people write down knowledge as readable **facts** and **rules**, and the computer reasons with them step by step.

**Why study them together?** Every AI program, including a symbolic one, is just a program, so it runs *on* an operating system and depends on it for CPU time, memory and files. Also, both fields manage complexity with explicit, inspectable rules. Seeing both side by side helps you understand what an OS really does and what "AI" really means.

**How the module is organised**

| Part | Big question | Sections | Practise with |
|---|---|---|---|
| **A. Operating systems** | What does the manager of a computer actually do? | 4 to 9 | Activities 1 to 5 |
| **B. Symbolic AI** | How can a computer reason using written-down rules? | 10 to 13 | Activities 6 to 7 |
| **C. Where they meet** | How are the two connected, and how are they different? | 14 to 15 | Activities 8 to 9 |

**Prerequisite words.** If you are new to computers, read this first. We use a kitchen analogy throughout.

| Word | Meaning | Kitchen analogy |
|---|---|---|
| **Hardware** | The physical parts of a computer | The kitchen itself: stove, counter, fridge |
| **Software** | Instructions that tell hardware what to do | Recipes |
| **CPU** | The part that carries out instructions, one tiny step at a time | The chef |
| **RAM (memory)** | Fast, temporary workspace; emptied when power is off | The counter where you work |
| **Storage (disk)** | Slower, permanent space for files | The pantry |
| **Program** | A set of instructions stored as a file | A recipe in a book |
| **I/O (input/output)** | Moving data in or out, for example reading a file or printing to a screen | Fetching from the pantry or serving a dish |

---

## 2. Learning Outcomes

By the end of this module you should be able to:

| # | Outcome | Sections |
|---|---|---|
| **LO1** | Explain what an operating system is and why computers need one | 4 |
| **LO2** | Describe the kernel, user mode vs kernel mode, and trace a system call | 5 |
| **LO3** | Distinguish a program, a process and a thread, and trace a process through its states | 6 |
| **LO4** | Calculate and compare waiting, turnaround and response times for FCFS and Round Robin scheduling | 7 |
| **LO5** | Explain paging and virtual memory, and translate a virtual address to a physical address | 8 |
| **LO6** | Decode file permissions and explain how the OS makes an access decision | 9 |
| **LO7** | Explain what symbolic AI is and how it differs from machine learning | 10 |
| **LO8** | Write simple facts and rules, and trace forward and backward chaining | 11, 12 |
| **LO9** | Describe the parts and limits of an expert system | 13 |
| **LO10** | Explain at least three connections between operating systems and symbolic AI, and avoid the mistake of calling an OS "AI" | 14, 15 |

---

# PART A: OPERATING SYSTEMS

## 3. How Part A is built

Sections 4 to 9 move from the big picture down to details: what an OS is (4), how programs ask it for help (5), how it runs many programs at once (6 and 7), how it shares memory (8), and how it protects files (9).

---

## 4. What Is an Operating System?

### 4.1 The problem

Imagine every program had to control the screen, the keyboard, the disk and the network by itself. Each programmer would rewrite the same difficult code, and two programs using the same disk at the same time would corrupt each other's data.

### 4.2 The solution

> **An operating system (OS)** is system software that manages the computer's hardware and provides common services so that application programs can run safely and share resources.

**Analogy: a restaurant manager.**

| Restaurant | Computer |
|---|---|
| Customers place orders | Programs request services |
| The manager decides who is served first | The OS schedules programs on the CPU |
| The manager assigns tables | The OS assigns memory |
| The kitchen staff do the cooking | The hardware does the work |
| House rules (no entering the kitchen) | Permissions and protection |

![Figure 1: Where the operating system sits. Layers from top to bottom are the user, application software, the operating system with process management, memory management, file system and device drivers, and finally the hardware.](../Diagrams%20and%20Pictures/09_fig1_os-layers.svg)

*Figure 1. The OS sits between application software and hardware. Applications ask it for services through system calls (Section 5).*

### 4.3 The OS's main jobs

| Job | Plain-English meaning | Section |
|---|---|---|
| **Process management** | Start, run, pause and stop programs; share the CPU | 6, 7 |
| **Memory management** | Give each program its own memory and keep them apart | 8 |
| **File management** | Organise data into files and folders on disk | 9 |
| **Device management** | Control keyboards, screens, printers and so on through **device drivers** | 5 |
| **Security and protection** | Decide who may do what | 9 |

Examples of operating systems: Windows, macOS, Linux, Android, iOS.

> **Common misunderstanding: "The OS is the desktop with the windows and icons."**
> The graphical interface (GUI) is only one part. Most of what the OS does, such as scheduling and memory management, is invisible.

**▶ Apply it:** Activity 8 (choosing between an OS mechanism and AI) uses this section.

---

## 5. Kernel, Modes and System Calls

### 5.1 Kernel

The **kernel** is the core of the OS. It always stays in memory and has complete control of the hardware.

### 5.2 User mode and kernel mode

The CPU can run in two **modes**:

| Mode | Who runs here | What is allowed |
|---|---|---|
| **User mode** | Ordinary applications | Limited: cannot touch hardware or other programs' memory directly |
| **Kernel mode** | The kernel | Everything, including hardware control |

**Why two modes?** Protection. If an ordinary application could do anything, a single buggy program could crash the whole computer or read another user's data.

### 5.3 System calls

A **system call** is a request from a program to the kernel for a service it is not allowed to do itself, such as reading a file or writing to the screen.

**Analogy:** In a restaurant, you (the program) cannot walk into the kitchen. You tell the waiter (the system call interface), and the kitchen (kernel) prepares the dish.

Common system call categories:

| Category | Examples of what the program asks for |
|---|---|
| Process control | Start a new process, end this process |
| File management | Open, read, write, close a file |
| Device management | Read from the keyboard, write to the screen |
| Information | Ask for the current time or process ID |
| Communication | Send data to another process |

### 5.4 Worked example 1: what happens when a program prints "Hello"?

```python
print("Hello")
```

1. Your program calls `print`.
2. The language's library prepares the text and asks the OS to write it to **standard output** (normally the screen or terminal).
3. A **system call** is made. On Linux this system call is named `write`; Windows uses a different, similar one. The CPU switches from **user mode** to **kernel mode**.
4. The kernel checks the request: is the output open, and is this process allowed to use it?
5. The kernel passes the text to the relevant **device driver**, which talks to the hardware.
6. The text appears. The kernel returns a result to the program, the CPU switches back to **user mode**, and your program continues with the next line.

**Key lesson:** The program never touched the screen. It *asked*, and the kernel did the privileged work.

**▶ Apply it:** Activity 1 (put the steps of saving a file in order).

---

## 6. Programs, Processes and Threads

### 6.1 Program vs process

| | Program | Process |
|---|---|---|
| What is it? | A file of instructions, sitting on disk | A program **being run**, with its own memory and state |
| Analogy | A recipe in a book | Someone actually cooking from the recipe |
| Can there be many? | One program file | Many processes can come from one program (open two browser windows) |

> **Common misunderstanding: "A program and a process are the same thing."**
> The recipe is not the cooking. Starting the same program twice creates two separate processes.

### 6.2 What the OS keeps about each process

The OS keeps a record called a **process control block (PCB)**. It holds the process ID, current state, where the process is in its instructions (the **program counter**), saved CPU register values, memory information, and a list of open files.

### 6.3 Process states

A process changes **state** during its life.

![Figure 2: Process states. New moves to Ready when admitted. Ready moves to Running when the scheduler picks it. Running returns to Ready when its time slice ends, moves to Waiting when it needs I/O, or moves to Terminated when it finishes. Waiting moves to Ready when the I/O finishes.](../Diagrams%20and%20Pictures/09_fig2_process-states.svg)

*Figure 2. Process states and the events that cause each change.*

| State | Meaning |
|---|---|
| **New** | The OS is creating the process |
| **Ready** | Prepared to run and waiting for the CPU |
| **Running** | Currently using the CPU |
| **Waiting** (blocked) | Cannot continue until something happens, such as a disk read finishing |
| **Terminated** | Finished; the OS reclaims its resources |

### 6.4 Worked example 2: one process's life

A text editor is opened, loads a file, and is closed.

| Step | Event | State change |
|---|---|---|
| 1 | You double-click the editor; the OS starts creating the process | **New** |
| 2 | Setup (memory and PCB) is finished | New → **Ready** |
| 3 | The scheduler gives it the CPU | Ready → **Running** |
| 4 | The editor asks to load your file from disk (slow I/O); the CPU is given to another process | Running → **Waiting** |
| 5 | The disk finishes | Waiting → **Ready** (not straight to Running) |
| 6 | The scheduler picks it again | Ready → **Running** |
| 7 | Its time slice ends while it still has work | Running → **Ready** |
| 8 | You choose Quit | Running → **Terminated** |

**Why does Waiting go to Ready and not straight to Running?** The scheduler decides who runs. Other processes may already be in line.

### 6.5 Threads

A **thread** is a smaller unit of execution *inside* a process. Threads of one process **share** the process's memory but each has its own position in the instructions.

**Analogy:** One kitchen (process) with several cooks (threads) sharing the same pantry, each working on a different dish.

**Example:** A word processor may use one thread for your typing, one for spell-checking and one for auto-save, so typing never freezes while auto-save writes to disk.

**▶ Apply it:** Activity 2 (predict state changes; find the error).

---

## 7. CPU Scheduling and Multitasking

### 7.1 The problem

There are usually more ready processes than CPU cores. The **scheduler** is the part of the OS that chooses which Ready process runs next. By switching very quickly, the OS creates the feeling that many programs run at once. This is **multitasking**.

> **Common misunderstanding: "A one-core CPU runs several programs at the same instant."**
> It runs *one* at a time and switches so fast it looks simultaneous. Truly simultaneous work needs several cores.

### 7.2 Measuring a schedule

All times below assume every process arrives at time 0 and uses only the CPU (no I/O), and we ignore the small cost of switching.

| Term | Meaning | How to compute |
|---|---|---|
| **Burst time** | CPU time the process needs in total | Given |
| **Completion time** | When the process finishes | From the timeline |
| **Turnaround time** | Total time from arrival to finishing | Completion − arrival |
| **Waiting time** | Time spent Ready but not Running | Turnaround − burst |
| **Response time** | Time until the process first gets the CPU | First start − arrival |

### 7.3 Two simple algorithms

- **First-Come, First-Served (FCFS):** processes run to completion in arrival order. Simple, but one long job makes everyone behind it wait (the **convoy effect**).
- **Round Robin (RR):** each process runs for at most one **time slice (quantum)**, then goes to the back of the Ready queue. This is fairer and keeps programs responsive.

### 7.4 Worked example 3: FCFS vs Round Robin

Three processes arrive at time 0 in the order P1, P2, P3, with burst times **P1 = 8, P2 = 2, P3 = 1**. Round Robin uses a time slice of **2**.

**FCFS timeline**

| Time | 0 to 8 | 8 to 10 | 10 to 11 |
|---|---|---|---|
| Running | P1 | P2 | P3 |

- Completion: P1 = 8, P2 = 10, P3 = 11
- Waiting (completion − burst): P1 = 0, P2 = 8, P3 = 10 → average = 18 ÷ 3 = **6.0**
- Response: P1 = 0, P2 = 8, P3 = 10 → average = **6.0**
- Turnaround: 8, 10, 11 → average = 29 ÷ 3 ≈ **9.67**

**Round Robin (slice = 2) timeline**

| Time | 0 to 2 | 2 to 4 | 4 to 5 | 5 to 7 | 7 to 9 | 9 to 11 |
|---|---|---|---|---|---|---|
| Running | P1 | P2 | P3 | P1 | P1 | P1 |
| Left to do afterwards | P1: 6 | P2: 0 | P3: 0 | P1: 4 | P1: 2 | P1: 0 |

(P2 needs exactly 2, so it finishes in its first slice. P3 needs only 1, so it finishes early and its slice ends at 5. P1 then runs alone, still in slices of 2.)

- Completion: P2 = 4, P3 = 5, P1 = 11
- Waiting: P1 = 11 − 8 = 3, P2 = 4 − 2 = 2, P3 = 5 − 1 = 4 → average = 9 ÷ 3 = **3.0**
- Response: P1 = 0, P2 = 2, P3 = 4 → average = **2.0**
- Turnaround: 11, 4, 5 → average = 20 ÷ 3 ≈ **6.67**

**Comparison**

| Measure (average) | FCFS | Round Robin |
|---|---|---|
| Waiting time | 6.0 | 3.0 |
| Response time | 6.0 | 2.0 |
| Turnaround time | 9.67 | 6.67 |

**What happened?** In FCFS the short jobs P2 and P3 were stuck behind the long job P1. RR let them finish early.

### 7.5 Trade-offs and cautions

- **Switching has a cost.** Each switch between processes (a **context switch**) takes time, so a very small time slice wastes effort. A very large slice behaves like FCFS. Choosing the slice is a design decision.
- **RR is not always better.** If all jobs are the same length, RR can give *worse* average turnaround than FCFS (see Activity 3, part c).
- **Priorities.** Real schedulers often favour some processes, for example interactive programs over background jobs. Notice that "IF the process is interactive THEN give it higher priority" is written like a rule. We return to this in Section 14.

**▶ Apply it:** Activity 3 (calculate and compare a new schedule).

---

## 8. Memory Management and Virtual Memory

### 8.1 The problem

RAM is limited and shared by many processes. The OS must (a) give each process room, (b) stop one process reading another's data, and (c) cope when programs need more memory than RAM can hold.

### 8.2 Virtual and physical addresses

- A **physical address** is a real location in RAM.
- A **virtual address** is the address the *program* uses. Each process sees its own private, tidy address space starting at 0.

The OS and hardware translate virtual addresses to physical ones, so processes cannot accidentally overwrite each other.

### 8.3 Paging

Memory is divided into equal-sized blocks:

- **Pages** are blocks of *virtual* memory.
- **Frames** are blocks of *physical* memory, the same size as a page.
- A **page table** records which frame holds each page.

A common page size is **4096 bytes (4 KB)**. A virtual address is split into:

```
page number = virtual address ÷ 4096   (whole-number part)
offset      = virtual address mod 4096 (the remainder)
physical address = (frame number × 4096) + offset
```

### 8.4 Worked example 4: translating an address

Page size = 4096. Page table of one process:

| Page | Frame |
|---|---|
| 0 | 5 |
| 1 | 2 |
| 2 | 7 |

**Translate virtual address 8200.**

1. Page number: 8200 ÷ 4096 = 2 remainder 8 (because 2 × 4096 = 8192 and 8200 − 8192 = 8). So page = **2**, offset = **8**.
2. Look up the page table: page 2 is in frame **7**.
3. Physical address = 7 × 4096 + 8 = 28672 + 8 = **28680**.

### 8.5 Virtual memory and page faults

A page that is not currently in RAM is marked "not present". When a program touches it, a **page fault** occurs:

1. The hardware alerts the OS.
2. The OS checks the access is legal. If not, the process is stopped with an error (often called a segmentation fault).
3. If legal, the OS finds the page on disk.
4. It loads the page into a free frame (making room by moving another page out if needed).
5. It updates the page table and restarts the instruction.

This lets a computer run programs larger than its RAM. This idea is called **virtual memory**.

**Thrashing.** If too many processes need more pages than fit in RAM, the OS spends most of its time moving pages between disk and RAM and little time doing real work. The computer becomes very slow and the disk light stays on. This is **thrashing**. (You will meet it again in the expert system example in Section 12.)

> **Common misunderstandings**
> - *"Virtual memory is an extra RAM chip."* No. It is a technique that uses disk space to extend what appears available.
> - *"A page fault is a crash."* No. Most page faults are normal and handled silently. Only an *illegal* access stops the program.

**▶ Apply it:** Activity 4 (translate addresses and predict page faults).

---

## 9. Files, Devices and Permissions

### 9.1 Files and devices

- A **file system** organises storage into named files and folders and tracks where each file's data physically lives.
- A **device driver** is software that lets the kernel control one specific piece of hardware, so applications do not need to know hardware details.

### 9.2 Permissions

The OS must decide whether a process, acting for a user, may read, write or run a file. On Linux and macOS each file has an **owner**, a **group**, and three sets of **permission bits**.

Example: `-rwxr-x---`

| Characters | Meaning |
|---|---|
| `-` (first) | File type: `-` is an ordinary file, `d` is a directory |
| `rwx` | **Owner** may read (r), write (w) and execute/run (x) |
| `r-x` | **Group** members may read and execute, not write |
| `---` | **Everyone else** has no access |

**Important rule:** The OS checks the *first matching class*: owner first, then group, then others. Only that one class's permissions apply.

### 9.3 Worked example 5: decoding permissions

File `report.sh` has permissions `-rwxr-x---`, owner **alex**, group **staff**. User **sam** is in group staff but is not the owner.

- Which class does sam fall into? Not owner, but in the group → **group** (`r-x`).
- Can sam read it? Yes (`r`). Can sam change it? No (`-` in the w place). Can sam run it? Yes (`x`).
- User **kim** is neither the owner nor in staff → **others** (`---`) → no access at all.

**Why this matters later:** a permission check is a decision made from facts ("who is the user, who owns the file") and a written policy. Keep this in mind for Part C.

**▶ Apply it:** Activity 5 (decode permissions, including a tricky case).

---

## Quick Check: Part A

1. Name two things an OS does that you cannot see.
   *Answer: for example, scheduling processes and managing memory (also file protection and driver control).*
2. A process finishes reading a file from disk. What state does it move to next?
   *Answer: from Waiting to Ready.*
3. Page size is 4096. Which page and offset does virtual address 4100 have?
   *Answer: page 1, offset 4 (4100 − 4096 = 4).*

---

# PART B: SYMBOLIC AI

## 10. What Is Symbolic AI?

### 10.1 Artificial intelligence in one sentence

**Artificial intelligence (AI)** is the field of making computers perform tasks that normally need human intelligence, such as diagnosing problems, understanding language or recognising images.

There is more than one way to do this. Two main families are:

- **Symbolic AI**: humans write down knowledge as **symbols** (readable labels such as `memory_full`) and **rules**, and the computer **reasons** by manipulating them.
- **Machine learning (ML)**: the computer is given many examples and **finds patterns itself** instead of being given rules.

A **symbol** here simply means a meaningful label a human can read, such as a word or a logical statement.

Symbolic AI is sometimes called **GOFAI** ("good old-fashioned AI"), a name coined by the philosopher John Haugeland. Many early AI systems (1950s to 1980s) were symbolic. A famous idea behind it is the **physical symbol system hypothesis** (Newell and Simon, 1976): that manipulating symbols is enough for general intelligent action. It is a *hypothesis* and researchers still debate it.

### 10.2 Worked example 6: two ways to filter spam

| | Symbolic (rule-based) | Machine learning |
|---|---|---|
| How it works | A human writes `IF subject contains "free money" THEN mark as spam` | The program studies thousands of emails labelled "spam" or "not spam" and finds its own patterns |
| Where knowledge comes from | Human experts | Data |
| Can you read why it decided? | Yes: point to the rule | Often hard to say |
| Weakness | Spammers change wording; humans must keep adding rules | Needs lots of labelled data; mistakes can be hard to explain |

### 10.3 Comparison summary

| | Symbolic AI | Machine learning |
|---|---|---|
| Knowledge comes from | Human-written rules and facts | Patterns learned from data |
| Explainable? | Usually yes | Often difficult |
| Handles messy, noisy input? | Poorly | Well |
| Needs a lot of data? | No | Usually yes |

> **Common misunderstandings**
> - *"Symbolic AI learns from data."* No, that is machine learning. In classic symbolic AI the knowledge is written by people.
> - *"Symbolic AI is fake or obsolete."* It is a different approach with real strengths (clear explanations, precise logic). Many systems today still use rules, sometimes combined with machine learning.

---

## 11. Representing Knowledge: Facts and Rules

### 11.1 Facts

A **fact** is a statement that is true in the current situation: `memory_full`, `disk_activity_high`, `owner(report.sh, alex)`.

### 11.2 Rules

A **rule** has the form:

```
IF  <condition 1> AND <condition 2> ...
THEN <conclusion>
```

- The IF part is the **condition** (also called the premise or antecedent).
- The THEN part is the **conclusion** (consequent or action).
- A rule can use **AND** (all must be true), **OR** (at least one true) and **NOT** (must be false).

| A | B | A AND B | A OR B | NOT A |
|---|---|---|---|---|
| true | true | true | true | false |
| true | false | false | true | false |
| false | true | false | true | true |
| false | false | false | false | true |

### 11.3 Worked example 7: turning English into a rule

English policy: *"A user who is not the file's owner, but is in the file's group, can read the file if the group has read permission."*

**Step 1:** Identify the conditions: not the owner; in the group; group has read permission.
**Step 2:** Identify the conclusion: the user can read the file.
**Step 3:** Write the rule:

```
IF  NOT owner(user, file)
AND in_group(user, file)
AND group_read(file)
THEN can_read(user, file)
```

**Why `NOT owner`?** Because (Section 9) the OS checks the owner class first and applies only the first matching class. The rule must say so, or it would give the wrong answer for owners whose own bits say "no".

**▶ Apply it:** Activity 6, part (a).

---

## 12. Inference: Forward and Backward Chaining

**Inference** means deriving new facts from known facts using rules. The part of the system that does this is the **inference engine**. Facts live in **working memory**. When all the conditions of a rule are true, the rule **fires** and its conclusion is added to working memory as a new fact.

### 12.1 A rule base to reason with

A small "Why is my computer slow?" rule base:

| Rule | Definition |
|---|---|
| **R1** | IF `cpu_usage_high` AND `one_process_uses_most_cpu` THEN `suspect_runaway_process` |
| **R2** | IF `memory_full` AND `disk_activity_high` THEN `suspect_thrashing` |
| **R3** | IF `suspect_thrashing` THEN `recommend_close_programs_or_add_ram` |
| **R4** | IF `suspect_runaway_process` THEN `recommend_end_that_process` |
| **R5** | IF `cpu_usage_low` AND `memory_not_full` AND `disk_activity_low` THEN `suspect_network_problem` |

### 12.2 Forward chaining (data-driven)

**Idea:** Start from the known facts and work forwards to see what follows.

**Algorithm:**
1. Compare every rule's conditions with the facts in working memory.
2. Fire a rule whose conditions are **all** true and whose conclusion is not yet known; add the conclusion as a new fact.
3. Repeat from step 1. Stop when no rule can add anything new.

If several rules are ready at once, **conflict resolution** picks the order (for example, first in the list, or the most specific rule).

### 12.3 Worked example 8: forward chaining

**Known facts:** `memory_full`, `disk_activity_high`, `cpu_usage_high`

![Figure 5: Forward chaining. The facts memory_full and disk_activity_high make rule R2 fire and add suspect_thrashing. Rule R3 then fires and adds the recommendation. The fact cpu_usage_high is known but R1 does not fire because one_process_uses_most_cpu is not known.](../Diagrams%20and%20Pictures/09_fig5_forward-chaining-trace.svg)

*Figure 5. Forward chaining trace for the example below.*

| Cycle | Rules checked | What happens | Working memory afterwards |
|---|---|---|---|
| 1 | R1: needs `one_process_uses_most_cpu`, not known → **no**. R2: both conditions true → **yes**. | **R2 fires**, adds `suspect_thrashing` | memory_full, disk_activity_high, cpu_usage_high, **suspect_thrashing** |
| 2 | R3: `suspect_thrashing` is now known → **yes** | **R3 fires**, adds the recommendation | …, **recommend_close_programs_or_add_ram** |
| 3 | No rule can add anything new | **Stop** | final result: close programs or add RAM |

**Notice:** R1 was *partly* matched (`cpu_usage_high` was true) but did not fire because AND needs **all** conditions. Also, R3 could only fire *after* R2 created its fact. That is a **chain** of reasoning.

### 12.4 Backward chaining (goal-driven)

**Idea:** Start from a **goal** and work backwards: "What would have to be true for this goal?"

**Algorithm:**
1. Find rules whose conclusion matches the goal.
2. Treat that rule's conditions as new sub-goals.
3. A sub-goal is proven if it is a known fact or can itself be proven by another rule. If a needed fact is unknown, the system can **ask the user**.

### 12.5 Worked example 9: backward chaining

**Goal:** `recommend_close_programs_or_add_ram`

1. Which rule concludes this goal? **R3**. Sub-goal: `suspect_thrashing`.
2. Which rule concludes `suspect_thrashing`? **R2**. Sub-goals: `memory_full` and `disk_activity_high`.
3. Are they facts? Yes, both are in working memory.
4. All sub-goals proven → **goal proven**.

### 12.6 Which to use?

| | Forward chaining | Backward chaining |
|---|---|---|
| Starts from | Known facts | A goal or question |
| Good for | Monitoring, configuring, "what follows from this data?" | Diagnosis and question-answering; asks only for facts it needs |
| Analogy | Following clues to see where they lead | A detective testing "if the butler did it, what must be true?" |

> **Common mistakes**
> - A rule fires only when **all** AND-conditions are true.
> - The inference engine does not contain medical, computing or other knowledge. The **rules** hold the knowledge; the engine just applies them.
> - Rules can feed each other: one rule's conclusion can be another rule's condition.

**▶ Apply it:** Activities 6 and 7.

---

## 13. Expert Systems

### 13.1 What is an expert system?

An **expert system** is a symbolic AI program that captures the knowledge of a human expert as rules and uses it to give advice or make decisions in a narrow area.

![Figure 3: Expert system architecture. The user talks to a user interface. The inference engine reads rules from the knowledge base and facts from working memory, adds new facts, and gives a rule trace to the explanation facility.](../Diagrams%20and%20Pictures/09_fig3_expert-system-architecture.svg)

*Figure 3. Parts of an expert system.*

| Part | Role |
|---|---|
| **Knowledge base** | The stored domain rules (and any fixed facts), written by people |
| **Working memory** | Facts about the current case, including facts derived so far |
| **Inference engine** | Applies rules to facts (forward or backward chaining) |
| **User interface** | Asks questions and shows results |
| **Explanation facility** | Shows *why* a conclusion was reached |

The person who turns an expert's know-how into rules is the **knowledge engineer**.

### 13.2 Real examples

- **MYCIN** (Stanford University, 1970s) advised doctors on diagnosing certain bacterial infections and choosing antibiotics using several hundred rules, and it attached **certainty factors** to conclusions to handle uncertainty. It was a research system that was tested well but never adopted for routine clinical use.
- **XCON** (also called **R1**; developed by John McDermott for Digital Equipment Corporation, early 1980s) checked customers' orders for VAX computer systems and decided which components and cables were needed. It grew to thousands of rules and is a classic example of an expert system used in a real business. Notice that it is a rule-based program about *configuring computers*, a first link between our two topics.

### 13.3 Worked example 10: where the explanation comes from

Using the trace from Section 12.3, the system can answer "Why do you recommend closing programs or adding RAM?" simply by replaying the rules that fired:

> *Because R3: `suspect_thrashing` was true. That was concluded by R2 because `memory_full` and `disk_activity_high` were both true.*

The explanation is not extra magic. It is the **rule trace**.

### 13.4 Strengths and limits

| Strengths | Limits |
|---|---|
| Decisions can be explained rule by rule | **Knowledge acquisition bottleneck:** getting expert knowledge into rules is slow and costly |
| Consistent and available at any time | **Brittleness:** it can fail badly on situations its rules did not anticipate |
| Good for narrow, well-defined problems | **Maintenance:** with thousands of rules, adding one can unexpectedly interact with others |
| Does not need large datasets | Poor with uncertainty, noise and common sense (needs extra techniques) |

**▶ Apply it:** Activity 7 (find the errors in a rule base) and Activity 9 (design your own).

---

## Quick Check: Part B

1. Which family of AI relies on human-written rules: symbolic AI or machine learning?
   *Answer: symbolic AI.*
2. In Section 12.1, suppose the only known facts are `cpu_usage_high` and `one_process_uses_most_cpu`. Which conclusion is reached, and which recommendation?
   *Answer: R1 fires → `suspect_runaway_process`; R4 then fires → `recommend_end_that_process`.*
3. Name the part of an expert system that holds the rules and the part that applies them.
   *Answer: knowledge base holds them; inference engine applies them.*

---

# PART C: WHERE THEY MEET

![Figure 4: Where operating systems and symbolic AI meet. Operating systems on the left, symbolic AI on the right. The overlap contains rule-based decisions and AI programs running as OS processes.](../Diagrams%20and%20Pictures/09_fig4_os-and-symbolic-ai-overlap.svg)

*Figure 4. Two different fields with real connection points.*

## 14. Four Connections

### 14.1 Connection 1: An AI program is a process

An expert system is a program, so when you run it the OS treats it like any other program.

| OS service (Part A) | What the expert system needs from it |
|---|---|
| File system | Loads its rule file from disk |
| Memory management | Keeps working memory in RAM; too much data can cause paging or thrashing |
| Scheduling | Gets CPU time to match rules |
| Device drivers / system calls | Prints its answer; reads the user's reply |
| Process termination | If a faulty rule set loops forever, the OS can end the process, but it cannot fix the faulty logic |

**Worked example 11: one run of a "SlowPC Doctor" expert system, double-click to answer**

1. You double-click it → the OS creates a process: **New → Ready → Running** (Section 6).
2. It needs its rules → a **system call** reads `rules.txt` from disk; the process goes **Waiting** during the slow disk read, then **Ready**, then **Running** again.
3. The rules go into **RAM** (pages in frames, Section 8). Working memory starts empty.
4. It asks you questions (system calls to read the keyboard and write the screen) and stores your answers as facts.
5. The **inference engine** runs forward chaining (Section 12): R2 fires, then R3.
6. It prints the recommendation (a `write` system call, Section 5.4).
7. You close it → the process is **Terminated** and the OS reclaims its memory.

### 14.2 Connection 2: Rule-shaped decisions inside the OS

An OS also contains rule-like logic: file permission checks (Section 9), firewall rules, and scheduler priorities ("IF interactive THEN higher priority"). They share the **IF-THEN shape** with symbolic AI rules, but they are different in purpose.

| | OS policy rules | Symbolic AI rule base |
|---|---|---|
| Main purpose | Enforce a fixed policy: allow, deny, or order work | Reason from knowledge to reach new conclusions |
| Typical result | A decision (allow/deny, which process next) | A conclusion or recommendation, often with explanation |
| Chaining | Usually one check or a fixed procedure | Rules feed each other (chains of inference) |
| Knowledge source | Policy set by designers or administrators | Expert knowledge captured by a knowledge engineer |
| Explains itself? | Usually just "denied" or a log entry | Can show which rules fired |
| Usually called AI? | No | Yes |

> **Common misunderstanding: "The OS scheduler is AI."**
> A scheduler follows a fixed algorithm. Similar *form* (IF-THEN) is not the same as the same *field*. A permission check looks things up; it does not build a knowledge base or reason in chains.

### 14.3 Connection 3: AI used on computers themselves

Symbolic AI has been applied to running and fixing computer systems. XCON configured computer orders (Section 13.2). Our "slow computer" rule base (Section 12) is a small diagnosis example, and the same idea sits behind many help-desk troubleshooting guides.

### 14.4 Connection 4: A historical meeting point

Because early symbolic AI was often written in the language **Lisp**, companies in the late 1970s and 1980s built **Lisp machines**: computers designed to run Lisp efficiently, with software environments built around it. They faded commercially as ordinary workstations and PCs became fast and cheap enough to run the same software.

### 14.5 Today (overview)

Machine learning now dominates much of AI, but modern AI systems still run on operating systems and rely on them for memory, scheduling and hardware drivers. Rule-based and logic-based ideas also remain in business rule engines, knowledge graphs and software verification, and researchers explore combining learning with symbols ("neuro-symbolic" AI). *This subsection is an overview, not core exam content.*

**▶ Apply it:** Activity 8 (choose the right tool and justify) and Activity 9 (design a mini expert system).

---

## 15. Common Misconceptions: Summary Table

| # | Misconception | Correct idea | Section |
|---|---|---|---|
| 1 | "The OS is the desktop and windows." | The GUI is one part; most OS work is invisible. | 4 |
| 2 | "A program and a process are the same." | A process is a program *being run*; one program can be many processes. | 6 |
| 3 | "A one-core CPU runs many programs at the same instant." | It runs one at a time and switches quickly. | 7 |
| 4 | "Round Robin is always better than FCFS." | It depends on job lengths and switching costs. | 7 |
| 5 | "Virtual memory is extra RAM hardware." | It is a technique using disk to extend memory. | 8 |
| 6 | "A page fault is a crash." | Most are normal; only illegal access stops the program. | 8 |
| 7 | "The OS scheduler is AI." | It follows a fixed algorithm; IF-THEN shape alone does not make it AI. | 14 |
| 8 | "Symbolic AI learns from data." | That describes machine learning. | 10 |
| 9 | "Symbolic AI is obsolete or fake." | It is a different approach with real strengths, still used. | 10 |
| 10 | "The inference engine contains the knowledge." | The knowledge base holds the knowledge; the engine applies it. | 12, 13 |
| 11 | "If every rule is correct, the system is always right." | Missing rules and unexpected cases cause failures (brittleness). | 13 |

---

## Summary

- The **OS** manages hardware and shares it safely among programs through **processes**, **scheduling**, **virtual memory**, **file systems** and **permissions**. Programs ask for services through **system calls**.
- **Symbolic AI** represents knowledge as readable **facts** and **rules** and reasons with an **inference engine** (forward or backward chaining). **Expert systems** package this for a narrow domain and can **explain** themselves, but they are **brittle** and costly to build.
- The two meet because AI programs **run as OS processes**, because both use **explicit rules**, because AI has been used to **configure and diagnose computers** (XCON), and because of history (**Lisp machines**). They are **different fields**: an OS is not an AI.

---

## Glossary (terms used consistently in this module)

| Term | Meaning |
|---|---|
| **Operating system (OS)** | System software that manages hardware and services for programs |
| **Kernel** | Core of the OS with full hardware control |
| **User mode / Kernel mode** | Restricted CPU mode for applications / unrestricted mode for the kernel |
| **System call** | A program's request for a kernel service |
| **Device driver** | Software that lets the kernel control specific hardware |
| **Program** | Instructions stored in a file |
| **Process** | A program being run, with its own memory and state |
| **Thread** | A unit of execution inside a process; threads share the process's memory |
| **Process control block (PCB)** | The OS's record of a process |
| **Process states** | New, Ready, Running, Waiting, Terminated |
| **Scheduler** | OS part that chooses which Ready process runs next |
| **Burst time** | Total CPU time a process needs |
| **Waiting time** | Time spent Ready but not Running |
| **Turnaround time** | Completion time − arrival time |
| **Response time** | Time until a process first gets the CPU |
| **Time slice (quantum)** | Maximum CPU time per turn in Round Robin |
| **Context switch** | Switching the CPU from one process to another |
| **FCFS / Round Robin** | Scheduling by arrival order / in rotating time slices |
| **Virtual / physical address** | Address a program uses / real location in RAM |
| **Page / frame / page table** | Block of virtual memory / block of RAM / table mapping pages to frames |
| **Page fault** | Access to a page not currently in RAM |
| **Virtual memory** | Technique that uses disk to extend available memory |
| **Thrashing** | Constant paging that leaves little time for real work |
| **Permission bits** | r, w, x settings for owner, group and others |
| **Symbolic AI** | AI that reasons with human-readable symbols and rules |
| **Machine learning** | AI that finds patterns from data |
| **Fact / Rule** | A statement true now / an IF-THEN statement |
| **Knowledge base** | Stored rules (and fixed facts) of an expert system |
| **Working memory** | Facts about the current case |
| **Inference engine** | Part that applies rules to facts |
| **Rule firing** | Using a rule whose conditions are all true to add its conclusion |
| **Forward / backward chaining** | Reasoning from facts to conclusions / from a goal back to facts |
| **Conflict resolution** | Choosing which rule fires when several are ready |
| **Expert system** | Symbolic AI program capturing expert knowledge for a narrow domain |
| **Explanation facility** | Part that shows which rules led to a conclusion |
| **Brittleness** | Failing badly outside the situations its rules cover |

---

## Scope Note and Honest Gaps

**Covered (core):** everything above.
**Not covered in this version (optional extensions):**
- Search and planning in symbolic AI (for example, state-space search)
- Deadlocks, file system internals and multicore scheduling details in operating systems
- The details of machine learning

These are labelled extensions, and they are recorded with next steps in the [Content Status and Mapping](../09_content-status-and-mapping.md) file.

**Where to practise:** [Learner Activities](../Learner%20Activity/09_learner-activities.md) (with answers) and the [Test Bank](../Test%20bank%20Question_Answer/09_test-bank.md).

**References:** see [References and AI Usage](../References%20and%20AI%20Usage/09_references-and-ai-usage.md). All diagrams (Figures 1 to 5) are original drawings made for this module.
