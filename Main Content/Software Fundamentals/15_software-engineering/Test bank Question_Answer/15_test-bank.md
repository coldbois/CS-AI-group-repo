# Module 15 Test Bank: Software Engineering

Back to: [Main Theory](../Main%20Theory/15_main-theory.md) · [Learner Activities](../Learner%20Activity/15_learner-activities.md)

**Format:** Each question shows its type, difficulty, the learning outcome (LO) and the Main Theory section it tests. Answers and explanations follow the questions.

**Coverage map**

| Group | Questions | Outcomes | Sections |
|---|---|---|---|
| A. Foundations and process models | Q1 to Q9 | LO1 to LO3 | 4 to 6 |
| B. Requirements and design | Q10 to Q15 | LO4, LO5 | 7, 8 |
| C. Version control, testing and code quality | Q16 to Q22 | LO6 to LO8 | 9 to 11 |
| D. Maintenance, risk, ethics and integration | Q23 to Q25 | LO9, LO10 | 12 to 15 |

---

# Group A: Foundations and Process Models

**Q1. [Multiple choice · Easy · LO1 · Section 4]**
Which statement best describes software engineering?
- A. Writing code as fast as possible
- B. A disciplined, team-based approach to planning, building, testing and maintaining software over its whole life
- C. Designing computer hardware
- D. Using only one programming language for every project

**Q2. [Multiple choice · Easy · LO2 · Section 5]**
In which SDLC stage are user stories first written?
- A. Testing
- B. Deployment
- C. Requirements
- D. Maintenance

**Q3. [Matching · Medium · LO2 · Section 5]**
Match each output to the SDLC stage that mainly produces it: (1) test cases and test results, (2) source code, (3) architecture and screen sketches, (4) a released version number.
Stages: Design · Implementation · Testing · Deployment.

**Q4. [True or false with correction · Medium · LO3 · Section 6]**
"In the Waterfall model, testing happens at the same time as requirements gathering." If false, correct it.

**Q5. [Multiple choice · Easy · LO3 · Section 6]**
What is a defining feature of Agile approaches such as Scrum?
- A. A complete plan is fixed before any work starts
- B. Working software is delivered in short cycles and feedback shapes what comes next
- C. Documentation is forbidden
- D. Customers are not involved until the end

**Q6. [Multiple choice · Easy · LO3 · Section 6]**
In Scrum, who decides what is most valuable to build and orders the Product Backlog?
- A. The Scrum Master
- B. The Developers
- C. The Product Owner
- D. The tester only

**Q7. [Calculation · Medium · LO3 · Section 6]**
A team completed **12, 15 and 18** story points in its last three sprints. **70** points remain. Estimate how many sprints are needed. Show your working.

**Q8. [Scenario · Medium · LO3 · Section 6]**
A government agency must build a system that processes a new set of forms. The law sets a fixed specification and a fixed deadline. Which approach would you lean towards, and why? Give one reason that supports it and one reason someone might argue for an alternative.

**Q9. [Find the error · Medium · LO3 · Section 6]**
A student writes: "Agile means there is no planning and no documentation." Identify the error and write a correct statement.

---

# Group B: Requirements and Design

**Q10. [Multiple choice · Medium · LO4 · Section 7]**
Which of these is the most **testable** requirement?
- A. "The system should be fast."
- B. "The event list loads in under 2 seconds for 95% of requests."
- C. "The app must be user-friendly."
- D. "The system should be secure."

**Q11. [Classification · Medium · LO4 · Section 7]**
Classify each as functional (F) or non-functional (N): (i) a member can cancel a registration; (ii) the system supports 500 users at the same time; (iii) data is stored in encrypted form; (iv) an organiser can export the attendee list.

**Q12. [Writing · Medium · LO4 · Section 7]**
Write one user story for "a member cancels a registration" and give **two** acceptance criteria in Given/When/Then form.

**Q13. [Multiple choice · Easy · LO5 · Section 8]**
What does **coupling** measure, and what should you aim for?
- A. How well one module's contents belong together; aim for low
- B. How much modules depend on each other's internals; aim for low
- C. How many lines a module has; aim for high
- D. How fast a module runs; aim for low

