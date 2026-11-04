
# Operating Systems: Study Guide

An operating system is the layer where software meets hardware: the CPU, GPU, NPU, RAM and motherboard are all managed by the OS, which is mostly written in C. This guide covers it as one topic that branches into eight areas, then joins them together and ends with practice questions.

## The Big Picture

operating system layers · 6 jobs between apps and hardware

Read the picture from top to bottom: applications ask the operating system for help, and the operating system controls the hardware. Each box in the middle is an area you will study below.

| Area | The question it answers |
| --- | --- |
| The Operating System and Its Kernel | What is an OS, and how do programs ask it for help? |
| Starting Up: Boot and the Motherboard | What happens between the power button and the desktop? |
| Running Programs: Processes and the CPU | How does one CPU run many programs? |
| Memory: Giving Every Program Its Own Space | Where do programs live while they run? |
| Devices and I/O: Talking to the Hardware | How does the OS use the keyboard, disk, GPU and NPU? |
| Files and Storage: Keeping Data Organised | How are files saved, found and protected? |
| Security: Who May Do What | How does the OS keep users and programs apart? |
| C for Operating Systems: Seeing the Ideas in Code | What does simple C look like behind these ideas? |

Each area follows the same pattern: definition, analogy, how it works, and a worked example where it helps. Latencies and bandwidths are typical orders of magnitude, not guarantees for any one machine.

## The Operating System and Its Kernel

Definition. An operating system (OS) is system software that manages the hardware resources of a computer and gives programs a common set of services, so each program does not have to talk to the hardware itself.

Analogy. Think of a hotel manager. The applications are guests, the hardware is the rooms, electricity and water. The manager decides who gets which room and for how long, and stops one guest from walking into another guest's room.

### The layers of a computer system

| Layer (bottom to top) | Examples | Talks to |
| --- | --- | --- |
| Hardware | CPU, RAM, GPU, NPU, SSD, network card | Electrical signals, buses |
| Firmware and bootloader | UEFI, GRUB, Windows Boot Manager | Hardware, then loads the kernel |
| Kernel | Linux kernel, Windows NT kernel, XNU | Hardware through drivers |
| System libraries | glibc, Win32 API | Kernel through system calls |
| Shell, GUI and utilities | bash, File Explorer, desktop | Libraries and kernel |
| Applications | Browser, Word, games | Libraries |

### Kernel mode and user mode

The CPU itself enforces two privilege levels. Code in kernel mode (ring 0 on x86) can execute every instruction, touch any memory and talk to any device. Code in user mode (ring 3 on x86; EL0 on ARM) cannot change page tables, disable interrupts or access devices directly. A user program cannot execute kernel-mode instructions directly; if it tries, the CPU raises an exception and the OS stops the program. This is why one crashing app does not take down the whole machine.

### System calls

A system call is the controlled doorway from user mode into the kernel. When a C program calls printf, the library eventually calls write(), which executes a special instruction (syscall on x86-64). The CPU switches to kernel mode and jumps to a fixed kernel entry point. The kernel does the work, then returns to user mode. This is the only way a user program can request a privileged service; it cannot write directly to the disk controller because it runs in user mode and must ask the kernel through a system call, and the kernel checks permissions first.

The program calls a library wrapper such as read(), write(), open(), fork() or mmap().

The wrapper puts the system call number and arguments in registers and executes syscall.

The CPU switches to kernel mode and runs the kernel's system call handler.

The kernel checks the arguments and permissions, performs the request and stores the result.

The CPU returns to user mode and the program continues.

### Kernel designs

| Design | Idea | Examples | Strength | Weakness |
| --- | --- | --- | --- | --- |
| Monolithic | Almost all OS services run in kernel space | Linux | Fast, since services call each other directly | A buggy driver can crash the whole system |
| Microkernel | Kernel keeps only scheduling, basic memory and message passing; the rest run as user-mode servers | MINIX 3, QNX, seL4 | More stable and secure, smaller trusted core | Message passing adds overhead |
| Hybrid | Microkernel structure with many services kept in kernel space for speed | Windows NT, macOS (XNU) | Balance of speed and structure | More complex |

In a microkernel, most services run as user-mode servers.

### Hardware abstraction

Drivers and the hardware abstraction layer hide differences between devices. A program that writes to a file does not care whether the disk is a hard drive, a SATA SSD or an NVMe SSD, and a game calling a graphics API does not care which GPU model is installed.

