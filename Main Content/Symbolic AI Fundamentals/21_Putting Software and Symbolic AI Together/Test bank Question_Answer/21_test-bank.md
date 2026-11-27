# 3.6 Test Bank: Putting Software and Symbolic AI Together

T24 and M24 are the same as in the *Dandroid's Logic Lab* Test Bank. Open-ended question O9 covers both 3.5 and 3.6; it is in the [3.5 Test Bank](../../20_advantages-and-limitations-of-symbolic-ai/Test%20bank%20Question_Answer/20_test-bank.md). Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T24 (True or False).** In Prolog, a word that starts with a capital letter, like X, is a variable.

**M24 (choose ONE).**
```prolog
parent(john, mary).
parent(mary, alice).
```
A grandparent is a parent of a parent. Who is John's grandchild?

- A. john
- B. nobody
- C. mary
- D. alice

**Q1.** In the Python admission example, what is printed if `gpa = 2.9` and `english_qualified = True`?

**Q2.** Name the five parts of a rule-based app.

**Q3.** In a neuro-symbolic maths-checking app, which part would notice that 2 + 3 = 6 is wrong?

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T24 | **True** | Names like `parent` start with a small letter. Capital words are variables Prolog fills in. |
| M24 | **D** | John → Mary → Alice. John can't be his own grandchild (A); Mary is his child (C). |
| Q1 | Does not meet both example criteria | 2.9 ≥ 3.0 is false, so `and` is false and the `else` runs. |
| Q2 | user interface, application logic, knowledge base, reasoning component, output | Figure 3.6a. |
| Q3 | The symbolic part | The neural part reads the handwriting; the maths rules check the sum and explain the mistake. |
