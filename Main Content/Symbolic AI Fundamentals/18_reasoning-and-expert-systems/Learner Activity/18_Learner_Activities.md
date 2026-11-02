# Topic 18 — Learner Activities

## Activity 1 — Trace the inference

**Goal:** Apply rules and show how a conclusion is reached.

A course helper has these rules:

```text
R1: IF assignment_submitted THEN assignment_ok.
R2: IF quiz_passed THEN quiz_ok.
R3: IF assignment_ok AND quiz_ok THEN course_requirement_met.
```

Known facts:

```text
assignment_submitted = true
quiz_passed = true
```

**Tasks:**

1. Show which rule fires first and what new fact it adds.
2. Continue until no more rules apply.
3. State the final conclusion.
4. Explain one thing this rule set does not check.

**Expected outcome:** R1 adds `assignment_ok`; R2 adds `quiz_ok`; R3 then adds `course_requirement_met`. The system does not check attendance, exam results or any requirement not included in these rules.

## Activity 2 — Forward or backward?

**Goal:** Compare two ways of using the same rule base.

Use the rules from Activity 1.

A. A system receives new facts about a student and wants to find every conclusion it can derive. Which chaining method is suitable? Trace the first two steps.

B. A user asks specifically, “Has the course requirement been met?” Which chaining method can start from that goal? List the facts it must check.

**Expected outcome:** A uses forward chaining: start with the known facts and apply R1 and R2, then R3. B uses backward chaining: start with `course_requirement_met`, find R3, then check `assignment_ok` and `quiz_ok`, which are supported by R1 and R2.

## Activity 3 — Review a simple expert system

**Goal:** Identify when rules are useful and where they are incomplete.

A fictional help desk system uses:

```text
R1: IF WiFi_not_working AND airplane_mode_on
    THEN suggest_turning_airplane_mode_off.

R2: IF WiFi_not_working AND airplane_mode_off
    THEN suggest_checking_router_or_network_settings.
```

A user reports: Wi-Fi is not working and airplane mode is off.

**Tasks:**

1. Which rule matches?
2. What should the system suggest?
3. Is this a confirmed cause or a troubleshooting suggestion?
4. Name two other pieces of information that could improve the system.

**Expected outcome:** R2 matches. It suggests checking the router or network settings. This is not a confirmed cause. Useful extra information could include whether other devices connect, whether the laptop sees the network, or whether the router is working.
