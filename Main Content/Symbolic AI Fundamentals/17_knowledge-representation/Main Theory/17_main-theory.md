# 3.2 Knowledge Representation

![Dandroid reading word cards](../../../assets/dandroid/dandroid-curious.png)

**Chapter 3 · Dandroid's Brain** · Study Guide pp. 117–123 · Slides 36–37 · Test Bank T18, M18

> **Mission.** Dandroid reads three words: "Mina", "Biology", "enrolled in". To Dandroid they're just letters. How can we store them so Dandroid knows *who* is enrolled in *what*?

**You will learn to**

- identify entities, attributes and relationships
- read simple logic statements
- choose between rules, graphs, frames and ontologies

**Key words:** entity, relationship, logic, triple, knowledge graph, frame, ontology

---

**Knowledge representation (KR)** means storing knowledge in a form a computer can use to reason. Before Dandroid can reason (3.3) or plan (3.4), its knowledge has to be written down in a clear, consistent way.

Three ideas come up again and again:

- an **entity** is a thing: Mina, Biology, University_A, Beijing;
- an **attribute** is a property of a thing: Mina's age, a laptop's memory;
- a **relationship** links two things: Mina *studies* Biology.

## Logic: knowledge as true/false statements

Logic writes knowledge as statements that are either true or false. Let **P** = "It is raining" and **Q** = "The ground is wet".

![Figure 3.2a](../Diagrams%20and%20Pictures/3-2_logic-table.png)

*Figure 3.2a. Logic symbols (Study Guide p. 118).*

| Symbol | Name | Meaning |
| --- | --- | --- |
| ¬P | NOT | it is not raining |
| P ∧ Q | AND | raining *and* the ground is wet |
| P ∨ Q | OR | at least one is true |
| P → Q | IMPLIES | *if* it rains, *then* the ground is wet |
| ∀x Human(x) → Mortal(x) | FOR ALL | every human is mortal (first-order logic) |
| Human(Socrates) | fact | Socrates is a human, so: Mortal(Socrates) |

The last two rows show **first-order logic**, which can talk about *every* member of a group. From "every human is mortal" and "Socrates is a human", a computer can derive "Socrates is mortal" by itself.

> **Bug alert.** From P → Q and Q, you *cannot* conclude P. The ground is wet? Maybe a sprinkler did it, not rain! (Slides 38–39 ask this as a class question, and [3.3](../../18_reasoning-and-expert-systems/Main%20Theory/18_main-theory.md) gives the trap its name.)

## Knowledge graphs: subject → predicate → object

A **triple** links two things with a labelled arrow: *(subject, predicate, object)*. Many triples together make a **knowledge graph**.

![Figure 3.2b](../Diagrams%20and%20Pictures/3-2_knowledge-graph.png)

*Figure 3.2b. Mina's knowledge graph (Study Guide p. 119; slide 36 uses the same graph).*

- (Mina, studies, Biology)
- (Mina, attends, University_A)
- (University_A, located_in, Beijing)
- (Mina, is_a, Student)

Dandroid can now *follow the arrows* to answer a question it was never told directly: **where is Mina's university?** Mina → attends → University_A → located_in → **Beijing**. This is the idea behind the W3C **RDF** standard, and behind the knowledge graphs that search engines use for their fact boxes.

> **Bug alert.** Storing a fact is not understanding it. Dandroid just follows the arrows it was given. If nobody added "located_in", it can't answer.

## More ways to represent knowledge

![Figure 3.2c](../Diagrams%20and%20Pictures/3-2_more-ways.png)

*Figure 3.2c. More ways to represent knowledge (Study Guide p. 120).*

| Representation | What it looks like | Good for | Watch out |
| --- | --- | --- | --- |
| **IF-THEN rules** | `IF passed_prerequisite THEN may_register` | clear conditions and decisions | many exceptions get messy |
| **Frames** | a form with slots: Laptop → brand, memory = 16 GB, OS = Linux | describing objects; can hold default values | defaults can be wrong for a special case |
| **Scripts** | a usual sequence: enter restaurant → order → eat → pay → leave | everyday routines | real life doesn't always follow the script |
| **Ontologies** | a shared vocabulary of classes: Course → ScienceCourse → Biology | agreeing on words across a big system; subclasses **inherit** properties | take effort to build and agree on |

> **Dandroid's tip.** No representation is best for everything. Ask: *what questions must the system answer?* Defaults and inheritance are useful, but watch out for exceptions (remember the penguin in [3.1](../../16_introduction-to-symbolic-ai-and-modern-relevance/Learner%20Activity/16_learner-activity.md)).

## Try it

**Sticky-Note Knowledge Graph** (20 min, pairs): turn four sentences about Kai into triples and a graph, then answer a question just by following arrows. Instructions and answers: [17_learner-activity.md](../Learner%20Activity/17_learner-activity.md).

## Check yourself

1. Write "Lee is a student" and "every student has an ID" in logic. What follows?
2. What are the three parts of a triple?
3. Which representation fits "a laptop with brand, memory and OS"?

**Answers (try first, then peek)**
1. Student(Lee) and ∀x Student(x) → HasID(x), so HasID(Lee).
2. Subject, predicate, object.
3. A frame (slots and values).


More questions: [17_test-bank.md](../Test%20bank%20Question_Answer/17_test-bank.md)

## Remember

- KR = storing knowledge so a computer can use it.
- Logic, rules, graphs, frames, scripts, ontologies.
- Pick the representation that fits the questions.

## Watch and explore

**W3C RDF 1.1 Primer** (w3.org/TR/rdf11-primer), Section 3 only. The official explanation of triples and graphs. Pick one example triple and redraw it as a graph. It is written for developers, so read only the first examples.

## References

- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. Chapters 8 and 10.
- W3C. (2014). *RDF 1.1 Primer*. https://www.w3.org/TR/rdf11-primer/
- Minsky, M. (1974). *A Framework for Representing Knowledge* (MIT AI Memo 306).

---

Previous: [3.1 Introduction to Symbolic AI](../../16_introduction-to-symbolic-ai-and-modern-relevance/Main%20Theory/16_main-theory.md) · Next: [3.3 Reasoning and Expert Systems](../../18_reasoning-and-expert-systems/Main%20Theory/18_main-theory.md) · Up: [Chapter 3 overview](../../README.md)
