# Section 8 — Basic C for Operating System Ideas

C is a programming language often used for software that works close to the computer's hardware, including parts of operating systems. The examples here use only variables, simple maths, and `printf`, which prints text on the screen.

## What a small C program looks like

```c
#include <stdio.h>

int main(void) {
    printf("Hello, operating system!\n");
    return 0;
}
```

`#include <stdio.h>` lets the program use tools such as `printf`. `main` is where the program starts. The text inside `printf` appears on screen, and `\n` moves to a new line. `return 0` is the usual way to report that the program finished successfully.

Save the code as `demo.c`. With GCC, compile it using `gcc demo.c -o demo`, then run it on a Unix-like system with `./demo`. A compiler turns source code into a form the computer can run. `%d` prints an integer, while `%.2f` prints a decimal number to two places.

## Example: calculating waiting time

**First Come, First Served (FCFS)** is a simple CPU scheduling method. Jobs are handled in arrival order, so each job waits for those before it to finish.

Suppose three jobs arrive at the same time and need 5, 3, and 8 time units of CPU work:

- Job 1 waits `0` units because it goes first.
- Job 2 waits `5` units for Job 1.
- Job 3 waits `5 + 3 = 8` units for Jobs 1 and 2.

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

The output gives waiting times of `0 5 8` and an average of `4.33`. Dividing by `3.0` allows a decimal result. In C, integer division such as `10 / 4` gives `2`, because the fractional part is dropped. `10 % 4` gives `2`, the remainder.

## What comes later in C?

`if` statements let a program make decisions, and loops repeat steps. Arrays hold several values, functions split code into reusable pieces, and pointers refer to memory addresses. `malloc()` requests dynamic memory and `free()` releases it. Processes and threads are ways an operating system runs programs and paths of execution.

You do not need those advanced features for the examples above. The main point is that even a few lines of C can model a basic operating-system idea.
