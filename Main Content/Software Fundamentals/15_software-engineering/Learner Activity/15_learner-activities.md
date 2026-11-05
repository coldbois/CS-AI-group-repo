# Module 15 Learner Activities: Software Engineering

Back to: [Main Theory](../Main%20Theory/15_main-theory.md) · [Test Bank](../Test%20bank%20Question_Answer/15_test-bank.md)

## How to use these activities

- Read the matching section of the Main Theory first, then **try each activity before looking at the answers**. The **Answer Key** is at the end of this file.
- Each activity gives all the information you need. You do not have to look anything up.
- The activities mix skills: sorting, choosing and justifying, rewriting, analysing a design, predicting, testing, refactoring, estimating and planning.
- Most activities use the **ClubSignup** project from the Main Theory (students register for club events).

| # | Activity | Skill practised | Main Theory section | Outcome |
|---|---|---|---|---|
| 1 | SDLC stages and artefacts | Classifying, explaining | 4, 5 | LO1, LO2 |
| 2 | Choose a process model; estimate with velocity | Comparing, explaining a decision, calculating | 6 | LO3 |
| 3 | Rewrite vague requirements; write a user story | Rewriting, creating | 7 | LO4 |
| 4 | Analyse and improve a design | Finding problems, comparing | 8 | LO5 |
| 5 | Predict Git history; resolve a conflict | Predicting, tracing | 9 | LO6 |
| 6 | Design tests; find a boundary bug | Designing tests, finding an error | 10 | LO7 |
| 7 | Refactor and verify | Improving code, checking | 11 | LO8 |
| 8 | Risk, maintenance types and estimates | Calculating, classifying | 12, 13 | LO9, LO10 |
| 9 | Plan a small project | Applying everything | 4 to 14 | LO1 to LO10 |

---

## Activity 1: SDLC stages and artefacts

**Goal:** Place project activities in the right stage and explain why.
**Time:** 15 minutes.

**Stages:** (R) Requirements · (D) Design · (I) Implementation · (T) Testing · (P) Deployment · (M) Maintenance

**Items**
1. Interviewing organisers about what they need from the attendee list
2. Drawing the three layers of ClubSignup and the database table plan
3. Writing the registration code and saving it to Git
4. Running a set of test cases against the registration code
5. Putting version 1.0.0 on the web server
6. Fixing a bug reported by a member after release
7. Writing acceptance criteria for "a member can register for an event"
8. Adding a waiting list because members asked for one after release

**Task**
- **(a)** Give each item a stage letter with a one-line reason.
- **(b)** Items 6 and 8 both come after release. Which goes with *corrective* maintenance and which with *perfective* maintenance?
- **(c) Explain:** A student says, "The SDLC is a strict one-way staircase." Give one example from ClubSignup that shows why this is wrong.

---

## Activity 2: Choose a process model; estimate with velocity

**Goal:** Justify a choice of approach and calculate a simple estimate.
**Time:** 25 minutes.

**Information:** Use Section 6.6 (comparison table) and Section 6.8 (velocity).

**Scenarios**
1. A hospital needs software to follow a new national reporting rule. The rule is published in full, the deadline is fixed by law, and the specification will not change.
2. A student team wants to build a new study-buddy app. They have only a rough idea and do not know which features users will like.
3. A company maintains an online shop and receives a steady stream of small improvement requests of different sizes.

**Task**
- **(a)** For each scenario, choose *plan-driven (Waterfall-like)*, *Agile (Scrum)* or *Kanban* and give **one reason**. More than one answer can be defensible if your reason is good.
- **(b) Velocity.** A team completed **14, 18 and 16** story points in its last three sprints. **76** points remain in the backlog and each sprint lasts **2 weeks**. How many sprints and how many weeks should it plan for? Show your working.
- **(c) Explain:** Why should the team recalculate this estimate after every sprint?

---

## Activity 3: Rewrite vague requirements; write a user story

**Goal:** Turn vague wishes into testable requirements.
**Time:** 25 minutes.

**Information:** A good requirement is clear, unambiguous, necessary, feasible and **testable**. User stories have the form *As a …, I want …, so that …* with Given/When/Then acceptance criteria.

