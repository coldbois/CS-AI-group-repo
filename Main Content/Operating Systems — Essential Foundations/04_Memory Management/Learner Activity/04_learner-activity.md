# Try it: Desk Tidy Challenge (1.4)

**Time:** 15 min · **Group:** solo or pairs · **You need:** paper, 3 sticky notes · Study Guide pp. 27–28 · Linked Test Bank question: O2

**Goal:** act out page replacement. When the desk (RAM) is full, which book (page) goes back to the shelf?

## Prepare

Draw a desk with **3 spaces** (frames) on a sheet of paper. Write book numbers on sticky notes as you need them. You need books in this order:

**1, 2, 3, 1, 4, 1, 5, 1**

Book 1 is your favourite: you keep coming back to it.

## Steps

1. **Predict first:** which policy will make fewer ✗ marks, FIFO or LRU?
2. **FIFO round.** Go through the requests. When the desk is full, return the book that has been on the desk **the longest**.
3. Each time a book is *not* on the desk, mark ✗ (a page fault). If it is already there, mark ✓ (a hit).
4. **LRU round.** Start again with an empty desk. This time return the book **used least recently**.
5. Count the ✗ marks for each round.

## Record

| Request | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FIFO | | | | | | | | |
| LRU | | | | | | | | |

## Reflect

- Why did LRU keep book 1 on the desk?
- What would happen if the desk had only 1 space?

## Check it: expected results

| Request | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 | Faults |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FIFO | ✗ | ✗ | ✗ | ✓ | ✗ (out: 1) | ✗ (out: 2) | ✗ (out: 3) | ✓ | **6** |
| LRU | ✗ | ✗ | ✗ | ✓ | ✗ (out: 2) | ✓ | ✗ (out: 3) | ✓ | **5** |

- **FIFO: 6 faults** (books 1, 2, 3, 4, 1, 5). It threw out favourite book 1 just because it was the oldest on the desk.
- **LRU: 5 faults** (books 1, 2, 3, 4, 5). It kept book 1 because you kept using it.
- A smart policy means fewer slow trips to storage.
- With only 1 space, almost every request is a fault. Too few frames means constant swapping (**thrashing**), which makes a computer very slow.
- Real operating systems use cleverer versions of these ideas.
