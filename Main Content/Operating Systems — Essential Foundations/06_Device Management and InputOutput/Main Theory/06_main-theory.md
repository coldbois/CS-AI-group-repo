
## Chapter 6: Files and Storage: Keeping Data Organised

**Definition.** A file system is the part of the OS that organises data on storage into named files and directories, tracks where each piece lives on the device, and controls who may access it.

**Analogy.** A library catalogue: the catalogue card (inode) says where the book is, how big it is and who may borrow it; the shelf (directory) lists book titles with their card numbers.

### 6.1 Files, inodes and directories

In Unix-style file systems, a file's **metadata** (size, owner, permissions, timestamps and pointers to its data blocks) is stored in an **inode**. The file's name is not in the inode: a **directory** is a table that maps names to inode numbers. This is why one file can have several names (**hard links**), while a **symbolic link** is a small file that stores a path to another file. Classic ext2 inodes hold direct pointers to data blocks, then a single, double and triple indirect pointer for large files. If you rename a file in the same directory, its inode does not change; only the directory entry that maps the name to the inode number changes. The inode stores a Unix file's size, owner and permissions.

### 6.2 How blocks are allocated

| **Method**      | **Idea**                             | **Trade-off**                               |
|-----------------|--------------------------------------|---------------------------------------------|
| Contiguous      | File occupies one run of blocks      | Fast reads but external fragmentation       |
| Linked          | Each block points to the next        | No fragmentation but slow random access     |
| Indexed (inode) | An index block lists all data blocks | Good random access; overhead for tiny files |

### 6.3 Common file systems

| **File system** | **Used by**            | **Notes**                                                 |
|-----------------|------------------------|-----------------------------------------------------------|
| FAT32           | USB sticks, cameras    | Simple; maximum file size 4 GB minus 1 byte               |
| exFAT           | Large removable drives | No 4 GB limit; no journaling                              |
| NTFS            | Windows                | Journaling, access control lists, compression, encryption |
| ext4            | Linux                  | Journaling, extents, large volumes                        |
| APFS            | macOS and iOS          | Snapshots, copy-on-write, built-in encryption             |

**Journaling** means the OS first writes what it intends to change into a log, then makes the change. After a power cut, the system replays or discards the log, so recovery takes seconds instead of a full disk check. Journaling speeds up recovery because the system replays or discards a short log of intended changes instead of checking the whole disk.

### 6.4 Permissions

Unix permissions give read (r), write (w) and execute (x) rights to three classes: owner, group and others. The command chmod 755 file sets rwxr-xr-x: the owner can read, write and execute, everyone else can read and execute. chmod 644 gives owner read and write, group read only, others read only (rw-r--r--). Windows uses access control lists (ACLs) with finer-grained rules.

### 6.5 Storage devices

| **Device**      | **How it works**                                                                                                                         | **Typical performance (approximate)**                                   |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Hard disk (HDD) | Spinning magnetic platters and a moving head                                                                                             | Seek and rotation 5–10 ms; 100–200 MB/s sequential                      |
| SATA SSD        | Flash memory behind the SATA interface                                                                                                   | Capped near 550 MB/s by the 6 Gb/s link                                 |
| NVMe SSD        | Flash memory directly on PCIe, with many parallel command queues (up to 64 thousand queues of 64 thousand commands in the specification) | Tens of microseconds latency; around 7 GB/s sequential on PCIe Gen 4 x4 |

An NVMe SSD does not connect through the SATA interface; it uses PCIe. Flash cannot overwrite a cell in place; it must erase a whole block first. The SSD's controller hides this with a **flash translation layer**, spreads wear across cells (**wear levelling**), and uses the OS's **TRIM** command to learn which blocks are free. The OS also keeps a **page cache** in RAM, so repeated reads of the same file come from memory, not from the device.

## Visual References

![Figure 6.1: Overview of a folder tree](https://addons.mathworks.com/downloads/e5/e59aa854-4a80-11e4-9553-005056977bd0/1.1.0/previewImage.png)

*Figure 6.1. Overview of a folder tree. Source: [MathWorks](https://addons.mathworks.com/downloads/e5/e59aa854-4a80-11e4-9553-005056977bd0/1.1.0/previewImage.png).*

![Figure 6.2: Diagram of a directory entry](https://cs.nyu.edu/~gottlieb/courses/2000s/2008-09-fall/os/lectures/diagrams/inodes.png)

*Figure 6.2. Diagram of a directory entry. Source: [cs.nyu.edu](https://cs.nyu.edu/~gottlieb/courses/2000s/2008-09-fall/os/lectures/diagrams/inodes.png).*

![Figure 6.3: Diferrence between HDD, SSD and NVMe](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXZIz3fFd4aEnQ40Tk1Ylwgfc16Ua8C1zjC_V2kD9nNtz-hGkF07MMrxGy&s=10)

*Figure 6.3. Difference between HDD, SSD and NVMe. Source: [thenetworkdna](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXZIz3fFd4aEnQ40Tk1Ylwgfc16Ua8C1zjC_V2kD9nNtz-hGkF07MMrxGy&s=10).*