### System software and developer tools

System software includes the OS, utilities and compilers. The tools below run on top of the OS and are used to build and maintain programs.

| Tool | What it does |
| --- | --- |
| Compiler | Translates the whole source code into machine code before the program runs (C, C++) |
| Interpreter | Executes source code line by line while it runs (Python, JavaScript) |
| Linker | Combines compiled files and libraries into one executable |
| Debugger | Pauses a program at breakpoints so you can inspect variables and find errors (GDB for C) |
| IDE | One application with a code editor, build tools and a debugger |
| Version control (Git) | Tracks changes to source code, restores earlier versions and lets a team collaborate |
| Unit tests | Check one small component in isolation, so regressions are caught early |

A compiler translates all the code into machine code first; an interpreter runs line by line and is usually easier to debug. A web browser such as Chrome is application software, not system software, because it serves the user instead of managing hardware. Middleware, on the other hand, acts as a bridge between applications and systems so different programs can communicate: think of databases, APIs and connectors.

## Starting Up: Boot and the Motherboard

Definition. Booting is the sequence that takes a machine from power-off to a running OS. The motherboard is the circuit board that connects the CPU, memory, storage and expansion cards, and decides which buses carry data between them.

Analogy. Booting is opening a shop in the morning: the lights come on (power), the manager checks every room works (firmware self-test), picks up the keys (bootloader), and only then the staff (kernel and services) start serving customers.

### What is on the motherboard

| Part | Job |
| --- | --- |
| CPU socket | Holds the processor; modern CPUs include the memory controller and many PCIe lanes |
| Chipset (platform controller hub) | Provides extra PCIe lanes, SATA, USB and other I/O the CPU does not provide directly |
| RAM slots | Connect DDR memory modules through the memory channels |
| PCIe slots and M.2 slots | Connect the GPU, NVMe SSDs, network cards and other add-in devices |
| UEFI flash chip | Stores the firmware that runs first |
| VRM (voltage regulators) | Convert supply voltage to the exact voltages the CPU and RAM need |
| CMOS battery | Keeps the clock and firmware settings when power is off |

### Buses: how data moves

| Bus | Connects | Typical speed (approximate) |
| --- | --- | --- |
| Memory bus (DDR channels) | CPU and RAM | Tens of GB/s per system, depending on channels and DDR generation |
| PCIe | CPU and GPU, NVMe SSD, NPU cards | About 1 GB/s per lane per direction on Gen 3, 2 GB/s on Gen 4, 4 GB/s on Gen 5; a x16 Gen 4 slot is about 31 GB/s each way |
| SATA | Chipset and SATA drives | 6 Gb/s link, about 550 MB/s in practice |
| USB | Chipset and peripherals | From 480 Mb/s (USB 2.0) to 40 Gb/s (USB4) |

### The boot sequence

Power on. The power supply signals that power is stable; the CPU starts executing from a fixed reset address that points into the firmware flash chip.

Firmware (UEFI) runs. It performs the power-on self-test (POST), initialises and trains the RAM, and enumerates the devices on the PCIe bus.

Boot device chosen. UEFI follows the boot order and reads the EFI System Partition (a small FAT32 partition) to find a bootloader.

Bootloader runs. GRUB or Windows Boot Manager loads the kernel image (and on Linux an initial RAM file system) into memory and passes it boot parameters. The bootloader is the component that loads the kernel into memory.

Kernel initialises. It sets up the CPU mode, page tables, interrupt handlers, the scheduler and the drivers, then mounts the root file system.

First user process starts. On Linux this is init or systemd (PID 1); services and then the login screen or desktop follow.

### BIOS vs UEFI

| Feature | Legacy BIOS | UEFI |
| --- | --- | --- |
| CPU mode at start | 16-bit real mode | 32-bit or 64-bit |
| Partition scheme | MBR: disks up to 2 TB, 4 primary partitions | GPT: disks beyond 2 TB, typically 128 partitions. UEFI supports GPT disks larger than 2 TB. |
| Security | None built in | Secure Boot checks the bootloader's digital signature |
| Interface | Text menus | Graphical menus, mouse support |

The chip on the motherboard that stores the firmware is the UEFI flash chip. Secure Boot matters because the firmware verifies the signature of the bootloader and kernel before running them, so malicious code cannot be slipped into the start of the boot chain.

### How the OS discovers hardware

