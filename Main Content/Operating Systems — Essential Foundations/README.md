# Chapter 1: Operating Systems

**Dandroid's Body: who is in charge inside the machine?**

Dandroid has just been switched on for the first time. Dozens of programs want the CPU, the memory and the screen at the same time. This chapter introduces the boss that keeps the peace: the operating system.

Suggested time: about 3 hours, including the activities. Study Guide pp. 7–53 · Slides 6–19 · Test Bank T1–T8, M1–M8, O1–O3.

| Topic | One-line summary | Activity |
| --- | --- | --- |
| [1.1 What an Operating System Is](01_What%20an%20Operating%20System%20Is/Main%20Theory/01_main-theory.md) | The manager between apps and hardware. | OS Detective |
| [1.2 Boot Process and the Motherboard](02_Boot%20Process%20and%20the%20Motherboard/Main%20Theory/02_main-theory.md) | UEFI → POST → bootloader → kernel. | Human Boot Relay |
| [1.3 Process and CPU Management](03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md) | Programs in action, taking turns on the CPU. | Process Musical Chairs |
| [1.4 Memory Management](04_Memory%20Management/Main%20Theory/04_main-theory.md) | Desk (RAM) vs bookshelf (storage). | Desk Tidy Challenge |
| [1.5 Device Management and I/O](05_Device%20Management%20and%20InputOutput/Main%20Theory/05_main-theory.md) | Drivers translate; interrupts ring the bell. | Analogy Match & Doorbell Game |
| [1.6 File Systems and Storage](06_File%20Systems%20and%20Storage/Main%20Theory/06_main-theory.md) | A catalogue, paths and backups. | Path Treasure Hunt |
| [1.7 Security and Access Control](07_Security%20and%20Access%20Control/Main%20Theory/07_main-theory.md) | CIA, logins and permissions. | Phishing Spotter & Permission Decoder |
| [1.8 Basic C for Operating System Ideas](08_Basic%20C%20for%20Operating%20System%20Ideas/Main%20Theory/08_main-theory.md) | The language Dandroid's OS is written in. | Predict the Output |

Each topic folder has the same five parts: Main Theory (the lesson), Diagrams and Pictures, Learner Activity (with expected answers), Test bank Question_Answer and Teammate_review.

## Chapter 1 quick quiz

True or false? Decide first, then check the answers.

1. The operating system and the desktop wallpaper are the same thing.
2. UEFI runs before the operating system kernel.
3. A one-core CPU can run two processes at exactly the same instant.
4. A page fault always means the program has crashed.
5. Authentication checks who you are; authorization checks what you may do.
6. In C, `//` starts a comment that the compiler ignores.

**Answers**
1. False: the GUI is only a small part of the OS.
2. True.
3. False: it switches very fast.
4. False: most page faults are normal.
5. True.
6. True.


Next: [Chapter 2: Software](../Software%20Fundamentals/README.md) · Back to [Start Here](../00_Start_Here.md)
