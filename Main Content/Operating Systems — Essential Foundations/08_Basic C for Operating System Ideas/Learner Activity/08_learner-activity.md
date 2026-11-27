# Try it: Predict the Output (1.8)

**Time:** 15 min · **Group:** solo · **You need:** a browser or paper · Study Guide pp. 49–50

**Goal:** read C code like a computer: predict first, then run it to check.

## Prepare

Open a free online C compiler such as OnlineGDB (onlinegdb.com/online_c_compiler, no account needed), or copy [hello.c](code/hello.c) and [time_slice.c](code/time_slice.c) if you have `gcc`. No internet? Do it on paper and use the answers below.

Every snippet goes inside `main`, between `{` and `return 0;`.

## Steps

1. **Predict** what this prints: `printf("%d\n", 7 + 5);`
2. **Predict:** `int a = 4; int b = a * 3; printf("%d\n", b);`
3. Run both. Were you right?
4. Change the time-slice program ([time_slice.c](code/time_slice.c)) to **5 processes**. Predict, then run.
5. Delete the `;` after `return 0`. What does the compiler say?

## Record

| Snippet | My prediction | Actual output |
| --- | --- | --- |
| `7 + 5` | | |
| `b = a * 3` | | |
| 5 processes | | |
| Missing `;` | | |

## Reflect

- Why did a missing `;` stop the program from running at all?
- Which mistakes can the compiler catch, and which can't it?

## Check it: expected results

These outputs were checked by compiling the code with `gcc`.

| Snippet | Output |
| --- | --- |
| `7 + 5` | `12` |
| `b = a * 3` | `12` (4 × 3) |
| 5 processes | `Total time: 10` (2 × 5) |
| Missing `;` | the program is not built. gcc says `error: expected ';' before '}' token` and points to the `return 0` line |

- A missing `;` is a **syntax error**: the code breaks C's grammar, so the compiler refuses to build it.
- The compiler catches broken grammar, but not wrong ideas (**logic errors**). If you had typed `+` where you meant `*`, it would happily print the wrong answer. You'll hunt that kind of bug in [2.3](../../../Software%20Fundamentals/11_computer-programming/Learner%20Activity/11_learner-activity.md).
