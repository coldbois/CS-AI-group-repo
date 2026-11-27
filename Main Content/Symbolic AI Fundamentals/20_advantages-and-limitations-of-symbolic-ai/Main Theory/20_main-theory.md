# 3.5 Advantages and Limitations of Symbolic AI

![Dandroid stuck on a case its rules don't cover](../../../assets/dandroid/dandroid-tired.png)

**Chapter 3 · Dandroid's Brain** · Study Guide pp. 142–150 · Slide 45 · Test Bank T23, M23, O9

> **Mission.** Dandroid's scholarship rule worked perfectly for months. Then the policy changed, a strange case appeared, and someone uploaded a photo instead of a form. Suddenly Dandroid was stuck. Why?

**You will learn to**

- explain the strengths of Symbolic AI
- explain its limitations
- choose symbolic, ML or hybrid for a task, and justify it

**Key words:** traceable, consistent, brittle, knowledge bottleneck, uncertainty, hybrid

---

## Strengths

![Figure 3.5a](../Diagrams%20and%20Pictures/3-5_strengths.png)

*Figure 3.5a. Strengths of Symbolic AI (Study Guide p. 143).*

| Strength | What it means | Example |
| --- | --- | --- |
| **Traceable** | you can see which rules fired | the HOW "receipt" in [3.3](../../18_reasoning-and-expert-systems/Main%20Theory/18_main-theory.md) |
| **Consistent** | same facts + same rules → same answer, every time | every student with GPA 3.8 gets `academic_ok` |
| **No big dataset** | works from rules people write; no millions of examples | the scholarship rule needs only the written policy |
| **Structured problems** | shines when conditions are clear | policies, forms, puzzles |
| **Direct control** | policy changed? Edit one rule and test it, without retraining | change 3.5 to 3.3 in one line |

Symbolic AI is the best fit for stable rules, decisions that must be explained, and a manageable number of exceptions.

## Limitations

![Figure 3.5b](../Diagrams%20and%20Pictures/3-5_limitations.png)

*Figure 3.5b. Limitations of Symbolic AI (Study Guide p. 144).*

| Limitation | What goes wrong |
| --- | --- |
| **Knowledge bottleneck** | turning an expert's know-how into rules is slow and costly; experts often can't say exactly how they decide |
| **Uncertainty** | basic rules are yes/no, but real evidence is often "maybe" |
| **Brittle on new cases** | no matching rule? No answer, or a silly one (the Battery Detective's silence in 3.3) |
| **Unstructured input** | photos, audio and free text must be turned into facts first |
| **Rule tangles** | thousands of rules can overlap and conflict |

The usual fix is a **hybrid**: machine learning perceives the messy world, and rules reason about what it found. Slide 45 puts it in one line: *learning reads the world; rules reason and explain.*

## Consistent ≠ correct

A rule-based system will apply a *wrong* rule perfectly consistently.

![Figure 3.5c](../Diagrams%20and%20Pictures/3-5_uncertainty-and-rules.svg)

*Figure 3.5c. When a crisp rule meets an uncertain world (team diagram, used on Study Guide p. 145).*

Rule: `IF fever AND cough THEN flag for review`.

- ✓ It flags every matching case, every time (**consistent**).
- ✗ It cannot say what the illness is: many causes fit (**uncertainty**).

High-stakes systems (health, money, law) need validated knowledge, testing and human oversight. And **explainable ≠ fair or correct**: you can read a rule and it can still be wrong.

## Worked example: the scholarship rule changes

Rule: `IF GPA ≥ 3.5 THEN academic_criterion_met`. Students: A (3.8), B (3.2), C (3.5), D (3.4).

| Student | GPA ≥ 3.5? |
| --- | --- |
| A (3.8) | ✓ |
| B (3.2) | ✗ |
| C (3.5) | ✓ (3.5 counts: the rule says "≥") |
| D (3.4) | ✗ |

Run it again tomorrow and you get exactly the same results: the rule is **consistent**.

Now the policy changes: students must *also* finish a community activity. The old rule is now **incomplete**. It still runs, still gives the same answers, and those answers are now wrong for anyone without the activity. The fix:

```
IF GPA ≥ 3.5 AND community_activity_done THEN both_criteria_met
```

Notice two things. The system had no way to notice the policy change by itself; a person had to update the rule. And the rule should be checked by a **policy expert**, not just the programmer.

## Choosing an approach

| Task | Best fit | Why |
| --- | --- | --- |
| apply a refund policy | Symbolic | clear written rules, must be explained |
| solve a logic puzzle | Symbolic | exact rules and states (3.4) |
| spot a cat in a photo | ML | too varied for hand-written rules |
| transcribe speech | ML | learned from lots of recordings |
| find themes in 10,000 reviews | ML | messy free text at scale |
| read a handwritten maths answer and check it | **Hybrid** | ML reads the handwriting; rules check the maths |

## Try it

- **The AI Decision Challenge** (20 min, pairs): test the scholarship rule for consistency, update it for the new policy, and sort six tasks into Symbolic, ML or Hybrid. [20_learner-activity-1.md](../Learner%20Activity/20_learner-activity-1.md)
- **Chat with ELIZA: Find the Cracks** (15 min, solo, browser): break a famous 1966 rule-based chatbot. [20_learner-activity-2.md](../Learner%20Activity/20_learner-activity-2.md)

## Check yourself

1. Explain the difference between consistency and correctness.
2. What is the knowledge-acquisition bottleneck?
3. Why might a photo-checking app need a hybrid design?

**Answers (try first, then peek)**
1. Consistent = the same answer every time; correct = the right answer. A wrong rule is consistently wrong.
2. Getting experts' knowledge into rules is slow, costly and hard.
3. ML is needed to recognise what's in the photo; rules can then reason about it.


More questions: [20_test-bank.md](../Test%20bank%20Question_Answer/20_test-bank.md)

## Remember

- Strengths: traceable, consistent, no big data, precise.
- Limits: knowledge bottleneck, uncertainty, brittleness, raw input.
- Pick the method that fits the task, or combine them.

## Watch and explore

**ELIZA historical project** (elizagen.org). The history of the first chatbot, with a "Try ELIZA" link. Read the short history, then do the ELIZA activity. Some online ELIZAs are modern remakes, so note which one you used.

## References

- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. Chapters 1 and 12.
- Weizenbaum, J. (1966). ELIZA: a computer program for the study of natural language communication between man and machine. *Communications of the ACM, 9*(1), 36–45.
- Garcez, A. d'A., & Lamb, L. C. (2023). Neurosymbolic AI: the 3rd wave. *Artificial Intelligence Review, 56*, 12387–12406.

---

Previous: [3.4 Planning](../../19_planning-and-problem-solving/Main%20Theory/19_main-theory.md) · Next: [3.6 Putting Software and Symbolic AI Together](../../21_Putting%20Software%20and%20Symbolic%20AI%20Together/Main%20Theory/21_main-theory.md) · Up: [Chapter 3 overview](../../README.md)
