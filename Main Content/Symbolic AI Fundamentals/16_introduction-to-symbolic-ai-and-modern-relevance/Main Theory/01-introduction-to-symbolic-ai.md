# Chapter 16 — Introduction to Symbolic AI and Modern Relevance

## Learning goals
By the end of this chapter, you should be able to:

1. Define Symbolic AI in your own words.
2. Identify facts, rules, a knowledge base and an inference engine.
3. Explain forward chaining and backward chaining at an introductory level.
4. Compare symbolic approaches with machine learning without assuming one is always better.
5. Give examples of why symbolic methods remain relevant.

**Prerequisites:** Basic familiarity with computers and the idea that a program follows instructions. No AI programming experience is required.

## 16.1 What is Artificial Intelligence?

Artificial Intelligence (AI) is a field of computing concerned with building systems that perform tasks commonly associated with intelligent behaviour, such as reasoning, problem-solving, planning, perception and language use. AI is not one single technique. Researchers have developed different approaches to represent information and produce intelligent behaviour.

One influential approach is **Symbolic Artificial Intelligence**, often called **Symbolic AI** or **classical AI**.

## 16.2 What is Symbolic AI?

Symbolic AI represents knowledge explicitly using symbols and structured relationships. A system can store facts, describe relationships, and apply logical rules to derive conclusions. Instead of relying only on patterns learned from a large dataset, a symbolic system uses knowledge that has been represented in a form its reasoning procedure can manipulate [1][2].

### A simple example: scholarship criteria

Imagine an application that checks two example scholarship conditions:

- Fact: a student's GPA is 3.8.
- Rule: if a student's GPA is at least 3.5, the academic requirement is met.
- Conclusion: the student meets this academic requirement.

The application has applied an explicit rule to a supplied fact. It has not learned the threshold from examples. The conclusion is limited to the condition represented: it does **not** prove that the student qualifies for every part of a real scholarship.

![Flow diagram showing facts entering a knowledge base, an inference engine applying rules, and a conclusion being produced.](../Diagrams%20and%20Pictures/ch1-01-symbolic-ai-process.svg)


## 16.3 The main building blocks

### Facts

A **fact** is a piece of information represented as true within the system's model. For example: `parent(john, mary)` states that John is a parent of Mary.

### Rules

A **rule** describes how a conclusion may follow when specified conditions hold. A common informal format is:

```text
IF condition is true
THEN conclude or perform an action
```

For example: `IF GPA >= 3.5 THEN academic_requirement_met = true`.

### Knowledge base

A **knowledge base** is an organized collection of the facts, rules and relationships used by a system. The quality of its output depends heavily on the relevance and accuracy of that knowledge [2].

### Inference engine

An **inference engine** applies reasoning procedures to the knowledge base and current input. It checks which rules apply and derives conclusions. Many classic rule-based expert systems separate the knowledge base from the inference mechanism [2].

![Diagram showing two parent facts and a grandparent rule producing a derived grandparent relationship.](../Diagrams%20and%20Pictures/ch1-02-facts-rules-conclusions.svg)


## 16.4 How does symbolic reasoning work?

A typical reasoning cycle is:

1. Receive facts or observations.
2. Represent them in the system's knowledge base or working memory.
3. Find rules whose conditions match the available facts.
4. Apply the relevant rules.
5. Return a conclusion, add a derived fact, or report that the information is insufficient.

Two common rule-processing strategies are:

- **Forward chaining:** starts with known facts and repeatedly applies rules to discover what follows. It is useful when the system wants to explore consequences of available information.
- **Backward chaining:** starts with a goal or query and works backwards to check which facts and rules would prove it. It is useful when answering a specific question.

![Side-by-side comparison of forward chaining from facts and backward chaining from a goal.](../Diagrams%20and%20Pictures/ch1-03-forward-backward-chaining.svg)



These strategies describe different directions of reasoning. They are not the only reasoning methods used in symbolic AI.

## 16.5 Symbolic AI and machine learning

