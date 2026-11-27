# 2.5 Test Bank: Data Structures

T14, M14 and O5 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T14 (True or False).** A stack gives back the item that was added first.

**M14 (choose ONE).** Which data structure works like a pile of plates (last in, first out)?

- A. Queue
- B. Stack
- C. Table
- D. Graph

**O5. Undo button and print queue** (about 100 words, 5 marks)

Dandroid is building a text editor with an Undo button. The school printer also needs to keep a list of print jobs. A user types "Hello", then "big", then "world", and then presses Undo twice.

(1) Should Undo use a stack or a queue? Why? (2) What text is left after pressing Undo twice? (3) Should the print jobs use a stack or a queue? Why?

Use these words: stack · queue · LIFO · FIFO · last · first

**Q1.** A stack holds (bottom → top) [A, B, C]. You push D, then pop twice. What is left?

**Q2.** In the array `["Mina", "Kai", "Ana"]`, what is at index 1?

**Q3 (True or False).** A queue serves the oldest item first. *(Chapter 2 quick quiz)*

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T14 | **False** | A stack is like a pile of plates: you take the one on top. Correct version: a stack gives back the item added last (LIFO); a queue gives back the first one (FIFO). |
| M14 | **B** | The last plate on top comes off first. A queue is a line (first in, first out); a table stores rows; a graph stores connections. |
| Q1 | [A, B] | Push D → [A, B, C, D]; pop D; pop C. |
| Q2 | "Kai" | Indexes start at 0, so index 1 is the second item. |
| Q3 | **True** | First in, first out. |

**O5 sample answer (110 words).** Undo should use a stack, because Undo must remove the last thing you did first. A stack is like a pile of plates: last in, first out (LIFO). After typing, the stack holds Hello, big, world (world on top). The first Undo removes "world". The second Undo removes "big". So only "Hello" is left. The print jobs should use a queue, like a line at the canteen: first in, first out (FIFO). The person who pressed Print first should get their pages first, which is fair. If the printer used a stack, the newest job would always jump ahead, and the first person might wait for a very long time.

**O5 key points (1 mark each):** stack for Undo because the last action is undone first · only "Hello" is left · queue for print jobs (first in, first out) · explains why a queue is fair for printing · uses LIFO/FIFO or the plates/line idea correctly. *Also accept* a drawing of the stack instead of words.
