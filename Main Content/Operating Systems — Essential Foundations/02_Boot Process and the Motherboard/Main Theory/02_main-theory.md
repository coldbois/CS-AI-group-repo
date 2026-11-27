# 1.2 Boot Process and the Motherboard

![Dandroid waking up](../../../assets/dandroid/dandroid-sleepy.png)

**Chapter 1 · Dandroid's Body** · Study Guide pp. 13–18 · Slides 8–10 · Test Bank T2, M2

> **Mission.** Someone presses Dandroid's power button. The screen is black... then a logo... then the desktop. What happened in those 10 seconds?

**You will learn to**

- name the main parts on a motherboard
- put the 7 steps of booting in order
- use the steps to troubleshoot start-up problems

**Key words:** motherboard, CPU, RAM, UEFI / BIOS, POST, bootloader

---

## Meet the motherboard team

The **motherboard** is the main circuit board of the computer. Every other part plugs into it, and data travels between the parts along connections called **buses** (PCIe is the fast bus used by graphics cards and SSDs).

![Figure 1.2a](../Diagrams%20and%20Pictures/1-2_motherboard-team.png)

*Figure 1.2a. The motherboard team (Study Guide p. 14).*

A few things worth noticing:

- The **CPU** runs almost everything, including most of the OS's own work.
- The **GPU** does many small calculations at the same time, which is perfect for graphics.
- The **NPU** speeds up some AI tasks using little power. Not every computer has one.
- **RAM** is fast but *volatile*: it forgets everything when the power goes off. That is why the OS has to be loaded again at every start-up.
- The **firmware chip** holds **UEFI**, the very first program that runs. Older computers used **BIOS**, which did the same job, so you will often hear both names.

## The boot sequence in 7 steps

**Booting** is everything that happens between pressing the power button and seeing the login screen.

![Figure 1.2b](../Diagrams%20and%20Pictures/1-2_boot-7-steps.png)

*Figure 1.2b. The boot sequence (Study Guide p. 15).*

| Step | What happens | If it fails, you see... |
| --- | --- | --- |
| 1. Power on | Electricity reaches the motherboard and parts. | nothing at all |
| 2. Firmware starts | UEFI runs from the firmware chip. | nothing, or the fans spin with no picture |
| 3. POST check | The Power-On Self-Test checks key hardware (RAM, graphics, keyboard). | beeps or an error message |
| 4. Find bootloader | UEFI looks on the drives for the small program that starts the OS. | "No bootable device" |
| 5. Load kernel | The bootloader copies the kernel from the drive into RAM and hands over control. | the logo appears, then freezes or restarts |
| 6. Start services | The kernel sets up memory, drivers and background services. | a freeze or error during the loading screen |
| 7. Login screen | Ready. The desktop appears after you sign in. | (you made it) |

The teaching slides (slide 8) show a shorter 5-step version for class: *power on → UEFI checks the hardware → find the bootloader → load the kernel → login screen*. It is the same sequence with steps 2–3 and 5–6 grouped together.

> **Dandroid's tip.** Why do we need a bootloader at all? The OS is stored on the drive, but the CPU can only run instructions that are in memory. The bootloader's whole job is to copy the kernel into RAM and start it.

> **Bug alert.** The OS does not start the computer. The firmware runs *first*, because at that moment the OS is still "asleep" on the drive.

## Worked example: which step failed?

Dandroid's screen says **"No bootable device"** (this is the class question on slides 9–10).

- Power is fine, because something is on the screen. So step 1 worked.
- UEFI is running, because it printed the message. Steps 2 and 3 worked.
- UEFI could not find a drive with a bootloader on it. **Step 4 failed.**

Likely causes: the drive is unplugged or broken, or the boot files were deleted. The fix is to check the drive cables and the boot order in the UEFI settings, or reinstall the OS.

## Try it

**Human Boot Relay** (15 min, groups of 7): each person is one boot step, the group lines up in order, then diagnoses four broken computers. Instructions and answers: [02_learner-activity.md](../Learner%20Activity/02_learner-activity.md).

## Going further (optional)

- **BIOS vs UEFI.** BIOS is the older firmware from the 1980s. It reads the first sector of the disk (the MBR) and has a 2 TB disk limit. UEFI is newer: it understands GPT disks, can show a mouse-driven settings menu and supports Secure Boot.
- **Secure Boot.** UEFI checks a digital signature on the bootloader before running it, and the bootloader checks the kernel. If someone has tampered with them, the chain stops. This protects against malware that tries to start before the OS.
- **Bootloader names.** Windows uses Windows Boot Manager; most Linux computers use GRUB.

## Check yourself

1. What is the job of the bootloader?
2. Which runs first: the kernel or UEFI?
3. A computer beeps and shows nothing. Which step probably failed?

**Answers (try first, then peek)**
1. It loads the OS kernel from the drive into memory and starts it.
2. UEFI (the firmware) runs first.
3. POST, the hardware check (step 3).


More questions: [02_test-bank.md](../Test%20bank%20Question_Answer/02_test-bank.md)

## Remember

- UEFI starts first and checks the hardware (POST).
- The bootloader loads the kernel into RAM.
- The kernel starts everything else.

## Watch and explore

Search for a short animated "how a computer boots" video. Pause at each step and name it from the 7-step list. Some videos say BIOS: it is the older name for UEFI.

## References

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Section 2.9 (system boot).
- UEFI Forum. (2022). *Unified Extensible Firmware Interface Specification*, version 2.10. https://uefi.org/specifications

---

Previous: [1.1 What an OS Is](../../01_What%20an%20Operating%20System%20Is/Main%20Theory/01_main-theory.md) · Next: [1.3 Process and CPU Management](../../03_Process%20and%20CPU%20Management/Main%20Theory/03_main-theory.md) · Up: [Chapter 1 overview](../../README.md)
