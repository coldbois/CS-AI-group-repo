# Chapter 3 — Putting Software and Symbolic AI Together

## Learning goals
By the end of this chapter, you should be able to:

1. Explain the relationship between software and symbolic AI.
2. Identify the common parts of a simple rule-based application.
3. Trace information through a small rule-based program.
4. Read a basic Prolog example containing facts, a rule and a query.
5. Explain, at a high level, how neural and symbolic components can be combined.

**Prerequisites:** Read Chapters 1 and 2. Basic familiarity with variables and conditional statements is helpful for the Python example, but not required for the Prolog introduction.

## 3.1 What is the relationship between software and Symbolic AI?

**Software** is a set of programs and related instructions that tell a computer how to perform tasks. **Symbolic AI** is an approach for representing knowledge and reasoning with symbols, relationships and logical rules.

When combined, software provides the application structure and execution environment, while symbolic methods provide a way to store knowledge and derive conclusions from it.

A conventional program may follow fixed instructions. A rule-based application can additionally inspect supplied facts, determine which rules apply and produce a result based on those rules. Not every program containing an `if` statement is a complete AI system; the Python example in this chapter is a small teaching model of rule execution.

## 3.2 Common components of a rule-based application

A simple application may contain these parts:

1. **User interface:** collects information and displays results. It may be a web form, desktop window or chatbot interface.
2. **Application logic:** validates input, manages the sequence of operations and connects the interface to the reasoning component.
3. **Knowledge base:** stores facts, rules and relationships.
4. **Inference engine or reasoning component:** evaluates facts and rules to derive conclusions.
5. **Output handling:** presents a recommendation, explanation, warning or other result.

These components can be arranged differently in real software. An expert system is commonly described using a knowledge base and inference engine, with software interfaces and other services around them [2].

![Architecture diagram connecting a user interface, application logic, reasoning component and output, with a knowledge base supplying rules.](../Diagrams%20and%20Pictures/ch3-01-software-symbolic-architecture.svg)


## 3.3 Worked example: admission criteria checker

Imagine a teaching application that checks two example admission criteria:

- Minimum GPA: 3.0.
- Required English qualification: yes.

The application receives:

- GPA: 3.5.
- English qualification: yes.

It applies three rules:

1. If GPA is at least 3.0, the academic criterion is met.
2. If the English qualification is present, the language criterion is met.
3. If both criteria are met, report that both example criteria are satisfied.

The result is: **Both specified criteria are satisfied.** This is not a real university admission decision. Real admissions can include further requirements, documentation checks and human review.

![Worked flow diagram of an example GPA and English qualification checker.](../Diagrams%20and%20Pictures/ch3-02-admission-checker-flow.svg)


## 3.4 Implementing rules in software

### Python: conditional rules

Python is a general-purpose programming language. A developer can use variables, conditions and logical operators to implement a small rule-based example.

```python
gpa = 3.5
english_qualified = True

if gpa >= 3.0 and english_qualified:
    print("Meets both example criteria")
else:
    print("Does not meet both example criteria")
```

What each part does:

- `gpa` stores a numeric value.
- `english_qualified` stores a Boolean value (`True` or `False`).
- `>=` compares the GPA with the threshold.
- `and` requires both conditions to be true.
- `if` selects which output statement runs.

This is a compact rule implementation. A production application would also validate inputs, manage errors, load policies from an appropriate source, record decisions responsibly and test edge cases.

### Prolog: logic programming

**Prolog** is a programming language associated with logic programming. A Prolog program commonly contains facts, rules and queries. A Prolog system tries to prove a query using the available program clauses [7][8].

```prolog
% Facts
parent(john, mary).
parent(mary, alice).

% Rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
```

Ask the query:

```prolog
?- grandparent(john, alice).
```

Expected answer:

```prolog
true.
```

Why does it succeed?

1. The first fact says John is a parent of Mary.
2. The second fact says Mary is a parent of Alice.
3. The rule says X is a grandparent of Y when X is a parent of Z and Z is a parent of Y.
4. John and Alice satisfy that rule with Mary as Z.

