# Try it: Process Musical Chairs (1.3)

**Time:** 20 min · **Group:** 4–5 people · **You need:** one chair, a timer, three job cards · Study Guide pp. 22–23 · Linked Test Bank question: O1

**Goal:** feel the difference between FCFS and Round Robin, and watch a deadlock happen.

## Prepare

- One chair = **the CPU**.
- Three volunteers = **processes**, each with a job card: **P1 claps 16 times, P2 claps 4, P3 claps 2.**
- One **timekeeper** counts every clap out loud (the clock).

Only the person in the chair may clap.

## Steps

1. **FCFS round.** P1 sits and claps all 16, then P2, then P3. The timekeeper writes down the clap count when each one finishes.
2. **Round Robin round.** Each person sits for only **4 claps** (the time slice), then goes to the back of the line if they still have claps left.
3. **Compare:** who finished sooner in each round?
4. **Deadlock bonus.** P1 holds a pen, P2 holds a notebook. Each needs *both* to write their name, and nobody is allowed to let go. What happens?

## Record

| Process | Finish (FCFS) | Finish (RR) |
| --- | --- | --- |
| P1 (16 claps) | | |
| P2 (4 claps) | | |
| P3 (2 claps) | | |

## Reflect

- Which round felt fairer to P3? Why?
- Which would you want for typing and web browsing?
- In the deadlock, how could the tie be broken?

## Check it: expected results

| Process | Finish (FCFS) | Wait (FCFS) | Finish (RR) | Wait (RR) |
| --- | --- | --- | --- | --- |
| P1 (16) | 16 | 0 | 22 | 6 |
| P2 (4) | 20 | 16 | 8 | 4 |
| P3 (2) | 22 | 20 | 10 | 8 |
| **Average wait** | | **12 claps** | | **6 claps** |

(Wait = finish − claps needed.)

How the RR round goes: P1 claps 1–4, P2 claps 5–8 and is done, P3 claps 9–10 and is done, then P1 has the chair alone and finishes at clap 22.

- Short jobs finish far sooner with Round Robin, so the computer *feels* responsive. That is what you want for typing and browsing.
- P1 finishes at 22 in both rounds: Round Robin doesn't make the long job faster.
- **Deadlock:** both wait forever. Fixes: one gives up its item, or everyone must grab items in the same order (pen first).
- Real switching costs a little time (a **context switch**), which this game ignores. If your group wants to show it, make each person count "1, 2" while swapping seats.

These are the same numbers as Test Bank question **O1**. They are the Study Guide example (8, 2 and 1 units, time slice 2) doubled.
