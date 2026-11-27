# Breadth-first search for the wolf-goat-cabbage puzzle (3.4).
# A state = the set of things on the LEFT bank. F = farmer, W = wolf, G = goat, C = cabbage.
from collections import deque

ALL = frozenset("FWGC")
START, GOAL = ALL, frozenset()          # everyone left -> everyone right


def safe(bank):
    # A bank without the farmer must not have wolf+goat or goat+cabbage.
    if "F" in bank:
        return True
    return not ({"W", "G"} <= bank or {"G", "C"} <= bank)


def moves(left):
    farmer_left = "F" in left
    here = left if farmer_left else ALL - left
    for item in [None] + [x for x in "WGC" if x in here]:   # cross alone or with one thing
        group = {"F"} | ({item} if item else set())
        new_left = left - group if farmer_left else left | group
        if safe(new_left) and safe(ALL - new_left):       # skip illegal states
            name = {"W": "wolf", "G": "goat", "C": "cabbage"}.get(item)
            if farmer_left:
                action = f"take {name}" if item else "cross alone"
            else:
                action = f"bring {name} BACK" if item else "return alone"
            yield action, frozenset(new_left)


def bfs():
    queue = deque([(START, [])])        # BFS uses a queue (2.5!)
    seen = {START}
    while queue:
        state, plan = queue.popleft()
        if state == GOAL:
            return plan
        for action, nxt in moves(state):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, plan + [(action, nxt)]))


show = lambda s: "".join(x for x in "FWGC" if x in s) or "-"
plan = bfs()
for step, (action, left) in enumerate(plan, 1):
    print(f"{step}. {action:16}  Left: {show(left):5} Right: {show(ALL - left)}")
print(len(plan), "crossings")
