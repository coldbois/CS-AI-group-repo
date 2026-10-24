# Section 9 — Where Operating Systems Meet Symbolic AI

An operating system (OS) manages a computer's resources. It shares CPU time, manages memory, and helps software use devices. These jobs matter to AI programs too.

**Symbolic AI** works with facts, symbols, rules, and logic. **Neural AI**, including deep learning, learns patterns from examples and often performs lots of numerical calculations.

## Why they use hardware differently

Symbolic AI may search a graph, compare facts with rules, or test possible solutions. The next step often depends on what it has found, so a CPU is a natural fit. Neural networks often repeat similar calculations across huge arrays of numbers. GPUs and NPUs can do many of these calculations in parallel.

These are general tendencies, not strict rules. Symbolic systems can use accelerators too, and not every neural network needs a GPU.

Symbolic programs may use lists, trees, and graphs, which can mean jumping between different places in memory. Neural networks often work with large arrays. The OS helps each program get processor time and memory, while device drivers help software communicate with hardware.

## Connecting AI ideas to the OS

- **Breadth-first search (BFS)** checks options one depth level at a time. It keeps a queue of options to visit, which can use a lot of memory.
- **Depth-first search (DFS)** follows one path as far as it can, then goes back to try another. It often uses less search memory, but very deep recursion can overflow the call stack.
- **Iterative deepening** runs depth-limited DFS repeatedly, increasing the limit each time. It repeats some work to save memory.
- **Garbage collection** automatically reclaims memory a program no longer needs. Lisp is historically associated with early garbage collection. In C, programmers often manage dynamic memory with `malloc()` and `free()`.
- **Rule engines** apply rules to facts. The Rete algorithm remembers partial matches so it does not have to repeat every comparison, trading extra memory for less work.
- **Expert systems** such as MYCIN, XCON, and CLIPS use stored facts and rules. Like other programs, they need memory and CPU time from the OS.
- **Semantic networks and ontologies** store concepts and relationships. Their speed can depend on how the data is arranged and accessed in memory.
- **Planning systems**, including A*, use structures such as priority queues and hash tables to keep track of possible paths and states already visited.

AI algorithms do not run in a vacuum. The way they search and store data affects the memory and processing time they need.

## A simple neuro-symbolic example

Imagine a system that looks at a medical image and helps explain a decision:

1. A scanner provides an image.
2. A machine-learning model analyses it, often using a GPU or NPU.
3. The model produces a label, such as “possible tumour detected.”
4. A symbolic rule engine checks that label alongside other facts and rules.
5. The system returns a result and may show which rules led to it.

The OS schedules the work and manages memory and device access. The model might run on an accelerator while the rule engine runs on the CPU, but actual designs can differ. This is an example of a possible setup, not a requirement.
