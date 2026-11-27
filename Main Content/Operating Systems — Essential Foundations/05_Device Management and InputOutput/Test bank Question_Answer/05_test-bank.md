# 1.5 Test Bank: Device Management and Input/Output

T5 and M5 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T5 (True or False).** A device driver helps the OS talk to a device, like a printer.

**M5 (choose ONE).** A video says "buffering...". What is happening?

- A. Video data is loading into a waiting area first
- B. The screen is turning off
- C. A virus is deleting the video
- D. The CPU is broken

**Q1.** Match: driver, interrupt, DMA, cache → doorbell, snack drawer, translator, delivery truck.

**Q2.** Your browser shows a website's logo instantly the second time you visit. Is that a buffer or a cache? Why?

**Q3.** Explain in two sentences why interrupts waste less CPU time than polling.

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T5 | **True** | A driver is a translator between the OS and one kind of device. |
| M5 | **A** | A buffer holds data before it is used. Buffering is normal: it is not the screen (B), a virus (C) or a broken CPU (D). |
| Q1 | driver–translator, interrupt–doorbell, DMA–delivery truck, cache–snack drawer | See Figure 1.5a. |
| Q2 | **Cache** | It keeps a copy of something you used before, so repeat access is fast. A buffer manages the flow of data that is on its way. |
| Q3 | Sample answer | With polling the CPU keeps checking devices even when nothing has happened, so most checks are wasted. With interrupts the CPU does other work and only stops when a device actually signals it. |