The kernel learns what hardware exists from tables handed over by the firmware (ACPI tables on PCs, a device tree on many ARM boards) and by scanning the PCIe bus. Every PCIe device exposes a vendor ID and a device ID in its configuration space, and the kernel matches those IDs to a driver.

## Running Programs: Processes and the CPU

Definition. The OS decides which program runs on which CPU core, for how long, and what happens when programs compete for the same resource. This is what makes multitasking possible.

Analogy. One chef (the CPU core) cooks for many tables (processes). The scheduler is the head waiter who decides which order to cook in; a context switch is the chef putting down one dish and picking up another.

### Program, process and thread

| Term | Meaning | Shares with others? |
| --- | --- | --- |
| Program | A passive file on disk (for example an .exe or ELF binary) | Not running |
| Process | A running instance of a program, with its own address space, open files and resources | Nothing by default; processes are isolated |
| Thread | One path of execution inside a process, with its own stack and registers | Shares code, heap and open files with the other threads of its process |

### The process control block (PCB)

The kernel keeps one PCB per process. It holds the process ID, state, program counter, saved CPU registers, scheduling information (priority), memory information (pointer to the page table), a list of open files and accounting data. The PCB is what lets the OS stop a process and resume it later exactly where it left off. The kernel structure that stores a process's saved state is the process control block (PCB).

### Process states

New: the process is being created.

Ready: it can run and waits for a CPU core.

Running: its instructions are executing on a core.

Waiting (blocked): it waits for an event such as a disk read to finish.

Terminated: it has finished.

Transitions: Ready to Running when the scheduler dispatches it; Running to Ready when its time slice ends (timer interrupt); Running to Waiting when it asks for I/O; Waiting to Ready when the I/O completes.

### Context switch

A context switch saves the registers and program counter of the running process into its PCB, loads those of the next process, and switches the page table (on x86, by loading a new value into the CR3 register). A context switch does not cost nothing; it costs time and also cools the caches and TLB, so the new process finds them filled with the old one's data.

### Scheduling goals and algorithms

Schedulers are judged on CPU utilisation, throughput, turnaround time (finish minus arrival), waiting time (turnaround minus burst) and response time.

| Algorithm | Rule | Strength | Weakness |
| --- | --- | --- | --- |
| FCFS (first come, first served) | Run in arrival order, no preemption | Simple | Convoy effect: one long job delays all short ones |
| SJF (shortest job first) | Run the job with the shortest next burst | Minimum average waiting time | Needs burst lengths in advance; long jobs may starve |
| Round Robin | Each process gets a fixed time quantum, then goes to the back of the queue | Fair, good response time | Quantum too small wastes time on switches; too large behaves like FCFS |
| Priority | Run the highest-priority process | Important work goes first | Starvation, fixed by aging (raising priority over time) |
| Multilevel feedback queue | Several queues; processes move between them by behaviour | Adapts to short and long jobs | Complex to tune |

SJF gives the lowest average waiting time when all burst lengths are known and jobs arrive together. Real kernels are more elaborate: the Linux scheduler (CFS) always runs the task with the least virtual runtime, kept in a red-black tree.

### Worked example

Three processes arrive at time 0 with CPU bursts P1 = 5, P2 = 3, P3 = 8 (time units). Waiting time = completion time minus burst time, since arrival is 0.

| Algorithm | Run order (Gantt chart) | Completion times | Waiting times | Average waiting time |
| --- | --- | --- | --- | --- |
| FCFS | P1 (0-5), P2 (5-8), P3 (8-16) | 5, 8, 16 | 0, 5, 8 | 4.33 |
| SJF | P2 (0-3), P1 (3-8), P3 (8-16) | 8, 3, 16 | 3, 0, 8 | 3.67 |
| Round Robin, quantum 4 | P1 (0-4), P2 (4-7), P3 (7-11), P1 (11-12), P3 (12-16) | 12, 7, 16 | 7, 4, 8 | 6.33 |

SJF has the lowest average waiting time, as the theory says. Round Robin has the highest average waiting time here but gives every process its first slice early, which is why interactive systems use it. For three jobs arriving at time 0 with bursts 4, 2 and 6 under FCFS, waiting times are 0, 4 and 6, so the average is 10 / 3 = 3.33.

### Multicore scheduling