Symbolic AI and machine learning are different approaches, but they can also be combined.

| Aspect | Symbolic AI | Machine learning |
|---|---|---|
| Main idea | Explicit symbols, facts, rules and relationships | A model is fitted to examples to learn statistical patterns |
| Where knowledge comes from | Often supplied by people or structured sources | Usually learned from training data |
| Typical strength | Structured reasoning with defined conditions | Pattern recognition in complex or high-dimensional data |
| Explanation | Rule paths may be traceable | Explanation depends on model type and tools |
| Updating | Edit or add knowledge/rules | Often retrain or update the model |
| Example | Check whether requirements are met | Classify an image or detect patterns in text |

This is a simplified comparison. Machine-learning systems vary, and symbolic systems can use statistical or probabilistic extensions. Neither approach is universally superior [1][8].

![Comparison diagram showing explicit facts and rules in symbolic AI and data-driven learning in machine learning, with a link indicating they can be combined.](../Diagrams%20and%20Pictures/ch1-04-symbolic-vs-machine-learning.svg)


## 16.6 A short historical orientation

The modern field of AI is commonly traced to the 1956 Dartmouth Summer Research Project on Artificial Intelligence, where researchers helped establish the field and the term [3]. Symbolic representation and logical reasoning became important strands of early AI work. Later decades saw the development of expert systems, while statistical machine learning and deep learning became increasingly influential in other areas.

This is a broad orientation, not a complete history. AI developed through several overlapping research traditions rather than a single approach replacing all others.

![Timeline showing the naming of AI in 1956, expert systems, the growth of statistical machine learning, deep learning, and current neuro-symbolic research.](../Diagrams%20and%20Pictures/ch1-05-history-and-modern-relevance.svg)


## 16.7 Why is Symbolic AI still relevant?

Symbolic methods remain useful when information can be represented explicitly and a task benefits from clear relationships, constraints or reasoning steps.

### Expert systems

An **expert system** is software designed to apply encoded specialist knowledge to questions or problems in a defined domain. A classic architecture uses a knowledge base and an inference engine [2]. A simple troubleshooting assistant is an illustrative example: it asks about symptoms and applies rules to suggest checks.

### Knowledge representation and knowledge graphs

A knowledge graph stores entities and relationships in a structured network. For example:

- Kathmandu — capital of — Nepal
- Nepal — located in — Asia
- Python — is a — programming language

Such representations can support querying and reasoning over connected information. Symbolic reasoning over knowledge graphs is also an active research area [9].

### Automated planning

A planning problem can be represented using an initial state, a goal, and actions with preconditions and effects. A planner searches for a sequence of actions that can transform the starting state into a state satisfying the goal [10][11]. A puzzle with legal moves and constraints is a simple teaching example.

### Neuro-symbolic AI

**Neuro-symbolic AI** explores ways to combine neural approaches, such as deep learning, with symbolic approaches such as logic and knowledge representation [1][8]. A neural component might identify objects in an image, while a symbolic component reasons about the recognized objects and explicit rules. This is a simplified illustration; real architectures differ.

## 16.8 Check your understanding

1. In your own words, what makes an AI approach symbolic?
2. What is the difference between a fact and a rule?
3. How does an inference engine use a knowledge base?
4. When would forward chaining be useful? When would backward chaining be useful?
5. Give one task where symbolic AI may be a good fit and explain why.

## Chapter summary

- Symbolic AI represents knowledge explicitly using symbols, facts, rules and relationships.
- A knowledge base stores represented knowledge; an inference engine applies reasoning procedures to it.
- Forward chaining begins with facts; backward chaining begins with a goal or query.
- Machine learning typically learns statistical patterns from examples, while symbolic systems manipulate explicit representations.
- Symbolic methods remain relevant in expert systems, knowledge representation, automated planning and neuro-symbolic research.

**Key takeaway:** Symbolic AI is most useful when a problem's knowledge, relationships and conditions can be represented clearly enough for a computer to reason over them.
