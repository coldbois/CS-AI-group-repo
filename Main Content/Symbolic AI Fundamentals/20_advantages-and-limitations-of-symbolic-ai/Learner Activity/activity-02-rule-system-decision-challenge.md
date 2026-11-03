# Activity 2 — The AI Decision Challenge

**Related chapter:** Chapter 2 — Advantages and Limitations of Symbolic AI  
**Difficulty:** Beginner–Intermediate  
**Suggested time:** 15–20 minutes  

## Goal

Explore consistency, rule coverage and the effects of changing a rule-based system.

## Preparation

Paper, spreadsheet or shared document.

## Scenario

A teaching application checks one scholarship condition using this rule:

```text
IF GPA >= 3.5
THEN academic_criterion_met = true
```

It receives these example records:

| Student | GPA |
|---|---:|
| A | 3.8 |
| B | 3.2 |
| C | 3.5 |
| D | 3.4 |

## Task

1. Apply the rule to each student and record whether the academic criterion is met.
2. Run through the table a second time. Did the same inputs produce the same results?
3. Imagine the organization adds another condition: the student must also have completed a required community activity.
4. Explain why the original rule is now incomplete.
5. Write a revised rule in plain English that checks both conditions.

## Observation record

| Student | GPA condition met? | Original rule result |
|---|---|---|
| A | | |
| B | | |
| C | | |
| D | | |

## Reflection

- Why can the original rule be consistent but incomplete?
- What new fact does the system need for the additional condition?
- Who should verify that the new rule accurately represents the policy?

## Hint

For the revised rule, ask whether both the GPA condition and the community-activity condition must be true. The word **both** is important.

## Expected outcome and feedback

- Students A and C meet the original GPA condition.
- Students B and D do not meet the original GPA condition.
- Repeating the same deterministic rule with the same records produces the same classification.
- The original rule does not contain the community-activity requirement, so it cannot check that condition.
- A possible revised rule is: `IF GPA >= 3.5 AND community_activity_completed THEN both_criteria_met = true`.

**Learning point:** Consistency means applying the same defined rules in the same way. It does not guarantee that the rules include every relevant condition or are correct.