Each core has its own run queue, and the OS balances load between cores while trying to keep a thread on the same core (processor affinity) so its cache stays warm. On hybrid CPUs with performance and efficiency cores, the scheduler must also decide which kind of core suits each thread; Intel's Thread Director gives the OS hints for this. Simultaneous multithreading (hyper-threading) lets one core present two logical CPUs to the OS.

### Synchronisation and deadlock

When threads share data, a race condition appears if the result depends on timing. A mutex or semaphore lets only one thread enter a critical section at a time.

A deadlock is a state where processes wait for each other forever, like four cars at a crossroads each waiting for the car on its right. It needs all four Coffman conditions at once:

| Condition | Meaning | How to break it |
| --- | --- | --- |
| Mutual exclusion | A resource can be used by only one process at a time | Use shareable resources where possible |
| Hold and wait | A process holds one resource while waiting for another | Request all resources at once |
| No preemption | Resources cannot be taken away by force | Allow the OS to take resources back |
| Circular wait | A cycle of processes each waiting for the next | Number the resources and always request in order |

The rule "always lock resource A before resource B" removes the circular wait condition. Avoidance uses the Banker's algorithm (grant a request only if the system stays in a safe state). Detection and recovery builds a wait-for graph, finds cycles, and kills or rolls back a process.

The ready queue of an FCFS or Round Robin scheduler is naturally a queue, which follows first in, first out (FIFO).

## Memory: Giving Every Program Its Own Space

Definition. Memory management is how the OS decides which process gets which part of RAM, keeps processes out of each other's memory, and makes a small amount of RAM look like a large private memory for every program.

Analogy. RAM is a library reading room with limited desks. Each reader (process) believes they have a whole private library (virtual memory); the librarian (OS plus the MMU hardware) quietly maps their imaginary shelves to real desks and fetches books from the archive (disk) when needed.

### The memory hierarchy

Faster memory is smaller and more expensive, so computers stack several levels. Figures are typical orders of magnitude.

| Level | Typical size | Typical access time |
| --- | --- | --- |
| Registers | Bytes to a few KB | Under 1 ns |
| L1 cache (per core) | 32-64 KB | About 1 ns |
| L2 cache (per core) | 256 KB-2 MB | A few ns |
| L3 cache (shared) | Several MB to tens of MB | 10-40 ns |
| DRAM (main memory) | GBs | 60-100 ns |
| NVMe SSD | Hundreds of GB to TB | 10-100 microseconds |
| Hard disk | TBs | 5-10 milliseconds |

The hierarchy works because of locality: programs reuse data they just used (temporal locality) and data next to it (spatial locality). Caches therefore move data in cache lines of 64 bytes.

### From contiguous allocation to paging

Early systems gave each process one continuous block of RAM. That wastes space through fragmentation: internal (unused space inside a block) and external (free space split into pieces too small to use). Modern systems use paging: virtual memory is cut into fixed-size pages (usually 4 KB) and physical memory into frames of the same size, so any page can sit in any frame.

### Address translation

A virtual address is split into a page number and an offset. With 4 KB pages the offset is 12 bits. The page table maps each virtual page to a physical frame, and each entry also holds control bits: present, read/write, user/supervisor, accessed, dirty and no-execute. The MMU (memory management unit, part of the CPU) does the lookup in hardware on every memory access. Page tables are multi-level (4 levels on x86-64 with 48-bit addresses) so they do not waste memory on unused address ranges.

To avoid a slow page-table walk on every access, the MMU keeps recent translations in the TLB (translation lookaside buffer). A TLB hit costs about one cycle; a TLB miss triggers a walk through the page-table levels in memory. A TLB miss only means the translation was not cached, so the MMU walks the page table and carries on; a page fault means the page is not in RAM, so the OS must load it from disk.

Worked example: translating an address. A 32-bit system uses 4 KB pages. The program uses virtual address 0x00403A7C.

Offset = the low 12 bits = 0xA7C.

Page number = the address shifted right by 12 bits = 0x403.

The page table says page 0x403 is stored in frame 0x1B2.

Physical address = (0x1B2 shifted left by 12) combined with the offset = 0x1B2A7C.

With 4096-byte pages, virtual address 8200 has page number 2 and offset 8 (8200 = 2 x 4096 + 8), so if page 2 is stored in frame 5, the physical address is 5 x 4096 + 8 = 20488.

Worked example: effective access time. With a TLB access of 1 ns, a memory access of 100 ns and a TLB hit ratio of 98%, a hit costs 1 + 100 = 101 ns and a miss costs 1 + 100 + 100 = 201 ns (one extra memory access for a single-level page table):

