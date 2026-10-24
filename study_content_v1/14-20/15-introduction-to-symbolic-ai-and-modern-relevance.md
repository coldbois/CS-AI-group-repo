# Section 15: Introduction to Symbolic AI and Modern Relevance

## 1. What is symbolic AI?

**Symbolic artificial intelligence (symbolic AI)** is an approach to AI that represents knowledge with symbols, facts, and rules, then uses logic to draw conclusions. It is also known as **Good Old-Fashioned AI (GOFAI)**, a name associated with the earlier, logic-oriented tradition of AI research.

For example, a symbolic system might store facts such as `Fever` and `Cough`, then apply a rule such as:

```text
IF Fever AND Cough
THEN ConsiderPossibleInfection
```

The rule does not automatically prove that a person has a particular disease. It only shows how a system can use explicitly represented information to reach a conclusion or recommendation.

A helpful analogy is a careful clerk working from a rulebook. The clerk applies the written rules and can show which rule was used. A machine-learning system is more like an apprentice who has learned patterns from many examples; it may make useful predictions, but its reasoning may not be easy to express as a short list of human-readable rules.

## 2. A short history

During the 1950s and 1960s, AI researchers explored whether parts of human intelligence could be modeled using logic, symbols, and explicit rules.

| Person | Contribution described in the source |
|---|---|
| John McCarthy | Helped organize the Dartmouth conference associated with the naming of AI, created the Lisp programming language, and is associated with the introduction of automatic garbage collection. |
| Alan Turing | Proposed the Turing Test as a way to discuss or assess whether a machine's behavior could appear intelligent. |
| Marvin Minsky | Co-founded the MIT AI Lab and contributed ideas such as frames and microworlds. |
| Herbert Simon and Allen Newell | Built early reasoning programs, including the Logic Theorist and General Problem Solver. |

During the 1960s and 1970s, these ideas contributed to **expert systems**: programs designed to apply stored specialist knowledge in areas such as medicine, engineering, and law.

## 3. Key features of symbolic AI

- **Symbolic representation:** Information is stored as symbols that stand for things, properties, or ideas. Examples include `Fever`, `Cough`, and `PatientA`.
- **Rule-based reasoning:** Explicit rules tell the system how to derive a conclusion from available facts. A common format is `IF condition THEN conclusion`.
- **Predictable rule application:** When the same rules, facts, and execution settings are used, a basic deterministic rule engine generally follows the same steps and reaches the same result. This does not mean that every real-world problem has a certain or correct answer; the stored facts and rules may be incomplete or wrong.
- **Knowledge-driven, top-down design:** Human experts or developers often encode knowledge and rules first, and the system applies them. This contrasts with many machine-learning methods, which learn patterns from data.

## 4. The physical symbol system idea

A **physical symbol system** is a system that manipulates symbols in structured ways to produce intelligent behavior. In this view, symbols can be combined into expressions, refer to objects or ideas, and be interpreted to guide decisions or actions.

For example, a simplified medical knowledge base might represent `Fever`, `Cough`, and `COVID19` as symbols. A rule could be written:

```text
IF Fever AND Cough
THEN Suspect(COVID19)
```

This is an example of a rule's form, not a reliable medical diagnostic rule. Real diagnosis requires much more evidence and professional judgment.

## 5. Applications

| Field | Example use described in the source |
|---|---|
| Medicine | Assist with diagnostic reasoning from stated symptoms and facts. |
| Business | Support decisions using explicit policies or rules. |
| Law | Analyze a case against a defined set of rules. |
| Robotics | Plan tasks and actions using symbolic descriptions of a situation. |

Symbolic systems are especially attractive when the relevant rules can be stated clearly and users need to inspect how a conclusion was reached.

## 6. Modern relevance: neuro-symbolic AI

**Neuro-symbolic AI** combines machine learning (including neural networks) with symbolic representations or reasoning.

A simplified workflow might look like this:

1. A machine-learning model processes raw input, such as an image, recording, or piece of text.
2. The model outputs a structured result, such as `TumourDetected` or `ObjectIsCup`.
3. A symbolic system combines that result with known facts and rules.
4. The system produces a conclusion and may show the rules or facts used to reach it.

The machine-learning component can be useful for recognizing patterns in complicated raw data. The symbolic component can help organize knowledge, enforce explicit rules, or explain the path from premises to conclusion. A hybrid approach does not automatically guarantee accurate predictions or trustworthy explanations; its reliability depends on the design and evidence.

The source identifies DeepMind's **AlphaGeometry** as a prominent example combining learning and symbolic reasoning. It also contrasts MYCIN, a classic rule-based medical expert system, with systems such as ChatGPT, AlphaGo, and Midjourney, which are not primarily symbolic AI systems.

## 7. Key takeaways

- Symbolic AI represents knowledge with symbols, facts, and explicit rules.
- Rule-based systems can make their inference steps easier to inspect, but they depend on the quality and completeness of their stored knowledge.
- Expert systems were an important application of symbolic AI.
- Neuro-symbolic AI aims to combine machine learning's pattern recognition with symbolic reasoning and structured knowledge.
