## Chapter 3: Running Programs: Processes and the CPU

**Definition.** The OS decides which program runs on which CPU core, for how long, and what happens when programs compete for the same resource. This is what makes multitasking possible.

**Analogy.** One chef (the CPU core) cooks for many tables (processes). The scheduler is the head waiter who decides which order to cook in; a context switch is the chef putting down one dish and picking up another.

### 3.1 Program, process and thread

| **Term** | **Meaning**                                                                           | **Shares with others?**                                                |
|----------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Program  | A passive file on disk (for example an .exe or ELF binary)                            | Not running                                                            |
| Process  | A running instance of a program, with its own address space, open files and resources | Nothing by default; processes are isolated                             |
| Thread   | One path of execution inside a process, with its own stack and registers              | Shares code, heap and open files with the other threads of its process |

### 3.2 The process control block (PCB)

The kernel keeps one PCB per process. It holds the process ID, state, program counter, saved CPU registers, scheduling information (priority), memory information (pointer to the page table), a list of open files and accounting data. The PCB is what lets the OS stop a process and resume it later exactly where it left off. The kernel structure that stores a process's saved state is the process control block (PCB).

### 3.3 Process states

1. **New:** the process is being created.

2. **Ready:** it can run and waits for a CPU core.

3. **Running:** its instructions are executing on a core.

4. **Waiting (blocked):** it waits for an event such as a disk read to finish.

5. **Terminated:** it has finished.

Transitions: Ready to Running when the scheduler dispatches it; Running to Ready when its time slice ends (timer interrupt); Running to Waiting when it asks for I/O; Waiting to Ready when the I/O completes.

### 3.4 Context switch

A context switch saves the registers and program counter of the running process into its PCB, loads those of the next process, and switches the page table (on x86, by loading a new value into the CR3 register). A context switch does not cost nothing; it costs time and also cools the caches and TLB, so the new process finds them filled with the old one's data.

### 3.5 Scheduling goals and algorithms

Schedulers are judged on CPU utilisation, throughput, turnaround time (finish minus arrival), waiting time (turnaround minus burst) and response time.

| **Algorithm**                   | **Rule**                                                                   | **Strength**                  | **Weakness**                                                           |
|---------------------------------|----------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------------------|
| FCFS (first come, first served) | Run in arrival order, no preemption                                        | Simple                        | Convoy effect: one long job delays all short ones                      |
| SJF (shortest job first)        | Run the job with the shortest next burst                                   | Minimum average waiting time  | Needs burst lengths in advance; long jobs may starve                   |
| Round Robin                     | Each process gets a fixed time quantum, then goes to the back of the queue | Fair, good response time      | Quantum too small wastes time on switches; too large behaves like FCFS |
| Priority                        | Run the highest-priority process                                           | Important work goes first     | Starvation, fixed by aging (raising priority over time)                |
| Multilevel feedback queue       | Several queues; processes move between them by behaviour                   | Adapts to short and long jobs | Complex to tune                                                        |

SJF gives the lowest average waiting time when all burst lengths are known and jobs arrive together. Real kernels are more elaborate: the Linux scheduler (CFS) always runs the task with the least virtual runtime, kept in a red-black tree.

### 3.6 Worked example

Three processes arrive at time 0 with CPU bursts P1 = 5, P2 = 3, P3 = 8 (time units). Waiting time = completion time minus burst time, since arrival is 0.

| **Algorithm**          | **Run order (Gantt chart)**                           | **Completion times** | **Waiting times** | **Average waiting time** |
|------------------------|-------------------------------------------------------|----------------------|-------------------|--------------------------|
| FCFS                   | P1 (0-5), P2 (5-8), P3 (8-16)                         | 5, 8, 16             | 0, 5, 8           | 4.33                     |
| SJF                    | P2 (0-3), P1 (3-8), P3 (8-16)                         | 8, 3, 16             | 3, 0, 8           | 3.67                     |
| Round Robin, quantum 4 | P1 (0-4), P2 (4-7), P3 (7-11), P1 (11-12), P3 (12-16) | 12, 7, 16            | 7, 4, 8           | 6.33                     |

SJF has the lowest average waiting time, as the theory says. Round Robin has the highest average waiting time here but gives every process its first slice early, which is why interactive systems use it. For three jobs arriving at time 0 with bursts 4, 2 and 6 under FCFS, waiting times are 0, 4 and 6, so the average is 10 / 3 = 3.33.

### 3.7 Multicore scheduling

Each core has its own run queue, and the OS balances load between cores while trying to keep a thread on the same core (processor affinity) so its cache stays warm. On hybrid CPUs with performance and efficiency cores, the scheduler must also decide which kind of core suits each thread; Intel's Thread Director gives the OS hints for this. Simultaneous multithreading (hyper-threading) lets one core present two logical CPUs to the OS.

### 3.8 Synchronisation and deadlock

When threads share data, a **race condition** appears if the result depends on timing. A **mutex** or **semaphore** lets only one thread enter a **critical section** at a time.

A **deadlock** is a state where processes wait for each other forever, like four cars at a crossroads each waiting for the car on its right. It needs all four Coffman conditions at once:

| **Condition**    | **Meaning**                                            | **How to break it**                              |
|------------------|--------------------------------------------------------|--------------------------------------------------|
| Mutual exclusion | A resource can be used by only one process at a time   | Use shareable resources where possible           |
| Hold and wait    | A process holds one resource while waiting for another | Request all resources at once                    |
| No preemption    | Resources cannot be taken away by force                | Allow the OS to take resources back              |
| Circular wait    | A cycle of processes each waiting for the next         | Number the resources and always request in order |

The rule "always lock resource A before resource B" removes the **circular wait** condition. Avoidance uses the Banker's algorithm (grant a request only if the system stays in a safe state). Detection and recovery builds a wait-for graph, finds cycles, and kills or rolls back a process.

The ready queue of an FCFS or Round Robin scheduler is naturally a **queue**, which follows first in, first out (FIFO).

## Visual References

![Figure 3.1: Task manager and running processes](https://www.lifewire.com/thmb/LGh8eIvqxll8X18cgRNPt6kEE8M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/task-manager-windows-11-980ae80d39694a14b75ddec1628d1924.png)

*Figure 3.1. Task manager and running processes. Source: [Lifewire](https://www.lifewire.com/thmb/LGh8eIvqxll8X18cgRNPt6kEE8M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/task-manager-windows-11-980ae80d39694a14b75ddec1628d1924.png).*

![Figure 3.2: Gantt charts](https://cdn.knowledgegate.ai/blog-assets/blog_asset_1784731060863_a91b5t.jpg)

*Figure 3.2. Gantt charts. Source: [Knowledge Gate](https://cdn.knowledgegate.ai/blog-assets/blog_asset_1784731060863_a91b5t.jpg).*

![Figure 3.3: Process state diagram](https://static.wixstatic.com/media/97d138_721d4680c3ba40818c38df043ba92c86~mv2.png/v1/fill/w_872,h_356,al_c,q_85,enc_avif,quality_auto/97d138_721d4680c3ba40818c38df043ba92c86~mv2.png)

*Figure 3.3. Process state diagram. Source: [Omegapy](https://static.wixstatic.com/media/97d138_721d4680c3ba40818c38df043ba92c86~mv2.png/v1/fill/w_872,h_356,al_c,q_85,enc_avif,quality_auto/97d138_721d4680c3ba40818c38df043ba92c86~mv2.png).*

