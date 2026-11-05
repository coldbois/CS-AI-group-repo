## Chapter 4: Memory: Giving Every Program Its Own Space

**Definition.** Memory management is how the OS decides which process gets which part of RAM, keeps processes out of each other's memory, and makes a small amount of RAM look like a large private memory for every program.

**Analogy.** RAM is a library reading room with limited desks. Each reader (process) believes they have a whole private library (virtual memory); the librarian (OS plus the MMU hardware) quietly maps their imaginary shelves to real desks and fetches books from the archive (disk) when needed.

### 4.1 The memory hierarchy

Faster memory is smaller and more expensive, so computers stack several levels. Figures are typical orders of magnitude.

| **Level**           | **Typical size**         | **Typical access time** |
|---------------------|--------------------------|-------------------------|
| Registers           | Bytes to a few KB        | Under 1 ns              |
| L1 cache (per core) | 32–64 KB                 | About 1 ns              |
| L2 cache (per core) | 256 KB–2 MB              | A few ns                |
| L3 cache (shared)   | Several MB to tens of MB | 10–40 ns                |
| DRAM (main memory)  | GBs                      | 60–100 ns               |
| NVMe SSD            | Hundreds of GB to TB     | 10–100 microseconds     |
| Hard disk           | TBs                      | 5–10 milliseconds       |

The hierarchy works because of **locality**: programs reuse data they just used (temporal locality) and data next to it (spatial locality). Caches therefore move data in cache lines of 64 bytes.

### 4.2 From contiguous allocation to paging

Early systems gave each process one continuous block of RAM. That wastes space through **fragmentation**: internal (unused space inside a block) and external (free space split into pieces too small to use). Modern systems use **paging**: virtual memory is cut into fixed-size pages (usually 4 KB) and physical memory into frames of the same size, so any page can sit in any frame.

### 4.3 Address translation

A virtual address is split into a page number and an offset. With 4 KB pages the offset is 12 bits. The **page table** maps each virtual page to a physical frame, and each entry also holds control bits: present, read/write, user/supervisor, accessed, dirty and no-execute. The **MMU** (memory management unit, part of the CPU) does the lookup in hardware on every memory access. Page tables are multi-level (4 levels on x86-64 with 48-bit addresses) so they do not waste memory on unused address ranges.

To avoid a slow page-table walk on every access, the MMU keeps recent translations in the **TLB** (translation lookaside buffer). A TLB hit costs about one cycle; a TLB miss triggers a walk through the page-table levels in memory. A TLB miss only means the translation was not cached, so the MMU walks the page table and carries on; a page fault means the page is not in RAM, so the OS must load it from disk.

**Worked example: translating an address.** A 32-bit system uses 4 KB pages. The program uses virtual address 0x00403A7C.

1. Offset = the low 12 bits = 0xA7C.

2. Page number = the address shifted right by 12 bits = 0x403.

3. The page table says page 0x403 is stored in frame 0x1B2.

4. Physical address = (0x1B2 shifted left by 12) combined with the offset = 0x1B2A7C.

With 4096-byte pages, virtual address 8200 has page number 2 and offset 8 (8200 = 2 x 4096 + 8), so if page 2 is stored in frame 5, the physical address is 5 x 4096 + 8 = 20488.

**Worked example: effective access time.** With a TLB access of 1 ns, a memory access of 100 ns and a TLB hit ratio of 98%, a hit costs 1 + 100 = 101 ns and a miss costs 1 + 100 + 100 = 201 ns (one extra memory access for a single-level page table):

```text
EAT = h(t_TLB + t_mem) + (1-h)(t_TLB + 2 x t_mem) = 0.98 x 101 + 0.02 x 201 = 103.0 ns
```

With a 95% hit ratio, EAT = 0.95 x 101 + 0.05 x 201 = 106.0 ns.

### 4.4 Virtual memory and page faults

