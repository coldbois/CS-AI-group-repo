# Try it: The AI Decision Challenge (3.5)

**Time:** 20 min · **Group:** pairs · **You need:** paper or a spreadsheet · Study Guide pp. 146–147 · Linked Test Bank question: O9

**Goal:** test a rule for consistency, find what it misses, and choose the right AI approach for different jobs.

## Prepare

- **Rule:** `IF GPA ≥ 3.5 THEN academic_criterion_met`
- **Students:** A 3.8 · B 3.2 · C 3.5 · D 3.4

## Steps

1. Apply the rule to each student. Then do it again. Same results?
2. **News:** students must also finish a community activity. Why is the old rule now incomplete? Rewrite it.
3. Sort these six tasks into **Symbolic**, **ML** or **Hybrid**:
   - apply a refund policy
   - spot a cat in a photo
   - solve a logic puzzle
   - transcribe speech
   - find themes in 10,000 reviews
   - read a handwritten maths answer and check it
4. Defend one choice to another pair.

## Record

| Student | GPA ≥ 3.5? | Meets the new rule? |
| --- | --- | --- |
| A (3.8) | | |
| B (3.2) | | |
| C (3.5) | | |
| D (3.4) | | |

## Reflect

- Why can a rule be consistent but incomplete?
- Who should check that a new rule matches the real policy?

## Check it: expected results

- **A ✓, C ✓ (3.5 counts!), B ✗, D ✗.** Same results every run: the rule is **consistent**.
- **New rule:** `IF GPA ≥ 3.5 AND community_activity_done THEN both_criteria_met`. The old rule had no way to check the new fact.
- The "Meets the new rule?" column can't be filled in yet: you need to know `community_activity_done` for each student. That is the point. The rule needs a new fact before it can decide.
- **Symbolic:** refund policy, logic puzzle. **ML:** cat photo, speech, review themes. **Hybrid:** the handwritten maths answer (ML reads it, symbolic rules check it).
- A **policy expert**, not just the programmer, should verify the rules.
