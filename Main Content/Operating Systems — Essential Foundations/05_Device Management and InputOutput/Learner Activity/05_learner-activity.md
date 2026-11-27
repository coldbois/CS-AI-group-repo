# Try it: Analogy Match & Doorbell Game (1.5)

**Time:** 10 min · **Group:** whole class · **You need:** a bell (or a clap), 10 cards · Study Guide pp. 32–33

**Goal:** link each I/O idea to a real-life twin, and feel how interrupts work.

## Prepare

Write the 5 terms and the 5 everyday twins on separate cards, then mix them up.

| Terms | Twins |
| --- | --- |
| driver | waiting room |
| interrupt | snack drawer |
| DMA | translator |
| buffer | doorbell |
| cache | delivery truck |

(The twins are deliberately in the wrong order.)

## Steps

1. **Analogy match.** Match each term to its twin. Check your matches against Figure 1.5a in the [topic page](../Main%20Theory/05_main-theory.md).
2. **Doorbell game.** One person reads a paragraph aloud: they are the **CPU**.
3. Everyone else is a **device**. Ring the bell at random moments. At each ring, the reader stops, says "Yes?", listens to a one-word answer, then continues **from the same word**.
4. **Polling round.** Play again, but now nobody rings. Instead the reader must stop every 5 seconds and ask "Does anyone need me?", even when nobody does.
5. Which round wasted more of the reader's time?

## Record

- How many times was the reader interrupted?
- Did the reader lose their place? How did they remember it?

## Reflect

- Why are interrupts better than checking every device again and again?
- Where have you seen a buffer in real life?

## Check it: expected results

- **Matches:** driver–translator, interrupt–doorbell, DMA–delivery truck, buffer–waiting room, cache–snack drawer.
- Interrupts let the CPU do useful work until a device actually needs it. Constant checking (**polling**) wastes time, because most of the checks find nothing.
- Remembering "the same word" is the CPU **saving its place** before it handles the interrupt, so it can carry on afterwards.
- Buffers you already know: video streaming, printer queues, typing ahead in a slow app.
