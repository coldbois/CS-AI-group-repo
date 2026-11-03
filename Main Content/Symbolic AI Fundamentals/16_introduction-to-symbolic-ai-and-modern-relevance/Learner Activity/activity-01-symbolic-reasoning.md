# Activity 1 — Can You Think Like a Symbolic AI System?

**Related chapter:** Chapter 1 — Introduction to Symbolic AI and Modern Relevance  
**Difficulty:** Beginner  
**Suggested time:** 10–15 minutes  

## Goal

Practise using facts and rules to derive conclusions.

## Preparation

Paper and pen, or a shared document. No programming is required.

## Scenario

A small knowledge base contains these statements:

**Facts**

- `sparrow` is a `bird`.
- `penguin` is a `bird`.

**Rules**

- All birds are animals.
- All birds in this example have wings.

Treat the statements as the complete knowledge supplied for this exercise. The rules are intentionally simplified for teaching.

## Task

1. Underline the facts and circle the rules.
2. Write down whether the system can conclude that a sparrow is an animal.
3. Write down whether the system can conclude that a penguin has wings.
4. Explain which rule was used for each conclusion.
5. Add a new fact: `owl` is a `bird`. What further conclusions can be derived?

## Observation record

| Question | Your observation |
|---|---|
| Which information was supplied directly? | |
| Which information was derived? | |
| Did adding the owl fact change the rules? | |

## Reflection

- How is deriving a conclusion different from simply storing a fact?
- What happens if a rule is incorrect?
- Does the system know facts that were not included or derivable from its knowledge base?

## Hint

Look for a rule whose condition matches the object type in each fact. The system can apply the same rule to more than one object.

## Expected outcome and feedback

- Sparrow is an animal because it is a bird and the rule says all birds are animals.
- Penguin has wings because it is a bird and the example rule says all birds have wings.
- Adding the owl fact allows the same rules to derive that the owl is an animal and has wings.
- The rules did not change; the new fact gave the system another case to which the rules could apply.

**Learning point:** A symbolic system can derive new information by applying general rules to specific facts. Its conclusions are limited by the knowledge and assumptions provided.
