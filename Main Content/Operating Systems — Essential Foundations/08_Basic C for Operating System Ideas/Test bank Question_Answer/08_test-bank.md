# 1.8 Test Bank: Basic C for Operating System Ideas

T8 and M8 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T8 (True or False).** A C program starts running in the `main` function.

**M8 (choose ONE).** What does this C code print?

`printf("%d", 4 * 3);`

- A. 12
- B. 4 * 3
- C. 4 3
- D. 7

**Q1.** What is printed by:
```c
int x = 10;
int y = x + 5;
printf("%d\n", y);
```

**Q2 (True or False).** In C, `//` starts a comment that the compiler ignores. *(Chapter 1 quick quiz)*

**Q3.** What does `return 0;` at the end of `main` tell the operating system?

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T8 | **True** | `int main(void)` is the starting point of every C program. |
| M8 | **A** | 4 × 3 = 12, and `%d` prints a whole number. `printf` works out the sum first (not B or C), and `*` means multiply, not add (not D). |
| Q1 | `15` | `y` holds 10 + 5. |
| Q2 | **True** | Comments are notes for humans. |
| Q3 | Success | The program finished successfully. A different number signals an error. |
