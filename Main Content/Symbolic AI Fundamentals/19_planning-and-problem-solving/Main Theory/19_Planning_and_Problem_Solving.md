# 19. Planning and Problem Solving

## 19.1 Topic overview

AI problem solving is about finding a way to reach a desired result from a starting situation. Planning is about choosing and organising actions so that the goal can be achieved. The ideas are connected: an AI system may search through possible states to find a path, or use a planning representation to describe which actions can change the world.

A simple example is a delivery robot. It starts at a depot, has several possible roads, and must reach a delivery point. It needs a description of its current state, the actions it can take, the goal and possibly the cost of each route. If a road is blocked, the robot may need to plan again.

### Learning outcomes

By the end of this topic, learners should be able to:

1. Describe a problem using an initial state, actions, transition model, goal test and cost.
2. Explain state spaces and search trees.
3. Trace breadth-first search (BFS), depth-first search (DFS) and uniform-cost search (UCS).
4. Explain heuristics, greedy search and A*.
5. Describe classical planning and represent a simple STRIPS action.
6. Formulate a simple constraint-satisfaction problem (CSP).
7. Explain why plans may need to be checked or revised in changing environments.

### Key terms

| Term | Meaning |
|---|---|
| State | A description of the current situation. |
| Initial state | Where the problem starts. |
| Goal test | A check for whether the required goal has been reached. |
| Action | An operation that changes a state. |
| Transition model | A description of the result of an action. |
| Path cost | The total cost of the actions taken so far. |
| Search tree | A structure showing possible states and the paths used to reach them. |
| Heuristic | An estimate used to guide search towards a goal. |
| Plan | A sequence of actions intended to reach a goal. |
| Constraint | A condition that a solution must satisfy. |

## 19.2 Formulating a search problem

Before selecting an algorithm, describe the problem clearly. A common search-problem formulation includes:

1. **Initial state:** The starting position or situation.
2. **Actions:** What the agent is allowed to do from a state.
3. **Transition model:** What state results from each action.
4. **Goal test:** How the system recognises success.
5. **Path cost:** How the cost of a sequence of actions is measured.

### Worked example — a small route problem

A robot starts at A and must reach D. It can follow these connections:

| From | To | Cost |
|---|---|---:|
| A | B | 2 |
| A | C | 1 |
| B | D | 2 |
| C | D | 5 |

- Initial state: A.
- Goal state: D.
- Actions: Move along a connected edge.
- Transition model: Moving along an edge changes the robot's location to the connected node.
- Path cost: Add the costs of the edges used.

There are two routes: A → B → D costs 4; A → C → D costs 6. The cheaper route is A → B → D. This example shows why “fewest steps” and “lowest total cost” are not always the same objective.

## 19.3 State spaces and search trees

A state space is the set of states that may be reached while solving a problem. A search tree shows the alternatives explored from the initial state. Each branch represents an action, and each child node represents the resulting state.

A search algorithm usually keeps a **frontier**: states that have been discovered but not yet expanded. Different algorithms choose the next frontier state in different ways.

A state-space graph may contain cycles or several paths to the same state. Implementations often keep track of visited or reached states to avoid repeating unnecessary work. A search tree and a state-space graph are related, but they are not identical: a tree can show the same state more than once if it is reached by different paths.

## 19.4 Uninformed search

Uninformed search does not use a heuristic estimate of how close a state is to the goal. It uses the problem structure and a rule for choosing which frontier node to expand.

### Breadth-first search (BFS)

BFS explores the shallowest nodes first, moving level by level. It is commonly implemented with a first-in, first-out (FIFO) queue.

For the tree below, assuming children are considered from left to right, BFS visits:

`A, B, C, D, E, F, G`.

BFS finds the shallowest solution. It also finds a minimum-step solution when every action has the same cost. It may use a lot of memory because it stores many nodes at a level.

### Depth-first search (DFS)

DFS follows one branch as far as it can before backtracking. It is commonly implemented with a last-in, first-out (LIFO) stack or recursion.

For the same tree, one possible DFS order is:

`A, B, D, E, C, F, G`.

DFS can use less memory than BFS in some search trees, but it may follow a long or unhelpful branch. It is not guaranteed to find the lowest-cost solution, and in an infinite-depth space it may fail to reach a solution unless limits or cycle checks are used.

### Uniform-cost search (UCS)

UCS expands the frontier path with the lowest total cost so far. It uses a priority queue. With non-negative action costs, UCS finds a least-cost solution. BFS is a special case when every action has the same cost.

| Method | Next node selected | Typical data structure | Main caution |
|---|---|---|---|
| BFS | Shallowest node | Queue | Memory use can be high; optimal only for equal step costs. |
| DFS | Deepest / most recently added node | Stack | Not cost-optimal; can get stuck down a deep branch. |
| UCS | Lowest path cost so far | Priority queue | Can explore many low-cost paths before reaching a distant goal. |

## 19.5 Informed search and heuristics

Informed search uses extra information to guide which states should be explored. A **heuristic function**, written `h(n)`, estimates the remaining cost from state `n` to a goal.

For a map where movement is allowed horizontally and vertically, Manhattan distance can be a useful estimate:

`h(n) = |x_current - x_goal| + |y_current - y_goal|`

It ignores obstacles, so it may be less than the actual route length. The estimate is useful because it gives the search an idea of direction without calculating every complete route first.

### Greedy best-first search

