# 3.1 Test Bank: Introduction to Symbolic AI and Modern Relevance

T17 and M17 are the same as in the *Dandroid's Logic Lab* Test Bank. Q1–Q3 are extra practice. Answers are at the bottom.

## Questions

**T17 (True or False).** Symbolic AI uses facts and rules that people can read.

**M17 (choose ONE).** Fact: GPA = 3.8. Rule: IF GPA ≥ 3.5 THEN academic_ok. What does Dandroid conclude?

- A. The GPA is too low
- B. Nothing
- C. The student failed
- D. academic_ok

**Q1.** Same rule, but the fact is GPA = 3.2. What does the system conclude, and what should it tell the student?

**Q2.** Name one strength of machine learning and one strength of Symbolic AI for a spam filter.

**Q3 (True or False).** In Symbolic AI, knowledge usually comes from human-written facts and rules. *(Chapter 3 quick quiz)*

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T17 | **True** | Example rule: IF GPA ≥ 3.5 THEN academic_ok. A person can read it and check it. |
| M17 | **D** | 3.8 ≥ 3.5, so the rule fires. 3.8 is above 3.5 (not A); the rule matches, so there is a conclusion (not B); the rule says nothing about failing (not C). |
| Q1 | No conclusion | The rule doesn't fire, so `academic_ok` is not derived. A good system says "not enough information" or "the GPA rule is not met (3.2 < 3.5)" rather than inventing an answer. |
| Q2 | ML: learns new spam patterns from data without anyone writing rules. Symbolic: can explain which rule marked an email as spam. | See Figure 3.1c. |
| Q3 | **True** | The knowledge comes from people, not from training data. |
