# 3.6 Putting Software and Symbolic AI Together

![Dandroid proud of its first app](../../../assets/dandroid/dandroid-proud.png)

**Chapter 3 · Dandroid's Brain** · Study Guide pp. 151–160 · Slides 44–45 · Test Bank T24, M24, O9

> **Mission.** Time to give Dandroid a real job: an app that checks admission criteria and helps users troubleshoot their computers. How do software and Symbolic AI fit together?

**You will learn to**

- name the parts of a rule-based application
- read and change small Python and Prolog programs
- explain how neuro-symbolic AI combines learning and rules

**Key words:** user interface, application logic, Prolog, fact, rule, query, neuro-symbolic

---

## Anatomy of a rule-based app

![Figure 3.6a](../Diagrams%20and%20Pictures/3-6_rule-app-anatomy.png)

*Figure 3.6a. Anatomy of a rule-based app (Study Guide p. 152).*

| Part | Job | Comes from |
| --- | --- | --- |
| **User interface** | a form, window or chatbot | Chapter 2 (software) |
| **Application logic** | checks the input, runs the steps in order | Chapter 2 |
| **Knowledge base** | facts and rules | Chapter 3 (3.1, 3.2) |
| **Reasoning component** | applies the rules | Chapter 3 (3.3) |
| **Output** | an answer, an explanation or a warning | both |

Software builds the pipes. Symbolic AI supplies the thinking. And underneath both, the OS from Chapter 1 runs the app as a process and gives it memory and CPU time.

> **Dandroid's tip.** Not every program with an `if` is AI. The difference: **explicit knowledge** kept apart from the code, and an **engine** that reasons with it.

## Rules in Python: you write the flow

![Figure 3.6b](../Diagrams%20and%20Pictures/3-6_python-rules.png)

*Figure 3.6b. Rules in Python (Study Guide p. 153). The file is [admission_rule.py](../Learner%20Activity/code/admission_rule.py).*

```python
gpa = 3.5
english_qualified = True

# Rule: both criteria must be met
if gpa >= 3.0 and english_qualified:
    print("Meets both example criteria")
else:
    print("Does not meet both example criteria")
```

Output (we ran it): `Meets both example criteria`

- `gpa` stores a number; `english_qualified` stores True/False (a **Boolean**).
- `>=` compares; `and` needs *both* conditions to be true.
- `if ... else` picks which message runs.

This example uses a different threshold (3.0) from the scholarship rule in 3.1 (3.5) on purpose: it is a different, made-up admission rule with two criteria.

> **Bug alert.** This is a teaching example, not a real admissions decision. A real app also checks the input, handles errors, logs its decisions and involves human review.

## Rules in Prolog: describe, then ask

**Prolog** ("programming in logic") works the other way round. You don't write the steps. You describe the facts and rules, then ask a question, and Prolog's built-in engine *searches* for a proof.

![Figure 3.6c](../Diagrams%20and%20Pictures/3-6_prolog-rules.png)

*Figure 3.6c. Rules in Prolog (Study Guide p. 154). The file is [family.pl](../Learner%20Activity/code/family.pl).*

```prolog
% Facts
parent(john, mary).
parent(mary, alice).

% Rule: X is a grandparent of Y if...
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Query
?- grandparent(john, alice).
```

Output: `true.`

- Facts end with a full stop. `parent(john, mary)` means John is Mary's parent.
- Words starting with a **capital** letter (X, Y, Z) are **variables**.
- `:-` means "if". The comma means AND.
- You don't write a loop: Prolog searches for a value of Z that makes both parts true. Z = mary works!

> **Dandroid's tip.** Python: *you* write the control flow. Prolog: you describe facts and rules; the *engine* finds the answer. That is the difference between ordinary software and a symbolic reasoning system in one sentence.

## Neuro-symbolic AI: the best of both

![Figure 3.6d](../Diagrams%20and%20Pictures/3-6_neuro-symbolic.png)

