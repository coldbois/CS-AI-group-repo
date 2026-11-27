# 1.3 Process and CPU Management

![Dandroid juggling tasks](../../../assets/dandroid/dandroid-excited.png)

**Chapter 1 · Dandroid's Body** · Study Guide pp. 19–24 · Slides 11–12 · Test Bank T3, M3, O1

> **Mission.** Dandroid is playing music, downloading a game and chatting, all with one CPU core. How can one core do three things at once?

**You will learn to**

- tell a program from a process
- follow a process through its 5 states
- compare FCFS and Round Robin scheduling

**Key words:** process, thread, scheduler, time slice, context switch, deadlock

---

## Program vs process

A **program** is a recipe: instructions saved in a file. A **process** is someone actually cooking that recipe. It is the program *while it is running*, with its own memory and its own place in the instructions.

- Open the same app twice and you get **two processes** from one program.
- The OS keeps a record for every process, called the **process control block (PCB)**. It stores the process's state, where it was in the code, and which memory and files it is using.
- A **thread** is a smaller worker inside a process. A media player might use one thread for sound and another for video.

## The life of a process

![Figure 1.3a](../Diagrams%20and%20Pictures/1-3_process-states.png)

*Figure 1.3a. The five states of a process (Study Guide p. 20).*

| State | Meaning |
| --- | --- |
| New | the OS is setting the process up |
| Ready | waiting in line for a turn on the CPU |
| Running | using the CPU right now (only one process per core) |
| Waiting | paused until something happens, such as a file loading or network data arriving (also called *blocked*) |
| Terminated | finished; the OS cleans up its memory |

Example: a download manager asks for network data and goes to **Waiting**. When the data arrives it goes back to **Ready**, not straight to Running, because another process may be using the CPU.

> **Bug alert.** One core does *not* run several programs at the same instant. It switches between them so fast (many times a second) that it *looks* simultaneous. Saving one process's place and loading the next one is called a **context switch**.

## Who goes next? The scheduler

The **scheduler** is the part of the OS that picks which Ready process runs next. We compare two simple methods with the same example used in the Study Guide and on slides 11–12.

Three processes arrive together: **P1 needs 8, P2 needs 2, P3 needs 1** time unit.

- **FCFS (First Come, First Served):** each process runs to the end, in arrival order.
- **Round Robin (RR):** each process gets a short **time slice** (here 2 units), then goes to the back of the line.

![Figure 1.3b](../Diagrams%20and%20Pictures/1-3_fcfs-vs-rr.png)

*Figure 1.3b. FCFS vs Round Robin (Study Guide p. 21).*

### Worked example: average waiting time

Waiting time = finish time − time needed.

| Process | Needs | FCFS finishes | FCFS wait | RR finishes | RR wait |
| --- | --- | --- | --- | --- | --- |
| P1 | 8 | 8 | 0 | 11 | 3 |
| P2 | 2 | 10 | 8 | 4 | 2 |
| P3 | 1 | 11 | 10 | 5 | 4 |
| **Average** | | | **6.0** | | **3.0** |

With FCFS, tiny P3 waits 10 units behind big P1. With Round Robin everyone gets a short turn soon, so short jobs finish quickly and the computer *feels* responsive. That is why desktop systems use time slices.

> **Dandroid's tip.** Round Robin is not always better. If all the jobs are the same length, RR can finish them later than FCFS, and every switch costs a little time. We ignored that cost in the example.

## Deadlock

A **deadlock** happens when processes wait for each other forever. P1 holds the pen and wants the notebook. P2 holds the notebook and wants the pen. Neither lets go, so neither can write. Two common fixes: make one process give up what it holds, or make everyone grab resources in the same order (always the pen first).

## Try it

**Process Musical Chairs** (20 min, 4–5 people): one chair is the CPU, volunteers are processes with clap counts, and you play an FCFS round, a Round Robin round and a deadlock bonus. Instructions and answers: [03_learner-activity.md](../Learner%20Activity/03_learner-activity.md).

## Going further (optional)

- **Shortest Job First (SJF)** always runs the shortest waiting job next. With our example the order is P3, P2, P1, so the finishes are 1, 3 and 11 and the waits are 0, 1 and 3: an average of about 1.3, the lowest possible. The catch is that a real OS rarely knows in advance how long a job will take.
- **Priority scheduling** gives important processes (for example, the one you are typing into) the CPU first. Low-priority jobs can *starve*, so real schedulers slowly raise the priority of jobs that have waited a long time.
- **Four conditions for deadlock** (Coffman, 1971): mutual exclusion, hold and wait, no preemption, circular wait. Break any one and deadlock cannot happen.

## Check yourself

1. What is the difference between a program and a process?
2. A process is waiting for a file to load. Which state is it in?
3. Why does Round Robin make a computer feel more responsive?

**Answers (try first, then peek)**
1. A program is stored instructions; a process is that program running.
2. Waiting (also called blocked).
3. Every process gets a short turn soon, so quick tasks don't wait behind long ones.


More questions: [03_test-bank.md](../Test%20bank%20Question_Answer/03_test-bank.md)

## Remember

- Process = a program in action.
- New → Ready → Running → (Waiting) → Terminated.
- The scheduler shares CPU time; deadlock means stuck waiting on each other.

## Watch and explore

**Little Man Computer** (online CPU simulator by Peter Higginson, peterhigginson.co.uk/lmc). Pick an example program, press STEP, and predict the next value in the accumulator before it appears. It is a simplified teaching CPU, not a real processor.

## References

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Chapters 3 and 5.
- Coffman, E. G., Elphick, M., & Shoshani, A. (1971). System deadlocks. *ACM Computing Surveys, 3*(2), 67–78.

---

Previous: [1.2 Boot Process](../../02_Boot%20Process%20and%20the%20Motherboard/Main%20Theory/02_main-theory.md) · Next: [1.4 Memory Management](../../04_Memory%20Management/Main%20Theory/04_main-theory.md) · Up: [Chapter 1 overview](../../README.md)
