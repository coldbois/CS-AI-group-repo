# Try it: Maze Race: BFS vs Greedy vs A* (3.4)

**Time:** 15 min · **Group:** solo · **You need:** a laptop browser · Study Guide pp. 139–140

**Goal:** watch search algorithms explore a maze and compare how much each one searches.

## Prepare

Open **PathFinding.js Visual** (qiao.github.io/PathFinding.js/visual). It is free and needs no account. On a phone or offline? Use the descriptions in "Check it" below instead.

## Steps

1. Draw a wall between the green start and the red end (click and drag).
2. **Predict:** which algorithm will explore the fewest squares?
3. Choose **Breadth-First-Search** and press **Start**. Note the path length and how much of the grid is coloured (explored).
4. Clear the path (keep the walls). Run **Best-First-Search**, then **A\***.
5. Make a U-shaped trap around the start, open towards the goal's opposite side, and run all three again.

## Record

| Algorithm | Path length | Explored: a lot / a little? |
| --- | --- | --- |
| Breadth-First | | |
| Best-First (greedy) | | |
| A* | | |

## Reflect

- Why does BFS colour so many squares?
- When did greedy best-first get fooled by the trap?
- Why is A* a good compromise?

## Check it: what to look for

- **BFS** spreads out in every direction like a ripple. It finds a shortest path but explores the most.
- **Greedy best-first** rushes towards the goal using only the estimate h(n), so walls can trick it into a longer path. The U-shaped trap shows this best.
- **A\*** uses cost so far + estimate. It usually explores less than BFS and still finds a shortest path (with an admissible heuristic such as Manhattan distance).
- Exact numbers depend on your walls and settings, so record them before you compare with a classmate.
