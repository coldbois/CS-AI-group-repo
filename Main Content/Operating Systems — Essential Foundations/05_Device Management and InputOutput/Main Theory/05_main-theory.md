## Chapter 5: Devices and I/O: Talking to the Hardware

**Definition.** Device management is how the OS controls input and output devices (keyboard, disk, network card, GPU, NPU) through device drivers, interrupts and DMA, and shares them safely between programs.

**Analogy.** The CPU is a manager who cannot stand at the door waiting for every delivery. Instead, delivery staff ring a bell (interrupt) when a parcel arrives, and a warehouse crew (DMA) carries the parcels to the shelves without the manager lifting anything.

### 5.1 Three ways to do I/O

| **Method**                 | **How it works**                                                                   | **Cost**                                              |
|----------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------|
| Polling                    | The CPU repeatedly checks a device status register                                 | Wastes CPU time while waiting                         |
| Interrupt-driven           | The device signals the CPU when it is ready; the CPU runs a handler                | Efficient for slow or irregular devices               |
| DMA (direct memory access) | A DMA engine copies data between device and RAM without the CPU touching each byte | Best for large transfers such as disk or network data |

DMA improves performance for a large file read because the CPU does not copy the data byte by byte; it starts the transfer, runs other processes, and handles one interrupt when the transfer is done.

### 5.2 Interrupts

An **interrupt** is a hardware signal that makes the CPU pause its current work, save its state and run an **interrupt service routine** found through the interrupt descriptor table (x86) or a vector table. A hardware signal that makes the CPU pause and run a handler is an interrupt. The ISR does the urgent work quickly and defers the rest to a later "bottom half". Interrupt controllers (APIC on x86; MSI and MSI-X messages for PCIe devices) route signals to cores. The **timer interrupt** fires many times per second and is what lets the scheduler take the CPU back from a running process. Do not confuse interrupts (from hardware, asynchronous) with exceptions such as page faults (caused by the running instruction, synchronous) and traps such as system calls (requested by software). A page fault is an exception caused by the running instruction, not an interrupt raised by a device.

### 5.3 DMA and the IOMMU

For a DMA transfer, the CPU programs the device with the memory address, the length and the direction, then goes back to other work. The device moves the data itself and raises an interrupt when finished. An **IOMMU** (Intel VT-d, AMD-Vi) translates and restricts the addresses a device can reach, so a faulty or malicious device cannot overwrite arbitrary memory.

### 5.4 Talking to a device

The CPU reaches a device's control registers by **memory-mapped I/O** (registers appear at special physical addresses and are read like memory) or by the older **port-mapped I/O** (special in and out instructions on x86).

### 5.5 Device drivers

A **driver** is kernel code (or a user-mode service in a microkernel) that knows one family of hardware and exposes a standard interface to the rest of the OS, such as open, read, write and ioctl. On Linux, devices appear as files under /dev. Drivers are the most common source of kernel crashes, which is one reason microkernels run them outside the kernel.

### 5.6 CPU, GPU and NPU compared

| **Feature**           | **CPU**                                               | **GPU**                                                                 | **NPU**                                                    |
|-----------------------|-------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------|
| Design goal           | Low latency on a few complex, branch-heavy threads    | High throughput on thousands of simple parallel threads                 | Efficient neural network inference at low power            |
| Core count            | Few (4–64 typical on consumer and workstation parts)  | Thousands of shader or CUDA-style cores                                 | Arrays of multiply-accumulate units                        |
| Good at               | OS code, control logic, decision-making and search | Graphics, matrix maths, neural network training and inference           | Running trained neural networks on-device (vision, speech) |
| Memory                | System RAM through L1–L3 caches                       | Own VRAM (GDDR or HBM) on discrete cards; shared RAM on integrated GPUs | Usually shared system memory plus small on-chip buffers    |
| How the OS reaches it | Scheduler runs threads directly on cores              | Driver stack with command queues                                        | Driver and runtime stack                                   |

A GPU is not better than a CPU at branch-heavy sequential logic; the CPU is better at branching, sequential code.

### 5.7 How a GPU job reaches the hardware

1. The application calls a graphics or compute API (Vulkan, DirectX, CUDA, OpenCL).

2. The user-mode driver turns the calls into a **command buffer** of GPU instructions.

3. The kernel-mode driver validates the buffer and submits it to a hardware queue, then rings a doorbell register by memory-mapped I/O.

4. For a discrete card, input data is copied from system RAM to VRAM by DMA over PCIe.

5. The GPU runs the work asynchronously; the OS can schedule several applications' jobs on the same GPU.

6. When finished, the GPU signals a fence or raises an interrupt; the driver notifies the application and results are copied back if needed.

On a discrete graphics card, input data is copied from RAM to VRAM over **PCIe**. The GPU has its own memory management unit and page tables, managed by the driver. The data path matters: a x16 PCIe Gen 4 link moves about 31 GB/s each way, while a high-end GPU's VRAM can move hundreds of GB/s or more, so copying data across PCIe is often the bottleneck and good programs minimise transfers. NPUs follow the same pattern (application, runtime, driver, queue, interrupt), although on many laptops and phones the NPU shares system memory with the CPU so no copy over PCIe is needed.

### Pictures for Chapter 5

> **Picture 5.1** (add your picture here): A photo of a GPU installed in a PCIe slot.  
> Save it as `images/5-1.png`, then replace this note with `![Picture 5.1: A photo of a GPU installed in a PCIe slot](images/5-1.png)`.

> **Picture 5.2** (add your picture here): A diagram comparing polling, interrupts and DMA.  
> Save it as `images/5-2.png`, then replace this note with `![Picture 5.2: A diagram comparing polling, interrupts and DMA](images/5-2.png)`.

> **Picture 5.3** (add your picture here): A screenshot of Device Manager showing a driver.  
> Save it as `images/5-3.png`, then replace this note with `![Picture 5.3: A screenshot of Device Manager showing a driver](images/5-3.png)`.

## Visual References

![Figure 5.1: GPU installed in a PCIe slot](https://cdn.mos.cms.futurecdn.net/v2/t:0,l:321,cw:1538,ch:1154,q:80,w:1538/83JkEKofc4SQ7yh43s8Xog.png)

*Figure 5.1. GPU installed in a PCIe slot. Source: [PC Gamer](https://cdn.mos.cms.futurecdn.net/v2/t:0,l:321,cw:1538,ch:1154,q:80,w:1538/83JkEKofc4SQ7yh43s8Xog.png).*

![Figure 5.2: Diagram of polling, interrupts and DMA](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsNz_mA3Y-LoMAZ4xwBKOhglsyhNnAiXN2SqHEpDjb9XbXZHB8EHsKlVSU&s=10)

*Figure 5.2. Diagram of polling, interrupts and DMA. Source: [TechieLearn](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsNz_mA3Y-LoMAZ4xwBKOhglsyhNnAiXN2SqHEpDjb9XbXZHB8EHsKlVSU&s=10).*

![Figure 5.3: Device manager showing a drive ](https://winaero.com/blog/wp-content/uploads/2021/05/Windows-10-Device-Manager-Devices-by-driver.png)

*Figure 5.3. Device manager showing a driver. Source: [Winaero](https://winaero.com/blog/wp-content/uploads/2021/05/Windows-10-Device-Manager-Devices-by-driver.png).*