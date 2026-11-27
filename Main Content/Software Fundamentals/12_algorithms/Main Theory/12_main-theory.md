# 2.4 Algorithms

![Dandroid searching](../../../assets/dandroid/dandroid-curious.png)

**Chapter 2 · Dandroid's Instructions** · Study Guide pp. 76–83 · Slides 25–26 · Test Bank T12, T13, M13

> **Mission.** Dandroid must find one name among 1,000,000 contacts. Checking them one by one could take ages. Is there a smarter way?

**You will learn to**

- define an algorithm and its properties
- compare linear and binary search
- use Big-O to describe how work grows

**Key words:** algorithm, linear search, binary search, sorting, Big-O, recursion

---

## What makes a good algorithm?

An **algorithm** is a finite list of clear steps that solves a problem. A recipe is an algorithm for food.

A good algorithm has:

- **Input:** what goes in (a list of names).
- **Output:** what comes out (where "Zara" is in the list).
- **Clear steps:** no guessing. A computer takes everything literally.
- **An end:** it must stop.

We also want it to be **correct** (the right answer) and **efficient** (little time or memory).

> **Dandroid's tip.** Warm-up game: write instructions for making a sandwich. A teammate follows them *exactly* as written ("put the bread on the knife"?). Watch the chaos, then improve your algorithm.

## Linear search vs binary search

**Linear search** checks items one by one from the start. It works on any list, but it can be slow.

**Binary search** only works on a **sorted** list. It checks the middle item, throws away the half that can't contain the target, and repeats.

![Figure 2.4a](../Diagrams%20and%20Pictures/2-4_linear-vs-binary.png)

*Figure 2.4a. Find 37 in a sorted list of 15 numbers (Study Guide p. 78). You can run this example: [search.py](../Learner%20Activity/code/search.py).*

| Step | Part of the list still possible | Middle | Decision |
| --- | --- | --- | --- |
| 1 | all 15 numbers | 33 | 33 < 37 → keep the right half |
| 2 | 37 ... 70 | 52 | 52 > 37 → keep the left part |
| 3 | 37, 41, 46 | 41 | 41 > 37 → go left again |
| 4 | 37 | 37 | found it |

Linear search needed **9 checks**; binary search needed **4**. The gap gets enormous as lists grow: for 1,000,000 names, linear search may need 1,000,000 checks, but binary search needs about **20**, because 1,000,000 can only be halved about 20 times before one name is left.

The same idea wins the number-guessing game on slides 25–26. Guessing a number from 1 to 100 by always picking the middle never needs more than **7** guesses: 100 → 50 → 25 → 13 → 7 → 4 → 2 → 1.

![Figure 2.4b](../Diagrams%20and%20Pictures/2-4_guess-my-number.png)

*Figure 2.4b. Halving the possibilities (slide 26).*

## Big-O: how fast does the work grow?

**Big-O** describes how the number of steps grows as the input size *n* grows.

![Figure 2.4c](../Diagrams%20and%20Pictures/2-4_big-o.png)

*Figure 2.4c. Big-O (Study Guide p. 79).*

| Big-O | Name | Example | n = 10 | n = 1,000 | n = 1,000,000 |
| --- | --- | --- | --- | --- | --- |
| O(1) | constant | look up `array[5]` | 1 | 1 | 1 |
| O(log n) | logarithmic | binary search | ≈ 3 | ≈ 10 | ≈ 20 |
| O(n) | linear | linear search | 10 | 1,000 | 1,000,000 |
| O(n log n) | n log n | merge sort | ≈ 33 | ≈ 10,000 | ≈ 20 million |
| O(n²) | quadratic | bubble sort | 100 | 1,000,000 | 1 trillion |

> **Bug alert.** Big-O is not a stopwatch time. It tells you how work *grows*. O(n²) is fine for 10 items and hopeless for a million.

## Sorting: putting things in order

Binary search needs sorted data, so sorting matters.

- **Bubble sort:** compare neighbours and swap them if they are in the wrong order; repeat until no swaps are needed. Simple, but O(n²).
- **Insertion sort:** take the next card and slide it into place, like sorting a hand of cards. O(n²) in the worst case, but fast on lists that are almost sorted.
- **Merge sort:** split the list in half, sort each half, then merge them. O(n log n), but it uses extra memory.

![Figure 2.4d](../Diagrams%20and%20Pictures/2-4_bubble-sort.gif)

*Figure 2.4d. Bubble sort in action (team animation from the Diagrams folder; it animates on GitHub). The big values "bubble" to the end on each pass.*

**Recursion** means solving a problem by solving smaller copies of it. Merge sort is recursive: to sort a list, it sorts two half-lists, which sort quarter-lists, and so on. Every recursive algorithm needs a **base case** that stops it; for merge sort, a list of one item is already sorted.

> **Dandroid's tip.** The best choice depends on the size of the data, the memory available and how the data is stored.

## Try it

**Guess My Number & Human Bubble Sort** (20 min, pairs then whole class): feel why binary search is fast, then sort six classmates with bubble sort. Instructions and answers: [12_learner-activity.md](../Learner%20Activity/12_learner-activity.md).

## Check yourself

1. What must be true about a list before you use binary search?
2. Which grows faster: O(n log n) or O(n²)?
3. What does recursion need so it doesn't run forever?

**Answers (try first, then peek)**
1. It must be sorted (and let you jump to the middle).
2. O(n²).
3. A base case.


More questions: [12_test-bank.md](../Test%20bank%20Question_Answer/12_test-bank.md)

## Remember

- Algorithm = clear, finite steps with an input and an output.
- Binary search halves the search each step: O(log n).
- Big-O shows how work grows with input size.

## Watch and explore

**VisuAlgo: Sorting** (visualgo.net/en/sorting). Animates bubble, insertion and merge sort step by step. Enter 6 numbers, run bubble sort, then merge sort, and count the steps. There are many options: stick to the sort buttons at first.

## References

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. Chapters 2–3.
- Bhargava, A. Y. (2016). *Grokking Algorithms*. Manning. Chapters 1–4.

---

Previous: [2.3 Computer Programming](../../11_computer-programming/Main%20Theory/11_main-theory.md) · Next: [2.5 Data Structures](../../13_data-structures/Main%20Theory/13_main-theory.md) · Up: [Chapter 2 overview](../../README.md)
