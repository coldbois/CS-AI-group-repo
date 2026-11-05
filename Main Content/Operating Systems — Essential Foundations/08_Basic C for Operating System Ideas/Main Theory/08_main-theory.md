## Chapter 8: C for Operating Systems: Seeing the Ideas in Code

Most operating systems are written in C. So far you have met the basics: `#include <stdio.h>`, `main`, variables, arithmetic and printf. The two short programs below use only those, and each one calculates an idea from the OS sections so you can check your hand calculations. Compile with `gcc demo.c -o demo` and run with `./demo`.

### 8.1 Anatomy of a C program

| **Line**              | **What it does**                                                                           |
|-----------------------|--------------------------------------------------------------------------------------------|
| `#include <stdio.h>` | Brings in the standard input/output library, which provides printf                         |
| `int main(void) {`      | The starting point: the OS begins running your program here                                |
| `int x = 5;`            | Declares a whole-number variable and gives it a value                                      |
| `printf("...\n");`      | Prints text; `\n` starts a new line, `%d` prints an int, `%.2f` prints a decimal with two places |
| `return 0;`             | Tells the OS the program finished successfully                                             |

`#include <stdio.h>` brings in the standard input/output library so you can use printf.

### 8.2 Demo 1: Hello, operating system

```c
#include <stdio.h>

int main(void) {
    printf("Hello, operating system!\n");
    return 0;
}
```

Output: `Hello, operating system!`. Behind this one line, printf calls the C library, which makes a write system call into the kernel, which sends the text to the screen (see The Operating System and Its Kernel).

### 8.3 Demo 2: FCFS waiting time

Three jobs arrive at time 0 with bursts 5, 3 and 8. Under first come, first served, each job waits for all the jobs before it.

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

Output: `Waiting times: 0 5 8` and `Average waiting time = 4.33`. Dividing by 3.0 instead of 3 keeps the decimal part; with 3 the division would be done in whole numbers and drop the decimals.

In C, 10 / 4 when both numbers are ints is 2 (the decimal part is dropped) and 10 % 4 is 2 (the remainder).

### 8.4 What you will learn later in C

As the course moves on, you will meet loops and if statements (to simulate a scheduler or count page faults step by step), arrays (for reference strings, page tables and ready queues), functions (to split a simulator into reusable parts), pointers (memory addresses, linked lists, how the heap works), malloc and free (dynamic allocation on the heap, see Memory), and fork and threads (creating processes and threads, see Running Programs). None of these are needed for the two demos above — they only use variables, arithmetic and printf.

## Visual References

![Figure 8.1: Overview of compiling with gcc](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMKKIq3ZopoE7Fs-nUDFmQfhJ2EsQCnI4lOtoee64vgLJ9bnObf2Iu2Fs&s=10)

*Figure 8.1. Overview of compiling with gcc. Source: [Medium](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMKKIq3ZopoE7Fs-nUDFmQfhJ2EsQCnI4lOtoee64vgLJ9bnObf2Iu2Fs&s=10).*