EAT = h(t_TLB + t_mem) + (1-h)(t_TLB + 2 x t_mem) = 0.98 x 101 + 0.02 x 201 = 103.0 ns

With a 95% hit ratio, EAT = 0.95 x 101 + 0.05 x 201 = 106.0 ns.

### Virtual memory and page faults

If the page table entry says the page is not present, the CPU raises a page fault. The OS finds the page on disk (swap space or the program file), picks a free frame (evicting another page if needed), loads the page, updates the page table and restarts the instruction. A page fault is not an error; it is how the OS loads memory lazily. If a system spends most of its time handling page faults instead of running code, it is thrashing; the fix is to give processes enough frames for their working set or to run fewer processes.

### Page replacement

When no frame is free, the OS must choose a victim page.

| Algorithm | Rule | Note |
| --- | --- | --- |
| FIFO | Evict the page that has been in memory longest | Simple; suffers Belady's anomaly |
| LRU | Evict the page unused for the longest time | Close to optimal in practice; needs hardware help or approximation (clock algorithm) |
| OPT (optimal) | Evict the page whose next use is farthest in the future | Impossible to implement; used as a benchmark |

Worked example. Reference string 2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2 with 3 frames (12 references):

| Algorithm | Page faults | Hits |
| --- | --- | --- |
| FIFO | 9 | 3 |
| LRU | 7 | 5 |
| OPT | 6 | 6 |

Belady's anomaly. For FIFO and the reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5, giving the process 3 frames causes 9 faults but giving it 4 frames causes 10: more memory produced more faults. Giving FIFO more frames can increase its page faults; LRU and OPT never behave this way.

### Stack vs heap

The address space of a C process is laid out from low to high addresses as: code (text), initialised data, uninitialised data (BSS), heap (grows up), memory-mapped regions, stack (grows down) and, in the upper part, the kernel.

| Feature | Stack | Heap |
| --- | --- | --- |
| Used for | Local variables and function call frames | Memory requested at run time |
| Allocation | Automatic, when a function is entered and left | Manual in C: malloc() and free() |
| Speed | Very fast (move one pointer) | Slower (allocator searches for a free block) |
| Size | Fixed limit, often 8 MB on Linux; overflow crashes the program | Limited by available memory; can fragment or leak |
| Also called | Static allocation, size fixed at compile time | Dynamic allocation, size decided at run time |

malloc() takes memory from the heap, while memory whose size is fixed at compile time, such as a local array, uses the stack.

Under malloc(), the C library keeps lists of free blocks and asks the OS for more memory only when it runs out, using the brk system call for the main heap or mmap for large requests (above roughly 128 KB in glibc by default). The OS usually does not give physical frames until the program first touches the memory, which is why a large malloc can succeed instantly. When a process calls fork(), parent and child share frames marked copy-on-write, and a private copy is made only when one of them writes.

## Devices and I/O: Talking to the Hardware

Definition. Device management is how the OS controls input and output devices (keyboard, disk, network card, GPU, NPU) through device drivers, interrupts and DMA, and shares them safely between programs.

Analogy. The CPU is a manager who cannot stand at the door waiting for every delivery. Instead, delivery staff ring a bell (interrupt) when a parcel arrives, and a warehouse crew (DMA) carries the parcels to the shelves without the manager lifting anything.

### Three ways to do I/O

| Method | How it works | Cost |
| --- | --- | --- |
| Polling | The CPU repeatedly checks a device status register | Wastes CPU time while waiting |
| Interrupt-driven | The device signals the CPU when it is ready; the CPU runs a handler | Efficient for slow or irregular devices |
| DMA (direct memory access) | A DMA engine copies data between device and RAM without the CPU touching each byte | Best for large transfers such as disk or network data |

DMA improves performance for a large file read because the CPU does not copy the data byte by byte; it starts the transfer, runs other processes, and handles one interrupt when the transfer is done.

### Interrupts

An interrupt is a hardware signal that makes the CPU pause its current work, save its state and run an interrupt service routine found through the interrupt descriptor table (x86) or a vector table. A hardware signal that makes the CPU pause and run a handler is an interrupt. The ISR does the urgent work quickly and defers the rest to a later "bottom half". Interrupt controllers (APIC on x86; MSI and MSI-X messages for PCIe devices) route signals to cores. The timer interrupt fires many times per second and is what lets the scheduler take the CPU back from a running process. Do not confuse interrupts (from hardware, asynchronous) with exceptions such as page faults (caused by the running instruction, synchronous) and traps such as system calls (requested by software). A page fault is an exception caused by the running instruction, not an interrupt raised by a device.