**Task**
- **(a)** Say why each requirement is weak and rewrite it so that it can be tested:
  1. "The website should be secure."
  2. "The attendee list must load quickly."
  3. "The app should be easy to use."
- **(b)** Classify each **rewritten** requirement as functional or non-functional.
- **(c)** Write **one user story** for an organiser who wants to download the attendee list, with **three acceptance criteria** (at least one for an unusual case, for example an event with no registrations).
- **(d) Prioritise.** Using MoSCoW, label these four items: (i) register for an event; (ii) confirmation email; (iii) dark mode; (iv) payment for paid events (the club has no paid events this year).

---

## Activity 4: Analyse and improve a design

**Goal:** Use cohesion, coupling and layers.
**Time:** 20 minutes.

**Information:** A first design of ClubSignup has these modules:

| Module | What it does |
|---|---|
| `App` | Draws all pages, checks logins, writes database queries, builds and sends emails, and calculates whether events are full |
| `Reports` | Reads `App`'s internal variables directly to count registrations |

**Task**
- **(a)** Which module has **low cohesion**? Explain.
- **(b)** Which relationship shows **high coupling**? What can go wrong?
- **(c)** Propose a better design with **at least four modules**, each with one responsibility, and place each in the **presentation**, **business logic** or **data** layer.
- **(d)** Describe in one sentence how `Reports` should get the registration count in your new design.

---

## Activity 5: Predict Git history; resolve a conflict

**Goal:** Trace a Git workflow and fix a conflict.
**Time:** 25 minutes.

**Information:** A file `plan.txt` has two lines at the start:

```
Choose a venue
Book the room
```

The following happens (all commits are made as stated):

1. On `main`: commit **A** with the file as above.
2. Create branch `food` from A. On `food`, change line 2 to `Book the room and order snacks`. Commit **B**.
3. Switch to `main`. Change line 2 to `Book the room and invite the guest speaker`. Commit **C**.
4. On `main`, run `git merge food`.

**Task**
- **(a)** Draw the commit graph just before step 4 (name the two branch tips).
- **(b)** Predict what Git reports at step 4 and why.
- **(c)** Write what the file looks like with conflict markers (the first line is unchanged).
- **(d)** Resolve the conflict so that **both** ideas are kept, and write the commands you would then run to finish the merge.
- **(e) Explain:** Name one habit that makes merge conflicts less frequent and easier.

---

## Activity 6: Design tests; find a boundary bug

**Goal:** Choose test inputs at the boundaries, then locate a bug from the test results.
**Time:** 30 minutes.

**Specification of `shipping_cost(weight)`** (weight in kg; used to charge for posting event merchandise):

| Weight | Result |
|---|---|
| 0 or less | invalid: raise an error |
| more than 0 up to **and including** 1 | cost 5 |
| more than 1 up to **and including** 5 | cost 10 |
| more than 5 | cost 20 |

**Task**
- **(a) Design.** List the **boundaries**, then write at least **eight** test cases (weight and expected result) that cover each boundary and include one invalid input.
- **(b) Find the bug.** A developer's version contains the lines `if weight < 1:` and `if weight < 5:` (instead of `<=`). Using your test cases, which ones **fail**, and what does the buggy code return for them?
- **(c) Explain:** Which technique found the bug, and why would testing only the weights 0.5, 3 and 8 miss it?
- **(d)** At which **level** of testing (unit, integration, system, acceptance) are these tests, and why?

---

## Activity 7: Refactor and verify

**Goal:** Remove duplication without changing behaviour.
**Time:** 20 minutes.

**Information:** These two functions are in ClubSignup:

```python
def event_fee_member(base):
    total = base + base * 0.05
    return round(total, 2)

def event_fee_guest(base):
    total = base + base * 0.25
    return round(total, 2)

def event_fee_sponsor(base):
    total = base + base * 0.00
    return round(total, 2)
```

