# 3.5 Test Bank: Advantages and Limitations of Symbolic AI

T23, M23 and O9 are the same as in the *Dandroid's Logic Lab* Test Bank (O9 covers 3.5 and 3.6). Q1–Q2 are extra practice. Answers are at the bottom.

## Questions

**T23 (True or False).** If a rule-based system always gives the same answer, that answer is always correct.

**M23 (choose ONE).** Which is a weakness of Symbolic AI?

- A. It does not need lots of training data
- B. It can show which rules it used
- C. It can fail on cases its rules did not expect
- D. It gives the same answer every time

**O9. Rules, learning or both?** (about 100 words, 5 marks)

Dandroid's school wants an app. A student takes a photo of a handwritten sum, like "2 + 3 = 6". The app must say whether it is right and explain why.

(1) Which part of the job needs machine learning? Why? (2) Which part needs Symbolic AI rules? Why? (3) What could go wrong, and how could the app handle it?

Use these words: machine learning · rules · hybrid · explain · mistake

**Q1.** Rule: IF GPA ≥ 3.5 THEN academic_criterion_met. Which of these students meet it: 3.8, 3.2, 3.5, 3.4?

**Q2 (True or False).** A consistent rule-based system is always correct. *(Chapter 3 quick quiz)*

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T23 | **False** | Same answer every time only means it is consistent. Correct version: a wrong rule gives the same wrong answer every time. Consistent does not mean correct. |
| M23 | **C** | This is called brittleness. A, B and D are strengths (no big data, traceable, consistent). |
| Q1 | 3.8 and 3.5 | 3.5 counts because the rule says "≥". |
| Q2 | **False** | It can be consistently wrong. |

**O9 sample answer (134 words).** Reading the handwriting needs machine learning. Everyone writes numbers differently, so it would be almost impossible to write rules for every handwriting style. A neural network that has learned from many examples is good at this. Checking the sum needs Symbolic AI rules. Maths rules are clear and always the same, and the app can show which rule it used, for example "2 + 3 = 5, not 6". So the best design is a hybrid: the learning part reads the photo and turns it into symbols, and the rule part checks the maths and explains the mistake. Something could still go wrong: the learning part might read a messy 5 as a 6. To handle this, the app could show what it read and ask "Did you write 6?" before marking the answer.

**O9 key points (1 mark each):** ML reads the handwriting (too varied for rules) · rules check the maths and can explain the answer · names the combination: hybrid (neuro-symbolic) · names a risk, e.g. misreading the handwriting · gives a sensible way to handle it. *Also accept:* a learner who chooses only one method can still earn marks if they explain what it would do badly.
