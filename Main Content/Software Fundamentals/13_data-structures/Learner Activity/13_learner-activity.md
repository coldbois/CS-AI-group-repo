# Part 13 — Learner Activity: Pick the Right Structure

**Time:** about 20 minutes · **You need:** pen and paper (Python is optional)

---

## Activity A — Match the problem to the structure

For each situation, choose **array, linked list, stack, queue, tree, graph, or hash table**, and write **one sentence** explaining why.

1. A café app serves coffee orders in the order customers paid.
2. A browser's **Back** button returns you to the page you visited most recently.
3. A student ID card system must find a student's record instantly from their ID number.
4. A navigation app finds a route between cities connected by roads.
5. A company chart shows the CEO, the managers under the CEO, and the staff under each manager.
6. A program stores exactly 7 daily temperatures and often asks "what was the temperature on day 3?"

---

## Activity B — Trace a stack and a queue

Start with an **empty stack** and an **empty queue**. Apply the same operations to both:

```
add 10
add 20
add 30
remove
add 40
remove
```

For the stack, *add* = push and *remove* = pop. For the queue, *add* = enqueue and *remove* = dequeue.

Fill in the table:

| Step | Operation | Stack (bottom → top) | Queue (front → back) |
|---|---|---|---|
| 1 | add 10 | | |
| 2 | add 20 | | |
| 3 | add 30 | | |
| 4 | remove | | |
| 5 | add 40 | | |
| 6 | remove | | |

**Questions:** which values were removed from the stack? Which were removed from the queue?

---

## Activity C — Think deeper (discussion)

A music app has a "Play next" button that puts a song at the front of the waiting list, and an "Add to queue" button that puts it at the back. Is the waiting list a pure stack, a pure queue, or neither? Explain.

---

## ✅ Answers / expected outcomes

### Activity A

| # | Structure | Reason |
|---|---|---|
| 1 | **Queue** | First paid, first served → FIFO. |
| 2 | **Stack** | The most recent page comes back first → LIFO. |
| 3 | **Hash table** | Key (student ID) → value (record) with very fast lookup. |
| 4 | **Graph** | Cities are nodes, roads are edges; routes can loop. |
| 5 | **Tree** | A hierarchy with one root (the CEO) and levels below. |
| 6 | **Array** | A fixed number of items accessed by position (index). |

Other answers can be accepted if the reason is sound, e.g. a sorted array for #3 also works, but a hash table is the usual choice for fast lookup by key.

### Activity B

| Step | Operation | Stack (bottom → top) | Queue (front → back) |
|---|---|---|---|
| 1 | add 10 | `10` | `10` |
| 2 | add 20 | `10, 20` | `10, 20` |
| 3 | add 30 | `10, 20, 30` | `10, 20, 30` |
| 4 | remove | `10, 20` (removed **30**) | `20, 30` (removed **10**) |
| 5 | add 40 | `10, 20, 40` | `20, 30, 40` |
| 6 | remove | `10, 20` (removed **40**) | `30, 40` (removed **20**) |

- Stack removed **30, then 40** (always the newest).
- Queue removed **10, then 20** (always the oldest).

You can check this in Python:

```python
from collections import deque
stack, queue = [], deque()
removed_s, removed_q = [], []
for op in ["add 10", "add 20", "add 30", "remove", "add 40", "remove"]:
    if op == "remove":
        removed_s.append(stack.pop())
        removed_q.append(queue.popleft())
    else:
        value = int(op.split()[1])
        stack.append(value)
        queue.append(value)
print(removed_s, stack)        # [30, 40] [10, 20]
print(removed_q, list(queue))  # [10, 20] [30, 40]
```

### Activity C

**Neither.** "Add to queue" behaves like a queue (add at the back), but "Play next" adds at the front, which a pure queue does not allow. A structure that lets you add and remove at **both** ends is called a **deque** (double-ended queue). Python's `collections.deque` supports this with `appendleft()`.