**Task**
- **(a)** What is the duplication, and why is it a problem?
- **(b)** Write **one** function `fee_with_surcharge(base, rate)` and show how the three original functions could use it.
- **(c) Verify.** For `base = 40` and `base = 12.5`, work out the three results from the **original** functions and from your new function. Show that they match.
- **(d) Explain:** Why is this change a *refactoring* and not a new feature?

---

## Activity 8: Risk, maintenance types and estimates

**Goal:** Rank risks and classify changes.
**Time:** 25 minutes.

**Part 1: Risks.** Use *exposure = probability × impact* (each scored 1 to 5).

| ID | Risk | Probability | Impact |
|---|---|---|---|
| R1 | The only tester is ill during the last two weeks | 3 | 4 |
| R2 | A key library is retired and no longer updated | 2 | 5 |
| R3 | The organisers keep adding "small" extra features | 5 | 3 |
| R4 | The test server crashes and loses data | 2 | 3 |

- **(a)** Calculate each exposure and rank the risks from highest to lowest.
- **(b)** Suggest one **reducing** action for the top-ranked risk.

**Part 2: Maintenance types.** Classify each change as **corrective**, **adaptive**, **perfective** or **preventive**:
1. Registration crashes when a member's name contains an apostrophe: fix it.
2. The college moves to a new version of its web server; update ClubSignup to run on it.
3. Add a calendar download button because members asked for it.
4. Reorganise the messy `Notifications` module and add tests, with no change in behaviour.

---

## Activity 9: Plan a small project

**Goal:** Apply everything in one plan.
**Time:** 40 minutes.

**Scenario:** A library wants a **book reservation app**. Students can search for a book and reserve a copy. Librarians see a list of reservations. The app stores students' names and emails. The library has no fixed idea of every feature, and a first version is wanted in 8 weeks.

**Task:** Write a one-page plan with these parts:
1. **Process model:** choose one and justify it in two sentences.
2. **Requirements:** write **three** user stories (at least one with acceptance criteria) and **two** non-functional requirements that are testable. Use MoSCoW to mark which are *Must*.
3. **Design:** list **at least four** modules and their layers.
4. **Version control:** describe your branching approach in two sentences (for example, how a feature gets merged).
5. **Testing:** give **three** test cases for the reservation rule "a student may reserve a book only if a copy is available" (include one boundary case).
6. **Risk:** name the **top two** risks with probability, impact and exposure, and one reducing action each.
7. **Ethics:** identify one privacy issue and say what you would do about it.
8. **Maintenance:** give one example each of a corrective and a perfective change you might make after release.

---

# Answer Key

## Answer 1
**(a)**

| # | Stage | Reason |
|---|---|---|
| 1 | **R** | Finding out what users need |
| 2 | **D** | Deciding the structure of the system |
| 3 | **I** | Writing code |
| 4 | **T** | Running test cases |
| 5 | **P** | Releasing a version to users |
| 6 | **M** | Changing software after release to fix a problem |
| 7 | **R** | Acceptance criteria define when a requirement is met |
| 8 | **M** | A new feature added after release (a change request) |

**(b)** Item 6 (fixing a bug) is **corrective**. Item 8 (adding a waiting list) is **perfective**.

**(c)** *(Model answer)* A test failure ("registration works for a full event") can send the team **back to design or implementation**, and members' feedback after release leads to **new requirements**. So the stages loop and overlap.

## Answer 2
**(a)** *(Model answers; other reasoned answers are acceptable.)*
1. **Plan-driven (Waterfall-like).** The requirements are complete, fixed and legal, so a detailed plan and documentation fit.
2. **Agile (Scrum).** The needs are unknown, so short sprints and feedback reduce the risk of building the wrong thing.
3. **Kanban.** A steady flow of small, varied requests suits a board that limits work in progress. (Scrum with short sprints is also defensible.)

**(b)** Average velocity = (14 + 18 + 16) ÷ 3 = 48 ÷ 3 = **16 points per sprint**. Sprints needed = 76 ÷ 16 = **4.75**, so plan for **5 sprints**, which is **10 weeks**.

**(c)** Velocity changes and the backlog changes (new items, sickness, surprises), so recalculating keeps the forecast honest.

## Answer 3
**(a) and rewrites (examples)**

