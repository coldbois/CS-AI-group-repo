# Try it: River Crossing Challenge (3.4)

**Time:** 20 min · **Group:** pairs · **You need:** 4 paper cut-outs and a drawn river · Study Guide pp. 133–134 · Slides 2, 42–43 · Linked Test Bank question: O8

**Goal:** solve a planning puzzle by hand, then describe it the way an AI planner would.

## Prepare

Cut out four pieces of paper: **Farmer, Wolf, Goat, Cabbage**. Draw a river with a left and a right bank. Everyone starts on the left.

**The rules:** the boat holds the farmer plus at most one item. Only the farmer rows. Left alone (without the farmer), the wolf eats the goat, and the goat eats the cabbage.

## Steps

1. **Predict:** how many crossings will you need?
2. Solve it by moving the cut-outs. Record every crossing.
3. Write the state after each move, e.g. `Left: W C | Right: F G`.
4. Circle any move you tried that was illegal (someone got eaten!).
5. List the start state, the goal state, the legal actions and the constraints.

## Record

| Move | Farmer takes... | Left bank | Right bank |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| ... | | | |

## Reflect

- Why is taking the goat first the only safe opening move?
- Which tempting move fails, and why?
- How is your list like a computer "searching" the possibilities?

## Check it: expected results

A 7-crossing plan:

| Move | Farmer... | Left bank | Right bank |
| --- | --- | --- | --- |
| 1 | takes the goat | W C | F G |
| 2 | returns alone | F W C | G |
| 3 | takes the wolf | C | F W G |
| 4 | **brings the goat back** | F G C | W |
| 5 | takes the cabbage | G | F W C |
| 6 | returns alone | F G | W C |
| 7 | takes the goat | (empty) | F W G C |

- Swapping the wolf and the cabbage in moves 3 and 5 also works.
- Taking the wolf or the cabbage first leaves the goat with something it eats, or something that eats it.
- **Start:** all on the left. **Goal:** all on the right. **Actions:** the farmer crosses with 0 or 1 item. **Constraint:** never leave W+G or G+C alone.
- The hard part is move 4: bringing the goat back feels like going backwards, so it is easy to get stuck with the wolf and the goat together on one bank.
- Trying moves and backing up when stuck is **search through a state space**. The program [river_bfs.py](code/river_bfs.py) does the same thing with breadth-first search and prints this plan.
