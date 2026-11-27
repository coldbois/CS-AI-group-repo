# 3.4 Planning and Problem Solving

![Dandroid scratching its head over the river puzzle](../../../assets/dandroid/dandroid-confused.png)

**Chapter 3 · Dandroid's Brain** · Study Guide pp. 132–141 · Slides 2, 40–43 · Test Bank T21, T22, M21, M22, O8

> **Mission.** A farmer must cross a river with a wolf, a goat and a cabbage. The boat holds the farmer plus one item. Left alone, the wolf eats the goat, and the goat eats the cabbage. Dandroid needs a plan!

This is the puzzle our teaching slides open with ("Can you beat Dandroid?", slide 2) and solve at the end (slide 43).

**You will learn to**

- describe a problem with states, actions, a goal and costs
- trace BFS and DFS; explain A*
- write a STRIPS action and a simple constraint problem

**Key words:** state, action, goal test, search tree, BFS, DFS, A*, heuristic

---

## Planning = searching through states

To let a computer solve a problem, we first describe it precisely.

![Figure 3.4a](../Diagrams%20and%20Pictures/3-4_river-states.png)

*Figure 3.4a. The river puzzle as states, moves and rules (slide 40).*

| Part | Meaning | River puzzle |
| --- | --- | --- |
| **Initial state** | where you start | Left: F W G C · Right: (empty) |
| **Actions** | what you may do | the farmer crosses with 0 or 1 item |
| **Transition model** | what each action changes | the farmer and the item switch banks |
| **Goal test** | how you know you're done | Left: (empty) · Right: F W G C |
| **Path cost** | the total cost of the actions | 1 per crossing, so fewer crossings is better |

The **constraints** are the eating rules: never leave W+G or G+C alone. A state that breaks them is **illegal**, and the search skips it.

## Cost matters: a road-map example

![Figure 3.4b](../Diagrams%20and%20Pictures/3-4_problem-graph.png)

*Figure 3.4b. Describing a problem like an AI (Study Guide p. 135).*

A → B → D costs **4**; A → C → D costs **6**. Both routes have 2 steps, but they don't cost the same. Fewest steps ≠ cheapest!

## Searching a tree: BFS vs DFS

A computer explores the possible states as a **search tree**: the start is the root, and each move leads to a child.

![Figure 3.4c](../Diagrams%20and%20Pictures/3-4_bfs-dfs.png)

*Figure 3.4c. Two ways to explore (slide 41; Study Guide p. 136).*

| | **BFS** (breadth-first) | **DFS** (depth-first) |
| --- | --- | --- |
| How | explore level by level | dive down one branch, then back up |
| Uses | a **queue** (FIFO) | a **stack** (LIFO) |
| Order in the tree | A B C D E F G | A B D E C F G |
| Strength | finds the shallowest goal (fewest steps) | uses less memory |
| Weakness | can use lots of memory | may wander down a long, useless branch |

**UCS** (uniform-cost search) always expands the *cheapest* path found so far, so it finds the cheapest route even when steps cost different amounts.

> **Dandroid's tip.** Remember [2.5](../../../Software%20Fundamentals/13_data-structures/Main%20Theory/13_main-theory.md)? Queue → BFS. Stack → DFS. Data structures power AI search!

## Worked example: Dandroid solves the river puzzle

Which first move is safe (the class vote on slide 42)? Only **taking the goat**. Take the wolf and the goat eats the cabbage; take the cabbage and the wolf eats the goat; cross alone and both disasters are possible. Wolf and cabbage are safe together.

![Figure 3.4d](../Diagrams%20and%20Pictures/3-4_river-plan.png)

*Figure 3.4d. The full plan (slide 43).*

| Step | Farmer... | Left bank | Right bank |
| --- | --- | --- | --- |
| 1 | takes the goat | W C | F G |
| 2 | returns alone | F W C | G |
| 3 | takes the wolf | C | F W G |
| 4 | **brings the goat back** | F G C | W |
| 5 | takes the cabbage | G | F W C |
| 6 | returns alone | F G | W C |
| 7 | takes the goat | (empty) | F W G C |

The trick is step 4: going backwards to move forwards. A person often misses it; a search doesn't, because it tries every legal move. Swapping the wolf and the cabbage in steps 3 and 5 also works.

