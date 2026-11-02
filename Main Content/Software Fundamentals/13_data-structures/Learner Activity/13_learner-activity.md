# Part 13 — Learner Activity: Data Structures in Everyday Life

**Time:** about 20 minutes · **You need:** pen and paper · **No coding needed**

Use this word bank for every activity:

> **array · linked list · stack · queue · tree · graph · hash table**

---

## Activity 1 — Warm-up: what does it remind you of?

Match each everyday thing to a data structure from the word bank.

| Everyday thing | Data structure |
|---|---|
| a) A pile of plates in the kitchen | |
| b) People waiting in line at a bus stop | |
| c) A family tree | |
| d) A row of numbered lockers | |
| e) A map of cities joined by roads | |
| f) A phone's contact list: type a name, get the number | |

> 💡 **Hint:** look back at the pictures in the Main Theory if you get stuck.

---

## Activity 2 — Which one fits?

Read each situation and pick a data structure from the word bank. Then finish the sentence: *"I chose it because…"*

1. A coffee shop makes drinks in the same order people paid.
2. The **Back** button in your web browser takes you to the page you just left.
3. Your school wants to find a student's record quickly by typing their student ID.
4. The folders on your computer: *Documents* contains *Homework*, and *Homework* contains *Maths*.
5. A social media app shows who is friends with whom.

> 💡 **Hint:** ask yourself, *"Is the newest one used first, or the oldest one? Is there a key? Are there levels? Are there connections?"*

---

## Activity 3 — Follow the steps

### 3a. A stack of books 📚

You put books on a pile, one on top of another. You can only take the **top** book.

```
put Red  →  put Blue  →  put Green  →  take one
```

1. Which book do you take?
2. Which books are left on the pile, from bottom to top?

### 3b. A queue at the bus stop 🚌

People join the line one at a time. The bus takes the person at the **front**.

```
Ana joins  →  Ben joins  →  Cho joins  →  bus takes one person
```

1. Who gets on the bus?
2. Who is still waiting, from front to back?

### 3c. Draw it

Draw boxes to show the pile of books after 3a and the line of people after 3b. Label the **top** of the stack and the **front** and **back** of the queue.

---

## Activity 4 — Draw your own tree

Draw a small tree with **at least 6 boxes** about something you know, for example:

- your family (grandparents → parents → you and your siblings), or
- your school (school → faculties → courses).

Then label:

- the **root** (the box at the very top),
- one **parent** and its **children**,
- every **leaf** (a box with nothing below it).

---

## ⭐ Bonus (optional) — Try it in Python

If you have Python, type this in and run it. Can you predict what it prints **before** you run it?

```python
pile = []
pile.append("Red")
pile.append("Blue")
pile.append("Green")
print(pile.pop())
print(pile)
```

---

## ✅ Answers

### Activity 1

| Everyday thing | Data structure |
|---|---|
| a) Pile of plates | **stack** |
| b) Line at a bus stop | **queue** |
| c) Family tree | **tree** |
| d) Numbered lockers | **array** |
| e) Map of cities and roads | **graph** |
| f) Contact list: name → number | **hash table** |

### Activity 2

| # | Answer | Because… |
|---|---|---|
| 1 | **queue** | first to pay, first to be served (FIFO) |
| 2 | **stack** | the most recent page comes back first (LIFO) |
| 3 | **hash table** | the student ID is a key that finds the record straight away |
| 4 | **tree** | folders sit inside folders, in levels |
| 5 | **graph** | people are connected to each other, like a network |

Other answers can be fine if the reason makes sense.

### Activity 3

- **3a.** You take **Green** (it went on last, so it comes off first). Left on the pile, bottom to top: **Red, Blue**.
- **3b.** **Ana** gets on the bus (she arrived first). Still waiting, front to back: **Ben, Cho**.
- **3c.** The drawing should show **Blue** on top of **Red** with "top" next to Blue, and **Ben** at the front and **Cho** at the back of the line.

### Activity 4

Check the drawing:

- The root is the one box at the top with nothing above it.
- Every other box has exactly **one** box above it (its parent).
- The leaves are the boxes with nothing below them.

### ⭐ Bonus

```
Green
['Red', 'Blue']
```

`pop()` takes the **last** item added, which is exactly how a stack works.