*Figure 3.6d. Neuro-symbolic AI (Study Guide p. 159). The same app is Test Bank question O9.*

1. **See (neural):** a neural network reads a handwritten sum: "2 + 3 = 6".
2. **Convert:** turn it into symbols: `2 + 3 = 6`.
3. **Reason (symbolic):** maths rules check it: 2 + 3 is 5, not 6 ✗.
4. **Explain:** the app gives feedback and says why.

Neural networks are great at perception (images, sound). Symbolic rules are great at logic and explanations. Together they cover each other's weak spots, but recognition mistakes still need handling: the app should show what it read ("Did you write 6?") before marking.

## The big picture: how Dandroid solved the river puzzle

![Figure 3.6e](../Diagrams%20and%20Pictures/3-6_how-dandroid-did-it.png)

*Figure 3.6e. All three chapters working together (slide 44).*

The river-puzzle solver from [3.4](../../19_planning-and-problem-solving/Main%20Theory/19_main-theory.md) ([river_bfs.py](../../19_planning-and-problem-solving/Learner%20Activity/code/river_bfs.py)) uses the whole module:

- **Brain (Symbolic AI, Chapter 3):** states, rules and a goal → search for a plan.
- **Instructions (Software, Chapter 2):** an algorithm (BFS) and a data structure (a queue).
- **Body (OS, Chapter 1):** ran the solver as a process and gave it CPU turns and memory.

*The OS runs it. Software builds it. Symbolic AI reasons with it.*

## Try it

- **Prolog Family Lab on SWISH** (30 min, pairs, browser): build and query a tiny family knowledge base, then add your own rule. [21_learner-activity-1.md](../Learner%20Activity/21_learner-activity-1.md)
- **Python Troubleshooting Assistant** (25 min, solo or pairs): run, test and extend a small rule-based helper. [21_learner-activity-2.md](../Learner%20Activity/21_learner-activity-2.md)

Then try the [Final Mission: Escape Dandroid's Lab](../../../Final_Mission.md).

## Check yourself

1. What does the software layer add to a rule-based app?
2. In Prolog, what does `:-` mean?
3. Describe one job for the neural part and one for the symbolic part of a hybrid system.

**Answers (try first, then peek)**
1. The interface, input checks, the order of steps and the output: it turns rules into a usable, testable app.
2. "If": the head is true if the body is true.
3. Neural: recognise handwriting or images. Symbolic: check them against rules and explain.


More questions: [21_test-bank.md](../Test%20bank%20Question_Answer/21_test-bank.md)

## Remember

- Rule-based app = UI + logic + knowledge base + reasoning + output.
- Python: you code the flow. Prolog: the engine searches for a proof.
- Neuro-symbolic = learning + reasoning together.

## Watch and explore

**Learn Prolog Now!**, Chapter 1, Section 1.1 "Some simple examples" (learnprolognow.org). A friendly introduction to facts, rules and queries. Try its first knowledge base in SWISH. Skip the exercises until you've done the SWISH lab.

## References

- Blackburn, P., Bos, J., & Striegnitz, K. (2006). *Learn Prolog Now!* College Publications. https://www.learnprolognow.org
- SWI-Prolog. (n.d.). *SWISH: SWI-Prolog for SHaring*. https://swish.swi-prolog.org
- Python Software Foundation. (n.d.). *The Python Tutorial*, section 4.1 (if statements). https://docs.python.org/3/tutorial/controlflow.html
- Garcez, A. d'A., & Lamb, L. C. (2023). Neurosymbolic AI: the 3rd wave. *Artificial Intelligence Review, 56*, 12387–12406.

---

Previous: [3.5 Advantages and Limitations](../../20_advantages-and-limitations-of-symbolic-ai/Main%20Theory/20_main-theory.md) · Next: [Final Mission](../../../Final_Mission.md) · Up: [Chapter 3 overview](../../README.md)
