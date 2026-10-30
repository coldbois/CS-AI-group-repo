# Section 20 — Putting Software and Symbolic AI Together

The topics in this guide fit together in layers. Hardware provides the computer's physical parts. The operating system manages resources such as CPU time, memory, files, and devices. System software and developer tools help people build and run programs. Applications use algorithms and data structures to solve problems. Software engineering gives teams a process for building and maintaining these programs. Symbolic AI adds facts, rules, reasoning, and planning.

## How the pieces can work together

In a neuro-symbolic system, a machine-learning model might process an image or sound and produce a label. A symbolic rule engine can use that label with other facts to reach a decision. The model might run on a GPU or NPU while the rule engine runs on a CPU. The operating system helps schedule the work and manage memory and devices. This is one possible setup, not a requirement for all AI systems.

A few OS ideas are worth remembering:

- A **process** is a running program with its own address space and resources.
- A **thread** is a path of execution inside a process. Threads in one process usually share code, heap memory, and open files, but each thread has its own stack and execution state.
- **Compilation** translates code into another form before it runs. **Interpretation** executes code through an interpreter at runtime. Modern language systems may combine both approaches.
- **Forward chaining** starts with facts and applies rules to reach conclusions. **Backward chaining** starts with a goal and checks whether facts and rules support it.
- A **page table** maps virtual pages to physical frames in RAM. A **TLB** keeps recent address translations nearby, so the processor does not need to look them up in the page table every time.

The main takeaway is that software and AI rely on the same computer systems underneath. Understanding how programs are organised, how data is stored, and how the operating system manages resources makes it easier to understand how an AI program actually runs.
