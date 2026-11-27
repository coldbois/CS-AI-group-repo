# 2.1 Test Bank: Where Operating Systems Meet Symbolic AI

T9 and M9 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T9 (True or False).** Every program that uses IF-THEN rules is artificial intelligence.

**M9 (choose ONE).** Which job is best for Symbolic AI rules?

- A. Checking a written school rule and explaining why
- B. Making the screen brighter
- C. Charging the laptop
- D. Recognising faces in photos

**Q1.** Facts: `memory_full`, `disk_activity_high`. Using the rules in Figure 2.1c, which rules fire and what is recommended?

**Q2.** An AI program gets stuck in an endless loop. What can the OS do, and what can't it do?

**Q3.** What was XCON, and why is it mentioned in this topic?

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T9 | **False** | An OS password check uses IF-THEN, but it just follows one fixed rule. Correct version: using IF-THEN does not make a program AI. Symbolic AI reasons with many rules and can explain its answer. |
| M9 | **A** | Clear written rules can become IF-THEN rules that explain themselves. B is a simple setting, C is hardware, and faces (D) are too varied for hand-written rules, so machine learning fits better. |
| Q1 | R2, then R3 | R2 adds `suspect_thrashing`, then R3 recommends closing programs or adding RAM. R1 needs `cpu_usage_high` AND `one_process_uses_most_cpu`, which are not both given. |
| Q2 | Stop it, not fix it | The OS can end the process and free its memory, but it can't correct the program's logic. |
| Q3 | An expert system | A 1980s expert system that used thousands of rules to configure computer orders: an early example of AI being used for computers. |