### DMA and the IOMMU

For a DMA transfer, the CPU programs the device with the memory address, the length and the direction, then goes back to other work. The device moves the data itself and raises an interrupt when finished. An IOMMU (Intel VT-d, AMD-Vi) translates and restricts the addresses a device can reach, so a faulty or malicious device cannot overwrite arbitrary memory.

### Talking to a device

The CPU reaches a device's control registers by memory-mapped I/O (registers appear at special physical addresses and are read like memory) or by the older port-mapped I/O (special in and out instructions on x86).

### Device drivers

A driver is kernel code (or a user-mode service in a microkernel) that knows one family of hardware and exposes a standard interface to the rest of the OS, such as open, read, write and ioctl. On Linux, devices appear as files under /dev. Drivers are the most common source of kernel crashes, which is one reason microkernels run them outside the kernel.

### CPU, GPU and NPU compared

| Feature | CPU | GPU | NPU |
| --- | --- | --- | --- |
| Design goal | Low latency on a few complex, branch-heavy threads | High throughput on thousands of simple parallel threads | Efficient neural network inference at low power |
| Core count | Few (4-64 typical on consumer and workstation parts) | Thousands of shader or CUDA-style cores | Arrays of multiply-accumulate units |
| Good at | OS code, control logic, decision-making and search | Graphics, matrix maths, neural network training and inference | Running trained neural networks on-device (vision, speech) |
| Memory | System RAM through L1-L3 caches | Own VRAM (GDDR or HBM) on discrete cards; shared RAM on integrated GPUs | Usually shared system memory plus small on-chip buffers |
| How the OS reaches it | Scheduler runs threads directly on cores | Driver stack with command queues | Driver and runtime stack |

A GPU is not better than a CPU at branch-heavy sequential logic; the CPU is better at branching, sequential code.

### How a GPU job reaches the hardware

The application calls a graphics or compute API (Vulkan, DirectX, CUDA, OpenCL).

The user-mode driver turns the calls into a command buffer of GPU instructions.

The kernel-mode driver validates the buffer and submits it to a hardware queue, then rings a doorbell register by memory-mapped I/O.

For a discrete card, input data is copied from system RAM to VRAM by DMA over PCIe.

The GPU runs the work asynchronously; the OS can schedule several applications' jobs on the same GPU.

When finished, the GPU signals a fence or raises an interrupt; the driver notifies the application and results are copied back if needed.

On a discrete graphics card, input data is copied from RAM to VRAM over PCIe. The GPU has its own memory management unit and page tables, managed by the driver. The data path matters: a x16 PCIe Gen 4 link moves about 31 GB/s each way, while a high-end GPU's VRAM can move hundreds of GB/s or more, so copying data across PCIe is often the bottleneck and good programs minimise transfers. NPUs follow the same pattern (application, runtime, driver, queue, interrupt), although on many laptops and phones the NPU shares system memory with the CPU so no copy over PCIe is needed.

## Files and Storage: Keeping Data Organised

Definition. A file system is the part of the OS that organises data on storage into named files and directories, tracks where each piece lives on the device, and controls who may access it.

Analogy. A library catalogue: the catalogue card (inode) says where the book is, how big it is and who may borrow it; the shelf (directory) lists book titles with their card numbers.

### Files, inodes and directories

In Unix-style file systems, a file's metadata (size, owner, permissions, timestamps and pointers to its data blocks) is stored in an inode. The file's name is not in the inode: a directory is a table that maps names to inode numbers. This is why one file can have several names (hard links), while a symbolic link is a small file that stores a path to another file. Classic ext2 inodes hold direct pointers to data blocks, then a single, double and triple indirect pointer for large files. If you rename a file in the same directory, its inode does not change; only the directory entry that maps the name to the inode number changes. The inode stores a Unix file's size, owner and permissions.

### How blocks are allocated

| Method | Idea | Trade-off |
| --- | --- | --- |
| Contiguous | File occupies one run of blocks | Fast reads but external fragmentation |
| Linked | Each block points to the next | No fragmentation but slow random access |
| Indexed (inode) | An index block lists all data blocks | Good random access; overhead for tiny files |

