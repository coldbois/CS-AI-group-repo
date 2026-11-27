# 3.1 Introduction to Symbolic AI and Modern Relevance

![Dandroid excited to get a brain](../../../assets/dandroid/dandroid-excited.png)

**Chapter 3 · Dandroid's Brain** · Study Guide pp. 109–116 · Slides 33–35 · Test Bank T17, M17

> **Mission.** A student asks Dandroid: "Do I meet the scholarship's GPA rule?" Dandroid has no training data, only the written rule. Can Dandroid still give a smart answer, and explain it?

**You will learn to**

- define Symbolic AI in your own words
- name the parts: facts, rules, knowledge base, inference engine
- compare Symbolic AI with machine learning

**Key words:** AI, symbol, fact, rule, knowledge base, inference engine, machine learning

---

## The building blocks of Symbolic AI

**Artificial intelligence (AI)** builds systems that reason, plan or solve problems. **Symbolic AI** does it with human-readable **symbols** and **rules**: words and statements that a person can read, check and change.

![Figure 3.1a](../Diagrams%20and%20Pictures/3-1_building-blocks.png)

*Figure 3.1a. Facts + rules → a conclusion (Study Guide p. 110; slide 34 shows the same example).*

We use one example throughout the module, on the slides and in the Test Bank:

| Part | Meaning | Our example |
| --- | --- | --- |
| **Fact** | something true in the system | `GPA = 3.8` |
| **Rule** | IF condition THEN conclusion | `IF GPA ≥ 3.5 THEN academic_ok` |
| **Knowledge base** | the collection of facts and rules | the fact and the rule above |
| **Inference engine** | applies rules to facts to reach conclusions | sees 3.8 ≥ 3.5, so the rule fires |
| **Conclusion** | the new fact it derives | `academic_ok` |

Because the rule is written down, Dandroid can also explain *why*: "academic_ok, because your GPA of 3.8 meets the rule GPA ≥ 3.5." You can always see which rule gave the answer.

> **Bug alert.** The rule checks only the GPA. It does *not* prove the student wins the whole scholarship. A symbolic system's conclusions are limited to the knowledge it was given.

## How a symbolic system reasons

![Figure 3.1b](../Diagrams%20and%20Pictures/3-1_five-steps.png)

*Figure 3.1b. How a symbolic system reasons (Study Guide p. 111).*

1. **Receive** the facts (GPA = 3.8).
2. **Store** them in working memory.
3. **Match:** find the rules whose IF part is true.
4. **Apply:** fire the rule and add its THEN part as a new fact.
5. **Answer:** give the conclusion, or say "not enough information".

> **Dandroid's tip.** Starting from the facts and seeing what follows is called **forward chaining**. Starting from a question and checking what would prove it is **backward chaining**. Both get a deep dive in [3.3](../../18_reasoning-and-expert-systems/Main%20Theory/18_main-theory.md).

## Symbolic AI vs machine learning

**Machine learning (ML)** is the other big family of AI. Instead of being given rules, an ML system finds patterns in lots of examples. Here are two ways to build a spam filter:

![Figure 3.1c](../Diagrams%20and%20Pictures/3-1_symbolic-vs-ml.png)

*Figure 3.1c. Two ways to build a spam filter (Study Guide p. 112; slide 35).*

| | **Symbolic AI** | **Machine learning** |
| --- | --- | --- |
| How it's built | a human writes `IF subject contains "free money" THEN spam` | it studies thousands of emails labelled spam / not spam |
| Knowledge comes from | people | data |
| Can it explain? | yes: you can point to the rule that decided | often hard to explain |
| Weak spot | spammers change their wording, so people must keep adding rules | needs lots of labelled examples |

> **Dandroid's tip.** Neither is always better. Many modern systems combine them, which is called **neuro-symbolic AI** ([3.6](../../21_Putting%20Software%20and%20Symbolic%20AI%20Together/Main%20Theory/21_main-theory.md)).

## A short history, and why it still matters

![Figure 3.1d](../Diagrams%20and%20Pictures/3-1_history.png)

*Figure 3.1d. A short history of AI (Study Guide p. 113).*

Symbolic AI was the main kind of AI for its first thirty years. It was never simply "replaced". Rules, knowledge graphs and planners are still everywhere today: eligibility checkers on government websites, route planners, game characters, and the knowledge graphs behind search-engine fact boxes. Wherever a decision must follow a written policy and be explained, rules are still a good fit.

## Try it

**Think Like a Symbolic AI (and Break It!)** (15 min, solo or pairs): derive new facts about birds, then add one rule that makes Dandroid announce that penguins can fly. Instructions and answers: [16_learner-activity.md](../Learner%20Activity/16_learner-activity.md).

## Check yourself

1. What is the difference between a fact and a rule?
2. Which part applies rules to facts?
3. Give one task that suits Symbolic AI and one that suits machine learning.

**Answers (try first, then peek)**
1. A fact is stored as true; a rule says what follows IF its conditions hold.
2. The inference engine.
3. Symbolic: checking a written policy. ML: recognising cats in photos.


More questions: [16_test-bank.md](../Test%20bank%20Question_Answer/16_test-bank.md)

## Remember

- Symbolic AI = explicit symbols + rules + reasoning.
- The knowledge base stores; the inference engine reasons.
- It is different from ML, and often combined with it.

## Watch and explore

**Machine Learning for Kids** (machinelearningforkids.co.uk). Train a tiny ML model to feel the contrast with writing rules: make a two-label text classifier, then write the same thing as IF-THEN rules. Which was easier? Check the account or "try it now" option before class.

## References

- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. Chapters 1 and 7.
- McCarthy, J., Minsky, M. L., Rochester, N., & Shannon, C. E. (1955). *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*.
- Stanford Encyclopedia of Philosophy. (2021). *Logic-Based Artificial Intelligence*. https://plato.stanford.edu/entries/logic-ai/

---

Previous: [2.7 Software Engineering](../../../Software%20Fundamentals/15_software-engineering/Main%20Theory/15_main-theory.md) · Next: [3.2 Knowledge Representation](../../17_knowledge-representation/Main%20Theory/17_main-theory.md) · Up: [Chapter 3 overview](../../README.md)
