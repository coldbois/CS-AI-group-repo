# Stack (Undo button) and queue (print jobs) from Study Guide pp. 86-87.
from collections import deque

# Undo uses a stack: last in, first out.
stack = []
for word in ["Hello", "big", "world"]:
    stack.append(word)                 # push
    print("type", word.ljust(6), "stack:", stack)

for _ in range(2):
    removed = stack.pop()              # pop the newest
    print("Undo -> removes", removed.ljust(6), "stack:", stack)

print("On screen:", " ".join(stack))

# Print jobs use a queue: first in, first out.
line = deque()
for person in ["Ana", "Ben", "Cho"]:
    line.append(person)                # enqueue at the back

first = line.popleft()                 # dequeue from the front
print("Printed first:", first, "| still waiting:", list(line))
