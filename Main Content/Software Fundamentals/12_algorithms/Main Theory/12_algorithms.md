# 12. Algorithms

## Topic overview

An algorithm is a finite, well-defined sequence of steps for solving a problem. Programs implement algorithms in a programming language. This chapter introduces algorithm design, correctness, common search and sorting methods, and efficiency.

### Learning outcomes

1. Define an algorithm and describe its required properties.
2. Compare linear search, binary search and common sorting approaches.
3. Interpret Big-O notation at an introductory level.

### Key terms

| Term | Meaning |
|---|---|
| **Algorithm** | A finite sequence of precise steps that solves a problem. |
| **Input** | Data supplied to an algorithm. |
| **Output** | The result produced by an algorithm. |
| **Complexity** | A way to describe resource use, often time or memory, as input size grows. |
| **Big-O notation** | A mathematical description of an upper-bound growth rate, commonly used for algorithm analysis. |
| **Heuristic** | A practical guide or estimate that can help choose a solution. |

## Main concepts

### 12.1 What makes an algorithm?

A useful algorithm has clearly defined inputs and outputs, unambiguous steps, and a stopping condition. It should produce the required result for valid inputs. Correctness asks whether it solves the stated problem; efficiency asks how much time or memory it uses.

### 12.2 Searching

Linear search checks items one by one and works even when the list is unsorted. Its worst-case time grows in proportion to n: O(n). Binary search repeatedly halves a sorted search range, giving O(log n) time, but it requires sorted data and random access to the middle element.

### 12.3 Sorting

Sorting arranges data into an order. Simple methods such as bubble sort and insertion sort can take O(n²) time in the worst case. Merge sort typically takes O(n log n) time and uses extra memory. The best choice depends on input size, memory, stability requirements and implementation.

### 12.4 Understanding Big-O

Big-O describes how work grows as input grows, rather than giving an exact run time. O(1) is constant; O(log n) grows slowly; O(n) grows linearly; O(n log n) is common for efficient comparison sorts; O(n²) grows quickly for large inputs.

### 12.5 Design and verification

Use examples, boundary cases and invariants to reason about correctness. A loop invariant is a condition that remains true at key points in a loop. Recursion solves a problem by solving smaller versions of it, and it needs a base case to stop.

## Worked example

Linear search for 12 in `[4, 9, 12, 20]` checks 4, then 9, then 12: it finds the item after three comparisons. Binary search can do fewer comparisons on a sorted list: check the middle item first, then continue in the half that could contain 12. The requirement that the data is sorted is essential.

## Visual references

![Figure 1: Overview of common sorting algorithms](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2Axqpk8FZDyrLoElne.png)

*Figure 1. Overview of common sorting algorithms. Source: [Medium](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2Axqpk8FZDyrLoElne.png)*


![Figure 2: Visualisation of the Quick Sort sorting algorithm.](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

*Figure 2: Visualisation of the Quick Sort sorting algorithm. Source: [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Sorting_quicksort_anim.gif)*


![Figure 3: Visualisation of the Bubble Sort sorting algorithm.](https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif)

*Figure 3: Visualisation of the Bubble Sort sorting algorithm. Source: [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Sorting_quicksort_anim.gif)*


![Figure 4: Visualisation of the Insertion Sort sorting algorithm.](https://upload.wikimedia.org/wikipedia/commons/2/24/Sorting_insertion_sort_anim.gif)

*Figure 4: Visualisation of the Insertion Sort sorting algorithm. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Sorting_insertion_sort_anim.gif)*

## Applications and limitations

These concepts appear in real software systems, but the simplified examples in this chapter leave out some implementation details. Practical systems must also consider performance, errors, security and changing requirements. Always check that the model matches the problem before relying on its output.

## Connection to the next topic

Topic 13 explains how data structures organise the information algorithms use.

## Key takeaways

- Define an algorithm and describe its required properties.
- Compare linear search, binary search and common sorting approaches.
- Interpret Big-O notation at an introductory level.
- Use the worked example to connect the terminology to a concrete situation.
- The diagrams are externally sourced images; check the source page and licence before public redistribution.
