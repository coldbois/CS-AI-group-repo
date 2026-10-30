# Section 12 — Algorithms

An algorithm is a set of clear steps for solving a problem. A recipe is a useful comparison: the order matters, and the instructions should be specific enough to follow. In computing, algorithms are used for searching, sorting, calculating, and finding routes.

The **input** is what you start with, and the **output** is the result. A good algorithm should be precise, finish after a limited number of steps, and give a correct answer for the inputs it claims to handle. One particular example being solved is called an instance of the problem.

An algorithm can be described in plain English, a flowchart, pseudocode, or code. The algorithm is the plan; pseudocode describes the plan in a code-like form; program code implements it.

## How we compare algorithms

**Time complexity** describes how the amount of work grows as the input gets larger. **Space complexity** describes how much memory is needed. Big-O notation gives a rough description of that growth.

Common growth rates, from generally more manageable to less manageable for large inputs, are:

`O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n²)`, `O(n³)`, `O(2ⁿ)`, `O(n!)`.

Here, `n` is the input size. `O(n)` grows roughly with the number of items, while `O(n²)` can grow much faster. Big-O describes growth, not an exact runtime for every computer.

A simple recursive Fibonacci algorithm can repeat the same work and take exponential time, while a loop can calculate the sequence in linear time. For the Traveling Salesman Problem, checking every order of `n` cities leads to factorial growth, so brute force quickly becomes impractical. Sometimes a faster method uses more memory; sometimes saving memory requires extra work.

## Searching

**Linear search** checks items one at a time and may inspect every item: `O(n)`.

**Binary search** works on a sorted list. It checks the middle and discards half the remaining items each time, giving `O(log n)` time.

For example, in `[3, 8, 15, 21, 27, 34, 40]`, binary search checks `21`, then `34`, then `27`. It finds 27 in three checks. Linear search would need five. Binary search only works this way when the list is sorted.

## Sorting

Sorting puts things in an order, such as smallest to largest.

- **Bubble sort** swaps neighbouring items that are out of order. Typical time: `O(n²)`.
- **Selection sort** repeatedly picks the smallest item left. Typical time: `O(n²)`.
- **Insertion sort** inserts each item into the sorted part. Typical time: `O(n²)`, but it can work well on small or nearly sorted lists.
- **Merge sort** splits the list, sorts each part, and merges them. Time: `O(n log n)`.
- **Quicksort** picks a pivot and splits items into smaller and larger groups. It is `O(n log n)` on average, but poor pivot choices can make it slower.
- **Heap sort** uses a heap to repeatedly take the largest item. Time: `O(n log n)`.

With quicksort, the first partition does not necessarily sort the whole list. It puts the pivot in the right position and leaves smaller sorting jobs on either side.

## Three ways to design algorithms

**Divide and conquer** breaks a problem into smaller ones and combines the results; merge sort is an example. **Greedy methods** choose what looks best at each step, but that does not always produce the best overall answer. **Dynamic programming** stores the answers to smaller, repeated problems so they do not need to be calculated again.

Two algorithms can give the same answer but use very different amounts of time and memory. That difference becomes important as the input grows.
