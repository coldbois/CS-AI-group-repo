# Section 16: Knowledge Representation

## 1. What is knowledge representation?

**Knowledge representation (KR)** is the way an AI system stores facts, concepts, relationships, and rules in a form that a computer can use for reasoning.

Think of a well-organized filing cabinet. Folders group related information, individual documents record particular things, labels describe properties, and cross-references connect related records. A knowledge representation serves a similar purpose: it gives the system a structured way to find and combine information.

## 2. Main tools for representing knowledge

| Tool | Basic idea | Simple example |
|---|---|---|
| Symbols and expressions | Use symbols and combine them into structured statements. | `Fever`, `Cough`, and a rule connecting them. |
| Propositional logic | Treat statements as true or false and combine them with logical operators. | “It is raining AND I have an umbrella.” |
| First-order logic (FOL) | Describe objects, properties, and relationships using variables, predicates, and quantifiers. | “For every x, if x is a superhero, then x fights evil.” |
| Ontologies | Define classes, individuals, properties, and relationships in an organized domain model. | A `Superhero` class, a particular superhero, and a `hasPower` relationship. |
| Semantic networks | Represent concepts as nodes connected by labeled links. | A graph connecting a superhero to a team or ability. |
| Frames | Store information in a record made of named slots and values. | A Batman frame might have `team: Justice League`. |

### Symbols and expressions

A **symbol** is a label representing something the system can reason about. An **expression** combines symbols into a meaningful structure. For example, `Likes(John, IceCream)` can represent the claim that John likes ice cream.

### Propositional logic

Propositional logic treats each complete statement as either true or false within the logical model. It uses operators, or **connectives**, to build more complex statements.

| Connective | Common notation | Meaning |
|---|---|---|
| AND | `p AND q` | True only when both p and q are true. |
| OR | `p OR q` | True when at least one of p or q is true. In standard inclusive logic, it is also true when both are true. |
| NOT | `NOT p` | Reverses the truth value of p. |
| IMPLIES | `p → q` | False only when p is true and q is false. It expresses a logical condition, not necessarily a physical cause-and-effect relationship. |
| BICONDITIONAL | `p ↔ q` | True when p and q have the same truth value; each implies the other. |

For instance, if p is true and q is true, then `p AND (NOT q)` is false, `NOT p OR q` is true, and `p → q` is true.

### First-order logic (FOL)

**First-order logic** extends propositional logic so statements can refer to individual objects and relationships between them. It uses:

- **Constants** for specific things, such as `SpiderMan`.
- **Variables** such as `x` and `y` to stand for objects.
- **Predicates** to describe properties or relationships, such as `Likes(John, IceCream)`.
- **Quantifiers** to describe how widely a statement applies.
  - `∀` means “for all.”
  - `∃` means “there exists at least one.”

For example, “Every superhero fights evil” can be represented as: for all `x`, if `Superhero(x)` is true, then `FightsEvil(x)` is true. “At least one butler exists” can be represented with the existential quantifier `∃`.

The source also gives fictional-character examples involving Batman, superheroes, powers, and a butler. Such examples are illustrations of the form of a logical statement; their truth depends on how the fictional domain is defined.

## 3. Classes, subtypes, instances, and properties

These terms describe different levels of information:

- **Class:** a general category, such as `Superhero`.
- **Subtype or subclass:** a more specific category under a broader one. A subclass may inherit properties from its parent class and add its own. For instance, `Superhero` may have a narrower subclass for heroes with a particular ability.
- **Instance or individual:** one specific member of a class, such as a named character.
- **Property:** information about an individual or a relationship. Examples include `age = 15` or `hasPower(Miles, SpiderSense)`.

The source uses examples such as Superman, Spider-Man, and Miles Morales. The exact class relationships depend on the chosen knowledge model; characters and names should not be treated as interchangeable with classes unless the model defines them that way.

## 4. Ontologies and constraints

An **ontology** is a structured description of the concepts in a domain and the relationships between them. It is not simply a list of unrelated facts. Logical constraints help keep the knowledge model consistent.

The source highlights these ideas:

- **Inheritance:** if every member of a subclass is also a member of its parent class, the individual can inherit applicable properties from the parent. For example, if every Spider-Man is modeled as a superhero, a Spider-Man instance also belongs to the `Superhero` category.
- **Disjointness:** two classes are disjoint when no individual may belong to both at once in that model. The source's example is that `Hero` and `Villain` cannot overlap. That is a modeling assumption, not a universal fact about every fictional setting.
- **Subclass conditions:** a class can be defined by conditions. The source's illustrative condition says that a Batmobile must be a vehicle with exactly four wheels.
- **Property constraints:** rules can set limits on values. Examples include cardinality (“exactly one sidekick”), type (“strength must be a number”), and existence (“every Avenger fights at least one villain”). These are examples of possible model constraints, not universal facts.

## 5. Semantic networks

A **semantic network** represents knowledge as a graph: nodes stand for concepts or individuals, and labeled edges show relationships such as `is-a`, `has-a`, or `hasPower`.

For example, a knowledge graph might connect `JusticeLeague` to its members, connect `Superman` to the group, and connect Superman to the ability `Flight`. If a reasoner follows those links, it can answer a question such as “Which Justice League member can fly?” This process of deriving an answer from stored links is a type of **inference**.

The source includes the chain `Animal → isa → Fish → isa → Cat`. Taken literally, this is not a sound biological hierarchy because a cat is not a kind of fish. Treat it as a malformed illustrative chain in the source, not as a correct taxonomy; a sensible `is-a` chain would place a cat under mammal and animal.

## 6. Frames

A **frame** is a structured record with named **slots** (attributes) and **fillers** (values). For example:

```text
Frame: Batman
  team: Justice League
  role: hero
```

Frames can store **default values**. If a frame does not specify a value, the system may use a value inherited from a parent frame. This is one form of **default reasoning**: make a reasonable assumption unless more specific information overrides it.

For example, a general `Hero` frame might contain a default team or role. A particular character's frame could supply a different value. A missing slot should not automatically be interpreted as proof that the property is false; it may simply be unknown or unspecified.

## 7. Key takeaways

- Knowledge representation determines how facts and relationships are stored so a program can reason with them.
- Propositional logic combines whole statements; first-order logic can express facts about individual objects and relationships.
- Ontologies organize classes and relations and can enforce constraints.
- Semantic networks use nodes and labeled links; frames use slots and values.
- A representation is only as useful as its definitions and data. Incorrect relationships can produce incorrect inferences.