### Common file systems

| File system | Used by | Notes |
| --- | --- | --- |
| FAT32 | USB sticks, cameras | Simple; maximum file size 4 GB minus 1 byte |
| exFAT | Large removable drives | No 4 GB limit; no journaling |
| NTFS | Windows | Journaling, access control lists, compression, encryption |
| ext4 | Linux | Journaling, extents, large volumes |
| APFS | macOS and iOS | Snapshots, copy-on-write, built-in encryption |

Journaling means the OS first writes what it intends to change into a log, then makes the change. After a power cut, the system replays or discards the log, so recovery takes seconds instead of a full disk check. Journaling speeds up recovery because the system replays or discards a short log of intended changes instead of checking the whole disk.

### Permissions

Unix permissions give read (r), write (w) and execute (x) rights to three classes: owner, group and others. The command chmod 755 file sets rwxr-xr-x: the owner can read, write and execute, everyone else can read and execute. chmod 644 gives owner read and write, group read only, others read only (rw-r--r--). Windows uses access control lists (ACLs) with finer-grained rules.

### Storage devices

| Device | How it works | Typical performance (approximate) |
| --- | --- | --- |
| Hard disk (HDD) | Spinning magnetic platters and a moving head | Seek and rotation 5-10 ms; 100-200 MB/s sequential |
| SATA SSD | Flash memory behind the SATA interface | Capped near 550 MB/s by the 6 Gb/s link |
| NVMe SSD | Flash memory directly on PCIe, with many parallel command queues (up to 64 thousand queues of 64 thousand commands in the specification) | Tens of microseconds latency; around 7 GB/s sequential on PCIe Gen 4 x4 |

An NVMe SSD does not connect through the SATA interface; it uses PCIe. Flash cannot overwrite a cell in place; it must erase a whole block first. The SSD's controller hides this with a flash translation layer, spreads wear across cells (wear levelling), and uses the OS's TRIM command to learn which blocks are free. The OS also keeps a page cache in RAM, so repeated reads of the same file come from memory, not from the device.

## Security: Who May Do What

Definition. OS security protects the confidentiality, integrity and availability of data and resources (the CIA triad) against mistakes and attacks, by controlling who can do what and by isolating programs from each other.

Analogy. A building with ID badges at the door (authentication), a list of which rooms each badge opens (authorisation), and solid walls between rooms (isolation).

### Authentication and authorisation

Authentication proves who the user is: passwords (stored as salted hashes, never as plain text), multi-factor authentication, biometrics, hardware keys.

Authorisation decides what that user may do. Discretionary access control (DAC) lets owners set permissions, as in Unix file modes. Mandatory access control (MAC), such as SELinux, enforces a system-wide policy that even the owner cannot override.

Least privilege means every program and user gets only the rights needed for the task.

The difference between authentication and authorisation is that authentication proves who you are, while authorisation decides what you may do. Passwords should never be stored as plain text; they should be stored as salted hashes.

### Hardware-backed protection

| Mechanism | What it does |
| --- | --- |
| Privilege rings (kernel vs user mode) | Stops user code from running privileged instructions |
| Separate address spaces | Each process sees only its own virtual memory, enforced by the MMU |
| Page permission bits and the NX (no-execute) bit | Mark memory as read-only or non-executable so data cannot run as code |
| ASLR (address space layout randomisation) | Randomises where code, stack and heap are placed, making attacks harder to aim |
| Stack canaries and SMEP/SMAP | Detect stack corruption and stop the kernel from running or reading user memory by mistake |
| Virtualisation extensions (Intel VT-x, AMD-V) | Let a hypervisor run isolated virtual machines efficiently |

The NX bit stops injected data from being run as code; ASLR makes the addresses an attacker needs unpredictable. Together they make memory attacks harder.

### Isolation above the process

Containers use kernel features (namespaces for what a process can see, cgroups for how much it can use) to isolate applications without a full virtual machine. Virtual machines isolate whole operating systems under a hypervisor.

### Encryption and the chain of trust

Disk encryption (BitLocker, LUKS, FileVault) protects data if a device is lost.

A TPM (trusted platform module) chip stores keys and measures the boot chain.

Secure Boot extends trust from firmware to bootloader to kernel by checking signatures at each step.

TLS protects data in transit across networks.

The CIA triad stands for confidentiality, integrity and availability.

## C for Operating Systems: Seeing the Ideas in Code

