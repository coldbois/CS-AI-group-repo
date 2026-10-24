# Operating Systems — Beginner-Friendly Study Notes

These notes cover **Chapters 1–8** of the study guide. They are written as a quick introduction, so the main goal is to understand what each part does and how the parts fit together.

## Contents

1. [What an Operating System Is](#1-what-an-operating-system-is)
2. [Boot Process and the Motherboard](#2-boot-process-and-the-motherboard)
3. [Process and CPU Management](#3-process-and-cpu-management)
4. [Memory Management](#4-memory-management)
5. [Device Management and Input/Output](#5-device-management-and-inputoutput)
6. [File Systems and Storage](#6-file-systems-and-storage)
7. [Security and Access Control](#7-security-and-access-control)
8. [Basic C for Operating System Ideas](#8-basic-c-for-operating-system-ideas)

---

## 1. What an Operating System Is

An **operating system (OS)** is the main software that manages a computer and lets other programs use its hardware. Without an OS, using a computer would be much harder because programs would have to manage the hardware themselves.

Think of the OS as the manager of a restaurant. The hardware is the kitchen and equipment, apps are the customers, and the OS decides how resources are shared.

### What does an OS do?

- Runs and switches between programs.
- Shares the CPU and RAM between programs.
- Communicates with devices such as keyboards, screens, printers, and graphics cards.
- Organizes files and folders.
- Helps protect the computer and its data.

Common operating systems include **Windows**, **macOS**, **Linux**, **Android**, and **iOS**. They look different, but they handle many of the same basic jobs.

### Where does the OS fit?

A simple way to picture the layers is:

1. **Hardware:** the physical parts, such as the CPU, RAM, storage, and screen.
2. **Operating system:** manages the hardware and provides services to programs.
3. **Applications:** programs such as games, browsers, and music players.
4. **User:** the person clicking, typing, or speaking to the computer.

Apps usually ask the OS to do hardware-related tasks rather than controlling the hardware directly.

### Kernel, user mode, and system calls

The **kernel** is the central part of the OS. It handles important tasks such as managing memory, running processes, and communicating with hardware.

Computers separate work into two broad privilege levels:

- **User mode:** where ordinary apps run with limited permissions.
- **Kernel mode:** where the kernel can perform more powerful operations.

This separation helps stop a faulty app from damaging the whole system.

When an app needs the OS to do something protected—such as opening a file—it makes a **system call**. The OS checks and handles the request, then returns the result to the app.

### Different kernel designs

- **Monolithic kernel:** many core OS services run together in kernel space. This can be fast, but a serious fault in a kernel component can affect the whole system.
- **Microkernel:** keeps the kernel small and moves more services outside it. This can improve isolation, though communication between components may add overhead.
- **Hybrid kernel:** combines ideas from both approaches.

These labels are useful general descriptions; real operating systems can be more complicated than a single label suggests.

**Remember:** The OS manages the computer's resources. The kernel is its core, apps normally run in user mode, and system calls let apps request protected OS services.

---

## 2. Boot Process and the Motherboard

**Booting** is the process of starting a computer and loading the operating system. The **motherboard** is the main circuit board that connects the computer's components and lets them communicate.

### The motherboard and main components

The motherboard has sockets and connectors for parts such as the CPU, RAM, storage, and add-in cards. Data travels between components over connections often called **buses**. PCIe is one important connection standard used by graphics cards and some SSDs.

Some key components:

- **CPU:** runs general-purpose instructions and most operating-system tasks.
- **GPU:** handles graphics and is good at doing many similar calculations in parallel.
- **NPU:** a processor designed to speed up certain AI tasks efficiently.
- **RAM:** fast temporary working memory; its contents are lost when power is off.
- **SSD or hard drive:** long-term storage that keeps files when the computer is off.

### What happens when you turn the computer on?

The usual start-up process looks roughly like this:

1. **Power on:** electricity reaches the motherboard and components.
2. **Firmware starts:** UEFI (the modern successor to the older BIOS) runs from the motherboard's firmware chip.
3. **Hardware check:** a process called POST checks important components. A problem may cause an error message, beep, or blank screen.
4. **Find a bootloader:** firmware locates the small program that begins loading the OS.
5. **Load the kernel:** the bootloader loads the operating-system kernel into memory and transfers control to it.
6. **Start system services:** the kernel initializes memory, detects hardware, and starts essential services.
7. **Show the login screen or desktop:** the system is ready for use.

The exact details vary by computer and operating system, but this is the general idea.

A bootloader is needed because the OS is stored on a drive, while the CPU needs instructions and data loaded into memory to run them.

### Common start-up problems

- **Nothing happens:** the power cable, power supply, or another power-related component may be at fault.
- **Beeps or a blank screen:** a hardware issue, such as RAM or graphics trouble, may be stopping start-up.
- **“No bootable device”:** the drive may not be detected, or the boot files may be missing or damaged.
- **Freezing while loading:** damaged OS files or a faulty driver may be involved.

**Remember:** UEFI starts first, checks the hardware, and finds the bootloader. The bootloader loads the kernel, and the kernel starts the rest of the OS.

---

## 3. Process and CPU Management

The OS manages which programs get to use the CPU and when. This helps several programs appear to run at once.

### Program vs. process

A **program** is a set of instructions stored as a file. A **process** is a program that is currently running. Opening the same app twice can create two separate processes.

The OS keeps information about each process in a record called a **process control block (PCB)**. It includes details such as the process's ID and current state.

### Process states

A process may be:

- **New:** it has just been created.
- **Ready:** it is waiting for CPU time.
- **Running:** it is currently using a CPU core.
- **Waiting/blocked:** it is waiting for something, such as data from a file or a key press.
- **Terminated:** it has finished or been stopped.

### Multitasking and context switches

A single CPU core runs one instruction stream at a time. The OS switches between processes very quickly, giving the impression that they are running together. This is called **multitasking**.

A **context switch** happens when the OS pauses one process, saves the information needed to resume it, and switches to another. A computer with multiple CPU cores can run work on more than one core at the same time.

### Scheduling: deciding who goes next

The **scheduler** chooses which ready process should use the CPU.

Two basic scheduling methods are:

- **First Come, First Served (FCFS):** processes run in the order they arrive. It is simple, but a long task can make shorter tasks wait.
- **Round Robin:** each process gets a short turn, called a time slice, before it goes to the back of the queue. This can make a system feel more responsive.

For example, suppose A needs 5 seconds, B needs 2 seconds, and C needs 1 second, and they all arrive together. With FCFS in the order A, B, C, process C waits while A and B run. With Round Robin, C can get CPU time earlier. The exact finish time depends on the time slice and scheduling details.

### Threads

A **thread** is a smaller unit of work inside a process. For example, a media player might use different threads for sound and video. Threads in the same process share much of their memory, so communication between them can be easier than communication between separate processes.

### Deadlock

A **deadlock** happens when processes are stuck waiting for resources held by one another. Imagine one process holds a printer and waits for a scanner, while another holds the scanner and waits for the printer. Neither can continue.

Operating systems and programs can reduce deadlock risks by carefully managing resources, changing the order in which resources are requested, or stopping a process when necessary.

**Remember:** A program is stored instructions; a process is a running instance. Scheduling shares CPU time, threads divide work inside a process, and deadlock means processes are stuck waiting on each other.

---

## 4. Memory Management

The OS manages RAM so programs have space to run and do not accidentally overwrite one another's data.

### RAM vs. storage

Think of RAM as a desk and storage as a bookshelf. RAM is the fast workspace for things being used right now. Storage keeps programs and files for the long term.

RAM is faster but temporary. An SSD or hard drive is slower but retains data when the computer is turned off.

### Memory addresses and protection

RAM is divided into tiny units, each with an **address**—like a house number. Programs use addresses to find the data they need.

The OS and the CPU's **memory management unit (MMU)** help give each process its own virtual address space. This makes it harder for one program to access another program's memory by mistake.

### Virtual memory and paging

**Virtual memory** lets each program work with its own set of addresses, which the system translates into locations in physical RAM. It improves protection and makes memory easier to manage.

Memory is often handled in fixed-size blocks called **pages**. If a program needs a page that is not currently in RAM, the system may need to fetch it from storage. This is called a **page fault**; it is not automatically an error.

When RAM is under pressure, the OS may move less-used pages to a reserved area on storage, often called **swap space** or a **page file**. Because storage is slower than RAM, relying heavily on this can make the computer feel sluggish.

If RAM is full, the OS may need to decide which page to remove to make room. Two example policies are:

- **FIFO (First In, First Out):** remove the page that has been in memory the longest.
- **LRU (Least Recently Used):** remove the page that has not been used for the longest time.

These are basic examples; real operating systems use more involved approaches.

### Stack and heap

Programs commonly use two kinds of memory areas:

- **Stack:** often stores information about active function calls and local variables. It is managed automatically as functions start and finish.
- **Heap:** used for data that needs more flexible lifetimes or sizes. Programs or their runtime manage this memory.

These are general concepts, and the exact details depend on the programming language and system.

**Remember:** RAM is the active workspace, storage keeps data long-term, and virtual memory helps isolate programs and manage limited RAM. A page fault means a needed page must be brought into memory, not necessarily that something is broken.

---

## 5. Device Management and Input/Output

**Input/output (I/O)** means receiving information from devices or sending information to them. Examples include reading a keyboard, displaying graphics, saving a file, or printing a document.

### Drivers: translators for hardware

A **device driver** is software that lets the OS communicate with a particular type of hardware. The OS uses the driver rather than needing to know every detail of every device.

### Interrupts

An **interrupt** is a signal that tells the CPU that something needs attention. For example, a keyboard can signal that a key was pressed. The CPU can pause its current work briefly, handle the event, and then continue.

### DMA

**Direct Memory Access (DMA)** allows certain devices to transfer data to or from RAM with less direct involvement from the CPU. This is useful for large transfers, such as data from storage or network devices.

### Buffers and caches

- A **buffer** temporarily holds data while it is being transferred or processed. It helps when two parts of a system work at different speeds.
- A **cache** keeps copies of data that may be needed again soon, so it can be accessed faster.

They sound similar, but their main purposes differ: buffers help manage data flow, while caches aim to speed up repeated access.

### CPU, GPU, and NPU

- **CPU:** flexible and suited to many different kinds of tasks.
- **GPU:** good at handling many similar calculations in parallel, such as graphics work.
- **NPU:** built to speed up certain AI calculations while using relatively little power.

Not every computer has a separate NPU, and the benefit depends on the task and software.

**Remember:** Drivers help the OS use devices, interrupts signal events, DMA helps transfer data, buffers smooth out data flow, and caches speed up repeated access.

---

## 6. File Systems and Storage

A **file system** is the method an OS uses to organize files and folders on a storage device. It keeps track of file names, locations, and other information needed to find data again.

### Files, folders, and paths

A file contains information, such as a photo or document. Folders group files together. A **path** tells the system where a file is located.

For example, `C:\Users\Sam\Documents\notes.txt` is a Windows-style path. Other operating systems use different path formats.

### What the OS does with files

The OS provides ways to:

- Create files and folders.
- Read files.
- Write or change their contents.
- Delete, rename, and move them.
- Control who is allowed to access them.

Deleting a file usually removes its directory entry or marks its space as available; it does not always mean every trace of the data is immediately erased.

### File systems you may see

- **FAT32:** widely compatible with many devices, but a single file cannot be larger than 4 GB.
- **NTFS:** commonly used by Windows; supports large files and features such as permissions and recovery tools.
- **APFS:** used by modern Apple operating systems.
- **ext4:** a common file system on Linux.

Different systems and devices may support additional formats.

### HDDs and SSDs

A **hard disk drive (HDD)** stores data on spinning magnetic disks and uses moving parts. A **solid-state drive (SSD)** uses flash memory and has no moving parts.

SSDs are generally much faster and quieter, and they handle physical shocks better. HDDs are often cheaper for large amounts of storage.

### Keeping files safe

Important files should be backed up. A backup is a separate copy that can be used if the original is lost, damaged, or encrypted by malware. Keeping a backup on the same drive is less helpful if that drive fails, so separate storage or a trusted backup service is preferable.

**Remember:** The file system organizes data; the storage device physically keeps it. An HDD uses moving parts, while an SSD uses flash memory. Backups help recover files if something goes wrong.

---

## 7. Security and Access Control

Computer security aims to protect information and keep systems working properly. The OS helps by checking who is using the computer and what they are allowed to do.

### The three main security goals

- **Confidentiality:** only authorized people can see the information.
- **Integrity:** information is not changed improperly.
- **Availability:** systems and data are available when needed.

These goals are often called the **CIA triad**.

### Authentication

**Authentication** checks that someone is who they claim to be. Examples include passwords, security keys, fingerprint recognition, and two-factor authentication (2FA).

Use long, unique passwords and enable 2FA where possible. Never share verification codes with someone who contacts you unexpectedly.

### Access control and permissions

After identifying a user, the system decides what they can do. This is **authorization** or access control.

Common permissions include:

- **Read:** view a file.
- **Write:** change a file.
- **Execute:** run a program or script.

The **principle of least privilege** means giving a user or program only the permissions it needs, rather than granting full access by default.

### Protection inside the computer

The OS uses several layers of protection, including:

- User mode and kernel mode.
- Separate memory spaces for processes.
- User accounts and file permissions.
- Sandboxing, which limits what an app can access.
- Firewalls, which filter network traffic.

No single measure prevents every attack, so multiple layers are used together.

### Common threats and basic defences

- **Malware:** harmful software. Avoid suspicious downloads and use trusted security tools.
- **Ransomware:** malware that locks or encrypts files to demand payment. Keep separate backups and install updates.
- **Phishing:** fake messages or websites designed to trick people into sharing information. Check the sender and links carefully.
- **Weak or reused passwords:** use unique passwords and a password manager.
- **Out-of-date software:** install security updates to fix known weaknesses.
- **Network attacks:** firewalls and secure network settings can reduce risk.

**Remember:** Security is about protecting confidentiality, integrity, and availability. Authentication checks identity; permissions determine access; updates, backups, and careful habits reduce common risks.

---

## 8. Basic C for Operating System Ideas

C is a programming language often used for operating systems, device drivers, and other software that needs close control over memory and hardware. You do not need to become an expert in C to understand the basic connection.

### A tiny C program

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, world!\n");
    return 0;
}
```

In simple terms:

- `#include <stdio.h>` gives the program access to standard input/output tools, including `printf`.
- `int main(void)` marks the main function, where this program begins.
- `printf(...)` prints text.
- `\n` starts a new line.
- `return 0;` indicates that the program finished successfully.

### Variables: labelled boxes

A **variable** stores a value that a program can use. For example:

```c
int seconds = 5;
printf("%d\n", seconds);
```

Here, `int` means the variable stores an integer, `seconds` is the variable's name, and `5` is its value. The `%d` tells `printf` to display an integer.

Variables use memory while a program runs. The OS manages the memory available to the process, while the programming language and compiler determine how variables are represented and used.

### A simple time-slice calculation

```c
int time_slice = 2;
int processes = 3;
int total_time = time_slice * processes;

printf("%d\n", total_time);
```

This calculates `2 × 3`, giving `6`. It is only a simple arithmetic example, not a full CPU scheduler. A real scheduler has to consider process states, arrival times, and other details.

### Comments

Comments are notes for people reading the code. The compiler ignores them.

```c
// Give each process a short turn.
int time_slice = 2;
```

Use comments to explain why something is done when the reason is not obvious. You do not need to comment every line.

### How C relates to operating systems

- A running C program becomes a process managed by the OS.
- Variables and other data use memory.
- Programs can ask the OS to open or save files.
- Device drivers allow the OS to communicate with hardware.
- Mistakes in C programs can cause crashes or security problems, which is one reason memory protection matters.

C programs normally run with user-mode restrictions. Writing an OS kernel or driver requires special techniques and privileges beyond an ordinary beginner program.

**Remember:** C is a language used for low-level software. A variable stores a value, `printf` displays text, and the OS manages the resources a running program needs.

---

## How the eight topics fit together

When you press the power button, the motherboard and firmware begin the boot process. The bootloader loads the kernel, and the OS starts managing the computer.

Once you open an app, it becomes a process. The scheduler gives it CPU time, and memory management provides protected space in RAM. Device drivers help the OS communicate with hardware, while the file system organizes files on storage. Security features control who can access the system and what they can do.

C is one of the languages used to build parts of this software. It provides a practical way to see how programs use variables, memory, and OS services.

The main idea is that the OS coordinates the hardware and software so that people can use a computer without managing every component themselves.
