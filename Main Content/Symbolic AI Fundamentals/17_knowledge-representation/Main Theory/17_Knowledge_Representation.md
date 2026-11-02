# 17. Knowledge Representation

## 17.1 Topic overview

Knowledge Representation (KR) is the way an AI system stores information about the world in a form that a computer can work with. It is not simply saving text in a file. A useful representation makes the important objects, facts, properties and relationships clear enough for a program to retrieve and reason about them.

For example, a university assistant might store that:

- `Student_A` is a student.
- `Student_A` studies Computer Science.
- Computer Science is offered by the university.
- A course has a teacher, timetable and set of requirements.

Once these facts are organised, the system can answer questions such as “Which subject does Student A study?” or “Who teaches this course?” This is the link between knowledge representation and reasoning: **KR describes what the system knows; reasoning uses that representation to draw conclusions.**

### Learning outcomes

By the end of this topic, learners should be able to:

1. Explain why AI systems need knowledge representations.
2. Identify facts, entities, attributes and relationships.
3. Read simple propositional and first-order logic statements.
4. Explain rules, semantic networks, knowledge graphs, frames and ontologies.
5. Choose a suitable representation for a simple problem and identify its limitations.

### Key terms

| Term | Meaning |
|---|---|
| Entity | A thing or concept being described, such as a student or course. |
| Attribute | A property of an entity, such as a course name. |
| Fact | A statement treated as true in the system's knowledge base. |
| Relationship | A link between entities, such as “enrolled in”. |
| Knowledge base | An organised collection of facts, rules or other represented knowledge. |
| Representation | The format used to describe knowledge so a system can process it. |

## 17.2 Why represent knowledge?

A computer can store a large amount of data, but storage alone does not explain what the data means. KR gives information a structure. It helps a system identify the difference between a person, a course, a location and a relationship between them.

A good representation should fit the problem, be clear enough to maintain and support the questions or reasoning the system needs to perform. No single representation is best for every task.

**Example — facts versus relationships**

Suppose a system stores these separate words: `Mina`, `Biology`, `enrolled in`. The words alone do not state the relationship. A structured fact makes the meaning clear:

`Mina — enrolled in — Biology`

The same information could be stored as a sentence, a database record, a logical statement or a graph edge. The choice depends on how the system will use it.

## 17.3 Logic as a representation

Logic represents information through statements with formal meanings. It is useful when a system needs to check whether a conclusion follows from known facts.

### Propositional logic

Propositional logic treats each complete statement as either true or false within the model. Let:

- `P`: It is raining.
- `Q`: The ground is wet.

Common connectives are:

| Symbol | Name | Meaning |
|---|---|---|
| `¬P` | NOT | P is false. |
| `P ∧ Q` | AND | Both P and Q are true. |
| `P ∨ Q` | OR | At least one of P or Q is true. |
| `P → Q` | IMPLIES | If P is true, Q must be true under this rule. |

A rule `P → Q` does not say that rain is the only possible cause of wet ground. It says that, in this model, rain is sufficient for the conclusion that the ground is wet. This distinction prevents a common mistake: from “if P then Q” and “Q”, we cannot automatically conclude P. Other causes of Q may exist.

### First-order logic

First-order logic (FOL) can describe objects, their properties and relationships. It adds variables and quantifiers to the logical connectives.

- `Human(Socrates)` means Socrates is human.
- `∀x (Human(x) → Mortal(x))` means every human is mortal.
- From these statements, we can conclude `Mortal(Socrates)`.

`∀` means “for all”; `∃` means “there exists”. FOL is more expressive than propositional logic, but statements must still be written carefully so their intended meaning is clear.

### Worked example

**Given:** Every enrolled student has a student record. Mina is an enrolled student.

1. Rule: `∀x (EnrolledStudent(x) → HasStudentRecord(x))`
2. Fact: `EnrolledStudent(Mina)`
3. Conclusion: `HasStudentRecord(Mina)`

The conclusion follows by applying the general rule to the individual Mina.

## 17.4 Rule-based representation

A rule-based representation stores knowledge as condition-and-conclusion statements, commonly written as **IF–THEN** rules.

```text
IF a student has passed the prerequisite course
THEN the student may register for the next course.
```

The condition is the IF part. The THEN part states what the system should conclude or do when the condition is met. A rule base may contain many such rules, and a reasoning component checks which rules match the current facts.

Rules are easy to read and are useful when knowledge can be stated clearly. They can become difficult to manage when there are many exceptions, overlapping rules or conflicting conclusions. A rule is only as reliable as the knowledge used to create it.

## 17.5 Semantic networks and knowledge graphs

