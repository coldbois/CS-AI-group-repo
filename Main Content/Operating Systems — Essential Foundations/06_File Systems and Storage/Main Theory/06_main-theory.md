# 1.6 File Systems and Storage

![Dandroid happy with its selfie](../../../assets/dandroid/dandroid-happy.png)

**Chapter 1 · Dandroid's Body** · Study Guide pp. 35–39 · Slide 14 · Test Bank T6, M6

> **Mission.** Dandroid saved a selfie. Next week it wants the photo back. How does the OS remember where it put it?

**You will learn to**

- explain what a file system does
- read and write a file path
- compare HDD and SSD, and explain why backups matter

**Key words:** file, folder, path, file system, HDD, SSD, backup

---

## The OS's catalogue

A **file** holds data: a photo, a song, an essay, a program. A **folder** (also called a *directory*) groups files and other folders.

A **file system** is the OS's catalogue. Like the card catalogue in a library, it records the name, location, size, date and owner of every file, and which blocks of the drive hold its data. Without it, the drive would just be billions of bytes with no labels.

## Paths: a file's address

A **path** is a file's full address. It starts at the top of the drive and lists every folder on the way down.

![Figure 1.6a](../Diagrams%20and%20Pictures/1-6_folder-tree.png)

*Figure 1.6a. Dandroid's folder tree (Study Guide p. 36).*

Follow the tree from the top to selfie.jpg and write each step with a backslash:

`C:\Users\Sam\Pictures\selfie.jpg`

which reads as: drive C → Users folder → Sam's folder → Pictures → the file. On a Mac or Linux the idea is the same but the separator is a forward slash and there is no drive letter, for example `/Users/Sam/Pictures/selfie.jpg`.

Two files in the same folder cannot have the same name, because they would have the same address and the OS couldn't tell them apart. Two files called `selfie.jpg` in *different* folders are fine.

> **Bug alert.** "Delete" usually just removes the catalogue entry. The data can stay on the drive until something else is written over it. That's why deleted files can sometimes be recovered, and why you should wipe a drive properly before giving a computer away.

## Formats you will meet

Different operating systems use different file systems: **FAT32** (USB sticks; a single file can be at most 4 GB), **NTFS** (Windows), **APFS** (Apple) and **ext4** (Linux). A USB stick formatted as FAT32 works almost everywhere, which is why it is still common.

## HDD vs SSD

| | **HDD** (hard disk drive) | **SSD** (solid-state drive) |
| --- | --- | --- |
| How it stores data | spinning magnetic disks with a moving arm | flash memory chips, no moving parts |
| Speed | slower | much faster |
| Toughness | can be damaged if dropped while spinning | tougher and quieter |
| Price | cheaper for lots of space | more expensive per GB |

## Backups

Drives fail, laptops get stolen and phones fall into pools. A **backup** is a copy kept *somewhere else*. A popular rule is **3-2-1**: 3 copies of important files, on 2 kinds of storage, with 1 copy off-site (for example, in a trusted cloud service). A second copy on the same laptop is not enough: if the laptop is lost, both copies go with it.

## Try it

**Path Treasure Hunt** (15 min, pairs): write paths from the folder tree, find a real path on a computer, and design a backup plan for Sam. Instructions and answers: [06_learner-activity.md](../Learner%20Activity/06_learner-activity.md).

## Going further (optional)

- **Blocks and inodes.** A drive is divided into blocks (often 4 KB). On Linux, each file has an *inode* that stores its details and the list of blocks holding its data. A folder is just a list of names that point to inodes.
- **Links.** A *hard link* is a second name for the same inode. A *symbolic link* (shortcut) is a tiny file that stores another file's path; if that file is deleted, the link breaks.
- **Journaling.** NTFS, APFS and ext4 write a short note of what they are about to change before changing it. If the power cuts out halfway, the OS reads the journal and repairs the file system instead of leaving it half-written.

## Check yourself

1. What is a file path?
2. Give two advantages of an SSD over an HDD.
3. Why might a "deleted" file still be recoverable?

**Answers (try first, then peek)**
1. The address that tells the OS where a file is stored.
2. Faster; no moving parts (quieter and tougher).
3. Deleting often removes only the catalogue entry; the data stays until it is overwritten.


More questions: [06_test-bank.md](../Test%20bank%20Question_Answer/06_test-bank.md)

## Remember

- The file system is the OS's catalogue.
- A path is a file's address.
- HDD = spinning disk; SSD = flash. Keep a backup somewhere else.

## Watch and explore

**Crash Course Computer Science #20: Files & File Systems** (PBS, YouTube). Shows how files are really stored as blocks on a drive. Afterwards, explain in one sentence what a directory stores. It uses older storage examples, but the ideas still apply.

## References

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Chapters 13–14.
- Microsoft. (n.d.). *File path formats on Windows systems*. Microsoft Learn. https://learn.microsoft.com/dotnet/standard/io/file-path-formats

---

Previous: [1.5 Devices](../../05_Device%20Management%20and%20InputOutput/Main%20Theory/05_main-theory.md) · Next: [1.7 Security and Access Control](../../07_Security%20and%20Access%20Control/Main%20Theory/07_main-theory.md) · Up: [Chapter 1 overview](../../README.md)
