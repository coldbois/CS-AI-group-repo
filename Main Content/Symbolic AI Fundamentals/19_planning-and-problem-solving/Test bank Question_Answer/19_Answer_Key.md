# Topic 19 — Answer Key

1. Problem solving is the broader process of finding a solution. Planning focuses on choosing and ordering actions to reach a goal.
2. Initial state, actions, transition model, goal test and path cost.
3. The set of states that may be reached in the problem.
4. BFS chooses the shallowest frontier node. DFS chooses the deepest or most recently added frontier node, depending on implementation order.
5. It selects the frontier path with the lowest total cost so far, usually using a priority queue.
6. BFS counts steps, not different action costs. If all steps cost the same, fewer steps also means lower cost; otherwise it may miss a cheaper path with more steps.
7. A heuristic estimates the remaining cost to a goal. For example, Manhattan distance estimates grid distance when movement is horizontal or vertical.
8. `g(n)` is the cost already paid; `h(n)` is the estimated remaining cost; `f(n)` is their sum.
9. Search asks which path reaches a goal; planning asks which sequence of actions changes the world to the goal; a CSP asks which variable assignments satisfy constraints.
10. `f = 4 + 7 = 11`.
11. X: `f=2+6=8`. Y: `f=5+2=7`. Y has the lower value and is selected first by A* among these options.
12. `HandEmpty` ensures the robot has a free hand before picking up the box. `Holding(Box)` becomes true after the action succeeds.
13. Constraint: `Math ≠ Physics`. One valid assignment is Math in the morning and Physics in the afternoon.
14. The route may become blocked; a new obstacle or changed destination may appear; the robot's model of the environment may be incomplete; or an action may not have the expected result.

## Marking note

For questions 1, 6, 9, 12 and 14, give credit for clear explanations that correctly use the concepts from the Main Theory.
