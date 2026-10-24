# Section 17: Reasoning and Expert Systems

## 1. Reasoning and expert systems

**Reasoning** is the process of using facts and rules to reach conclusions. An **expert system** is an AI program designed to solve problems in a particular field by using stored specialist knowledge and a reasoning process.

Imagine a doctor considering a patient's symptoms, applying medical knowledge, and reaching a diagnosis. A rule-based expert system attempts to reproduce a limited, structured part of this process: it receives facts, checks rules, and derives a conclusion. It does not automatically possess a doctor's broad understanding, judgment, or responsibility.

## 2. Three kinds of reasoning

| Type | Direction | Example | What it provides |
|---|---|---|---|
| Deductive | General rule → specific conclusion | All cats have a property; Luna is a cat; therefore Luna has that property. | A conclusion follows necessarily if the premises and inference rule are true and valid. |
| Inductive | Specific observations → general pattern | Every cat observed so far has whiskers; a new cat probably has whiskers. | A generalization that may be useful but is not guaranteed. |
| Abductive | Observation → best available explanation | Muddy footprints appear indoors; perhaps the dog walked inside. | A plausible explanation, not a proof that it is the only explanation. |

Deduction is central to classical symbolic AI because rules can be applied logically. However, a deductive conclusion is only as reliable as its premises and the validity of the inference. Induction and abduction are less conclusive: they help generalize or explain observations, but other possibilities may exist.

## 3. Main components of an expert system

| Component | Job | Example |
|---|---|---|
| Knowledge base | Stores facts and rules about the domain. | `IF car_wont_start AND battery_dead THEN inspect_or_replace_battery`. |
| Inference engine | Applies rules to known facts to derive new facts or decisions. | Checks whether the conditions of a rule are satisfied. |
| User interface | Lets a person enter information and receive results or explanations. | A screen that asks questions and displays a recommendation. |

Some expert systems also include explanation facilities or tools for editing the knowledge base, but the source's core model focuses on these three components.

## 4. How inference works

Two common strategies are **forward chaining** and **backward chaining**.

### Forward chaining: facts first

Forward chaining starts with facts already known and repeatedly applies rules whose conditions are satisfied. It is called **data-driven** because the available facts determine which rules can fire.

Example:

```text
Fact: HasCold
Fact: HasFlu
Rule: IF HasCold AND HasFlu THEN MayBeSick
Conclusion: MayBeSick
```

The system begins with the known conditions and works forward to a conclusion. The conclusion's meaning depends on the rule: in a realistic health system, a simplistic rule like this is not enough to make a reliable medical decision.

### Backward chaining: goal first

Backward chaining starts with a question or goal and checks whether known facts and rules can support it. It is **goal-driven** because the system works backward from the desired conclusion.

For example, if the goal is to determine whether `MayBeSick` follows, the system looks for a rule that concludes `MayBeSick`, then checks whether the rule's conditions, such as `HasCold` and `HasFlu`, can be established.

## 5. Famous systems in the source

| System | Field | Purpose described in the source |
|---|---|---|
| MYCIN | Medicine | Diagnosed bacterial infections and recommended antibiotics. It is a classic example of a medical rule-based expert system. |
| DENDRAL | Chemistry | Helped identify molecular structures of chemical compounds. |
| XCON (also called R1) | Computer configuration | Helped configure computer systems for customers. |
| CLIPS | General expert-system development | A framework for building expert systems, with uses that include engineering and business; the source also notes NASA use in spacecraft-related control applications. |

These systems demonstrate that expert systems can be useful where specialist knowledge can be expressed in structured rules. They are not the same thing as a general-purpose human expert, and their outputs depend on the scope and quality of their knowledge bases.

## 6. Key takeaways

- Reasoning uses information to derive a conclusion.
- Deduction follows from premises and rules; induction generalizes from examples; abduction proposes a likely explanation.
- An expert system combines a knowledge base with an inference engine and a user interface.
- Forward chaining works from facts toward conclusions; backward chaining works from a goal toward the facts needed to support it.
- MYCIN, DENDRAL, XCON, and CLIPS are examples associated with expert systems and rule-based reasoning.
