# Section 12: Algorithms

## 1. What is an algorithm?

An **algorithm** is a precise procedure that takes some input, follows a finite sequence of steps, and produces an output. Algorithms are used to solve computational problems such as sorting a list or finding a particular item.

An everyday analogy is a morning routine: wake up, brush your teeth, shower, get dressed, eat, and leave. The order matters, and changing the order can change the result.

A particular input to a problem is called an **instance** of that problem. For example, one sorting instance is:

```text
Input:  31, 41, 59, 26, 41, 58
Output: 26, 31, 41, 41, 58, 59
```

An algorithm is correct when it terminates and produces the required output for every valid input in the problem's scope. An algorithm that works on small examples but fails on some larger valid inputs is not fully correct.

## 2. Qualities of a good algorithm

| Quality | Meaning | Example |
|---|---|---|
| **Finiteness** | The procedure ends after a limited number of steps. | “Stir the batter 50 times” has a definite end; “stir until you feel like it” does not specify one. An algorithm must not run forever. |
| **Input** | The algorithm starts with data, although some algorithms can also work with no input. | A list such as `[5, 3, 8, 1]`. |
| **Output** | It produces a clear result. | The sorted list `[1, 3, 5, 8]`. |
| **Definiteness** | Each step is precise and unambiguous. | “Bake at 180°C for 25 minutes” is more precise than “bake until golden.” |
| **Efficiency** | It uses time and memory sensibly for the problem. | Compare algorithms using time and space complexity, often described with Big-O notation. |

An algorithm does not have to be written as program code. It can be expressed in clear English, a flowchart, or **pseudocode**—a structured, code-like description that is not tied to one programming language. The algorithm is the plan; pseudocode describes the plan; source code implements it in a programming language.

## 3. Measuring efficiency with Big-O notation

An algorithm's efficiency is not judged only by how many seconds it takes on one computer. It is also important to understand how the amount of work changes as the input gets larger.

- **Time complexity** describes how the running work grows with input size.
- **Space complexity** describes how the memory requirement grows with input size.
- **Big-O notation** summarizes an upper-bound style of growth, especially for large inputs. In introductory comparisons, it is often used to describe an algorithm's typical growth rate.

Let `n` stand for the size of the input. The following common growth rates are ordered from slower-growing to faster-growing:

`O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)`

| Complexity | Beginner-friendly interpretation |
|---|---|
| `O(1)` | Constant: the amount of work stays roughly the same as the input grows. |
| `O(log n)` | Logarithmic: the work grows slowly; repeatedly cutting a search space in half is a common example. |
| `O(n)` | Linear: the work grows roughly in proportion to the number of items. |
| `O(n log n)` | A common growth rate for efficient comparison-based sorting algorithms. |
| `O(n²)` | Quadratic: for example, the work can grow roughly with the number of pairs of items. |
| `O(n³)` | Cubic: work can grow roughly with three nested dimensions of the input. |
| `O(2ⁿ)` | Exponential: the work can roughly double for every additional input element. |
| `O(n!)` | Factorial: the number of possibilities can grow extremely quickly as `n` increases. |

### Example: the Traveling Salesman Problem

The Traveling Salesman Problem asks for a route that visits each of `n` cities exactly once and returns to the starting city. Checking every possible ordering of cities can require factorial-scale work.

Using the simple `n!` count in the source material:

- `3` cities: `3! = 6` possible orderings.
- `5` cities: `5! = 120` possible orderings.
- `10` cities: `10! = 3,628,800` possible orderings.

This illustrates why checking every possible route quickly becomes impractical. **Counting note:** the exact count of distinct tours depends on conventions, such as whether reversed routes or different starting points count as separate routes. The examples above follow the source's simplified `n!` illustration.

### Example: Fibonacci numbers

The Fibonacci sequence starts with values such as `0, 1, 1, 2, 3, 5, 8, ...`, where each later value is the sum of the two before it.

- A simple recursive implementation that calculates the same values repeatedly can take `O(2ⁿ)` time and `O(n)` stack space.
- A loop-based implementation can calculate the sequence in `O(n)` time while using `O(1)` extra space if it stores only a fixed number of previous values.

Both approaches can produce the same answer, but their resource costs can be very different.