![Figure 8.2: Programming using C and output](https://user-images.githubusercontent.com/47841385/104401862-0277f680-5590-11eb-8e94-ec0112d71569.png)

*Figure 8.2. Programming using C and output. Source: [GitHub](https://user-images.githubusercontent.com/47841385/104401862-0277f680-5590-11eb-8e94-ec0112d71569.png ).*

![Figure 8.3: Diagram of the anatomy of a C program](https://www.startertutorials.com/blog/wp-content/uploads/2016/04/structure-of-cprogram.png)

*Figure 8.3. Diagram of the anatomy of a C program. Source: [Starter Tutorials](https://www.startertutorials.com/blog/wp-content/uploads/2016/04/structure-of-cprogram.png).*

## Bringing It Together: The Great Invention

Every chapter above is one department of the same company. The best way to see this is to follow one simple action from start to finish: **you press the power button and open a game.**

### The story

1. **Motherboard and boot (Chapter 2).** You press the power button. Electricity flows across the motherboard, UEFI wakes up, POST checks the parts, and the bootloader loads the kernel into RAM.
2. **The OS takes charge (Chapter 1).** The kernel starts in kernel mode, loads the drivers and shows the login screen.
3. **Security (Chapter 7).** You log in. The OS checks your password and gives you the permissions of a normal user.
4. **Files (Chapter 6).** You double-click the game. The file system finds the game's files on your SSD using their path.
5. **Processes (Chapter 3).** The OS creates a process for the game. The scheduler gives it CPU time while your music app keeps running too.
6. **Memory (Chapter 4).** The OS gives the game its own private part of RAM through virtual memory, and loads the needed pages from the SSD.
7. **Devices (Chapter 5).** Drivers let the game talk to the GPU for graphics, the keyboard and mouse for control (using interrupts), and the speakers for sound. If the game uses AI for characters or upscaling, the NPU or GPU can help.
8. **C (Chapter 8).** Much of the OS code that did all of this, and many drivers, are written in C. The game's own requests reach the kernel through system calls.

### The bridge: one table

| Chapter | Its job in one line | Without it |
| --- | --- | --- |
| 1. The OS and its kernel | The manager of the computer | Apps would fight over the hardware |
| 2. Boot and the motherboard | Wakes everything up and connects the parts | The computer could not even start |
| 3. Processes and the CPU | Shares the CPU fairly | Only one program could run |
| 4. Memory | Gives each program safe space | Programs would overwrite each other |
| 5. Devices and I/O | Lets software use hardware | Keyboard, screen and GPU would be useless |
| 6. Files and storage | Saves and finds data | Everything would vanish at shutdown |
| 7. Security | Protects users and data | Anyone or any program could damage the system |
| 8. C | The language the OS is built from | The OS would be slower and harder to build |

### Why the operating system is a great invention

- **It hides complexity.** You click an icon, and the OS handles thousands of tiny steps across the CPU, memory, storage and devices.
- **It shares resources fairly.** Many programs and many users can use one computer at the same time.
- **It protects.** One crashed app does not take down the whole machine.
- **It lets software be written once and run on many machines.** A programmer does not need to learn every keyboard, drive and screen in the world.
- **It is the foundation for everything else.** Browsers, games, apps, AI tools and the internet all stand on top of an operating system.

In short: the hardware is the body, the operating system is the brain and nervous system that makes the body useful, and the applications are the things you actually do. Without the operating system, a computer is just a box of very expensive parts.

## Practice: Check Yourself and Test Bank

Work through these after reading the guide, using the worked examples as models. There are 26 questions: 8 application questions where you show your steps, 7 fill in the blanks and 11 true or false. Each question names its chapter. Check your work against the answers underneath.

## References

The topics in this guide are standard operating systems content. Typical orders of magnitude for speeds and sizes come from these kinds of sources, so check any figure you reuse against them.

1. Arpaci-Dusseau, R. H. and Arpaci-Dusseau, A. C. *Operating Systems: Three Easy Pieces*. Free online book at [ostep.org](https://pages.cs.wisc.edu/~remzi/OSTEP/). Covers processes, scheduling, virtual memory, paging, I/O and file systems (Chapters 1, 3, 4, 5, 6).
2. Silberschatz, A., Galvin, P. B. and Gagne, G. *Operating System Concepts*, 10th edition. Wiley, 2018. Covers scheduling, deadlock, page replacement and file systems (Chapters 3, 4, 6).
3. Tanenbaum, A. S. and Bos, H. *Modern Operating Systems*, 4th edition. Pearson, 2014. Covers kernel designs, memory management and security (Chapters 1, 4, 7).
4. Kernighan, B. W. and Ritchie, D. M. *The C Programming Language*, 2nd edition. Prentice Hall, 1988. Covers the basic C used in the demos (Chapter 8).
5. Hennessy, J. L. and Patterson, D. A. *Computer Architecture: A Quantitative Approach*. Morgan Kaufmann. Covers the memory hierarchy, caches and the TLB (Chapter 4).
6. UEFI Forum. *UEFI Specification*. [uefi.org](https://uefi.org/specifications). Covers firmware, the boot process and Secure Boot (Chapters 2, 7).
7. PCI-SIG and NVM Express. PCIe and NVMe specifications at [pcisig.com](https://pcisig.com) and [nvmexpress.org](https://nvmexpress.org). Cover buses, lanes and SSD queues (Chapters 2, 5, 6).
8. The Linux kernel documentation at [kernel.org/doc](https://www.kernel.org/doc/html/latest/). Covers the Linux scheduler, memory management and device drivers (Chapters 3, 4, 5).