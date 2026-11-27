# 1.4 Memory Management

![Dandroid tired from too many tabs](../../../assets/dandroid/dandroid-tired.png)

**Chapter 1 · Dandroid's Body** · Study Guide pp. 25–29 · Slide 13 · Test Bank T4, M4, O2

> **Mission.** Dandroid opened 40 browser tabs and everything slowed to a crawl. Where did all the memory go?

**You will learn to**

- compare RAM and storage
- explain virtual memory, pages and page faults
- predict which page FIFO and LRU remove

**Key words:** RAM, address, virtual memory, page, page fault, swap

---

## Desk vs bookshelf

We use one picture for memory in every resource (guide, slides and Test Bank question O2):

| | **RAM = the desk** | **Storage = the bookshelf** |
| --- | --- | --- |
| Size | small | big |
| Speed | very fast | slower |
| Holds | what you are using right now | everything you keep |
| Power off | **cleared** | kept |
| Examples | 8 GB or 16 GB of RAM | SSD or hard drive (HDD) |

The CPU can only work with what is on the desk. When you open an app, the OS fetches it from the bookshelf and puts it on the desk.

Every byte of RAM has an **address**, a number like a house number, so the CPU can find it.

## Virtual memory and pages

If every program used real RAM addresses directly, one program could read or overwrite another's memory. So the OS gives each program its own private, pretend set of addresses called **virtual memory**, and quietly maps them to real RAM.

To make the mapping manageable, memory is cut into equal blocks called **pages** (often 4 KB each). The space in real RAM that holds one page is called a **frame**. The OS keeps a **page table** for each program: a map that says "page 0 is in frame 5, page 1 is in frame 2..."

![Figure 1.4a](../Diagrams%20and%20Pictures/1-4_pages-to-frames.png)

*Figure 1.4a. Pages map to frames; page 3 is out on the disk (Study Guide p. 26). Notice that the program's pages do not have to sit next to each other in real RAM.*

- Need a page that isn't in RAM? That is a **page fault**. The OS fetches the page from storage, updates the page table and lets the program carry on.
- RAM full? The OS moves pages that haven't been used for a while out to **swap space** on the drive. That frees a frame, but fetching those pages back later is slow.

> **Bug alert.** A page fault is not a crash. It is normal and happens all the time. A program is only stopped if it tries to touch memory that isn't its own.

## Why 40 tabs make the laptop slow

Each tab needs pages on the desk. With 40 tabs, the desk is full, so the OS keeps moving pages to the bookshelf and fetching them back. The drive light flashes and everything waits for storage, which is far slower than RAM. When a computer spends more time swapping than working, it is called **thrashing**.

What helps: close tabs and apps you aren't using, restart the browser, or add more RAM.

## Which page goes back to the shelf?

When the desk is full and a new page is needed, the OS must pick a **victim** page to remove. Two simple policies:

- **FIFO (First In, First Out):** remove the page that has been in RAM the longest.
- **LRU (Least Recently Used):** remove the page that hasn't been *used* for the longest time.

### Worked example (3 frames, requests 1, 2, 3, 1, 4, 1, 5, 1)

F = page fault, H = hit (already on the desk). The desk contents are shown after each request.

| Request | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **FIFO** | F [1] | F [1,2] | F [1,2,3] | H | F [2,3,4] | F [3,4,1] | F [4,1,5] | H |
| **LRU** | F [1] | F [1,2] | F [1,2,3] | H | F [1,3,4] | H | F [1,4,5] | H |

FIFO makes **6** faults and LRU makes **5**. FIFO threw out page 1 just because it arrived first, even though it was used all the time. LRU kept it because it kept being used. Real operating systems use cleverer versions of LRU.

## Try it

**Desk Tidy Challenge** (15 min, paper and 3 sticky notes): act out this exact example with FIFO and LRU and count your faults. Instructions and answers: [04_learner-activity.md](../Learner%20Activity/04_learner-activity.md).

## Going further (optional)

- **Address translation.** With 4 KB pages (4096 bytes), virtual address 8200 is in page 8200 ÷ 4096 = 2 (whole number), at offset 8200 − 2 × 4096 = 8. If page 2 is in frame 7, the real address is 7 × 4096 + 8 = 28 680.
- **The TLB.** Looking up the page table for every memory access would be slow, so the CPU keeps a small cache of recent translations called the translation lookaside buffer.
- **Memory hierarchy.** Registers → CPU cache → RAM → SSD → hard drive: each level is bigger, cheaper per GB and slower than the one before.

## Check yourself

1. Why is RAM called temporary memory?
2. What is a page fault?
3. Your laptop slows down with many apps open and the drive is busy all the time. What is happening?

**Answers (try first, then peek)**
1. Its contents are lost when the power is off.
2. A request for a page that isn't in RAM yet, so the OS loads it from storage.
3. RAM is full, so the OS keeps swapping pages to and from the slower drive.


More questions: [04_test-bank.md](../Test%20bank%20Question_Answer/04_test-bank.md)

## Remember

- RAM = fast desk; storage = big bookshelf.
- Virtual memory gives each program its own protected addresses.
- Page faults are normal; too much swapping is slow.

## Watch and explore

**Crash Course Computer Science #19: Memory & Storage** (PBS, YouTube). Shows how RAM and storage differ physically. Write down two differences between RAM and an SSD. There is some hardware detail; you only need the big picture.

## References

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Chapters 9–10.
- Denning, P. J. (1968). Thrashing: Its causes and prevention. *Proceedings of the AFIPS Fall Joint Computer Conference*, 915–922.

---

Previous: [1.3 Processes](../../03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md) · Next: [1.5 Device Management and I/O](../../05_Device%20Management%20and%20InputOutput/Main%20Theory/05_main-theory.md) · Up: [Chapter 1 overview](../../README.md)