### Time and memory trade-offs

Sometimes an algorithm uses extra memory to avoid repeating work. Another algorithm might save memory but spend more time recalculating results. There is not always one best option for every constraint.

For example, if Algorithm A takes `O(n²)` time and Algorithm B takes `O(n log n)` time, B's growth rate is lower and it will generally scale better for sufficiently large inputs, assuming comparable conditions and implementations.

## 4. Searching algorithms

A **searching algorithm** tries to find a target item in a collection of data.

| Algorithm | How it works | Time complexity |
|---|---|---|
| **Linear search** | Checks items one at a time until it finds the target or reaches the end. | `O(n)` |
| **Binary search** | Requires sorted data. Checks the middle item and discards the half that cannot contain the target, repeating the process. | `O(log n)` |

### Worked example: find `27`

Consider the sorted array below. Positions are numbered from `0` to `6`.

```text
Value:     3   8  15  21  27  34  40
Position:  0   1   2   3   4   5   6
```

Binary search proceeds as follows:

1. Check position `3`, which contains `21`. Since `27` is larger, discard positions `0` through `3` and keep the right side.
2. Check the middle of positions `4` through `6`, which is position `5` and contains `34`. Since `27` is smaller, keep the portion to the left of position `5`.
3. Check position `4`, which contains `27`. The target has been found.

Binary search finds the target in `3` checks in this example. A linear search from the start checks `3`, `8`, `15`, `21`, and then `27`, so it needs `5` checks.

## 5. Sorting algorithms

A **sorting algorithm** rearranges items into a chosen order, such as from smallest to largest.

| Algorithm | Basic idea | Typical time complexity |
|---|---|---|
| **Bubble sort** | Compare adjacent items and swap them when they are out of order. Large values gradually move toward the end. | `O(n²)` |
| **Selection sort** | Find the smallest item in the unsorted part and place it next in the sorted part. | `O(n²)` |
| **Insertion sort** | Take each new item and insert it into the correct location in the part that is already sorted. | `O(n²)` |
| **Merge sort** | Split the list into halves, sort the halves, and merge the sorted results. | `O(n log n)` |
| **Quick sort** | Choose a pivot, partition items into smaller and larger groups, then sort the groups. | `O(n log n)` on average. |
| **Heap sort** | Build a max heap, then repeatedly remove the largest item to produce the sorted order. | `O(n log n)` |

A **pivot** is the chosen value used to partition data in quick sort. A **heap** here is a tree-based data structure that keeps an item with the highest priority (in a max heap, the largest item) easy to access. This is a different use of the word *heap* from the memory region discussed in C programming.

### Worked quick-sort partitions

The following examples show the first partition only; they do **not** show a fully sorted array yet.

**Example A:** `[45, 12, 88, 32, 60]`, using the first element, `45`, as the pivot.

- Values smaller than the pivot: `[12, 32]`
- Values larger than the pivot: `[88, 60]`
- After the first partition: `[12, 32, 45, 88, 60]`

The pivot is in its final position, but the right-hand group `[88, 60]` still needs to be sorted.

**Example B:** `[30, 10, 50, 20, 40]`, using `30` as the pivot.

- Smaller group: `[10, 20]`
- Larger group: `[50, 40]`
- After the first partition: `[10, 20, 30, 50, 40]`

Again, the two groups still need their own sorting steps.

## 6. Common algorithm-design principles

- **Divide and conquer:** Break a large problem into smaller subproblems, solve those subproblems, and combine their results. Merge sort is a common example.
- **Greedy method:** Choose what seems to be the best available option at each step. This can be fast and simple, although a greedy choice does not guarantee the best overall answer for every problem.
- **Dynamic programming:** Store and reuse answers to overlapping subproblems instead of recalculating them. A Fibonacci program can use a table of previously calculated values.

## Key takeaways

- A good algorithm has clear steps, handles its intended inputs, produces the required output, and terminates.
- Big-O notation helps compare how time or memory use grows as the input grows.
- Binary search is efficient for finding a value in sorted data; linear search does not require sorted data.
- Sorting algorithms use different strategies and have different growth rates.
- Divide and conquer, greedy methods, and dynamic programming are common ways to design algorithms, each suited to particular problems.
