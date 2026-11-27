# 1.3 Test Bank: Process and CPU Management

T3, M3 and O1 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T3 (True or False).** If you open the same app twice, you get two processes.

**M3 (choose ONE).** Round Robin scheduling gives each process...

- A. a turn only if it is the biggest
- B. one long turn until it finishes
- C. a short turn, then the next process goes
- D. no turns at all

**O1. Fair turns for P3?** (about 100 words, 5 marks)

One chair is the CPU. Three processes take turns: P1 claps 16 times, P2 claps 4 times, P3 claps 2 times. FCFS finishes: P1 16, P2 20, P3 22. Round Robin finishes: P1 22, P2 8, P3 10.

(1) In which round did little P3 finish sooner? (2) Why is Round Robin good when someone is typing and browsing the web? (3) Give one downside of Round Robin.

Use these words: CPU · turn · time slice · wait · fair

**Q1.** A process is running and its time slice ends. Which state does it move to?

**Q2.** Three processes arrive together: A needs 3 units, B needs 6, C needs 1. Using FCFS in the order A, B, C, what is the average waiting time?

**Q3 (True or False).** A one-core CPU can run two processes at exactly the same instant. *(Chapter 1 quick quiz)*

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T3 | **True** | A process is a program that is running. Two running copies = two processes. |
| M3 | **C** | Everyone gets a short time slice, again and again. B describes FCFS. |
| Q1 | **Ready** | It goes back to the line. It only goes to Waiting if it is waiting for I/O. |
| Q2 | **4** | A finishes at 3 (wait 0), B at 9 (wait 3), C at 10 (wait 9). (0 + 3 + 9) ÷ 3 = 4. |
| Q3 | **False** | One core switches very fast; it only looks simultaneous. |

**O1 sample answer (127 words).** P3 finished much sooner in the Round Robin round: at clap 10 instead of clap 22. In the FCFS round, P3 had to wait for big P1 to clap 16 times and then for P2, even though P3 only needed 2 claps. In Round Robin, every process gets a short time slice (here 4 claps) and then goes to the back of the line, so short jobs do not get stuck behind a long one. This is good for typing and browsing, because each program gets the CPU again very soon, so the computer feels quick and fair. One downside is that switching between processes takes a little time, and the long job P1 does not finish any sooner: it ends at clap 22 in both rounds.

**O1 key points (1 mark each):** P3 finished sooner with RR (10 instead of 22) · in FCFS P3 waited behind the long job · time slices: short turns, then back of the line · links RR to a computer that feels quick · gives a downside (switching takes time, or long jobs are not faster). *Also accept:* a learner who says FCFS is simpler, if they also explain why P3 waits longer.
