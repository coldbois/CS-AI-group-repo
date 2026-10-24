# Section 8: Basic C for Operating System Ideas

## What this section is about

Many operating systems and other low-level system programs are written in **C**, a programming language that provides control over memory and how a computer works. This section uses a few basic C features to model ideas from operating systems.

The examples require only variables, arithmetic, `printf`, and the basic structure of a C program. They do not require advanced programming techniques.

To compile a file named `demo.c` with GCC, run:

```bash
gcc demo.c -o demo
```

Then run the resulting program on a Unix-like system with:

```bash
./demo
```

A compiler such as GCC translates the C source code into a program the computer can run.

## 1. Anatomy of a C program

| Code or feature | What it does |
|---|---|
| `#include <stdio.h>` | Makes declarations from C's standard input/output library available, including `printf`. |
| `int main(void) {` | Defines `main`, the usual entry point of a C program. The C runtime calls it when the program starts. |
| `int x = 5;` | Creates an integer variable named `x` and gives it the value `5`. An integer is a whole number. |
| `printf("...\n");` | Prints text or formatted values. `\n` means “start a new line.” `%d` is a placeholder for an integer, while `%.2f` displays a floating-point value to two decimal places. |
| `return 0;` | Ends `main` and conventionally reports that the program completed successfully. |

In particular, `#include <stdio.h>` is what lets this example use `printf` without declaring it from scratch.

## 2. Demo 1: Hello, operating system

```c
#include <stdio.h>

int main(void) {
    printf("Hello, operating system!\n");
    return 0;
}
```

**Output:**

```text
Hello, operating system!
```

Although the program prints only one line, several layers of software may be involved. `printf` is part of the C standard library. The library uses operating-system services to write the text, typically through a **system call**. A system call is a controlled way for a program to request a service from the operating system's **kernel**, the central component that manages resources such as CPU time, memory, and devices. The operating system and its device software then make the output appear on the screen or terminal.

## 3. Demo 2: Calculating FCFS waiting time

**First come, first served (FCFS)** is a simple scheduling rule: jobs are handled in the order they arrive. A job that arrives after another job must wait for the earlier job to finish.

Suppose three jobs all arrive at time `0`, and their CPU **burst times**—the amounts of CPU time they need—are `5`, `3`, and `8` time units.

- Job 1 starts immediately, so its waiting time is `0`.
- Job 2 waits for Job 1, so its waiting time is `5`.
- Job 3 waits for Jobs 1 and 2, so its waiting time is `5 + 3 = 8`.

The average waiting time is the sum of the three waiting times divided by three.

```c
#include <stdio.h>

int main(void) {
    int burst1 = 5, burst2 = 3, burst3 = 8;

    int wait1 = 0;
    int wait2 = burst1;
    int wait3 = burst1 + burst2;

    double average = (wait1 + wait2 + wait3) / 3.0;

    printf("Waiting times: %d %d %d\n", wait1, wait2, wait3);
    printf("Average waiting time = %.2f\n", average);
    return 0;
}
```

**Output:**

```text
Waiting times: 0 5 8
Average waiting time = 4.33
```

The average is `(0 + 5 + 8) / 3 = 13 / 3`, which is approximately `4.33` time units. The code divides by `3.0` rather than `3` to ensure that the calculation uses floating-point arithmetic and keeps the fractional part.

In C, when both operands are integers, `10 / 4` evaluates to `2`: integer division discards the fractional part. The expression `10 % 4` evaluates to `2`, the remainder after dividing `10` by `4`.

## 4. C topics you will meet later

The examples above are deliberately basic. Later programs can use additional features:

| Feature | What it is useful for |
|---|---|
| `if` statements | Make a decision based on a condition. |
| Loops | Repeat steps, such as processing each job in a scheduling simulation or counting page faults. A **page fault** occurs when a program requests a memory page that is not currently available in the expected state in physical memory. |
| Arrays | Store several related values, such as a sequence of page references, page-table entries, or a queue of jobs. |
| Functions | Split a program into named, reusable pieces. |
| Pointers | Work with memory addresses and linked data structures. A pointer stores an address rather than an ordinary data value. |
| `malloc()` and `free()` | Request and release memory dynamically from an area commonly called the **heap**. |
| `fork()` and threads | Create processes or threads on operating systems that support them. A process is a running program with its own execution context; a thread is a path of execution within a process. |

These topics are not required for the two demos in this section. The demos use only variables, arithmetic, `printf`, and the standard layout of a C program.

## Key takeaways

- `main` is the usual entry point of a C program.
- `printf` produces formatted output; format placeholders such as `%d` and `%.2f` determine how values are displayed.
- FCFS calculates a job's waiting time from the time needed by the jobs placed before it.
- Integer division and floating-point division can produce different results.
- More advanced C features are useful for simulating operating-system behavior, but are not needed for these introductory examples.