**Q14. [Design analysis · Medium · LO5 · Section 8]**
One module draws web pages, runs database queries and sends emails. (a) Which design property is poor? (b) Suggest how to split it into at least three modules and name their layers.

**Q15. [Multiple choice · Medium · LO5 · Section 8]**
In a layered design, in which layer does the rule "an event that is full rejects new registrations" belong?
- A. Presentation layer
- B. Business logic layer
- C. Data layer
- D. None; rules are not part of a design

---

# Group C: Version Control, Testing and Code Quality

**Q16. [Multiple choice · Easy · LO6 · Section 9]**
Which statement about Git and GitHub is correct?
- A. They are two names for the same thing
- B. Git is the version control tool; GitHub is a service that hosts Git repositories
- C. GitHub is a programming language
- D. Git can only be used on the internet

**Q17. [Ordering · Medium · LO6 · Section 9]**
Put these steps in the correct order for adding a feature on a separate branch:
- (a) `git merge feature/reminder` (while on `main`)
- (b) Edit the files for the feature
- (c) `git switch -c feature/reminder`
- (d) `git add` and `git commit -m "Add reminder"`
- (e) `git switch main`

**Q18. [Short answer · Medium · LO6 · Section 9]**
What is a merge conflict, and how is it resolved? Give three steps.

**Q19. [Test design · Hard · LO7 · Section 10]**
A function `ticket_price(age)` must follow this specification: ages 0 to 11 cost 5; ages 12 to 64 cost 10; ages 65 and over cost 7; a negative age is invalid and must raise an error. List **at least six** test inputs, with expected results, that include the **boundary values**.

**Q20. [Find the bug · Hard · LO7 · Section 10]**
A developer writes `if age <= 65: return 10` for the middle band (ages 12 to 64). Using your tests from Q19, which test fails, and what does the code return for it?

**Q21. [Multiple choice · Medium · LO7 · Section 10]**
What is regression testing?
- A. Testing the code's speed only
- B. Re-running earlier tests after a change to check that nothing that used to work has broken
- C. Testing before any code is written
- D. Asking users whether they like the colours

**Q22. [True or false with correction · Medium · LO8 · Section 11]**
"Refactoring means adding a new feature to code." If false, correct it and say why tests are useful when refactoring.

---

# Group D: Maintenance, Risk, Ethics and Integration

**Q23. [Classification · Medium · LO9 · Section 12]**
Classify each change as corrective, adaptive, perfective or preventive: (i) fix a crash on login; (ii) update the app to run on a newly released operating system version; (iii) add a dark mode; (iv) tidy messy code and add tests with no change in behaviour.

**Q24. [Calculation · Medium · LO10 · Section 13]**
Three risks are scored (probability, impact), each from 1 to 5: **R-A** (4, 2), **R-B** (2, 5), **R-C** (3, 3). Calculate each exposure, rank them, and say which to address first.

**Q25. [Scenario · Hard · LO10 · Section 14]**
One day before launch, a tester finds that members' email addresses can be seen by anyone who changes the web address. Your manager says to launch anyway. Describe what you would do, using at least **three** steps and mentioning the public interest.

---

# Answer Key with Explanations

## Group A

**Q1: B.** Software engineering covers the whole life cycle and teamwork. A is only speed, C is hardware, D is unrelated.

**Q2: C. Requirements.** User stories capture what users need.

**Q3:** (1) **Testing**, (2) **Implementation**, (3) **Design**, (4) **Deployment**.

**Q4: False.** In Waterfall each stage is finished before the next begins, so testing comes after implementation, not together with requirements.

**Q5: B.** Agile delivers working software in short cycles and adapts to feedback. A describes plan-driven approaches; C and D are untrue.

**Q6: C. The Product Owner.** The Scrum Master helps the team use Scrum; the Developers build the increment.

**Q7: 5 sprints.** Average velocity = (12 + 15 + 18) ÷ 3 = 45 ÷ 3 = **15**. Sprints = 70 ÷ 15 ≈ **4.67**, so plan for **5** sprints (the estimate should be recalculated each sprint).

**Q8: Model answer.** Lean towards a **plan-driven (Waterfall-like)** approach. *Supporting reason:* the specification and deadline are fixed, so detailed planning and documents fit. *Alternative argument:* an iterative approach could still deliver early working parts and catch misunderstandings sooner. *(Award marks for a reasoned choice, one supporting reason and one fair counterpoint.)*

