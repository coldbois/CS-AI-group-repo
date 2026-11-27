# 2.5 Data Structures

![Dandroid lost in a messy pile of data](../../../assets/dandroid/dandroid-confused.png)

**Chapter 2 · Dandroid's Instructions** · Study Guide pp. 84–90 · Slides 27–29 · Test Bank T14, M14, O5

> **Mission.** Dandroid's memory is one giant messy pile of data. Finding anything takes forever. How should Dandroid organise it?

**You will learn to**

- explain why programs organise data
- describe 7 common data structures with everyday examples
- choose a structure by asking what the program does most

**Key words:** array, linked list, stack, queue, tree, graph, hash table

---

## Why organise data?

Imagine a library where every book is thrown in one big pile. To find one book you would have to check every book. Put them on labelled shelves and you can walk straight to the right one. The books are the same; only the organisation changed.

![Figure 2.5a](../Diagrams%20and%20Pictures/2-5_why-organise-data.svg)

*Figure 2.5a. Same books, very different search times (team diagram, used on Study Guide p. 84).*

A **data structure** is a way of organising data in memory so that the things a program does most often are fast.

## Seven structures, seven everyday twins

![Figure 2.5b](../Diagrams%20and%20Pictures/2-5_seven-structures.png)

*Figure 2.5b. Seven structures, seven everyday twins (Study Guide p. 85).*

| Structure | Everyday twin | Good at |
| --- | --- | --- |
| **Array** | numbered lockers; jump straight to locker 2 (the index starts at **0**) | reading any position instantly |
| **Linked list** | a treasure hunt: each clue points to the next one | adding and removing items in the middle |
| **Stack** | a pile of plates: **last in, first out (LIFO)** | undo, going back |
| **Queue** | a canteen line: **first in, first out (FIFO)** | serving things fairly in order |
| **Tree** | a family tree or folders: one root, many levels | things inside things (like the folder tree in [1.6](../../../Operating%20Systems%20%E2%80%94%20Essential%20Foundations/06_File%20Systems%20and%20Storage/Main%20Theory/06_main-theory.md)) |
| **Graph** | a map of cities and roads: anything can link to anything | networks: friends, roads, the web |
| **Hash table** | a coat check: hand in ticket 17, get coat 17 instantly | finding something by its key (a name, an ID) |

> **Dandroid's tip.** No structure is best at everything. Ask: *what will my program do most often?* Then pick the structure that makes that fast.

## Stack vs queue

These two cause the most mix-ups, so we look at them side by side (the same comparison is on slide 27).

![Figure 2.5c](../Diagrams%20and%20Pictures/2-5_stack-vs-queue.png)

*Figure 2.5c. Stack vs queue (Study Guide p. 86).*

| | **Stack (LIFO)** | **Queue (FIFO)** |
| --- | --- | --- |
| Add | **push** = put on top | **enqueue** = join the back |
| Remove | **pop** = take from the top | **dequeue** = leave from the front |
| Comes out first | the **newest** item | the **oldest** item |
| Used for | the Undo button, the browser Back button, function calls | printer jobs, chat support, the CPU's ready queue ([1.3](../../../Operating%20Systems%20%E2%80%94%20Essential%20Foundations/03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md)) |
| Python | `stack.append(x)` and `stack.pop()` | `line.append(x)` and `line.popleft()` (with `collections.deque`) |

> **Bug alert.** Common mix-up: stack = plates (newest first). Queue = line of people (oldest first).

## Worked example: build an Undo button

Undo always reverses the *most recent* action, so the newest comes out first: that's a stack.

| Step | Action | Stack (bottom → top) | On screen |
| --- | --- | --- | --- |
| 1 | type "Hello" → push | [Hello] | Hello |
| 2 | type "big" → push | [Hello, big] | Hello big |
| 3 | type "world" → push | [Hello, big, world] | Hello big world |
| 4 | Undo → pop "world" | [Hello, big] | Hello big |
| 5 | Undo → pop "big" | [Hello] | Hello |

![Figure 2.5d](../Diagrams%20and%20Pictures/2-5_undo-worked-example.svg)

*Figure 2.5d. The Undo button is a stack (team diagram, used on Study Guide p. 87).*

**Predict first:** why not a queue? *A queue would undo "Hello" first, the oldest action. That's not what users expect!*

You can run this example, plus a print queue, in [stack_and_queue.py](../Learner%20Activity/code/stack_and_queue.py). We ran it: after two Undos only `Hello` is left, and in the print queue Ana's job prints first while Ben and Cho wait.

## Try it

**Data Structure Match-Up** (20 min, solo or pairs): match real situations to structures and trace a stack and a queue. Instructions and answers: [13_learner-activity.md](../Learner%20Activity/13_learner-activity.md).

## Going further (optional)

- **Why arrays start at 0.** The index is how far you move from the start of the array. The first item is 0 steps away.
- **How a hash table jumps straight there.** A *hash function* turns the key (for example the name "Mina") into a slot number. Looking up the slot is O(1) on average, no matter how many names are stored. Two keys landing in the same slot is called a *collision*, and the table has to handle it.
- **Trees in search.** In [3.4](../../../Symbolic%20AI%20Fundamentals/19_planning-and-problem-solving/Main%20Theory/19_main-theory.md), breadth-first search explores a tree using a queue, and depth-first search uses a stack. The two structures from this page come back.

## Check yourself

1. What does LIFO stand for, and which structure uses it?
2. Why is a hash table fast for finding a phone number by name?
3. Which structure suits a road map?

**Answers (try first, then peek)**
1. Last In, First Out: a stack.
2. A hash function turns the name (key) into a slot number, so it jumps straight there.
3. A graph.


More questions: [13_test-bank.md](../Test%20bank%20Question_Answer/13_test-bank.md)

## Remember

- Choose a structure by what your program does most.
- Stack = LIFO; queue = FIFO.
- Trees = levels; graphs = networks; hash tables = instant lookup by key.

## Watch and explore

**Crash Course Computer Science #14: Data Structures** (PBS, YouTube). An animated tour of arrays, lists, stacks, queues, trees and graphs. Pause at each structure and name an everyday twin. It mentions pointers briefly; it's fine to skip that part.

## References

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. Chapters 10–11.
- Python Software Foundation. (n.d.). *Data Structures* (Python tutorial, section 5). https://docs.python.org/3/tutorial/datastructures.html

---

Previous: [2.4 Algorithms](../../12_algorithms/Main%20Theory/12_main-theory.md) · Next: [2.6 Databases](../../14_Databases/Main%20Theory/14_main-theory.md) · Up: [Chapter 2 overview](../../README.md)
