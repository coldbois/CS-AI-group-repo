# Try it: OS Detective (1.1)

**Time:** 15 min · **Group:** solo or pairs · **You need:** any laptop or phone · Study Guide pp. 10–11

**Goal:** see the OS at work by spying on the programs it is managing right now.

## Prepare

- Windows: press **Ctrl + Shift + Esc** to open Task Manager, then the *Processes* tab.
- Mac: open **Activity Monitor** (Applications → Utilities).
- Phone: Settings → Battery shows which apps have been using the device.

## Steps

1. **Predict first:** how many programs (processes) do you think are running right now? Write down a number before you look.
2. Open the tool and count them (Task Manager shows the total at the top of the list on most versions). Were you close?
3. Sort the list by **Memory**. Which app uses the most?
4. Open one more app. Watch the CPU and memory numbers change.
5. Find one process that you did not start yourself.

## Record

| What I checked | My prediction | What I saw |
| --- | --- | --- |
| Number of processes | | |
| Biggest memory user | | |
| A process I didn't start | | |

## Reflect

- Why are so many programs running that you never opened?
- Which OS job did you just watch: sharing the CPU, memory, devices, files or security?

## Check it: expected results

- Most people guess 5–10. A normal laptop is often running **100 or more** processes.
- Many of them are OS services working in the background: updates, Wi-Fi, sound, antivirus, the clock.
- Watching the CPU and memory numbers move when you open an app is the OS **sharing resources** between apps. That is the main job from [1.1](../Main%20Theory/01_main-theory.md).
- The "process I didn't start" will usually be an OS service, for example `svchost.exe` (Windows) or `WindowServer` (Mac).

**No access to Task Manager?** (some school computers block it) Use the sample screenshot in the Study Guide on p. 10, and answer the questions from that.

**Safety note:** only look. Do not end any process you do not recognise, because some of them keep the OS running.
