# 1.1 Test Bank: What an Operating System Is

Questions T1 and M1 are the same as in the *Dandroid's Logic Lab* Test Bank (same numbers, same answers). Q1–Q4 are extra practice for this topic. Answers are at the bottom.

## Questions

**T1 (True or False).** An operating system (OS) manages the computer's hardware, like the CPU and memory.

**M1 (choose ONE).** What is the main job of an operating system?

- A. Manage the hardware and share it between apps
- B. Write new apps
- C. Charge the battery
- D. Make websites look nice

**Q1.** Put these in order from the top (closest to you) to the bottom: kernel, hardware, apps.

**Q2.** A music app wants to play a song stored on the disk. Explain, in two or three sentences, why it has to use a system call instead of reading the disk itself.

**Q3 (True or False).** The operating system and the desktop wallpaper are the same thing. *(Chapter 1 quick quiz, Study Guide p. 53)*

**Q4.** A game freezes, but you can still close it and use your browser. Which idea from this topic explains why the whole computer did not freeze?

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T1 | **True** | The OS is the manager. It shares the CPU, memory and devices between all the apps. |
| M1 | **A** | The OS is the manager between apps and hardware. People write apps (B), the charger charges the battery (C), and the browser draws websites (D). |
| Q1 | apps → kernel → hardware | Apps ask the kernel; only the kernel controls the hardware (Figure 1.1a). |
| Q2 | Sample answer | The music app runs in user mode, so it is not allowed to control the disk directly. It makes a system call (for example `read`), the CPU switches to kernel mode, and the kernel checks the request and reads the data for it. This keeps one app from damaging files that belong to others. |
| Q3 | **False** | The GUI and wallpaper are only a small, visible part. Most OS work is invisible. |
| Q4 | User mode vs kernel mode | The game runs in user mode, so its crash stays inside its own process. The kernel is still running and can stop the game. |