Most operating systems are written in C. So far you have met the basics: #include <stdio.h>, main, variables, arithmetic and printf. The two short programs below use only those, and each one calculates an idea from the areas above so you can check your hand calculations. Compile with gcc demo.c -o demo and run with ./demo.

### Anatomy of a C program

| Line | What it does |
| --- | --- |
| #include <stdio.h> | Brings in the standard input/output library, which provides printf |
| int main(void) { | The starting point: the OS begins running your program here |
| int x = 5; | Declares a whole-number variable and gives it a value |
| printf("...\n"); | Prints text; \n starts a new line, %d prints an int, %.2f prints a decimal with two places |
| return 0; | Tells the OS the program finished successfully |

#include <stdio.h> brings in the standard input/output library so you can use printf.

### Demo 1: Hello, operating system

#include <stdio.h>

int main(void) {
    printf("Hello, operating system!\n");
    return 0;
}

Output: Hello, operating system!. Behind this one line, printf calls the C library, which makes a write system call into the kernel, which sends the text to the screen (see The Operating System and Its Kernel).

### Demo 2: FCFS waiting time

Three jobs arrive at time 0 with bursts 5, 3 and 8. Under first come, first served, each job waits for all the jobs before it.

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

Output: Waiting times: 0 5 8 and Average waiting time = 4.33. Dividing by 3.0 instead of 3 keeps the decimal part; with 3 the division would be done in whole numbers and drop the decimals.

In C, 10 / 4 when both numbers are ints is 2 (the decimal part is dropped) and 10 % 4 is 2 (the remainder).

### What you will learn later in C

As the course moves on, you will meet loops and if statements (to simulate a scheduler or count page faults step by step), arrays (for reference strings, page tables and ready queues), functions (to split a simulator into reusable parts), pointers (memory addresses, linked lists, how the heap works), malloc and free (dynamic allocation on the heap, see Memory), and fork and threads (creating processes and threads, see Running Programs). None of these are needed for the two demos above: they only use variables, arithmetic and printf.

## Bringing It Together: The Great Invention

Every area above is one department of the same company. The best way to see this is to follow one simple action from start to finish: you press the power button and open a game.

### The story

Motherboard and boot. You press the power button. Electricity flows across the motherboard, UEFI wakes up, POST checks the parts, and the bootloader loads the kernel into RAM.

The OS takes charge. The kernel starts in kernel mode, loads the drivers and shows the login screen.

Security. You log in. The OS checks your password and gives you the permissions of a normal user.

Files. You double-click the game. The file system finds the game's files on your SSD using their path.

Processes. The OS creates a process for the game. The scheduler gives it CPU time while your music app keeps running too.

Memory. The OS gives the game its own private part of RAM through virtual memory, and loads the needed pages from the SSD.

Devices. Drivers let the game talk to the GPU for graphics, the keyboard and mouse for control (using interrupts), and the speakers for sound. If the game uses AI for characters or upscaling, the NPU or GPU can help.

C. Much of the OS code that did all of this, and many drivers, are written in C. The game's own requests reach the kernel through system calls.

### The bridge: one table

| Area | Its job in one line | Without it |
| --- | --- | --- |
| The OS and its kernel | The manager of the computer | Apps would fight over the hardware |
| Boot and the motherboard | Wakes everything up and connects the parts | The computer could not even start |
| Processes and the CPU | Shares the CPU fairly | Only one program could run |
| Memory | Gives each program safe space | Programs would overwrite each other |
| Devices and I/O | Lets software use hardware | Keyboard, screen and GPU would be useless |
| Files and storage | Saves and finds data | Everything would vanish at shutdown |
| Security | Protects users and data | Anyone or any program could damage the system |
| C | The language the OS is built from | The OS would be slower and harder to build |

### Why the operating system is a great invention

It hides complexity. You click an icon, and the OS handles thousands of tiny steps across the CPU, memory, storage and devices.

It shares resources fairly. Many programs and many users can use one computer at the same time.

It protects. One crashed app does not take down the whole machine.

It lets software be written once and run on many machines. A programmer does not need to learn every keyboard, drive and screen in the world.

It is the foundation for everything else. Browsers, games, apps, AI tools and the internet all stand on top of an operating system.

In short: the hardware is the body, the operating system is the brain and nervous system that makes the body useful, and the applications are the things you actually do. Without the operating system, a computer is just a box of very expensive parts.