The capital letters `X`, `Y` and `Z` are variables. The operator `:-` separates a rule's conclusion from the conditions required to prove it. The comma means that both conditions must hold.

![Prolog diagram showing facts, a grandparent rule and a query that succeeds.](../Diagrams%20and%20Pictures/ch3-03-prolog-facts-rules-query.svg)



### Python and Prolog compared

| Python example | Prolog example |
|---|---|
| Uses explicit program statements and conditions | Describes relationships as facts and logical rules |
| The programmer writes the control flow | The Prolog engine searches for a proof of a query |
| `if` checks whether a condition is true | A query succeeds if it can be proven from clauses |
| General-purpose language | Logic programming language |

![Illustration of conditional program flow from an input to different suggested outputs.](../Diagrams%20and%20Pictures/ch3-04-python-rule-based-flow.svg)


## 3.5 Tools for learning and experimenting

- [SWI-Prolog documentation](https://www.swi-prolog.org/Documentation.html): the official reference and documentation for SWI-Prolog [8].
- [Learn Prolog Now! — Facts, Rules and Queries](https://lpn.swi-prolog.org/lpnpage.php?pageid=lpn-htmlch1&pagetype=html): an introductory chapter explaining the three basic Prolog constructs [7].
- [SWISH online Prolog environment](https://swish.swi-prolog.org/): a browser-based environment for trying Prolog examples [9].

**Suggested learner route:** Read the first section of *Learn Prolog Now!*, open SWISH, enter the family facts and rule above, then run the query. Predict the output before executing it. Change one fact and run the query again. Record what changed and why.

## 3.6 Practical applications

Software that uses symbolic reasoning can support a range of tasks. Examples include:

- **Education:** checking whether a learner has completed prerequisites and suggesting the next topic under defined rules.
- **Customer support:** applying troubleshooting rules to a user's reported symptoms.
- **Business processes:** checking whether a case meets a written policy or set of conditions.
- **Healthcare decision support:** organizing specialist knowledge and checking information against validated criteria. Such tools should support, not replace, qualified professionals.
- **Automated planning:** representing a starting state, legal actions and a goal, then searching for a sequence of actions that can reach the goal [10][11].

The examples show possible application patterns; they are not claims that every organization uses one identical architecture.

## 3.7 Modern development: neuro-symbolic AI

Neural networks are effective for learning patterns from complex data, including images and audio. Symbolic systems are useful for explicit knowledge, relationships, constraints and logical reasoning. **Neuro-symbolic AI** investigates combinations of these approaches [1][8].

A simplified educational example:

1. A neural component recognizes a handwritten mathematical expression.
2. The output is converted into a structured expression.
3. A symbolic component checks the expression using mathematical rules.
4. The software presents feedback.

The example illustrates a possible division of work; real systems vary and must handle recognition errors and uncertainty.

![Illustration showing a neural component converting perceptual input into structured symbols that a symbolic reasoner checks against rules.](../Diagrams%20and%20Pictures/ch3-05-neuro-symbolic-integration.svg)



## Check your understanding

1. What does the software layer contribute to a rule-based application?
2. What is the role of a knowledge base? What is the role of an inference engine?
3. In the Prolog example, which lines are facts and which line is a rule?
4. Explain why the Python example is a useful teaching model but not, by itself, a complete expert system.
5. Describe one possible division of work between a neural component and a symbolic component.

## Chapter summary

- Software provides the application structure; symbolic AI provides explicit knowledge representation and reasoning.
- A common rule-based application includes an interface, application logic, a knowledge base, a reasoning component and output handling.
- Python can express simple rules with conditions. Prolog represents facts and rules and answers queries by attempting to prove them.
- SWI-Prolog and SWISH provide tools for experimenting with Prolog.
- Neuro-symbolic AI explores combining pattern learning with explicit symbolic reasoning.

**Key takeaway:** Symbolic reasoning becomes useful in an application when software connects the knowledge, reasoning process, input and output into a testable system.