**Q9: Error.** Agile does not mean no planning or documentation. **Correct statement:** "Agile plans in short cycles, welcomes change, and values working software over exhaustive documentation, while still documenting what is useful."

## Group B

**Q10: B.** It has a measurable target (under 2 seconds, 95% of requests). The others cannot be checked.

**Q11:** (i) **F**, (ii) **N** (performance/scalability), (iii) **N** (security), (iv) **F**.

**Q12: Model answer.**
> **As a** member, **I want** to cancel my registration, **so that** someone else can take my place.

1. **Given** I am registered for an upcoming event, **when** I cancel, **then** my name is removed from the list and I see a confirmation.
2. **Given** I am not registered for that event, **when** I try to cancel, **then** I am told I have no registration and nothing changes.

*(Other valid criteria are acceptable if they are clear and testable.)*

**Q13: B.** Coupling is how much modules depend on each other's internals. Aim for **low** coupling.

**Q14: Model answer.** (a) **Low cohesion** (several unrelated jobs in one module). (b) Example split: `Pages` (presentation), `EventStore` (data), `Notifications` (business logic), and optionally `Registration` (business logic).

**Q15: B.** The rule about full events is a business rule, so it belongs in the business logic layer.

## Group C

**Q16: B.** Git is the tool; GitHub hosts Git repositories and adds collaboration features.

**Q17: c → b → d → e → a.** Create and move to the branch (c); edit (b); commit (d); return to `main` (e); merge the branch (a).

**Q18: Model answer.** A merge conflict occurs when two branches changed the **same lines** differently, so Git cannot decide automatically. Resolve it by: (1) opening the file and editing it to the wanted text, removing the conflict marker lines; (2) `git add <file>`; (3) `git commit` to finish the merge.

**Q19: Example test set (checked by running a correct version).**

| # | age | Expected |
|---|---|---|
| 1 | -1 | error |
| 2 | 0 | 5 |
| 3 | 11 | 5 |
| 4 | 12 | 10 |
| 5 | 64 | 10 |
| 6 | 65 | 7 |
| 7 | 66 | 7 |

The boundaries are 0, 11/12 and 64/65, so tests at those points matter most.

**Q20: Test 6 (age 65) fails.** The buggy code returns **10** instead of 7, because `<= 65` wrongly includes 65 in the middle band. Tests 4 and 5 still pass, which shows why the boundary at 65 must be tested.

**Q21: B.** Regression testing re-runs earlier tests after a change.

**Q22: False.** Refactoring improves the **structure** of code **without changing its behaviour**. Automated tests are useful because they confirm that the behaviour has not changed after the restructuring.

## Group D

**Q23:** (i) **Corrective**, (ii) **Adaptive**, (iii) **Perfective**, (iv) **Preventive**.

**Q24:** R-A = 4 × 2 = **8**; R-B = 2 × 5 = **10**; R-C = 3 × 3 = **9**. Ranking: **R-B (10), R-C (9), R-A (8)**. Address **R-B** first.

**Q25: Model answer.**
1. **Identify the issue:** members' personal data is exposed, which harms the public and is unsafe to release.
2. **Report it clearly and in writing** to the manager and, if needed, to a more senior person, with the evidence from the tester.
3. **Offer workable options:** delay the launch until it is fixed, or launch without the affected feature or with restricted access while the fix is finished.
4. **Do not release the exposed feature,** and keep a record of what was reported and decided.

The reasoning draws on the duty to act in the **public interest** and to be honest about the software's safety (Section 14). *(Award marks for naming the privacy harm, reporting, at least one realistic option and the public-interest reasoning.)*

---

## Review status

| Check | Done by | Result |
|---|---|---|
| Calculations (Q7, Q24) recomputed independently | [Teammate name] | [To be completed] |
| Test tables (Q19, Q20) run against correct and buggy code | [Teammate name] | [To be completed] |
| Git order (Q17) checked by actually running the commands | [Teammate name] | [To be completed] |
| Questions match the Main Theory wording and terminology | [Teammate name] | [To be completed] |
| Each multiple-choice question has exactly one defensible answer | [Teammate name] | [To be completed] |
