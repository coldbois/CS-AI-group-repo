# 1.8 Basic C for Operating System Ideas

![Dandroid saying hello](../../../assets/dandroid/dandroid-confident.png)

**Chapter 1 · Dandroid's Body** · Study Guide pp. 46–51 · Slide 18 · Test Bank T8, M8

> **Mission.** Most of Dandroid's operating system is written in a language called C. Let's read Dandroid's very first words... and make Dandroid count.

**You will learn to**

- read a tiny C program line by line
- use variables and `printf`
- explain how a running C program relates to the OS

**Key words:** C, main, printf, variable, int, comment

---

## Why C?

C was created in the early 1970s by Dennis Ritchie at Bell Labs to write the Unix operating system. It is still the language of most OS kernels (Linux, much of Windows and macOS) and device drivers, because it is fast and lets programmers work close to the hardware. You don't need to become a C programmer for this module. You only need to *read* a few lines.

## Dandroid says hello

![Figure 1.8a](../Diagrams%20and%20Pictures/1-8_hello-world.png)

*Figure 1.8a. Your first C program (Study Guide p. 47). The file is in [hello.c](../Learner%20Activity/code/hello.c).*

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, world!\n");
    return 0;
}
```

| Line | What it means |
| --- | --- |
| `#include <stdio.h>` | brings in the standard input/output tools, such as `printf` |
| `int main(void)` | where the program starts. Every C program begins in `main` |
| `printf("Hello, world!\n");` | prints the text. `\n` means "new line". The `;` ends the statement |
| `return 0;` | tells the OS "I finished successfully" (any other number means an error) |

**Output:** `Hello, world!`

## Variables: labelled boxes in memory

A **variable** is a named box in memory that holds a value. In C you must say what kind of value goes in the box. `int` means a whole number.

![Figure 1.8b](../Diagrams%20and%20Pictures/1-8_variables.png)

*Figure 1.8b. Variables (Study Guide p. 48). The file is in [time_slice.c](../Learner%20Activity/code/time_slice.c).*

```c
// Give each process a short turn.
int time_slice = 2;
int processes = 3;
int total_time = time_slice * processes;
printf("Total time: %d\n", total_time);
```

- `//` starts a **comment**: a note for humans that the compiler ignores.
- `int time_slice = 2;` makes a box called `time_slice` that holds 2.
- `*` multiplies: 2 × 3 = 6.
- `%d` is a gap where `printf` puts a whole number.

**Output:** `Total time: 6`

> **Bug alert.** This is just arithmetic, not a real scheduler. But it is a real **process**: while it runs, the OS gives it CPU time and memory, and its variables live in the memory the OS gave it ([1.3](../../03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md), [1.4](../../04_Memory%20Management/Main%20Theory/04_main-theory.md)).

## From source code to a running process

C is a **compiled** language. A program called a compiler (for example `gcc`) translates the whole file into machine code *before* it runs:

```
hello.c  →  compiler (gcc)  →  hello.exe  →  the OS loads it into memory as a process
```

If the code breaks C's grammar, for example a missing `;`, the compiler refuses to build it and points to the line. This is a **syntax error**. With `gcc`, a missing `;` after `return 0` gives:

```
error: expected ';' before '}' token
```

The compiler only checks grammar. It can't tell whether your *idea* is right. A program that runs but gives the wrong answer has a **logic error**, and you will hunt one in [2.3](../../../Software%20Fundamentals/11_computer-programming/Main%20Theory/11_main-theory.md).

## Running the examples

- **Online, no install:** paste the code into a free online C compiler such as OnlineGDB (onlinegdb.com/online_c_compiler) and press Run.
- **On your own computer:** with `gcc` installed, run `gcc hello.c -o hello`, then `./hello` (or `hello.exe` on Windows).
- **No internet:** predict the output on paper, then check against the answers in the activity.

## Try it

**Predict the Output** (15 min, solo): predict, run, change and break four tiny C programs. Instructions and answers: [08_learner-activity.md](../Learner%20Activity/08_learner-activity.md).

## Going further (optional)

- **Integer division.** `7 / 2` in C gives `3`, not `3.5`, because both numbers are `int` and the part after the point is thrown away. Write `7 / 2.0` to get `3.5`.
- **A tiny scheduler calculation.** [fcfs_wait.c](../Learner%20Activity/code/fcfs_wait.c) uses a loop and an array to compute the FCFS waiting times from 1.3. It prints `P1 waits 0`, `P2 waits 8`, `P3 waits 10` and `Average wait: 6.0`, the same numbers as Figure 1.3b.
- **The four stages of building.** `gcc` actually runs the preprocessor (handles `#include`), the compiler (C → assembly), the assembler (assembly → machine code) and the linker (joins your code with library code such as `printf`).

## Check yourself

1. Where does every C program start running?
2. What does `int score = 10;` do?
3. Why does memory protection matter for C programs?

**Answers (try first, then peek)**
1. In the `main` function.
2. Creates a whole-number variable called `score` that holds 10.
3. A buggy C program can misuse memory; the OS stops it from damaging other programs.


More questions: [08_test-bank.md](../Test%20bank%20Question_Answer/08_test-bank.md)

## Remember

- C is used to build operating systems and drivers.
- Variables are named boxes in memory.
- A running C program is a process managed by the OS.

## Watch and explore

**OnlineGDB C compiler** (onlinegdb.com/online_c_compiler). Run every code example in this topic and change one value each time. It needs internet, and some school networks block it; predict on paper instead.

## References

- Kernighan, B. W., & Ritchie, D. M. (1988). *The C Programming Language* (2nd ed.). Prentice Hall.
- Ritchie, D. M. (1993). The development of the C language. *ACM SIGPLAN Notices, 28*(3), 201–208.

---

Previous: [1.7 Security](../../07_Security%20and%20Access%20Control/Main%20Theory/07_main-theory.md) · Next: [Chapter 2: Software](../../../Software%20Fundamentals/README.md) · Up: [Chapter 1 overview](../../README.md)
