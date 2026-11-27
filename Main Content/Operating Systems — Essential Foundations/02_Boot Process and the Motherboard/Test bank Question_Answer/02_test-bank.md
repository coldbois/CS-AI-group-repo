# 1.2 Test Bank: Boot Process and the Motherboard

T2 and M2 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q4 are extra practice. Answers are at the bottom.

## Questions

**T2 (True or False).** When a computer starts, the kernel loads before the UEFI firmware.

**M2 (choose ONE).** What runs first when you switch on a computer?

- A. The web browser
- B. The UEFI firmware
- C. The login screen
- D. Your music app

**Q1 (choose ONE).** Dandroid's screen says "No bootable device". Which step failed? *(slides 9–10)*

- A. Power on
- B. UEFI hardware check
- C. Finding the bootloader
- D. Login screen

**Q2.** Match each part to its job: CPU, RAM, SSD, firmware chip.

(a) keeps files when the power is off (b) holds UEFI (c) runs instructions (d) fast working space that is cleared at power-off

**Q3.** Why does the computer need a bootloader? Answer in one or two sentences.

**Q4 (True or False).** UEFI runs before the operating system kernel. *(Chapter 1 quick quiz)*

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T2 | **False** | The firmware must run first, because the OS is still "asleep" on the drive. Correct version: UEFI runs first, then the bootloader loads the kernel. |
| M2 | **B** | UEFI starts first and checks the hardware. Apps and the login screen only appear after the OS is ready. |
| Q1 | **C** | The firmware worked (it printed the message) but could not find a drive with a bootloader. With A nothing would happen; with B you would hear beeps or see a hardware error; D only appears after the kernel has loaded. |
| Q2 | CPU (c), RAM (d), SSD (a), firmware chip (b) | See Figure 1.2a. |
| Q3 | Sample answer | The OS is stored on the drive, but the CPU can only run what is in memory. The bootloader copies the kernel into RAM and starts it. |
| Q4 | **True** | Firmware first, then bootloader, then kernel. |
