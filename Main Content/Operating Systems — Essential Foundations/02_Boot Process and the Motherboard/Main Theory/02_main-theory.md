## Chapter 2: Starting Up: Boot and the Motherboard

**Definition.** Booting is the sequence that takes a machine from power-off to a running OS. The motherboard is the circuit board that connects the CPU, memory, storage and expansion cards, and decides which buses carry data between them.

**Analogy.** Booting is opening a shop in the morning: the lights come on (power), the manager checks every room works (firmware self-test), picks up the keys (bootloader), and only then the staff (kernel and services) start serving customers.

### 2.1 What is on the motherboard

| **Part**                          | **Job**                                                                              |
|-----------------------------------|--------------------------------------------------------------------------------------|
| CPU socket                        | Holds the processor; modern CPUs include the memory controller and many PCIe lanes   |
| Chipset (platform controller hub) | Provides extra PCIe lanes, SATA, USB and other I/O the CPU does not provide directly |
| RAM slots                         | Connect DDR memory modules through the memory channels                               |
| PCIe slots and M.2 slots          | Connect the GPU, NVMe SSDs, network cards and other add-in devices                   |
| UEFI flash chip                   | Stores the firmware that runs first                                                  |
| VRM (voltage regulators)          | Convert supply voltage to the exact voltages the CPU and RAM need                    |
| CMOS battery                      | Keeps the clock and firmware settings when power is off                              |

### 2.2 Buses: how data moves

| **Bus**                   | **Connects**                     | **Typical speed (approximate)**                                                                                            |
|---------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Memory bus (DDR channels) | CPU and RAM                      | Tens of GB/s per system, depending on channels and DDR generation                                                          |
| PCIe                      | CPU and GPU, NVMe SSD, NPU cards | About 1 GB/s per lane per direction on Gen 3, 2 GB/s on Gen 4, 4 GB/s on Gen 5; a x16 Gen 4 slot is about 31 GB/s each way |
| SATA                      | Chipset and SATA drives          | 6 Gb/s link, about 550 MB/s in practice                                                                                    |
| USB                       | Chipset and peripherals          | From 480 Mb/s (USB 2.0) to 40 Gb/s (USB4)                                                                                  |

### 2.3 The boot sequence

1. **Power on.** The power supply signals that power is stable; the CPU starts executing from a fixed reset address that points into the firmware flash chip.

2. **Firmware (UEFI) runs.** It performs the power-on self-test (POST), initialises and trains the RAM, and enumerates the devices on the PCIe bus.

3. **Boot device chosen.** UEFI follows the boot order and reads the EFI System Partition (a small FAT32 partition) to find a bootloader.

4. **Bootloader runs.** GRUB or Windows Boot Manager loads the kernel image (and on Linux an initial RAM file system) into memory and passes it boot parameters. The bootloader is the component that loads the kernel into memory.

5. **Kernel initialises.** It sets up the CPU mode, page tables, interrupt handlers, the scheduler and the drivers, then mounts the root file system.

6. **First user process starts.** On Linux this is init or systemd (PID 1); services and then the login screen or desktop follow.

### 2.4 BIOS vs UEFI

| **Feature**       | **Legacy BIOS**                             | **UEFI**                                                                                    |
|-------------------|---------------------------------------------|---------------------------------------------------------------------------------------------|
| CPU mode at start | 16-bit real mode                            | 32-bit or 64-bit                                                                            |
| Partition scheme  | MBR: disks up to 2 TB, 4 primary partitions | GPT: disks beyond 2 TB, typically 128 partitions. UEFI supports GPT disks larger than 2 TB. |
| Security          | None built in                               | Secure Boot checks the bootloader's digital signature                                       |
| Interface         | Text menus                                  | Graphical menus, mouse support                                                              |

The chip on the motherboard that stores the firmware is the **UEFI flash chip**. Secure Boot matters because the firmware verifies the signature of the bootloader and kernel before running them, so malicious code cannot be slipped into the start of the boot chain.

### 2.5 How the OS discovers hardware

The kernel learns what hardware exists from tables handed over by the firmware (ACPI tables on PCs, a device tree on many ARM boards) and by scanning the PCIe bus. Every PCIe device exposes a vendor ID and a device ID in its configuration space, and the kernel matches those IDs to a driver.

## Visual References

![Figure 2.1: Labelled photo of a motherboard](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWUY8GEa5CG2LhTBmKmhlV4CwJdTbL0qtg6HNwOnxtB5UlUSweXbNYvR81&s=10)

*Figure 2.1. Labelled photo of a motherboard. Source: [Art of PC](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWUY8GEa5CG2LhTBmKmhlV4CwJdTbL0qtg6HNwOnxtB5UlUSweXbNYvR81&s=10).*

![Figure 2.2: UEFI settings showing the boot order](https://i0.wp.com/www.deskdecode.com/wp-content/uploads/2021/10/Boot-Sequence-Configuration-of-UEFI-BIOS.jpg?fit=957%2C537&ssl=1)

*Figure 2.2. UEFI settings showing the boot order. Source: [deskdecode](https://i0.wp.com/www.deskdecode.com/wp-content/uploads/2021/10/Boot-Sequence-Configuration-of-UEFI-BIOS.jpg?fit=957%2C537&ssl=1).*

![Figure 2.3: Visualisation of boot steps](https://thumb.wikimedia.org/wikipedia/commons/thumb/b/bf/Flow-diagram-computer-booting-sequences.svg/960px-Flow-diagram-computer-booting-sequences.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail&_=20241119163658)

*Figure 2.3. Visualisation of boot steps. Source: [Wikimedia Commons](https://thumb.wikimedia.org/wikipedia/commons/thumb/b/bf/Flow-diagram-computer-booting-sequences.svg/960px-Flow-diagram-computer-booting-sequences.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail&_=20241119163658).*

