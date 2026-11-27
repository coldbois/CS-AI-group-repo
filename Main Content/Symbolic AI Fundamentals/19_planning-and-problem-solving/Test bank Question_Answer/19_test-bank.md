# 3.4 Test Bank: Planning and Problem Solving

T21, T22, M21, M22 and O8 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T21 (True or False).** Breadth-first search (BFS) explores a search tree level by level.

**T22 (True or False).** In the wolf–goat–cabbage puzzle, the farmer should take the goat across first.

**M21 (choose ONE).** Breadth-first search (BFS) uses which data structure?

- A. A queue
- B. A hash table
- C. A spreadsheet
- D. A stack

**M22 (choose TWO).** In the river puzzle, which two are rules the farmer must follow?

- A. Never leave the wolf alone with the goat
- B. Never leave the goat alone with the cabbage
- C. The boat can carry everything at once
- D. The goat can row the boat

**O8. River crossing plan** (about 100 words, 5 marks)

A farmer must take a wolf, a goat and a cabbage across a river. The boat holds the farmer plus one thing. Left alone, the wolf eats the goat, and the goat eats the cabbage.

(1) Why must the goat go across first? (2) Describe the plan. (Hint: at one point the farmer brings the goat back.) (3) How is solving this puzzle like a computer searching?

Use these words: state · move · rule · goal · search

**Q1 (choose ONE, slide 42).** Remember the river? Which first crossing is safe?

- A. Take the wolf  B. Take the goat  C. Take the cabbage  D. Cross alone

**Q2.** Using the tree in Figure 3.4c, in what order does DFS visit the nodes?

**Q3 (True or False).** A* always finds the best route, even if its heuristic overestimates. *(Chapter 3 quick quiz)*

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T21 | **True** | BFS checks everything on one level before going deeper. It uses a queue. |
| T22 | **True** | Wolf and cabbage are safe together. Any other first move leaves something to be eaten. |
| M21 | **A** | First in, first out keeps BFS level by level. Depth-first search (DFS) uses a stack (D). |
| M22 | **A, B** | The wolf would eat the goat; the goat would eat the cabbage. The boat carries the farmer plus one item (not C), and only the farmer rows (not D). |
| Q1 | **B** | See T22. |
| Q2 | A B D E C F G | Dive down the left branch first, then back up. |
| Q3 | **False** | The heuristic must be admissible (never overestimate). |

**O8 sample answer (137 words).** The goat must go first because the wolf and the cabbage are safe together. If the farmer took the wolf, the goat would eat the cabbage; if he took the cabbage, the wolf would eat the goat. The plan has 7 crossings: (1) take the goat over, (2) come back alone, (3) take the wolf over, (4) bring the goat back, (5) take the cabbage over, (6) come back alone, (7) take the goat over. Now everyone is safe on the other side. A computer solves this in a similar way. Each arrangement on the banks is a state, each crossing is a move, and the eating rules tell it which states are not allowed. It tries moves, goes back when it gets stuck, and stops when it reaches the goal: everyone across. This is called search.

**O8 key points (1 mark each):** explains why the goat must go first · a correct 7-crossing plan · mentions the trick move: bringing the goat back · uses state, move/action, rule and goal correctly · links trying moves and going back to computer search. *Also accept* the other correct plan: take the cabbage in move 3 and the wolf in move 5.