A semantic network represents concepts as **nodes** and their relationships as **labelled links**. A knowledge graph uses the same general idea but is often built as a structured, queryable collection of connected entities and facts.

A common data model for expressing graph facts is an RDF triple. The W3C RDF Primer describes this subject–predicate–object structure: [W3C RDF 1.1 Primer](https://www.w3.org/TR/rdf-primer/).

`subject — predicate — object`

Example:

`Mina — studies — Biology`

Here Mina is the subject, studies is the predicate, and Biology is the object. Another triple could be `Biology — offered by — University_A`. Together, the triples form a small graph.

### Worked example — build a small graph

Start with these facts:

1. Mina studies Biology.
2. Mina attends University A.
3. University A is in Beijing.

Represent them as triples:

```text
(Mina, studies, Biology)
(Mina, attends, University_A)
(University_A, located_in, Beijing)
```

A system can follow the links to answer questions about Mina's subject or university location. RDF is a W3C standard for expressing information about resources as triples.

## 17.6 Frames and scripts

A **frame** describes a familiar object or concept using slots (properties) and values. It is similar to a structured record.

| Frame: Laptop | Value |
|---|---|
| Type | Computer |
| Brand | Example brand |
| Memory | 16 GB |
| Operating system | Linux |

A frame can include default values or inherit properties from a more general frame. Defaults are useful, but they should not be treated as facts that are always true; a specific object may be an exception.

A **script** represents a familiar sequence of events. A restaurant script might be:

1. Enter the restaurant.
2. Find a table.
3. Read the menu.
4. Order food.
5. Eat and pay.
6. Leave.

Scripts can help a system interpret a familiar situation, but real events do not always follow the expected order. A customer may order takeaway or pay before eating, for example.

## 17.7 Ontologies, categories and inheritance

An ontology is a formal description of the important concepts in a domain and the relationships between them. It gives different systems or people a shared vocabulary. In an ontology, classes describe categories, individuals describe particular things, and properties describe relationships or attributes.

A simple taxonomy is a hierarchy of categories:

```text
Course
├── ScienceCourse
│   ├── Biology
│   └── Physics
└── ComputingCourse
    ├── Programming
    └── ArtificialIntelligence
```

A more specific class can inherit properties from a general class. For instance, if every course has a course code, a Biology course also has a course code. Real ontologies can express more than a simple tree: they can define properties, restrictions and relationships between classes.

W3C's OWL 2 language is designed for representing ontologies on the Web ([OWL 2 overview](https://www.w3.org/TR/owl-overview/)). RDF and OWL are related but not identical: RDF provides a graph data model for statements, while OWL adds richer vocabulary and formal semantics for describing classes and relationships.

## 17.8 Choosing a representation

| Representation | Useful when… | Watch out for… |
|---|---|---|
| Propositional logic | The problem uses simple true/false statements. | It does not directly describe objects and their relationships. |
| First-order logic | Facts involve individuals, properties and quantified rules. | Complex formulas may be difficult to write and process. |
| IF–THEN rules | Expert knowledge can be expressed as conditions and conclusions. | Many exceptions can create a large, conflicting rule set. |
| Semantic network / knowledge graph | The links between entities are important. | Poorly defined labels can make relationships ambiguous. |
| Frames | Objects have a familiar set of properties. | Defaults may be mistaken for universal facts. |
| Ontology | A domain needs a shared, formal vocabulary. | Building and maintaining it takes specialist effort. |

## 17.9 Limitations and common misunderstandings

- A knowledge base is not automatically correct. It may contain missing, old or conflicting facts.
- A graph shows relationships, but the system still needs clear meanings for its labels.
- A rule does not cover every possible situation unless the designer has included the relevant cases.
- Inheritance is useful, but exceptions must be represented carefully.
- Symbolic representations can be clear and explainable, but building them can require substantial manual knowledge modelling.

**Common misunderstanding:** “If an AI stores a fact, it understands it like a person.” Storing and manipulating a formal representation is not the same as human understanding. The system operates according to the representation and procedures it has been given.

## 17.10 How this topic connects to the next one

Topic 17 explains how knowledge is represented. Topic 18 explains how a system can use that knowledge to infer new facts or make recommendations. For example, a graph may store that a learner completed a prerequisite; a rule-based reasoner can then check whether the learner meets a course requirement.

## Key takeaways

- KR organises facts, objects, properties and relationships so a system can use them.
- Logic, rules, graphs, frames and ontologies are different representation approaches.
- The best representation depends on the task and the kinds of questions the system must answer.
- Accuracy and maintenance matter as much as the representation format.
