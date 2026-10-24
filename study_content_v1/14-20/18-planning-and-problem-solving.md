# Section 18: Planning and Problem Solving

## 1. What is AI problem-solving and planning?

In AI, **problem-solving** means finding a sequence of actions that can move a system from its current situation to a desired goal. **Planning** means deciding on such a sequence, often before carrying out the actions.

A maze is a useful analogy. You begin at the entrance, explore possible routes, and try to reach the exit. In a computer model, the entrance is the **initial state**, the exit is the **goal state**, and moving through the maze represents taking actions.

## 2. Four elements of a problem

| Element | Meaning | Example in a maze |
|---|---|---|
| Initial state | The situation at the start. | Your location at the entrance. |
| Actions or operators | Choices that change one state into another. | Move north, south, east, or west where allowed. |
| Goal test | A check that tells the system whether it has reached the goal. | Check whether the current location is the exit. |
| Path cost | A measure of how expensive a sequence of actions is. | Number of moves, distance traveled, time, or energy used. |

A **state-space search** explores the states that could be reached from the initial state by applying available actions, looking for a state that satisfies the goal test.

## 3. Common problem-solving methods

| Method | How it works | Important point |
|---|---|---|
| Means-end analysis | Compare the current state with the goal, identify a difference, and choose an action intended to reduce it. | Helps break a large gap between current and desired conditions into manageable steps. |
| Uninformed (blind) search | Explores states without a special estimate of how close they are to the goal. Examples include DFS, BFS, and uniform-cost search (UCS). | It uses only the problem definition and search rules, not a goal-distance heuristic. |
| Informed (heuristic) search | Uses a **heuristic**, an estimate that helps guide the search. Examples include Greedy Best-First Search and A*. | A useful estimate can reduce unnecessary exploration. |
| Problem reduction | Break a difficult problem into smaller subproblems. | The smaller subproblems must still combine into a solution to the original problem. |
| Hill climbing | Repeatedly move to a neighboring state that looks better according to the chosen evaluation. | Can get stuck at a local maximum or another point where no nearby move looks better. |
| Iterative deepening | Run depth-first search with a depth limit of 1, then 2, then 3, and so on. | Combines some memory advantages of DFS with the ability to search progressively deeper. |

## 4. Search algorithms compared

| Algorithm | Basic idea | Strength | Weakness or condition |
|---|---|---|---|
| Depth-first search (DFS) | Follow one path as deeply as possible, then backtrack when it cannot continue. | Often uses relatively little memory. | Does not generally find the shortest path; in some search spaces it can spend a long time in deep branches. |
| Breadth-first search (BFS) | Explore all states one step away, then two steps away, and so on. | Finds a path with the fewest steps when every action has the same cost. | Can require a large amount of memory because it stores many frontier states. |
| Uniform-cost search (UCS) | Expand the frontier path with the lowest total cost so far. | Finds a least-cost solution under the usual nonnegative-cost assumptions. | May explore many states before reaching the goal. |
| Greedy Best-First Search | Choose the state that appears closest to the goal according to a heuristic `h(n)`. | Can be fast when the heuristic is useful. | Does not guarantee the shortest or cheapest path in general. |
| A* search | Evaluate nodes using `f(n) = g(n) + h(n)`, where `g(n)` is the cost so far and `h(n)` estimates the remaining cost. | Can find an optimal least-cost path when the heuristic and search conditions meet the required assumptions. It is used in pathfinding, robotics, and games. | May use significant memory and depends on a suitable heuristic. |

### Understanding the A* formula

- `n` represents a state or search node.
- `g(n)` is the known cost from the start to `n`.
- `h(n)` is an estimate of the remaining cost from `n` to the goal.
- `f(n)` combines the actual cost so far with the estimated cost still to come.

The source says A* is optimal if the heuristic is **admissible**. An admissible heuristic never overestimates the true remaining cost. Optimality also relies on the usual assumptions about path costs and the implementation/search setting; the heuristic condition alone should not be treated as a universal guarantee for every possible implementation.

## 5. Types of planning

| Type | Main idea |
|---|---|
| Classical planning | Plans in a well-defined, static environment where the relevant facts are known. The planner may search forward from the initial state or backward from the goal. |
| Hierarchical Task Network (HTN) planning | Break a complex task into smaller tasks and subgoals, repeating this decomposition until the tasks can be carried out. |
| Reactive planning | Chooses or adjusts actions in response to the environment, rather than depending entirely on one complete plan computed in advance. |
| Conditional or contingent planning | Includes branches for different possible outcomes. The plan says what to do if one outcome occurs and what to do if another occurs. |
| Probabilistic or stochastic planning | Accounts for actions whose outcomes are uncertain or have different probabilities, often considering risk and expected cost. |
| STRIPS | Represents planning actions with preconditions and effects. A precondition states what must be true before an action can be performed; effects describe what changes after it is performed. |

## 6. STRIPS worked example: making a sandwich

The source uses making a sandwich to illustrate action planning.

- **Goal:** Make a sandwich.
- **Initial state:** Ingredients are available on the table.
- **Action/operator:** `spread_peanut_butter(bread)`.
- **Preconditions:** Bread exists and peanut butter is available.
- **Effect:** The bread now has peanut butter spread on it.

A planner can link actions together. For example, it may ensure bread is available, spread peanut butter, add other ingredients, and assemble the sandwich. Each action must be applicable in the state produced by the preceding actions.

A **heuristic** is a function that estimates the cost or distance between the current state and the goal. In a maze, straight-line distance to the exit might be a heuristic; in a task-planning problem, a heuristic might estimate how many actions remain.

## 7. Key takeaways

- A problem-solving task can be described using an initial state, actions, a goal test, and a path cost.
- Search algorithms differ in how they select the next state and in their memory, speed, and optimality properties.
- Heuristics guide search but do not automatically guarantee a best solution.
- Planning can be classical, hierarchical, reactive, conditional, probabilistic, or based on action operators such as STRIPS.
