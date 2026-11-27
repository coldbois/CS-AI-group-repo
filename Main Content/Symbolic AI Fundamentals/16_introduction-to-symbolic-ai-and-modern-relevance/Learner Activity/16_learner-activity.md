# Try it: Think Like a Symbolic AI (and Break It!) (3.1)

**Time:** 15 min · **Group:** solo or pairs · **You need:** pen and paper · Study Guide pp. 114–115

**Goal:** use facts and rules to derive new conclusions, then discover what happens when a rule is too simple.

## Prepare

Copy this tiny knowledge base:

- **Facts:** sparrow is a bird. penguin is a bird.
- **Rules:** all birds are animals. all birds have wings.

## Steps

1. Underline the facts and circle the rules.
2. Can the system conclude "sparrow is an animal"? Which rule did it use?
3. Can it conclude "penguin has wings"?
4. Add the fact **owl is a bird**. What new conclusions appear? Did any rule change?
5. **Break it:** add the rule **"all birds can fly"**. What does the system now say about the penguin?

## Record

| Conclusion | Supplied or derived? | Rule used |
| --- | --- | --- |
| sparrow is an animal | | |
| penguin has wings | | |
| owl is an animal | | |
| penguin can fly | | |

## Reflect

- How is *deriving* a fact different from *storing* it?
- Does the system know anything that wasn't given or derivable?
- How could you fix the flying-penguin problem?

## Check it: expected results

| Conclusion | Supplied or derived? | Rule used |
| --- | --- | --- |
| sparrow is an animal | derived | all birds are animals |
| penguin has wings | derived | all birds have wings |
| owl is an animal (and has wings) | derived | both rules, applied to the new fact |
| penguin can fly | derived | all birds can fly |

- Adding the owl did not change any rule. The new fact simply gave the existing rules a new case. That is the power of rules: write them once, use them for every new fact.
- With "all birds can fly", the system says **penguins fly**. That's wrong in the real world, but it follows logically from its rules.
- **Fix:** add an exception, for example `IF bird AND NOT penguin THEN can_fly`. Rules are only as good as the knowledge inside them, a limitation we come back to in [3.5](../../20_advantages-and-limitations-of-symbolic-ai/Main%20Theory/20_main-theory.md).
- The system knows nothing beyond what was given or derivable. Ask it "can a sparrow swim?" and it has no answer.
