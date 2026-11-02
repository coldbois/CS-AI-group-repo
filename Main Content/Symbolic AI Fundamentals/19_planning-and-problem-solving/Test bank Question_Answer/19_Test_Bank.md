# Topic 19 — Test Bank

## A. Short answer

1. What is the difference between problem solving and planning in AI?
2. Name five parts of a search-problem formulation.
3. What is a state space?
4. How does BFS choose the next node? How does DFS choose it?
5. What does uniform-cost search use to choose the next node?

## B. Explain or compare

6. Why is BFS optimal only when all step costs are equal?
7. What is a heuristic? Give one example.
8. Explain the meaning of `g(n)`, `h(n)` and `f(n)` in A*.
9. Compare a search problem, a planning problem and a CSP.

## C. Apply the idea

10. A route has cost 4 so far and an estimated remaining cost of 7. Calculate its A* value.
11. A* has two frontier options: X has `g=2, h=6`; Y has `g=5, h=2`. Which one has the lower `f` value?
12. For the action `PickUp(Box)`, explain why `HandEmpty` might be a precondition and `Holding(Box)` an add-list effect.
13. A timetable has variables `Math` and `Physics`, each with the domain `{Morning, Afternoon}`. The same teacher teaches both. Write the constraint and give one valid assignment.
14. Give two reasons why a robot may need to replan after it has started following a plan.
