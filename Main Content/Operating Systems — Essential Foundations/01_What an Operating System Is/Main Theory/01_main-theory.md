# 1.1 What an Operating System Is

![Dandroid looking curious](../../../assets/dandroid/dandroid-curious.png)

**Chapter 1 · Dandroid's Body** · Study Guide pp. 8–12 · Slides 6–7 · Test Bank T1, M1

> **Mission.** Dandroid has 30 apps open. Every one of them wants the screen, the CPU and the memory right now. Who decides who gets what?

**You will learn to**

- explain what an operating system (OS) does
- describe the kernel, user mode and kernel mode
- explain how a system call lets an app ask the OS for help

**Key words:** operating system, kernel, user mode, kernel mode, system call

---

## The OS is the manager

An **operating system** is the software that manages the computer's hardware and shares it between all the programs that want to use it. Windows, macOS, Linux, Android and iOS are all operating systems.

We use a restaurant to picture it (the same picture is on slide 7). The customers are the apps. The kitchen is the hardware: the CPU, the memory, the disk and the screen. The manager is the OS. Customers never walk into the kitchen and start cooking. They tell the manager what they want, and the manager decides who is served next.

![Figure 1.1a](../Diagrams%20and%20Pictures/1-1_os-layers.png)

*Figure 1.1a. Where the OS sits. Read it from the top: you click and type, apps ask the OS for help, and only the OS controls the hardware. (Same diagram as Study Guide p. 9.)*

## Kernel, user mode and kernel mode

The **kernel** is the core of the OS. It is the part that stays in memory the whole time and has full control of the hardware.

The CPU itself has two modes, and this is what keeps the computer from falling apart when one app misbehaves:

| Mode | Who runs in it | What it may do |
| --- | --- | --- |
| **Kernel mode** | the kernel | everything: every instruction, all of memory, every device |
| **User mode** | ordinary apps (games, browsers, music players) | only its own memory; it must ask the kernel for anything else |

Because apps live in user mode, a buggy app can crash itself but cannot wreck the whole system. The OS simply stops it.

## System calls: asking the OS for help

A **system call** is an app's request to the kernel: "OS, please open this file for me", "please send this over the network", "please give me more memory".

Here is what happens when a text editor saves your essay:

1. The editor (in user mode) makes a system call such as `write`.
2. The CPU switches to kernel mode and runs the kernel's code for that call.
3. The kernel checks that the editor is allowed to write to that file.
4. The kernel tells the disk driver to store the data.
5. The CPU switches back to user mode and the editor carries on, with a result saying "done" or "error".

The app never touched the disk itself. It asked, and the OS did the work.

> **Bug alert.** The OS is not just the desktop with its windows and icons. The desktop (the GUI) is a small, visible part. Most of the OS's work, like sharing the CPU, managing memory and talking to devices, is invisible.

## What the OS does all day

The rest of Chapter 1 takes these jobs one at a time:

| OS job | Everyday version | Where we study it |
| --- | --- | --- |
| Start the computer | waking the restaurant up in the morning | [1.2 Boot Process](../../02_Boot%20Process%20and%20the%20Motherboard/Main%20Theory/02_main-theory.md) |
| Share the CPU | deciding which customer is served next | [1.3 Processes](../../03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md) |
| Share memory | giving each table its own space | [1.4 Memory](../../04_Memory%20Management/Main%20Theory/04_main-theory.md) |
| Talk to devices | the waiter who carries orders to the kitchen | [1.5 Devices](../../05_Device%20Management%20and%20InputOutput/Main%20Theory/05_main-theory.md) |
| Organise files | the store-room catalogue | [1.6 Files](../../06_File%20Systems%20and%20Storage/Main%20Theory/06_main-theory.md) |
| Keep things safe | checking who is allowed in the kitchen | [1.7 Security](../../07_Security%20and%20Access%20Control/Main%20Theory/07_main-theory.md) |

## Try it

**OS Detective** (15 min): open Task Manager or Activity Monitor and count how many processes your OS is managing right now. Full instructions and expected results: [01_learner-activity.md](../Learner%20Activity/01_learner-activity.md).

## Going further (optional)

You do not need this for the test bank, but it helps if you continue in computer science.

- **Kernel designs.** In a *monolithic* kernel (Linux) almost all OS services run in kernel mode, which is fast but means a bad driver can crash everything. A *microkernel* (MINIX 3, QNX, seL4) keeps only the basics in kernel mode and runs the rest as user-mode servers, which is safer but adds overhead. *Hybrid* kernels (Windows NT, macOS XNU) sit in between.
- **Privilege levels.** On x86 processors kernel mode is called ring 0 and user mode ring 3. ARM processors call them EL1 and EL0.
- **Library wrappers.** When a C program calls `printf`, the C library eventually makes the `write` system call for it (you will see `printf` in [1.8](../../08_Basic%20C%20for%20Operating%20System%20Ideas/Main%20Theory/08_main-theory.md)).

## Check yourself

1. Name three jobs an operating system does.
2. Why do ordinary apps run in user mode?
3. An app wants to save a file. What does it send to the OS?

**Answers (try first, then peek)**
1. Any three: run and switch programs, share the CPU and memory, control devices, organise files, protect the computer.
2. So that a buggy or harmful app cannot damage the whole system.
3. A system call.


More questions: [01_test-bank.md](../Test%20bank%20Question_Answer/01_test-bank.md)

## Remember

- The OS manages the hardware and shares it between apps.
- The kernel is the core of the OS; apps live in user mode.
- Apps ask for help through system calls.

## Watch and explore

**Crash Course Computer Science #18: Operating Systems** (PBS, YouTube). A quick, visual story of why operating systems were invented. While watching, list three problems the first operating systems solved. It is fast, so turn on captions.

## References

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Chapters 1–2.
- Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson. Chapter 1.

---

Next: [1.2 Boot Process and the Motherboard](../../02_Boot%20Process%20and%20the%20Motherboard/Main%20Theory/02_main-theory.md) · Up: [Chapter 1 overview](../../README.md)