| Original | Why weak | Testable rewrite |
|---|---|---|
| 1. "Secure" | Not measurable; "secure" against what? | "Passwords are stored in hashed form, and an account is locked for 15 minutes after 5 failed logins." |
| 2. "Quickly" | No measurable target | "The attendee list for an event with 300 registrations loads in under 3 seconds for 95% of requests." |
| 3. "Easy to use" | An opinion | "A new organiser can export an attendee list within 3 clicks without help; test with 5 new organisers." |

**(b)** Rewrites 1, 2 and 3 are **non-functional** (security, performance, usability). *(Rewrite 1's lock-out rule can also be seen as a functional behaviour; an explained answer is acceptable.)*

**(c) Example user story**

> **As an** organiser, **I want** to download the attendee list for my event, **so that** I can print it for the door.

1. **Given** an event with registrations, **when** I choose download, **then** I receive a file listing each attendee's name.
2. **Given** an event with **no registrations**, **when** I choose download, **then** I get an empty list with a clear message "No registrations yet" and no error.
3. **Given** I am not the organiser of that event, **when** I try to download its list, **then** access is denied.

**(d)** (i) **Must**, (ii) **Should** (or Must, if the club insists; justify), (iii) **Could**, (iv) **Won't** (this time).

## Answer 4
**(a)** **`App`** has low cohesion: it draws pages, checks logins, writes queries, sends emails and checks whether events are full, which are unrelated jobs in one module.

**(b)** `Reports` reading `App`'s **internal variables** is high coupling. If `App` changes how it stores counts, `Reports` can break without warning.

**(c) Example design**

| Module | Responsibility | Layer |
|---|---|---|
| `Pages` | Shows lists, forms, confirmation messages | Presentation |
| `Accounts` | Login and permissions | Business logic |
| `Registration` | Rules: free places, duplicates | Business logic |
| `Notifications` | Builds and sends emails | Business logic |
| `Reports` | Produces attendee lists | Business logic |
| `EventStore` | Saves and loads events and registrations | Data |

**(d)** `Reports` should call a defined function such as `registration_count(event)` provided by `Registration` (or `EventStore`) and never touch internal variables.

## Answer 5
**(a)**
```
A --- C   <- main
 \
  B       <- food
```
Both `main` (tip C) and `food` (tip B) start from A.

**(b)** Git reports a **conflict** in `plan.txt`: both branches changed **line 2** in different ways, so Git cannot decide which to keep. The merge stops until a person resolves it.

**(c)**
```
Choose a venue
<<<<<<< HEAD
Book the room and invite the guest speaker
=======
Book the room and order snacks
>>>>>>> food
```

**(d)** Edit the file to keep both ideas and delete the marker lines, for example:
```
Choose a venue
Book the room, invite the guest speaker and order snacks
```
Then run:
```
git add plan.txt
git commit -m "Merge food: combine speaker and snacks"
```

**(e)** Examples: merge small branches often; pull the latest changes before starting work; agree who edits which files; keep changes focused.

## Answer 6
**(a)** **Boundaries:** 0, 1 and 5 (with points just beside them). *(Example test set, checked by running the correct code.)*

| # | Weight | Expected |
|---|---|---|
| 1 | -2 | error (invalid) |
| 2 | 0 | error (invalid) |
| 3 | 0.5 | 5 |
| 4 | 1 | 5 |
| 5 | 1.01 | 10 |
| 6 | 5 | 10 |
| 7 | 5.01 | 20 |
| 8 | 8 | 20 |

**(b)** The buggy version fails **test 4** (weight 1: returns **10**, expected 5) and **test 6** (weight 5: returns **20**, expected 10). Tests 3, 5, 7 and 8 still pass, and tests 1 and 2 still raise the error.

**(c)** **Boundary value analysis** found it. The values 0.5, 3 and 8 are all comfortably inside their ranges, so the wrong `<` would still return the right answer for them. Only values **exactly at** 1 and 5 expose the error.

**(d)** **Unit** level: each test checks one small function on its own.

## Answer 7
**(a)** The three functions repeat the same steps (add a percentage, then round), differing only in the rate. If the rounding rule changes, all three must be edited, and one may be missed (it breaks **DRY**).

**(b)**
```python
def fee_with_surcharge(base, rate):
    return round(base + base * rate, 2)

def event_fee_member(base):
    return fee_with_surcharge(base, 0.05)

def event_fee_guest(base):
    return fee_with_surcharge(base, 0.25)

def event_fee_sponsor(base):
    return fee_with_surcharge(base, 0.00)
```
(The old function names can stay, so other code is not affected, or be replaced by direct calls.)

**(c)**

| base | member (0.05) | guest (0.25) | sponsor (0.00) |
|---|---|---|---|
| 40 | 42.0 | 50.0 | 40.0 |
| 12.5 | 13.12 | 15.62 | 12.5 |

Both the original and the new functions give these same numbers. *(For 12.5: member = 12.5 + 0.625 = 13.125, shown as 13.12 because of how the computer rounds; guest = 12.5 + 3.125 = 15.625, shown as 15.62. The rounding behaviour is identical in both versions.)*

**(d)** A refactoring improves **structure** while the **behaviour stays the same** (same inputs give same outputs). A new feature would change what the program does.

## Answer 8
**Part 1**
**(a)**

| ID | Probability | Impact | Exposure |
|---|---|---|---|
| R1 | 3 | 4 | **12** |
| R2 | 2 | 5 | **10** |
| R3 | 5 | 3 | **15** |
| R4 | 2 | 3 | **6** |

Ranking: **R3 (15), R1 (12), R2 (10), R4 (6)**.

**(b)** For R3 (scope creep): prioritise requests with MoSCoW, agree the sprint scope with the organisers, and put new ideas in the product backlog for later.

**Part 2**
1. **Corrective** (fix a bug)
2. **Adaptive** (keep working in a changed environment)
3. **Perfective** (add a feature or improvement)
4. **Preventive** (restructure to avoid future problems)

## Answer 9 (model answer and marking guide)
1. **Process model:** *Agile (Scrum)*: the library has no fixed idea of every feature and wants a first version in 8 weeks, so four 2-week sprints with feedback each time fit best.
2. **Requirements (examples)**
   - *Must:* "As a student, I want to search for a book by title, so that I can see if it is available." / "As a student, I want to reserve an available copy, so that it is held for me." (Acceptance: *Given* a copy is available, *when* I reserve it, *then* I get a confirmation and the available count drops by one.) / *Should:* "As a librarian, I want a list of reservations, so that I can prepare the books."
   - *Non-functional (testable):* "Search results appear within 2 seconds for 95% of searches." / "Student emails are visible only to librarians."
3. **Design:** e.g. `Pages` (presentation), `Search` and `Reservation` and `Accounts` (business logic), `BookStore` (data).
4. **Version control:** e.g. each feature is built on its own branch, reviewed in a pull request, and merged to `main` only if the tests pass.
5. **Test cases (example):** copies available = 2, reserve → success (1 left); copies available = 1, reserve → success (0 left); copies available = 0, reserve → rejected (**boundary**).
6. **Risks (example):** R-A: personal data exposed (probability 3, impact 5, exposure 15): reduce with access controls and review. R-B: scope creep (probability 4, impact 3, exposure 12): reduce with MoSCoW.
7. **Ethics:** the app stores names and emails, which are personal data. Collect only what is needed, restrict access, and tell students how their data is used.
8. **Maintenance:** *corrective:* fix a bug where two students reserve the last copy at the same moment; *perfective:* add email reminders when a reserved book is ready.

**Marking guide (self-check):** ☐ Model justified ☐ Three user stories with at least one acceptance criterion ☐ Two testable non-functional requirements ☐ MoSCoW used ☐ Four modules with layers ☐ Branching described ☐ Three test cases with a boundary ☐ Two risks with exposure ☐ Privacy issue named ☐ Both maintenance types given.

---

*The code and Git examples in this module were run to confirm their behaviour, and the calculations were checked twice. A teammate who is not the author should re-check them and record the result in the [Teammate Review](../Teammate_review/15_teammate-review.md).*
