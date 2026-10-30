# Section 18 — Planning and Problem Solving

In AI, problem-solving means finding actions that move a situation from where it is now to a goal. Planning is deciding which actions to take, often before carrying them out. A maze is a useful example: you know where you start and where you want to go, but there may be many possible routes.

A problem can be described with four parts: the **initial state** (where you start), **actions** (what you can do), a **goal test** (how you know you have succeeded), and **path cost** (how expensive a route is, perhaps in steps or energy). Exploring possible states and moves is called **state-space search**.

## Search methods

**Depth-first search (DFS)** follows one route as far as it can, then goes back and tries another. It often uses less memory, but it does not guarantee the shortest route.

**Breadth-first search (BFS)** explores all states one step away, then two steps away, and so on. If every move has the same cost, it finds a route with the fewest steps. It may use a lot of memory because it stores many options waiting to be explored.

**Uniform-cost search (UCS)** always expands the route with the lowest total cost so far. It is useful when moves have different costs and can find the least-cost route under the usual conditions, but it may explore many states.

**Greedy Best-First Search** chooses the option that looks closest to the goal. It can be quick, but it may miss the best route because it focuses on the estimate.

**A* (A-star)** combines the cost already paid, `g(n)`, with an estimate of the remaining cost, `h(n)`: `f(n) = g(n) + h(n)`. With suitable cost assumptions and an admissible heuristic (one that does not overestimate the remaining cost), it can find an optimal route. It is used in pathfinding, games, and robotics.

**Iterative deepening** repeats DFS with a depth limit that increases each time. It uses relatively little memory but repeats some work.

## Other ways to approach a problem

**Means-end analysis** compares the current state to the goal and chooses an action that reduces the difference. **Problem reduction** breaks a large task into smaller subgoals. **Hill climbing** moves to a neighbouring state that looks better, but can get stuck at a local maximum: a point that seems best nearby without being the best overall.

## Types of planning

**Classical planning** assumes the world is clearly described and mostly stable. **Hierarchical Task Network (HTN) planning** breaks a big task into smaller tasks. **Reactive planning** changes its plan as the environment changes. **Conditional planning** includes branches for different possible outcomes. **Probabilistic planning** takes account of the chance that actions may succeed or fail.

**STRIPS** describes actions using preconditions and effects. Preconditions are what must already be true; effects are what changes after the action.

For example, to make a sandwich, `spread_peanut_butter(bread)` might require bread and peanut butter to be available. Its effect is that the bread now has peanut butter. A planner links actions like this to reach the goal. A **heuristic** is an estimate that helps the search decide which options to try first.

No one method is best for every problem. The choice depends on how many possibilities there are, whether actions have different costs, how much memory is available, and whether the world might change during planning.
