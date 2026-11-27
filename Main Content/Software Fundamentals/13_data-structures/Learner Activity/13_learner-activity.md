# Try it: Data Structure Match-Up (2.5)

**Time:** 20 min · **Group:** solo or pairs · **You need:** pen and paper · Study Guide pp. 88–89 · Slides 28–29 · Linked Test Bank question: O5

**Goal:** pick the right structure for real situations, and trace a stack and a queue.

**Word bank:** array · linked list · stack · queue · tree · graph · hash table

## Steps

1. **Match** each situation to a structure and write "I chose it because...":
   - (a) coffee made in the order people paid
   - (b) the browser Back button
   - (c) find a student by ID instantly
   - (d) folders inside folders
   - (e) who is friends with whom
2. **Stack:** put three books on a pile: Red, then Blue, then Green. Now take one. Which book? What's left?
3. **Queue:** Ana, Ben and Cho join a bus line in that order. The bus takes one person. Who gets on? Who's waiting?
4. **Tree:** draw a tree of your family or school with at least 6 boxes. Label the root and the leaves.

## Record

- Each match with "I chose it because...".
- Draw the pile and the line after each step.

## Reflect

- Which situations had more than one sensible answer?
- Which structure did the OS use in [1.3](../../../Operating%20Systems%20%E2%80%94%20Essential%20Foundations/03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md) to line up processes?

## Check it: expected answers

| Situation | Structure | Why |
| --- | --- | --- |
| (a) coffee in order paid | **queue** | first in, first out |
| (b) Back button | **stack** | the most recent page comes back first |
| (c) student by ID | **hash table** | jump straight to the slot for that ID |
| (d) folders in folders | **tree** | one root, many levels |
| (e) friendships | **graph** | anyone can link to anyone |

- **Stack:** you take **Green**; left (bottom → top): Red, Blue.
- **Queue:** **Ana** gets on; still waiting: Ben, Cho.
- **Tree check:** exactly one root; every other box has one parent; leaves have no children.
- The OS's ready queue in 1.3 is a **queue**.
- Situations with two sensible answers: (c) could be an array if IDs are small numbers like 0–99 (the ID is the index). That's a good answer if you explain it.
