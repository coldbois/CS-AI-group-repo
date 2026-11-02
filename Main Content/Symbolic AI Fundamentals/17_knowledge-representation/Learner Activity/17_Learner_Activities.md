# Topic 17 — Learner Activities

These activities use the ideas from the main theory. Students can work individually or in pairs. The answer guidance is included so the activity can be completed without extra information from the teacher.

## Activity 1 — Build a small knowledge graph

**Goal:** Identify entities and relationships and represent them as triples.

**Information:**

- Kai is a student.
- Kai studies Mathematics.
- Kai attends North College.
- North College is located in Beijing.

**Instructions:**

1. List the entities in the information.
2. Identify the relationship in each sentence.
3. Rewrite each sentence as `subject — predicate — object`.
4. Draw a graph with one node per entity and one labelled arrow per relationship.
5. Answer: Which college does Kai attend? Where is it located?

**Expected outcome / answer guide:**

Entities: Kai, Mathematics, North College and Beijing. Triples:

```text
(Kai, type, Student)
(Kai, studies, Mathematics)
(Kai, attends, North_College)
(North_College, located_in, Beijing)
```

Kai attends North College, which is located in Beijing. The graph should use labelled arrows; simply placing the names beside one another is not enough to show the relationships.

## Activity 2 — Choose a representation

**Goal:** Compare representation methods rather than memorising their names.

For each situation, choose a suitable representation and explain why:

A. A program must check whether a student has passed a prerequisite before allowing course registration.

B. A website needs to connect people, books and authors so that users can follow relationships.

C. A system stores standard details about a laptop, such as model, memory and operating system.

D. A university needs a shared formal description of departments, courses, teachers and their relationships.

**Expected outcome / answer guide:**

- A: IF–THEN rules or first-order logic can represent the requirement. Example: `IF Passed(Prerequisite) THEN EligibleToRegister(NextCourse)`.
- B: A knowledge graph / RDF-style triples are suitable because connections are central.
- C: A frame or structured record is suitable because the system stores attributes of one object.
- D: An ontology is suitable because the university needs a shared vocabulary and formal relationships.

There can be more than one reasonable answer. Credit explanations that connect the representation to the task.

## Activity 3 — Translate simple statements into logic

**Goal:** Practise reading and writing logical representations.

Let:

- `Student(x)` mean x is a student.
- `HasID(x)` mean x has a student ID.

A. Write “Every student has a student ID” using a quantifier.

B. Write “Lee is a student”.

C. What conclusion follows from A and B?

D. Explain why the conclusion depends on the rule being accepted as true in the model.

**Expected outcome / answer guide:**

A. `∀x (Student(x) → HasID(x))`

B. `Student(Lee)`

C. `HasID(Lee)`

D. The logic shows what follows from the premises. It does not independently check whether the premises accurately describe the real university.
