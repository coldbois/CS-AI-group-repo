# 18. Reasoning and Expert Systems

## 18.1 Topic overview

Topic 17 explained how knowledge can be represented. This topic looks at what an AI system does with that knowledge. **Reasoning** is the process of using facts and rules to reach conclusions. An **expert system** is a computer program that uses knowledge about a particular subject area and reasoning procedures to provide advice, classifications or possible solutions.

A simple example is a computer-support system. It may ask whether a laptop turns on, whether its charger is connected and whether an indicator light is visible. It then compares the answers with stored rules and suggests a possible next check. It is not a human technician; it works within the knowledge and rules provided to it.

### Learning outcomes

By the end of this topic, learners should be able to:

1. Distinguish deduction, induction and abduction.
2. Explain inference and use basic inference patterns.
3. Describe the parts of a rule-based inference system.
4. Trace forward chaining and backward chaining.
5. Explain the architecture and purpose of an expert system.
6. Identify practical uses, limitations and the need for human oversight.

### Key terms

| Term | Meaning |
|---|---|
| Reasoning | Using available information to reach a conclusion. |
| Inference | Deriving a conclusion from premises or facts. |
| Premise | A statement used as a starting point for reasoning. |
| Inference engine | The component that applies rules to facts. |
| Working memory | Information about the current case or problem. |
| Expert system | A program that applies specialist knowledge to a limited problem area. |
| Explanation facility | A component that can show which facts and rules led to a result. |

## 18.2 Three common forms of reasoning

### Deductive reasoning

Deduction applies a general rule to a specific case. If the premises are true and the reasoning is valid, the conclusion must follow.

Example:

- Rule: Every enrolled student has a student record.
- Fact: Asha is an enrolled student.
- Conclusion: Asha has a student record.

### Inductive reasoning

Induction uses several observations to form a general pattern. The conclusion is plausible but not guaranteed.

Example: A student notices that the library was busy on several Monday afternoons and expects it to be busy next Monday. The pattern may be useful, but an exam week or holiday could change it.

### Abductive reasoning

Abduction starts with an observation and considers a possible explanation. The explanation is not certain because other causes may produce the same observation.

Example: A laptop battery is empty. One possible explanation is that the charger was not connected, but the battery or charger could also be faulty.

| Type | Starts with | Result | Is the result guaranteed? |
|---|---|---|---|
| Deduction | Rule and facts | A conclusion that follows from them | Yes, if premises are true and inference is valid |
| Induction | Repeated observations | A general pattern | No |
| Abduction | An observation | A plausible explanation | No |

Do not mix up “a likely explanation” with “a proven cause”. That difference matters in diagnosis and troubleshooting.

## 18.3 Inference and basic inference rules

Inference is the step where a system derives a new statement from statements it already has. A rule base may contain logical patterns that the system can apply repeatedly.

### Modus Ponens

If `P → Q` and `P` are true, then `Q` follows.

Example:

- If a file is saved, it appears in the selected folder.
- The file was saved in the selected folder.
- Therefore, it appears in that folder.

In symbolic form:

```text
P → Q
P
----
Q
```

### Modus Tollens

If `P → Q` and `¬Q` are true, then `¬P` follows.

```text
P → Q
¬Q
----
¬P
```

This pattern is valid when the conditional statement is being treated as a strict rule. In everyday situations, the rule itself may be incomplete. For example, a website might be unavailable even when a computer is connected to the internet, so the example must state its assumptions.

### A common invalid step

From `P → Q` and `Q`, we cannot conclude `P`. This is called affirming the consequent. If the ground is wet, it may have rained, but a sprinkler could also have made it wet.

## 18.4 Inference engines and rule-based systems

An inference engine applies rules to facts. A simple rule-based system usually contains:

- **Knowledge base:** The stored facts and rules about the domain.
- **Working memory:** Facts about the current case being considered.
- **Inference engine:** Matches rules against the facts and derives conclusions.
- **User interface:** Lets a user enter information and receive results.
- **Explanation facility:** Shows which rules or facts contributed to a conclusion, if the system provides this feature.

### Worked example — course eligibility

Knowledge base:

```text
Rule 1: IF prerequisite_passed THEN prerequisite_ok.
Rule 2: IF fees_paid THEN finance_ok.
Rule 3: IF prerequisite_ok AND finance_ok THEN may_register.
```

Current case:

```text
prerequisite_passed = true
fees_paid = true
```

Reasoning:

1. Rule 1 matches, so add `prerequisite_ok` to working memory.
2. Rule 2 matches, so add `finance_ok`.
3. Rule 3 now matches, so add `may_register`.

The system concludes that the student may register under these rules. It has not checked any requirement that was not included in the knowledge base.

## 18.5 Forward chaining and backward chaining

Both methods apply rules, but they start from different places.