Greedy search chooses the frontier node with the smallest heuristic value `h(n)`. It prefers the node that appears closest to the goal. It can be quick when the estimate is good, but it may choose a poor route because it ignores the cost already spent.

### A* search

A* combines the cost so far with the estimated cost still to come:

`f(n) = g(n) + h(n)`

- `g(n)`: actual cost from the start to the current node.
- `h(n)`: estimated cost from the current node to a goal.
- `f(n)`: estimated total cost of a solution through that node.

**Worked example:**

| Option | `g(n)` so far | `h(n)` estimate | `f(n) = g + h` |
|---|---:|---:|---:|
| B | 2 | 4 | 6 |
| C | 1 | 2 | 3 |

A* gives C the lower estimated total cost and would select it first if these are the current frontier options. This does not mean the estimate is guaranteed to be correct; it guides the search.

An **admissible heuristic** never overestimates the true minimum remaining cost. UC Berkeley’s CS188 notes explain this condition and the A* evaluation function ([Informed Search](https://inst.eecs.berkeley.edu/~cs188/textbook/search/informed.html)). For common graph-search implementations, consistency or a method for reopening a state when a cheaper path is found is also important. Under the standard conditions for A*, this supports finding an optimal solution. A heuristic that overestimates may still be useful in some applications, but it removes the general optimality guarantee.

## 19.6 Classical planning and STRIPS

Classical planning represents a world as a set of facts and describes actions that change those facts. A planner searches for a sequence of actions that changes the initial state into one that satisfies the goal. Basic classical planning often assumes the world is fully known, actions are deterministic, and the relevant facts do not change unexpectedly while the plan is being formed.

### STRIPS action representation

In a STRIPS-style representation, an action has. The original Fikes and Nilsson paper describes operator preconditions and add/delete effects ([IJCAI 1971 paper](https://ijcai.org/proceedings/1971/63)); UBC AIspace gives a teaching explanation of the action lists ([AIspace planning help](https://www.cs.ubc.ca/labs/lci/AIspace/cs322/planning/help/general.shtml)).

- **Preconditions:** Facts that must be true before the action can happen.
- **Add list:** Facts that become true after the action.
- **Delete list:** Facts that become false after the action.

### Worked example — pick up a box

Suppose a robot can pick up a box from a table.

```text
Action: PickUp(Box)

Preconditions:
- OnTable(Box)
- HandEmpty
- Clear(Box)

Add list:
- Holding(Box)

Delete list:
- OnTable(Box)
- HandEmpty
- Clear(Box)
```

If all the preconditions are true, the action can be applied. The new state removes the delete-list facts and adds the add-list facts. The robot is now holding the box. If `HandEmpty` is false, the action is not available under this model.

A plan is a sequence of applicable actions. The planner must check that the actions lead to a state that satisfies the goal, not just that the actions sound reasonable individually.

## 19.7 Constraint-satisfaction problems (CSPs)

Some problems are mainly about assigning values while satisfying restrictions. A CSP is usually described with:

1. **Variables:** What needs a value.
2. **Domains:** The possible values for each variable.
3. **Constraints:** Conditions that limit which combinations are allowed.

### Worked example — a small timetable

Two classes, Mathematics and Physics, must be placed in two time slots: Monday morning and Monday afternoon. The same teacher teaches both classes, so they cannot be at the same time.

- Variables: `Math`, `Physics`.
- Domains: `{Monday morning, Monday afternoon}` for each variable.
- Constraint: `Math ≠ Physics`.

One solution is Mathematics on Monday morning and Physics on Monday afternoon. Swapping the slots is also a solution. The important point is that both assignments satisfy the constraint.

A CSP can be solved with search, checking whether partial assignments can still satisfy the constraints. More advanced methods include backtracking and constraint propagation.

## 19.8 Planning, search and CSP: what is the difference?

| Idea | Main question | Example |
|---|---|---|
| Search problem | Which path reaches the goal? | Find a route through a map. |
| Planning | Which sequence of actions changes the world to the goal state? | Move a robot arm to put a box on a shelf. |
| CSP | Which assignment satisfies all restrictions? | Put classes into time slots without clashes. |

These ideas can overlap. A planner may use search; a CSP may be solved using a search procedure. They describe different ways to formulate a problem.

## 19.9 Applications and limitations

**Applications** include robot navigation, logistics, production scheduling, route finding, game search and timetable planning.

**Limitations** include:

- The number of possible states may grow very quickly.
- A search algorithm may use too much time or memory.
- A heuristic may be inaccurate.
- A plan may fail when the environment changes.
- A simplified model may leave out important real-world conditions.

A practical system may need to observe what happened after each action and replan when its assumptions are no longer true. For example, a delivery robot may need a new route when a corridor is closed.

## 19.10 How this topic connects to the previous topics

Knowledge representation describes the current world and the relationships between objects. Reasoning can establish which facts and conditions hold. Planning then uses the state, available actions and goal to work out what to do. These stages can be combined in a symbolic AI system, although real systems may also use sensors, probability or machine learning.

## Key takeaways

- A search problem needs a start state, actions, transition model, goal test and often a path cost.
- BFS, DFS and UCS differ in how they select the next node.
- A* combines cost so far with a heuristic estimate.
- STRIPS describes actions using preconditions, add effects and delete effects.
- A CSP uses variables, domains and constraints to define valid assignments.
- A plan must be checked against the goal and may need to be updated when the world changes.