We checked this with a short BFS program, [river_bfs.py](../Learner%20Activity/code/river_bfs.py). It uses a queue, skips illegal states, and prints exactly this 7-crossing plan.

## Smart search: heuristics and A*

BFS explores *everything* near the start. On a big map that is slow. A **heuristic** h(n) is a smart *estimate* of the cost still to go (for example, the straight-line distance to the goal). **A\*** adds it to the cost so far:

**f(n) = g(n) + h(n)**

![Figure 3.4e](../Diagrams%20and%20Pictures/3-4_a-star.png)

*Figure 3.4e. Smart search with A* (Study Guide p. 137).*

| Option | g(n): cost so far | h(n): estimate to goal | f(n) = g + h |
| --- | --- | --- | --- |
| Via B | 3 | 5 | 8 |
| Via C | 4 | 2 | **6** ← A* tries this first |

- **Greedy best-first** search uses only h(n). It is fast, but walls and dead ends can fool it.
- An **admissible** heuristic never *overestimates* the true cost. With one, A* is guaranteed to find the cheapest route.
- On a grid map, **Manhattan distance** (blocks across + blocks up, ignoring walls) is a common admissible heuristic.

> **Bug alert.** A* picks C first, but that isn't proof C is on the best route. It's a guided guess that A* keeps checking as it searches.

## Planning actions and constraint puzzles

![Figure 3.4f](../Diagrams%20and%20Pictures/3-4_strips-csp.png)

*Figure 3.4f. STRIPS and constraint problems (Study Guide p. 138).*

**STRIPS** describes each action by what must be true before it (*preconditions*), what it makes true (*add list*) and what it makes false (*delete list*):

```
Action: PickUp(Box)
  Preconditions: OnTable(Box), HandEmpty, Clear(Box)
  Add list:      Holding(Box)
  Delete list:   OnTable(Box), HandEmpty, Clear(Box)
```

A **plan** is a sequence of actions whose preconditions are met, ending at the goal.

A **constraint satisfaction problem (CSP)** asks which values break no rules. Timetable example: variables Math and Physics; each can be Monday morning or Monday afternoon; constraint Math ≠ Physics (same teacher). One solution: Math in the morning, Physics in the afternoon (swapping works too).

> **Dandroid's tip.** Search asks "which path?". Planning asks "which actions?". A CSP asks "which values break no rules?". Real systems mix all three, and replan when the world changes.

## Try it

- **River Crossing Challenge** (20 min, pairs): solve the puzzle with paper cut-outs, then describe it like an AI planner. [19_learner-activity-2.md](../Learner%20Activity/19_learner-activity-2.md)
- **Maze Race: BFS vs Greedy vs A\*** (15 min, solo, browser): watch three search algorithms explore the same maze. [19_learner-activity-1.md](../Learner%20Activity/19_learner-activity-1.md)

## Check yourself

1. Name the five parts of a search problem.
2. Which search uses a queue? Which uses a stack?
3. In A*, what does h(n) mean?

**Answers (try first, then peek)**
1. Initial state, actions, transition model, goal test, path cost.
2. BFS uses a queue; DFS uses a stack.
3. The estimated cost from n to the goal.


More questions: [19_test-bank.md](../Test%20bank%20Question_Answer/19_test-bank.md)

## Remember

- Problems = states + actions + goal + cost.
- BFS goes wide, DFS goes deep, A* = cost so far + smart estimate.
- STRIPS describes actions; CSPs find values that break no rules.

## Watch and explore

**UC Berkeley CS188 notes: Informed Search** (inst.eecs.berkeley.edu/~cs188/textbook). Clear, free notes on heuristics and A*. Find the definition of an admissible heuristic and give your own map example. It is university level: read the first part only.

## References

- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. Chapters 3, 6 and 11.
- Fikes, R. E., & Nilsson, N. J. (1971). STRIPS: A new approach to the application of theorem proving to problem solving. *Artificial Intelligence, 2*(3–4), 189–208.
- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. *IEEE Transactions on Systems Science and Cybernetics, 4*(2), 100–107.

---

Previous: [3.3 Reasoning and Expert Systems](../../18_reasoning-and-expert-systems/Main%20Theory/18_main-theory.md) · Next: [3.5 Advantages and Limitations](../../20_advantages-and-limitations-of-symbolic-ai/Main%20Theory/20_main-theory.md) · Up: [Chapter 3 overview](../../README.md)