### Forward chaining — data-driven

Forward chaining starts with known facts, finds rules whose conditions match those facts, and adds their conclusions. It repeats this process until it reaches a useful conclusion or no more rules can be applied.

Using the course example:

`prerequisite_passed` and `fees_paid` → `prerequisite_ok` and `finance_ok` → `may_register`.

This is useful when new facts arrive and the system needs to work out what follows from them.

### Backward chaining — goal-driven

Backward chaining starts with a question or goal and works backwards to see what would be needed to prove it.

Question: `may_register`?

1. Find the rule whose conclusion is `may_register`.
2. Check whether `prerequisite_ok` and `finance_ok` are true.
3. To prove `prerequisite_ok`, check `prerequisite_passed`.
4. To prove `finance_ok`, check `fees_paid`.
5. If both starting facts are available, the goal is supported.

Backward chaining is useful when the system has a specific question to answer. It may ask for missing information when a required fact is not already known.

| Forward chaining | Backward chaining |
|---|---|
| Starts with facts. | Starts with a goal or query. |
| Data-driven. | Goal-driven. |
| Derives what follows from available facts. | Checks what facts are needed to support a particular goal. |

## 18.6 Expert system architecture

An expert system focuses on a particular domain, such as equipment troubleshooting or a narrow medical decision-support task. Its knowledge is usually collected from specialists, documented sources or validated domain rules.

A common architecture contains:

1. **Knowledge base:** Domain facts, rules and relationships.
2. **Inference engine:** Applies the rules to the current case.
3. **Working memory:** Holds case-specific facts and intermediate conclusions.
4. **User interface:** Collects information and presents the result.
5. **Explanation facility:** Explains the path to the conclusion.
6. **Knowledge acquisition and maintenance:** The process of collecting, checking and updating domain knowledge.

The knowledge base and inference engine are kept separate in many designs. This makes it possible to update rules without rewriting the entire reasoning procedure.

### Worked example — a simple support expert system

A fictional system uses these rules:

```text
R1: IF laptop_does_not_turn_on AND charger_not_connected
    THEN suggest_checking_power_connection.

R2: IF laptop_does_not_turn_on AND charger_connected
    AND charging_light_off
    THEN suggest_checking_charger_or_power_port.
```

A user reports that the laptop does not turn on, the charger is connected and the charging light is off. R2 matches. The system suggests checking the charger or power port. This is a suggestion based on a simplified rule set, not a confirmed diagnosis.

## 18.7 Historical examples and applications

- **MYCIN:** A Stanford-developed research expert system from the 1970s. Stanford technical-report material and a PubMed-indexed article describe its rule-based consultation and explanation approach ([Stanford report](https://i.stanford.edu/pub/cstr/reports/cs/tr/82/926/CS-TR-82-926.pdf); [Sotos, 1990](https://pubmed.ncbi.nlm.nih.gov/2241738/)). It used rules to assist with a narrow medical task involving certain infections. It is a historical example, not a current medical product or a substitute for a clinician.
- **DENDRAL:** An early expert system that helped analyse chemical data and infer molecular structures.
- **R1/XCON:** A system used by Digital Equipment Corporation to help configure computer orders.

Expert-system ideas have also been applied to equipment fault diagnosis, technical support, configuration and decision support. In modern settings, rule-based components may be combined with databases, statistical models or machine-learning systems.

## 18.8 Strengths and limitations

**Strengths**

- Rules can make a system's decisions easier to inspect.
- A knowledge base can preserve specialist knowledge.
- The same rules can be applied consistently to similar cases.
- A system can quickly check many clearly defined conditions.

**Limitations**

- Building and updating the knowledge base can take a lot of work.
- The system may fail when a case falls outside its rules.
- Rules can conflict or rely on assumptions that are no longer true.
- The system may not handle uncertainty or common-sense context well unless these are explicitly modelled.
- A clear explanation does not guarantee that the conclusion is correct; the facts and rules may still be wrong.

### Rule conflict example

Suppose one rule recommends approving an application when all documents are present, while another rule blocks approval when a required document is expired. If both rules match, the system needs a defined priority or conflict-resolution policy. It should not silently choose an arbitrary result.

## 18.9 How this topic connects to the next one

Reasoning can establish what is true, what conditions are satisfied or which options are supported. Planning uses facts, goals and action descriptions to work out what should happen next. For example, a system might reason that a robot is holding a box, then plan a sequence of moves to place it on a shelf.

## Key takeaways

- Deduction follows from premises; induction finds patterns; abduction proposes explanations.
- An inference engine applies rules to facts.
- Forward chaining begins with facts; backward chaining begins with a goal.
- An expert system combines domain knowledge with a reasoning procedure.
- Expert systems are limited by the quality and coverage of their knowledge and should be used with suitable human oversight.