If the page table entry says the page is not present, the CPU raises a **page fault**. The OS finds the page on disk (swap space or the program file), picks a free frame (evicting another page if needed), loads the page, updates the page table and restarts the instruction. A page fault is not an error; it is how the OS loads memory lazily. If a system spends most of its time handling page faults instead of running code, it is **thrashing**; the fix is to give processes enough frames for their working set or to run fewer processes.

### 4.5 Page replacement

When no frame is free, the OS must choose a victim page.

| **Algorithm** | **Rule**                                                | **Note**                                                                             |
|---------------|---------------------------------------------------------|--------------------------------------------------------------------------------------|
| FIFO          | Evict the page that has been in memory longest          | Simple; suffers Belady's anomaly                                                     |
| LRU           | Evict the page unused for the longest time              | Close to optimal in practice; needs hardware help or approximation (clock algorithm) |
| OPT (optimal) | Evict the page whose next use is farthest in the future | Impossible to implement; used as a benchmark                                         |

**Worked example.** Reference string 2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2 with 3 frames (12 references):

| **Algorithm** | **Page faults** | **Hits** |
|---------------|-----------------|----------|
| FIFO          | 9               | 3        |
| LRU           | 7               | 5        |
| OPT           | 6               | 6        |

**Belady's anomaly.** For FIFO and the reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5, giving the process 3 frames causes 9 faults but giving it 4 frames causes 10: more memory produced more faults. Giving FIFO more frames can increase its page faults; LRU and OPT never behave this way.

### 4.6 Stack vs heap

The address space of a C process is laid out from low to high addresses as: code (text), initialised data, uninitialised data (BSS), **heap** (grows up), memory-mapped regions, **stack** (grows down) and, in the upper part, the kernel.

| **Feature** | **Stack**                                                      | **Heap**                                          |
|-------------|----------------------------------------------------------------|---------------------------------------------------|
| Used for    | Local variables and function call frames                       | Memory requested at run time                      |
| Allocation  | Automatic, when a function is entered and left                 | Manual in C: malloc() and free()                  |
| Speed       | Very fast (move one pointer)                                   | Slower (allocator searches for a free block)      |
| Size        | Fixed limit, often 8 MB on Linux; overflow crashes the program | Limited by available memory; can fragment or leak |
| Also called | Static allocation, size fixed at compile time                  | Dynamic allocation, size decided at run time      |

malloc() takes memory from the **heap**, while memory whose size is fixed at compile time, such as a local array, uses the **stack**.

Under malloc(), the C library keeps lists of free blocks and asks the OS for more memory only when it runs out, using the brk system call for the main heap or mmap for large requests (above roughly 128 KB in glibc by default). The OS usually does not give physical frames until the program first touches the memory, which is why a large malloc can succeed instantly. When a process calls fork(), parent and child share frames marked copy-on-write, and a private copy is made only when one of them writes.

## Visual References

![Figure 4.1: Visualisation of registers down to the hard disk](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY341W0E7hvsRMBz-OWBAPrl-IlJqv-aZiEev67QNXR6rc2pSKiCWs14Y&s=10)

*Figure 4.1. Visualisation of registers down to the hard disk. Source: [patch.update](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY341W0E7hvsRMBz-OWBAPrl-IlJqv-aZiEev67QNXR6rc2pSKiCWs14Y&s=10).*

![Figure 4.2: Diagram of address translation](https://courses.cs.washington.edu/courses/cse451/24sp/lectures/figures/translation-single-level.png)

*Figure 4.2. Diagram of address translation. Source: [CSE 451 24sp](https://courses.cs.washington.edu/courses/cse451/24sp/lectures/figures/translation-single-level.png).*

![Figure 4.3: Computer's memory usage](https://d1q3zw97enxzq2.cloudfront.net/images/How_to_check_memory_-.width-702.bgcolor-000.format-webp.webp)

*Figure 4.3. Computer's memory usage. Source: [Corsair](https://d1q3zw97enxzq2.cloudfront.net/images/How_to_check_memory_-.width-702.bgcolor-000.format-webp.webp).*



