# Try it: Human Boot Relay (1.2)

**Time:** 15 min · **Group:** groups of 7 · **You need:** 7 printed step cards · Study Guide pp. 16–17

**Goal:** remember the boot order by acting it out, then use it to diagnose broken computers.

## Prepare

Print or write the 7 boot steps on separate cards, one per person, and shuffle them:

`Power on` · `Firmware starts (UEFI)` · `POST check` · `Find bootloader` · `Load kernel` · `Start services` · `Login screen`

Smaller group? Give some people two cards.

## Steps

1. Each person takes one card. **Without talking**, line up in boot order. Time yourselves.
2. Each person says their step aloud in one sentence ("I'm POST. I check the RAM and graphics before anything loads.").
3. Read the four broken-computer cases below. For each case, the group points to the person whose step failed.
4. Swap cards and try to beat your time.

| Broken-computer case | Which step failed? |
| --- | --- |
| A: nothing at all happens | |
| B: beeps, then a black screen | |
| C: "No bootable device" | |
| D: logo appears, then freezes | |

My group's best time: ______ s

## Reflect

- Which step was hardest to place? Why?
- Why must the firmware run before the OS?

## Check it: expected results

**Order:** power → UEFI → POST → bootloader → kernel → services → login.

| Case | Answer | Why |
| --- | --- | --- |
| A | Step 1, power | No power reaches the board: check the cable, socket or power supply. |
| B | Step 3, POST | The hardware check found a problem, often RAM or graphics. |
| C | Step 4, find bootloader | The drive or the boot files were not found. |
| D | Steps 5–6, kernel or services | Damaged OS files or a faulty driver. |

The firmware runs first because the OS is still "asleep" on the drive. Something already stored on the motherboard has to wake it.

**Teacher note:** if a group puts "find bootloader" before POST, don't correct them straight away. Ask: "Would you look for the bootloader before you know the drive is working?"
