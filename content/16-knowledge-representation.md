# Section 16 — Knowledge Representation

Knowledge representation is how an AI system stores facts and relationships in a form it can use. Think of an organised filing system: categories tell you what a document is about, labels describe it, and cross-references show how things are connected.

Symbolic AI relies on this structure because its reasoning depends on the facts and relationships it can access.

## Logic basics

**Symbols and expressions** are the building blocks. A system might have symbols for `Fever`, `Cough`, and `PatientA`, then combine them into facts and rules.

**Propositional logic** treats whole statements as true or false. It combines them with:

- `AND`: both statements are true.
- `OR`: at least one is true.
- `NOT`: a statement is false.
- `IMPLIES`: if one statement is true, a rule says another follows.
- `IF AND ONLY IF`: each statement implies the other.

If `p` means “it is raining” and `q` means “I have an umbrella,” then `p AND q` means both statements are true. Logic provides a precise way to combine claims, but it does not prove that the original claims are true in the real world.

**First-order logic** can describe individual objects and relationships. It uses variables such as `x`, predicates such as `Likes(x, IceCream)`, and quantifiers. `∀` means “for all,” and `∃` means “there exists.” For example, “Every cat is an animal” makes a statement about all cats.

## Organising concepts

An **ontology** is a structured description of the types of things in a subject and how they relate. A **class** is a category, such as `Superhero`. An **instance** is one specific member of a class. A **property** describes something about it, such as age or abilities. A **subclass** is a more specific category that can inherit properties from a broader one.

Ontologies can have rules. **Inheritance** means a subclass receives properties from its parent. **Disjointness** means an individual cannot belong to two categories that have been defined as mutually exclusive. Other constraints can specify a property’s type or how many values it can have. These rules depend on how the model is defined.

A **semantic network** represents knowledge as a graph. Nodes are concepts and labelled links show relationships such as “is a” or “has.” For example, `Superman` can be linked to `Superhero`, and to `Flight` through a `hasPower` link. A system can follow these links to answer questions.

A **frame** is like a record with named slots and values. A Batman frame might have `team: Justice League`. Frames can also use default values from a more general frame unless a specific value is supplied.

The main point is that the way knowledge is organised affects what the system can work out. Incorrect facts or poorly designed categories can lead to bad conclusions, even when the reasoning steps themselves are consistent.
