# Topic 19 — Learner Activities

## Activity 1 — Trace BFS and DFS

**Goal:** Compare two search strategies using the same search tree.

Use this tree:

```text
          A
        /   \
       B     C
      / \   / \
     D   E F   G
```

Assume children are considered from left to right.

**Tasks:**

1. Write the order in which BFS visits the nodes.
2. Write one possible order for DFS.
3. Which method uses a FIFO queue? Which uses a LIFO stack?
4. If the goal is D, which method reaches it after fewer node visits in this example?

**Expected outcome:** BFS: `A, B, C, D, E, F, G`. DFS: `A, B, D, E, C, F, G`. BFS uses a FIFO queue; DFS uses a LIFO stack. DFS reaches D after three visits in this ordering, while BFS also reaches D after four visits. This illustrates that the goal's position in the tree affects how much is explored; it does not mean DFS is generally better.

## Activity 2 — Compare route costs and A* values

**Goal:** Calculate path costs and understand the A* evaluation function.

A delivery robot is at A and wants to reach D. It has two current route options:

| Option | Cost so far `g(n)` | Estimated remaining cost `h(n)` |
|---|---:|---:|
| B | 3 | 5 |
| C | 4 | 2 |

**Tasks:**

1. Calculate `f(n) = g(n) + h(n)` for B and C.
2. Which option does A* consider first?
3. Does this guarantee that C is on the best final route? Explain.
4. What property should an admissible heuristic have?

**Expected outcome:** `f(B)=8`; `f(C)=6`; A* considers C first. This is a selection based on the current estimates, not proof that every later path through C is best. An admissible heuristic does not overestimate the true minimum remaining cost.

## Activity 3 — Create a simple STRIPS action or CSP

**Goal:** Represent a problem in a structured way.

Choose **A or B**.

**A. STRIPS:** A robot places a box on a shelf. Write one action called `PlaceOnShelf(Box)` with at least two preconditions, one add-list fact and one delete-list fact. State what must be true before the action can happen.

**B. CSP:** A small group must schedule two lessons, English and Programming, into two time slots: Tuesday morning and Tuesday afternoon. The same teacher teaches both lessons. Identify the variables, domains and constraint, then give one valid assignment.

**Expected outcome:**

- A possible STRIPS answer: Preconditions: `Holding(Box)`, `AtShelf`. Add list: `OnShelf(Box)`. Delete list: `Holding(Box)`. Other reasonable action models are acceptable if the conditions and state changes are consistent.
- CSP answer: Variables: English and Programming. Domain for each: Tuesday morning or Tuesday afternoon. Constraint: the two lessons must use different slots. One valid assignment is English in the morning and Programming in the afternoon.
