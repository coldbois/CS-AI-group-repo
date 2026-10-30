# Section 17 — Reasoning and Expert Systems

Reasoning means using facts and rules to reach a conclusion. An **expert system** is a program designed to solve problems in one area using stored knowledge and a reasoning process. A rough analogy is a doctor considering symptoms and applying medical knowledge, although real medical decisions are much more complicated than a simple rule system.

## Three types of reasoning

**Deductive reasoning** applies a general rule to a specific case. If all cats are mammals and Luna is a cat, then Luna is a mammal. If the premises and logic are correct, the conclusion follows.

**Inductive reasoning** looks at examples and suggests a general pattern. If many cats you have seen have whiskers, you might expect another cat to have whiskers too. That conclusion is likely, not guaranteed.

**Abductive reasoning** looks at an observation and suggests a possible explanation. Muddy footprints might mean a dog came inside, but there could be another reason.

Symbolic AI often relies on deduction because the rules can be written explicitly. Induction and abduction are useful too, but they involve generalising from examples or choosing a likely explanation.

## How an expert system is put together

The **knowledge base** stores facts and rules. A toy rule might be `IF car will not start AND battery is dead THEN check the battery`.

The **inference engine** applies the rules. The **user interface** lets a person enter information and receive the result. Some systems can also show which rules they used.

Two common reasoning strategies are:

- **Forward chaining** starts with known facts and applies rules to see what conclusions follow. It is data-driven.
- **Backward chaining** starts with a goal or question and checks which facts and rules would support it. It is goal-driven.

For example, if the system knows `Cold` and `Flu` and has the rule `Cold AND Flu -> Sick`, forward chaining can conclude `Sick`. Backward chaining starts by asking whether `Sick` can be supported, then checks the required facts. This is a simplified logic example, not medical advice.

## Famous examples

- **MYCIN** was designed to identify bacterial infections and recommend antibiotics.
- **DENDRAL** helped researchers identify chemical structures.
- **XCON (R1)** configured computer systems for customers.
- **CLIPS** is a framework for building rule-based expert systems and has been used in engineering work, including projects associated with NASA.

Expert systems can work well when knowledge can be written down clearly. Their results still depend on the quality of their facts and rules, and keeping those rules up to date can take a lot of effort.
