# Module 15: Software Engineering

**Software Fundamentals · Study Guide content · V2.0 working draft**

| | |
|---|---|
| **Audience** | Complete beginners (some idea of what a program is helps, see Module 10) |
| **Estimated study time** | 5 to 6 hours, including the activities |
| **Author** | [Your name] |
| **Reviewer (not the author)** | [Teammate name, to be completed] |
| **Draft date** | 2026-11-03 |

**Files in this module:**
[Main Theory (this file)](15_main-theory.md) ·
[Learner Activities](../Learner%20Activity/15_learner-activities.md) ·
[Test Bank](../Test%20bank%20Question_Answer/15_test-bank.md) ·
[References and AI Usage](../References%20and%20AI%20Usage/15_references-and-ai-usage.md) ·
[Teammate Review](../Teammate_review/15_teammate-review.md) ·
[Content Status and Mapping](../15_content-status-and-mapping.md)

**Related modules:** [Module 09: Operating Systems and Symbolic AI](../../09_where-operating-systems-meet-symbolic-ai/Main%20Theory/09_main-theory.md) · [Module 10: Introduction to Software](../../10_introduction-to-software/Main%20Theory/10_main-theory.md) (bugs, licences and version numbers are introduced there and used again here).

---

## 1. Module Overview

Writing a small program on your own is one skill. Building software that many people depend on, that a team creates over months or years, and that must keep working as the world changes, is a different skill. That skill is **software engineering**.

This module answers five beginner questions:

1. **What is software engineering**, and how is it different from programming?
2. **How is a software project organised** (stages and process models)?
3. **How do teams decide what to build and how to structure it** (requirements and design)?
4. **How do teams keep quality high** (version control, testing, code quality)?
5. **What happens after the first release**, and how are teams and risks managed?

**One running example.** Throughout the module we follow a small project called **ClubSignup**, a web app where students browse club events, register for them, and receive a confirmation email, while organisers see who is coming. Using one example means each idea builds on the last.

**How the module is organised**

| Part | Big question | Sections | Practise with |
|---|---|---|---|
| **A. Foundations** | What is software engineering and what are its stages? | 4, 5 | Activity 1 |
| **B. Process models** | How do teams organise the work? | 6 | Activity 2 |
| **C. Requirements and design** | What should we build, and how should it be structured? | 7, 8 | Activities 3, 4 |
| **D. Building and checking quality** | How do we collaborate, test and keep code healthy? | 9 to 11 | Activities 5 to 7 |
| **E. Delivering, maintaining, managing** | What happens after release, and how do teams manage risk and responsibility? | 12 to 15 | Activities 8, 9 |

**Prerequisite words**

| Word | Meaning |
|---|---|
| **Program / software** | Instructions for a computer / programs plus their data, documents and settings (Module 10) |
| **Source code** | The text of a program written by people |
| **Bug** | A mistake that makes software behave wrongly (Module 10) |
| **Stakeholder** | Anyone affected by or interested in the software: users, customers, developers, managers |
| **User** | A person who uses the software |

---

## 2. Learning Outcomes

By the end of this module you should be able to:

| # | Outcome | Sections |
|---|---|---|
| **LO1** | Explain what software engineering is and how it differs from programming | 4 |
| **LO2** | Describe the stages of the software development life cycle and what each produces | 5 |
| **LO3** | Compare Waterfall, iterative and Agile (Scrum) approaches and choose one for a scenario | 6 |
| **LO4** | Write clear, testable requirements, user stories and acceptance criteria | 7 |
| **LO5** | Apply design principles (modularity, cohesion, coupling, layers) to a simple system | 8 |
| **LO6** | Explain how version control works and resolve a simple merge conflict | 9 |
| **LO7** | Design test cases, including boundary values, and place tests at the right level | 10 |
| **LO8** | Recognise good code practice and refactor duplicated code safely | 11 |
| **LO9** | Describe deployment, continuous integration and the four types of maintenance | 12 |
| **LO10** | Rank risks, describe team roles, and reason about a professional and ethical dilemma | 13, 14 |

---

# PART A: FOUNDATIONS

## 3. How Part A is built

Section 4 explains what software engineering is. Section 5 introduces the six stages that nearly every project goes through, using ClubSignup as the example.

---

## 4. What Is Software Engineering?

### 4.1 Definition

> **Software engineering** is the disciplined way of planning, designing, building, testing and maintaining software so that it is reliable, meets users' needs, and stays affordable to change. It usually involves a team working over a long time.

**Analogy:** Cooking dinner for yourself is programming. Running a restaurant kitchen is software engineering: you need a menu (requirements), a kitchen layout (design), several cooks working together (teamwork), quality checks (testing), a way of handling complaints and changing the menu (maintenance), and rules for hygiene and safety (professional standards).

### 4.2 Programming vs software engineering

| | Programming | Software engineering |
|---|---|---|
| **Main question** | "How do I make this code work?" | "How do we build the *right* thing, well, as a team, and keep it working?" |
| **Size** | Often one person, one file or a few | Many people, many components, years |
| **Time horizon** | Until it runs | The whole life of the software, including years of changes |
| **Activities** | Writing code | Requirements, design, coding, testing, release, maintenance, teamwork, risk management |
| **Success means** | The program produces output | Users' needs are met, on time, with acceptable quality and cost |

### 4.3 Why engineering ideas are needed

- **Software is invisible.** You cannot see a half-built program the way you can see a half-built bridge, so progress and quality are hard to judge without good practices.
- **Needs change.** Users, laws and technology change while the project runs.
- **Teams need coordination.** Several people changing the same code can overwrite each other's work.
- **Software lives long.** Over the whole life of a system, maintenance often takes a large share of the total effort (Sommerville, reference 1).
- **Failures can be costly.** Bugs can lose money, leak personal data or, in some systems, put people at risk.

The term "software engineering" became widely used after a 1968 NATO conference, which discussed projects that were running late, over budget and unreliable (reference 7). Many practices in this module grew out of attempts to solve those problems.

### 4.4 What "good" means

You met the main qualities in Module 10: **correct**, **reliable**, **usable**, **efficient**, **secure** and **maintainable**. Software engineering is the set of practices that help a team reach these qualities on purpose, not by luck. Because the qualities can pull against each other (for example, extra security checks can make an app slower or harder to use), engineers make **trade-offs** and explain them.

> **Common misunderstanding: "Software engineering is just coding with extra paperwork."**
> Documents are only a means. The aim is to deliver software that people can rely on and that the team can change safely.

---

## 5. The Software Development Life Cycle (SDLC)

### 5.1 Six stages

The **software development life cycle (SDLC)** is the set of stages a software project passes through, from idea to retirement.

![Figure 1: The software development life cycle. Six stages: requirements, design, implementation, testing, deployment, maintenance. Each lists what it produces. An arrow from maintenance back to requirements shows that new needs and bug reports start the next round.](../Diagrams%20and%20Pictures/15_fig1_sdlc.svg)

*Figure 1. The SDLC. Real projects overlap and repeat these stages.*

| Stage | Key question | Typical output | Who is mainly involved |
|---|---|---|---|
| **1. Requirements** | What do users need? | Requirements list, user stories | Stakeholders, analysts, product owner |
| **2. Design** | How will we structure it? | Architecture, screen sketches, data plan | Designers, senior developers |
| **3. Implementation** | Let's build it | Source code, kept in version control | Developers |
| **4. Testing** | Does it work, and is it right? | Test cases and results, bug reports | Testers, developers |
| **5. Deployment** | How do users get it? | A released, running version | Developers, operations staff |
| **6. Maintenance** | How do we keep it useful? | Fixes, updates, new versions | Whole team |

### 5.2 Worked example 1: ClubSignup through the six stages

| Stage | What the ClubSignup team does | Output |
|---|---|---|
| **Requirements** | Interviews members and organisers; learns that members want to register in a few clicks and organisers want an attendee list | 12 user stories, ranked by importance |
| **Design** | Splits the app into pages, rules and a database; sketches the registration screen | A layered design and a database table plan (Module 14) |
| **Implementation** | Writes the code in small steps and saves each step in Git | Source code history |
| **Testing** | Checks registration, full events, and the email | Test cases; a bug report: "Registration still works for full events" |
| **Deployment** | Puts version `1.0.0` on a web server | A live app |
| **Maintenance** | Fixes the bug (`1.0.1`), later adds a waiting list (`1.1.0`) | New versions (see semantic versioning in Module 10) |

**Key lesson:** The stages are a map, not a strict schedule. A test failure can send you back to design; user feedback after release goes back to requirements.

**▶ Apply it:** Activity 1 (stages and artefacts).

---

## Quick Check: Part A

1. Give two differences between programming and software engineering.
   *Answer: for example, software engineering involves teams and the whole life cycle, while programming is mainly about making code work.*
2. In which stage would you write test cases for a user story?
   *Answer: testing (test cases are best planned from the requirements, though they can be drafted earlier).*
3. Why does the SDLC arrow go from maintenance back to requirements?
   *Answer: new needs and bug reports lead to new or changed requirements.*

---

# PART B: PROCESS MODELS

## 6. Organising the Work: Process Models

A **process model** is an agreed way of organising the SDLC stages in time.

![Figure 2: Waterfall compared with Agile. Top: waterfall as a staircase of five stages, each finishing before the next starts. Bottom: agile as three sprints, each ending with working software that grows with each sprint.](../Diagrams%20and%20Pictures/15_fig2_waterfall-vs-agile.svg)

*Figure 2. Waterfall (top) and Agile (bottom).*

### 6.1 Waterfall

Stages happen **one after another**, and each is finished before the next begins.

- **Strengths:** clear milestones; thorough documents; fits projects whose needs are well understood and stable.
- **Weaknesses:** users see working software only near the end; discovering a misunderstanding late is costly.
- *Note:* the name is often linked to a 1970 paper by Winston Royce, who actually warned that a strictly one-pass approach is risky for large systems (reference 8).

### 6.2 Iterative and incremental

The team builds the software in **repeated rounds** (iterations). Each round adds or improves features, so working versions exist early and can be improved. Agile methods are a popular form of this idea.

### 6.3 Agile

**Agile** is a family of approaches built on short cycles, working software and regular feedback. The Agile Manifesto (2001, reference 3) states four values, summarised here in our own words:

1. People and their collaboration matter more than rigid processes and tools.
2. Working software matters more than exhaustive documentation.
3. Working closely with the customer matters more than negotiating a contract.
4. Responding to change matters more than following a fixed plan.

The manifesto says there is value in the items on the right too, but the items on the left matter more.

### 6.4 Scrum

**Scrum** is the most widely used Agile framework. The vocabulary below follows the Scrum Guide (reference 4).

![Figure 3: The Scrum cycle. The product backlog feeds sprint planning, which produces the sprint backlog. The sprint, with a daily scrum, produces an increment. Sprint review and sprint retrospective follow, then the next sprint planning. Review feedback updates the product backlog.](../Diagrams%20and%20Pictures/15_fig3_scrum-cycle.svg)

*Figure 3. One Scrum cycle.*

| Term | Meaning |
|---|---|
| **Product Backlog** | An ordered list of everything that might be built |
| **Sprint** | A fixed-length period (one month or less) in which a usable increment is built |
| **Sprint Planning** | The team chooses which backlog items to do in the sprint and how |
| **Sprint Backlog** | The chosen items plus the plan for doing them |
| **Daily Scrum** | A 15-minute daily check-in on progress and obstacles |
| **Increment** | The working, usable software produced by the sprint |
| **Sprint Review** | The team shows the increment and gathers feedback |
| **Sprint Retrospective** | The team reflects on how it worked and chooses improvements |
| **Product Owner** | Decides what is most valuable to build and orders the backlog |
| **Developers** | The people who build the increment (including testing) |
| **Scrum Master** | Helps the team understand and use Scrum well |

### 6.5 Kanban (briefly)

**Kanban** shows work on a board with columns such as *To do*, *Doing* and *Done*, and **limits how many items are in "Doing"** at once so that work flows steadily instead of piling up half-finished.

### 6.6 Comparing the approaches

| | Waterfall | Iterative / Agile (Scrum) |
|---|---|---|
| **Planning** | Detailed plan up front | Plan in short cycles; adjust often |
| **Change** | Expensive after early stages | Expected and welcomed |
| **First working software** | Late | After the first sprint or iteration |
| **Documentation** | Heavy | Enough to support the team; working software first |
| **Customer involvement** | Mostly at the start and end | Continuous |
| **Fits best when** | Needs are stable and clear; strict rules or contracts | Needs are uncertain or likely to change |

Many real organisations mix ideas (for example, detailed documentation required by regulations plus short iterative cycles).

### 6.7 Worked example 2: choosing an approach

There is rarely one correct answer. The reasoning is what matters.

| Scenario | A reasonable choice | Reasoning |
|---|---|---|
| A payroll system must be updated for a new tax law with a fixed specification and a legal deadline | **Plan-driven (Waterfall-like)** | Requirements are fixed and well understood; a clear plan and documentation help meet the deadline |
| A start-up builds a new social app and is unsure what users will like | **Agile (for example Scrum)** | Needs are uncertain; early releases and feedback reduce the risk of building the wrong thing |
| Software for a regulated medical device | **A hybrid: plan-driven documentation and approvals with iterative development and heavy testing** | Safety rules demand traceable documents, but iterations still catch problems early |

### 6.8 Worked example 3: estimating with velocity

In Agile, the size of a backlog item is often estimated in **story points**, a relative measure of effort, not hours. A team's **velocity** is the number of points it completes per sprint.

ClubSignup team's last three sprints: **18, 22 and 20** points.
- Average velocity = (18 + 22 + 20) ÷ 3 = **20 points per sprint**.
- Remaining backlog = **90 points**.
- Sprints needed = 90 ÷ 20 = **4.5**, so plan for **5 sprints**.
- At 2 weeks per sprint, that is about **10 weeks**.

**Caution:** this is an estimate. New requirements, illness or surprises change the result, so the team recalculates after every sprint.

**▶ Apply it:** Activity 2 (choose a model; compute an estimate).

---

## Quick Check: Part B

1. What is the main difference in *when* users see working software, Waterfall vs Agile?
   *Answer: Waterfall delivers it near the end; Agile delivers working increments every sprint.*
2. Name the three Scrum roles.
   *Answer: Product Owner, Developers, Scrum Master.*
3. A team's velocity averages 25 points and 110 points remain. How many sprints?
   *Answer: 110 ÷ 25 = 4.4, so 5 sprints.*

---

# PART C: REQUIREMENTS AND DESIGN

## 7. Requirements

### 7.1 What are requirements?

**Requirements** describe what the software must do and the qualities it must have. They come from **stakeholders**. Teams gather them by **elicitation**: interviews, surveys, observing users, studying existing systems, and showing prototypes.

| Kind | Meaning | ClubSignup example |
|---|---|---|
| **Functional requirement** | A thing the system must *do* | "A member can register for an event." |
| **Non-functional requirement** | A *quality* the system must have: speed, security, usability, reliability, accessibility | "The event list loads in under 2 seconds for 95% of requests." |
| **Constraint** | A limit on the solution | "The app must run on the college's existing web server." |

### 7.2 What makes a good requirement?

A good requirement is **clear**, **unambiguous**, **necessary**, **feasible** and, above all, **testable**: someone can check whether it has been met.

### 7.3 User stories and acceptance criteria

In Agile projects, requirements are often written as **user stories**:

> **As a** *type of user*, **I want** *a goal*, **so that** *a benefit*.

Each story has **acceptance criteria**, written as examples, often in the form *Given / When / Then*. They say when the story counts as done.

### 7.4 Prioritising: MoSCoW

Teams rank requirements with **MoSCoW**: **M**ust have, **S**hould have, **C**ould have, **W**on't have (this time). This keeps the first release small and valuable.

### 7.5 Worked example 4: from vague to testable

| Vague requirement | Problem | Testable version |
|---|---|---|
| "The system should be fast." | "Fast" cannot be measured | "The event list page loads in under 2 seconds for 95% of requests with 200 users online." (non-functional) |
| "The app must be user-friendly." | Opinion, not a check | "A new member can register for an event in at most 3 steps without help; test with 5 new users." (non-functional) |
| "The system sends emails and notifications." | Unclear: which events, how many, when? | "When a member registers, the system sends one confirmation email within 1 minute." (functional) |

**A complete user story**

> **As a** club member, **I want** to register for an event, **so that** I get a place.

**Acceptance criteria**
1. **Given** an event with free places, **when** I register, **then** I see a confirmation and my name appears on the attendee list.
2. **Given** an event that is full, **when** I try to register, **then** I am told it is full and my name is not added.
3. **Given** I am already registered, **when** I try again, **then** I am told so and no duplicate is created.

*Notice that these criteria are exactly the examples a tester will later turn into test cases (Section 10).*

> **Common misunderstandings**
> - *"Requirements are fixed at the start."* Needs change, so teams revisit and reprioritise them.
> - *"Users always know exactly what they want."* Often they do not, which is why prototypes and feedback matter.

**▶ Apply it:** Activity 3 (rewrite and write requirements).

---

## 8. Design

### 8.1 What is design?

**Design** decides how the software will be structured to meet the requirements, before and while it is built. A good design makes the software easier to build, test, understand and change.

### 8.2 Key design principles

| Principle | Meaning | Everyday analogy |
|---|---|---|
| **Abstraction** | Hide complicated details behind a simple interface | Driving a car without knowing how the engine works |
| **Modularity** | Divide the system into separate parts (modules) | A kitchen with separate stations |
| **Separation of concerns** | Each part handles one kind of job | The chef cooks, the waiter serves |
| **Cohesion** | How closely the things inside one module belong together. **High** is good | A toolbox drawer holding only screwdrivers |
| **Coupling** | How much modules depend on each other's internals. **Low** is good | Appliances that connect by a standard plug, not by being wired together |
| **DRY (Don't Repeat Yourself)** | Keep each piece of knowledge in one place | One recipe card, not ten copies that drift apart |

### 8.3 Architecture: layers

A common **architecture** (overall structure) is **layered**. Each layer talks only to the layer next to it.

```
+----------------------------------------------+
| Presentation layer: pages, forms, buttons    |   what the user sees
+----------------------------------------------+
| Business logic layer: rules                  |   e.g. "is the event full?"
+----------------------------------------------+
| Data layer: reading and writing the database |   (Module 14)
+----------------------------------------------+
```

Another common pattern is **client-server**: the user's browser (client) sends requests to a program on a server that holds the logic and data (see Modules 09 and 10 for how programs and operating systems support this).

### 8.4 Worked example 5: designing ClubSignup

**Modules and their single responsibilities**

| Module | Responsibility | Layer |
|---|---|---|
| `EventPages` | Shows the event list and registration form | Presentation |
| `Registration` | Rules: free places, duplicates, adding a name | Business logic |
| `Notifications` | Builds and sends emails | Business logic |
| `EventStore` | Saves and loads events and registrations | Data |

**A poor design.** One giant module that draws pages, checks logins, writes database queries *and* sends emails has **low cohesion** (many unrelated jobs). Changing the email wording risks breaking page layout.

**A coupling problem.** If `Registration` reaches inside `Notifications` and edits its internal variables, any change to `Notifications` can break `Registration` (**high coupling**).

**An improvement.** `Notifications` offers one clear function, for example `send_confirmation(member, event)`. `Registration` calls only that function and knows nothing about how emails are built (**low coupling**, and the details are hidden through abstraction).

**▶ Apply it:** Activity 4 (analyse and improve a design).

---

## Quick Check: Part C

1. Is "The system must be secure" a good requirement? Why or why not?
   *Answer: no; it is vague and untestable. A better form states a checkable rule, such as "Passwords are stored in hashed form and accounts lock after 5 failed logins".*
2. Do you want high or low coupling? High or low cohesion?
   *Answer: low coupling and high cohesion.*
3. What does MoSCoW help a team do?
   *Answer: prioritise requirements (Must, Should, Could, Won't this time).*

---

# PART D: BUILDING AND CHECKING QUALITY

## 9. Version Control and Collaboration

### 9.1 The problem

Several developers changing the same files can overwrite each other's work, and mistakes need to be undone. **Version control** records every change, lets many people work in parallel, and lets you return to an earlier version.

**Git** is the most widely used version control tool. **GitHub** is a website that hosts Git projects and adds collaboration features. They are not the same thing: Git is the tool; GitHub is a service that hosts repositories that use it.

### 9.2 Key ideas

| Term | Meaning |
|---|---|
| **Repository (repo)** | A project's files together with their full history |
| **Commit** | A saved snapshot of the project with a message explaining the change |
| **Branch** | A separate line of work, so changes can be made without disturbing the main line |
| **Merge** | Combining the work of two branches |
| **Merge conflict** | Two branches changed the same lines differently, so a person must choose the result |
| **Remote** | A copy of the repository on a server (for example on GitHub) |
| **Push / Pull** | Send your commits to the remote / bring new commits from the remote |
| **Pull request** | A request to merge a branch, usually with a review by teammates |

### 9.3 Everyday commands

| Command | What it does |
|---|---|
| `git init` | Start a new repository |
| `git status` | Show what has changed |
| `git add <file>` | Mark a change to be included in the next commit |
| `git commit -m "message"` | Save a snapshot with a message |
| `git switch -c <name>` | Create a new branch and move to it |
| `git switch <name>` | Move to an existing branch |
| `git merge <name>` | Merge the named branch into the current branch |
| `git log --oneline --graph --all` | Show the history as a graph |
| `git push` / `git pull` | Share commits with a remote / get others' commits |

**Good commit messages** say *what changed and why* (for example, "Reject registration for full events"), not "stuff" or "fix".

> **Common misunderstandings**
> - *"Git and GitHub are the same."* Git is the tool; GitHub hosts Git repositories.
> - *"A commit is a backup on the internet."* A commit is saved in your **local** repository. It reaches the remote only when you push.

### 9.4 Worked example 6: branch, conflict and merge

![Figure 4: A Git branch and a merge. Main has commits C1, C2, C3 and a merge commit M. A feature branch starts at C2, has one commit F1, and is merged into main at M.](../Diagrams%20and%20Pictures/15_fig4_git-branch-merge.svg)

*Figure 4. The history we are about to create.*

The file `notes.txt` is edited on two branches. (These commands were run with Git 2.43 to produce the output shown.)

```
git init -b main
# create notes.txt with two lines, then:
git add notes.txt
git commit -m "C1: add notes"
# add a third line "Members get a confirmation email", then:
git commit -am "C2: add email note"

git switch -c feature/reminder
# add a fourth line "Send a reminder the day before", then:
git commit -am "F1: add reminder note"

git switch main
# on main, add a different fourth line "Print attendance list on the day", then:
git commit -am "C3: add attendance note"

git merge feature/reminder
```

Git responds:

```
Auto-merging notes.txt
CONFLICT (content): Merge conflict in notes.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Both branches changed the **same place** (the fourth line), so Git cannot decide. It marks the file:

```
Club sign-up notes
Events open on Monday
Members get a confirmation email
<<<<<<< HEAD
Print attendance list on the day
=======
Send a reminder the day before
>>>>>>> feature/reminder
```

**How to read it**
- Between `<<<<<<< HEAD` and `=======` is the version on the branch you are on (`main`).
- Between `=======` and `>>>>>>> feature/reminder` is the version from the branch being merged.

**Resolving it**
1. Edit the file to the text you want, here **both** lines, and delete the three marker lines.
2. `git add notes.txt`
3. `git commit -m "M: merge feature/reminder"`

The result, shown with `git log --oneline --graph --all`:

```
*   4394958 M: merge feature/reminder
|\
| * 902551d F1: add reminder note
* | 6e2e9d3 C3: add attendance note
|/
* bc3a182 C2: add email note
* 531bc01 C1: add notes
```

(Your commit IDs will differ; the shape of the graph will match Figure 4.)

**Key lesson:** A conflict is not a failure. It is Git asking a person to decide. Small branches that are merged often produce fewer and easier conflicts.

**▶ Apply it:** Activity 5 (predict history and resolve a conflict).

---

## 10. Testing

### 10.1 Why test?

**Testing** means running software to find bugs and to check that it meets its requirements. A well-known remark by the computer scientist Edsger Dijkstra is that testing can show bugs are present but cannot prove there are none. So a good test set aims to find bugs where they are most likely, rather than just to run many cases.

### 10.2 Levels of testing

![Figure 5: Levels of testing. A pyramid: unit at the bottom, then integration, system, and acceptance at the top. Lower levels have more, faster, cheaper tests.](../Diagrams%20and%20Pictures/15_fig5_testing-levels.svg)

*Figure 5. Levels of testing.*

| Level | What is tested | ClubSignup example |
|---|---|---|
| **Unit** | One small piece (a function) on its own | "Is a 17-year-old eligible?" |
| **Integration** | Pieces working together | The registration code and the database save the right row |
| **System** | The complete system against the requirements | Register, receive the email, appear on the organiser's list |
| **Acceptance** | Whether users or the client accept it | Organisers try it on a real event |

Other useful ideas:
- **Regression testing:** re-run earlier tests after a change to check that nothing that worked has broken.
- **Black-box testing:** test only inputs and outputs, without looking at the code. **White-box testing:** test with knowledge of the code's structure.
- **Functional vs non-functional testing:** does it do the right thing, versus is it fast, secure and usable enough.
- **Automated tests** run by a program and are cheap to repeat; **manual tests** are done by a person and suit exploring and usability.

### 10.3 Designing test cases

A **test case** has an **input**, an **expected result** and, after running, an **actual result** and a pass or fail verdict.

Two techniques help you choose inputs wisely:
- **Equivalence partitions:** group inputs that the program should treat the same, and test one from each group.
- **Boundary value analysis:** bugs cluster at the edges, so test values **at and just beside each boundary**.

### 10.4 Worked example 7: testing an eligibility rule

**Requirement:** ClubSignup membership is for ages **16 to 25 inclusive**.

```python
def is_eligible(age):
    """Club membership is for ages 16 to 25 inclusive."""
    return 16 <= age <= 25
```

**Choosing test inputs.** The boundaries are 16 and 25, so test 15, 16, 17 (around the lower edge) and 24, 25, 26 (around the upper edge), plus a normal value and an invalid one.

| Test | Input (age) | Expected | Actual | Result |
|---|---|---|---|---|
| T1 | 15 | False | False | Pass |
| T2 | 16 | True | True | Pass |
| T3 | 17 | True | True | Pass |
| T4 | 20 | True | True | Pass |
| T5 | 25 | True | True | Pass |
| T6 | 26 | False | False | Pass |
| T7 | -3 | False | False | Pass |

**As automated tests**

```python
assert is_eligible(15) == False
assert is_eligible(16) == True
assert is_eligible(25) == True
assert is_eligible(26) == False
print("All tests passed")
```

**What boundary tests catch.** Suppose a developer wrongly writes `16 <= age < 25`. Running the same inputs gives the right answer for 15, 16 and 26, but **False for 25**. Only the boundary test T5 exposes the bug. This kind of mistake (using `<` instead of `<=`) is common and is called an **off-by-one error**.

> **Common misunderstandings**
> - *"If all my tests pass, the software is correct."* It is correct only for the cases you tested.
> - *"Testing is something done only at the end."* Tests are planned from the requirements and run throughout; the earlier a bug is found, the cheaper it usually is to fix.
> - *"More tests always mean better tests."* Well-chosen tests (boundaries, typical, invalid) matter more than quantity.

**Test-driven development (TDD)**, briefly: write a failing test first, write the smallest code that makes it pass, then tidy the code. It keeps requirements and tests close together.

**▶ Apply it:** Activity 6 (design tests and find a boundary bug).

---

## 11. Code Quality

### 11.1 Why quality of the *code itself* matters

Code is read far more often than it is written. A teammate, or you in six months, must be able to understand it to fix or extend it.

| Practice | What it means |
|---|---|
| **Meaningful names** | `registration_count` instead of `x` |
| **Small, single-purpose functions** | Each function does one thing (high cohesion) |
| **Consistent style** | The team formats code the same way |
| **Helpful comments** | Explain *why* something is done, not what the next line obviously does |
| **No duplication (DRY)** | Fix a rule in one place, not five |
| **Code review** | Teammates read changes before merging (a pull request) to catch bugs and share knowledge |
| **Refactoring** | Improving the structure of code **without changing what it does**, protected by tests |

### 11.2 Worked example 8: refactoring duplicated code

**Before.** Three functions repeat the same calculation with different discount rates:

```python
def student_price(price):
    discounted = price - price * 0.20
    return round(discounted, 2)

def senior_price(price):
    discounted = price - price * 0.30
    return round(discounted, 2)

def staff_price(price):
    discounted = price - price * 0.15
    return round(discounted, 2)
```

**Problem:** if the rounding rule changes, three places must be edited, and one is likely to be forgotten.

**After.** One function holds the rule; the rate is an input:

```python
def discounted_price(price, rate):
    return round(price - price * rate, 2)
```

**Behaviour must not change.** Run the old and new versions on the same inputs:

| Price | `student_price` | `discounted_price(price, 0.20)` | `senior_price` | `discounted_price(price, 0.30)` | `staff_price` | `discounted_price(price, 0.15)` |
|---|---|---|---|---|---|---|
| 80 | 64.0 | 64.0 | 56.0 | 56.0 | 68.0 | 68.0 |
| 19.99 | 15.99 | 15.99 | 13.99 | 13.99 | 16.99 | 16.99 |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

The outputs are identical, so this is a safe **refactoring**: structure improved, behaviour unchanged. In a real project the team's automated tests would check this for them.

**▶ Apply it:** Activity 7 (refactor and verify).

---

## Quick Check: Part D

1. What is the difference between `git add` and `git commit`?
   *Answer: `git add` marks changes for the next commit; `git commit` saves the snapshot.*
2. Which test input would catch the bug `16 <= age < 25`?
   *Answer: 25 (a boundary value).*
3. What must stay the same when you refactor?
   *Answer: the behaviour of the code.*

---

# PART E: DELIVERING, MAINTAINING AND MANAGING

## 12. Deployment and Maintenance

### 12.1 Deployment

**Deployment** puts the software where users can use it. Teams usually keep several **environments**:

| Environment | Purpose |
|---|---|
| **Development** | Where developers write and try code |
| **Testing / staging** | A copy of the real setup for final checks |
| **Production** | The live system real users depend on |

**Continuous integration (CI)** means that every time someone submits a change, an automated system builds the software and runs the tests, so problems are found within minutes. **Continuous delivery/deployment (CD)** extends this by preparing, or automatically performing, the release. Good teams also plan a **rollback** (returning to the previous version if a release goes wrong) and **monitor** the live system.

### 12.2 Maintenance

**Maintenance** is everything done after release. It is often a large share of a system's total effort over its life.

| Type | Purpose | ClubSignup example |
|---|---|---|
| **Corrective** | Fix bugs | Stop registration for full events (`1.0.1`) |
| **Adaptive** | Keep working in a changed environment | Update the app when the web server's software is upgraded |
| **Perfective** | Improve or add features, speed or usability | Add a waiting list (`1.1.0`) |
| **Preventive** | Restructure to avoid future problems | Refactor the duplicated discount code |

### 12.3 Technical debt

**Technical debt** is the extra future work created when a team takes a shortcut now (for example, skipping tests or copying code). Like a loan, it lets you go faster at first, but "interest" accumulates: the longer it stays, the harder each later change becomes. Teams manage it by paying it down regularly (refactoring, adding tests, updating documents) and by deciding shortcuts knowingly.

### 12.4 Documentation

Useful documentation is **just enough, and kept up to date**: a **README** (what the project is and how to run it), comments for tricky parts, a user guide, and notes explaining major design decisions.

---

## 13. Teams and Project Management

### 13.1 Roles

| Role | Typical responsibility |
|---|---|
| **Product owner / product manager** | Decides what to build and in what order |
| **Developer** | Designs and writes code and tests |
| **Tester / QA** | Plans and runs tests; reports bugs |
| **Designer (UX)** | Designs how the software looks and feels to use |
| **Project / delivery manager** | Keeps work on track and communication clear |
| **Scrum Master** (in Scrum) | Helps the team use Scrum well |

On small teams one person often holds several roles.

### 13.2 Communication and scope

Good teams communicate often: daily check-ins, shared boards, written decisions, and pull request reviews. **Scope creep** is the gradual growth of a project's requirements without matching time or budget. Fred Brooks (reference 10) observed that simply adding people to a late project often makes it later, because new people must learn the project and the team has more communication to manage.

### 13.3 Managing risk

A **risk** is something that might go wrong and harm the project. For each risk, estimate:
- **Probability** (how likely, scale 1 to 5), and
- **Impact** (how bad, scale 1 to 5).

**Risk exposure = probability × impact.** Work first on the highest exposure. Typical responses: **avoid** it, **reduce** it, **transfer** it (for example, buy a service instead of building it), or **accept** it.

### 13.4 Worked example 9: ranking ClubSignup risks

| ID | Risk | Probability (1 to 5) | Impact (1 to 5) | Exposure |
|---|---|---|---|---|
| R1 | The only developer who knows the email code leaves | 2 | 5 | **10** |
| R2 | New feature requests keep arriving (scope creep) | 4 | 3 | **12** |
| R3 | A security flaw exposes members' personal data | 3 | 5 | **15** |
| R4 | The web host shuts down with no notice | 1 | 5 | **5** |

**Ranking (highest first):** R3 (15), R2 (12), R1 (10), R4 (5).

**Responses (examples):** *R3:* reduce it by security testing, careful storage of data and code review. *R2:* reduce it by prioritising with MoSCoW and agreeing the sprint scope. *R1:* reduce it by pair programming and documenting the email module. *R4:* accept it for now, but keep a backup.

**▶ Apply it:** Activity 8 (risk, maintenance types and estimates).

---

## 14. Professional Responsibility and Ethics

Software affects real people, so engineers have responsibilities beyond making code run. The ACM/IEEE Software Engineering Code of Ethics (reference 6) asks engineers to act in the **public interest**, be **honest** about what the software can and cannot do, protect **privacy and data**, respect **others' work and licences** (Module 10), and keep **quality and safety** in mind.

### 14.1 A simple way to reason through a dilemma

1. **Identify the facts** and the stakeholders.
2. **Identify the issue** (what harm or duty is involved).
3. **List the options** you really have.
4. **Weigh each option** (who is helped or harmed; honesty; the rules).
5. **Decide, act and record** what you did and why.

### 14.2 Worked example 10: launch pressure

**Situation.** The ClubSignup deadline is tomorrow. A tester finds that member email addresses can be viewed by anyone who edits the web address. Your manager says, "Launch anyway; we can patch it next week."

| Step | Analysis |
|---|---|
| **Facts and stakeholders** | Members (their data is exposed), organisers, the college, the team |
| **Issue** | Personal data would be exposed to anyone; this harms the public and breaks honesty about the product's safety |
| **Options** | (a) Launch as asked. (b) Delay until the fix is done. (c) Launch without the affected feature, or with limited access, while the fix is finished. (d) Escalate to a more senior person |
| **Weighing** | (a) puts members at real risk. (b) and (c) protect members; (c) may still meet the deadline. (d) is appropriate if the manager insists |
| **Decision (example)** | Report the issue in writing, recommend (c) or (b), and do not release the exposed feature. Keep a record of the report |

**Key lesson:** Professional duty to the public can outweigh a deadline. A good engineer raises the problem clearly and offers workable options, rather than staying silent or refusing without a plan.

**▶ Apply it:** Activity 9 (a full plan that includes an ethical check).

---

## 15. Putting It All Together

### 15.1 Worked example 11: one change request from report to release

**Report.** A member emails: "I registered for a full event and it worked." The team traces this change through everything in the module.

| Step | What happens | Stage / idea | Tool or section |
|---|---|---|---|
| 1 | The email is logged as a **bug report** with steps to reproduce | Maintenance (corrective) | Sections 5, 12 |
| 2 | The team confirms the bug and links it to the requirement "a full event rejects registration" (acceptance criterion 2) | Requirements | Section 7 |
| 3 | A developer writes a **failing test**: register for a full event and expect rejection | Testing (unit level) | Section 10 |
| 4 | They create a branch `fix/full-event` and change the rule in the `Registration` module only (**low coupling** helps) | Implementation, version control | Sections 8, 9 |
| 5 | They commit with a clear message and open a **pull request** | Version control, code review | Sections 9, 11 |
| 6 | **CI** builds the code and runs all tests, including **regression** tests | Testing, CI | Sections 10, 12 |
| 7 | A teammate reviews and approves; the branch is **merged** | Version control | Section 9 |
| 8 | Version **1.0.1** (a PATCH: bug fix only) is released to production | Deployment, versioning (Module 10) | Section 12 |
| 9 | The team **monitors** the live app and tells the member | Maintenance | Section 12 |

**Key lesson:** The practices work together. Clear requirements gave the test its expected result; modular design kept the change small; version control and review kept it safe; CI protected older features; and versioning communicated what changed.

---

## 16. Common Misconceptions: Summary Table

| # | Misconception | Correct idea | Section |
|---|---|---|---|
| 1 | "Software engineering is just programming." | It covers the whole life cycle, teamwork and quality. | 4 |
| 2 | "The SDLC stages happen once, in strict order." | They overlap and repeat; feedback loops back. | 5 |
| 3 | "Agile means no planning or no documentation." | Agile plans in short cycles and documents what is useful. | 6 |
| 4 | "Waterfall is always wrong." | It can suit stable, well-understood, regulated work. | 6 |
| 5 | "Requirements are fixed at the start." | Needs change; teams revisit and reprioritise them. | 7 |
| 6 | "'The system should be fast' is a requirement." | It is untestable until it has a measurable target. | 7 |
| 7 | "High coupling is fine if it works." | It makes change risky, because one edit breaks other parts. | 8 |
| 8 | "Git and GitHub are the same." | Git is the tool; GitHub hosts Git repositories. | 9 |
| 9 | "A merge conflict means someone made a mistake." | It means two people changed the same lines; a person must choose. | 9 |
| 10 | "All tests passing means no bugs." | It means no bugs were found by those tests. | 10 |
| 11 | "Refactoring changes what the program does." | It keeps behaviour the same while improving structure. | 11 |
| 12 | "Maintenance is only bug fixing." | It has four types, including adding features and adapting. | 12 |
| 13 | "Adding more developers always speeds up a late project." | It can slow it down at first, because of learning and communication. | 13 |

---

## Summary

- **Software engineering** is the disciplined, team-based way to plan, build, test and maintain software that meets users' needs over its whole life.
- The **SDLC** has six stages (requirements, design, implementation, testing, deployment, maintenance) that overlap and repeat. **Waterfall** works stage by stage; **Agile/Scrum** works in short sprints with regular feedback.
- **Requirements** should be testable (user stories with acceptance criteria). **Design** aims for **high cohesion, low coupling** and clear layers.
- **Git** gives history and safe collaboration (branches, merges, conflicts). **Testing** uses several levels and boundary values; passing tests do not prove correctness. **Refactoring** improves structure without changing behaviour.
- After release, teams **deploy, monitor and maintain** (corrective, adaptive, perfective, preventive), manage **technical debt** and **risk**, and act **responsibly and ethically**.

---

## Glossary (terms used consistently in this module)

| Term | Meaning |
|---|---|
| **Software engineering** | Disciplined, team-based building and maintenance of software |
| **SDLC** | Software development life cycle: the stages from idea to retirement |
| **Stakeholder** | Anyone affected by or interested in the software |
| **Process model** | An agreed way of organising the SDLC in time |
| **Waterfall** | Each stage finishes before the next begins |
| **Iterative / incremental** | Building in repeated rounds that add features |
| **Agile** | Short cycles, working software and regular feedback |
| **Scrum** | An Agile framework using sprints and defined roles |
| **Sprint** | A fixed-length period (one month or less) that produces an increment |
| **Product Backlog / Sprint Backlog** | Ordered list of wanted work / items chosen for the sprint |
| **Increment** | Working, usable software produced by a sprint |
| **Product Owner / Developers / Scrum Master** | Scrum roles |
| **Kanban** | A board-based method that limits work in progress |
| **Story points / Velocity** | Relative effort estimate / points completed per sprint |
| **Requirement** | What the software must do or be |
| **Functional / Non-functional requirement** | A thing the system does / a quality it must have |
| **User story** | "As a …, I want …, so that …" |
| **Acceptance criteria** | Examples that say when a story is done |
| **MoSCoW** | Must, Should, Could, Won't (this time) prioritisation |
| **Design / Architecture** | How the software is structured / its overall structure |
| **Abstraction** | Hiding details behind a simple interface |
| **Modularity** | Dividing a system into separate parts |
| **Cohesion / Coupling** | How well a module's contents belong together (aim high) / how much modules depend on each other (aim low) |
| **DRY** | Don't Repeat Yourself |
| **Version control** | Recording changes so many people can work together and undo mistakes |
| **Repository / Commit / Branch / Merge** | Project history / saved snapshot / separate line of work / combining lines of work |
| **Merge conflict** | Two branches changed the same lines differently |
| **Pull request** | A request to merge a branch, usually with review |
| **Test case** | An input, an expected result and an actual result |
| **Unit / Integration / System / Acceptance testing** | Levels of testing, from one piece to user approval |
| **Regression testing** | Re-running tests after a change |
| **Black-box / White-box testing** | Testing without / with knowledge of the code's structure |
| **Boundary value analysis** | Testing at and beside the edges of valid ranges |
| **Off-by-one error** | A mistake at a boundary, such as `<` instead of `<=` |
| **Code review** | Teammates read changes before they are merged |
| **Refactoring** | Improving code structure without changing behaviour |
| **Continuous integration (CI)** | Automatically building and testing every change |
| **Deployment / Rollback** | Releasing software / returning to the previous version |
| **Maintenance (corrective, adaptive, perfective, preventive)** | Fixing / adapting / improving / preventing future trouble |
| **Technical debt** | Future work caused by shortcuts taken now |
| **Risk exposure** | Probability × impact |
| **Scope creep** | Requirements growing without matching time or budget |

---

## Scope Note and Honest Gaps

**Covered (core):** everything above.
**Not covered in this version (optional extensions):**
- Detailed UML modelling and other diagram notations
- Security engineering in depth, and DevOps tooling beyond the idea of CI/CD
- Formal methods and software metrics
- Cost estimation techniques beyond story points and velocity
- Legal and contract aspects (briefly touched on in Modules 10 and 15 only)

Duplication with Module 10 (errors, versions, licences), Module 11 (writing code) and Module 12 (algorithms) must be checked against the teammates' work. These gaps and the next steps are recorded in the [Content Status and Mapping](../15_content-status-and-mapping.md) file.

**Where to practise:** [Learner Activities](../Learner%20Activity/15_learner-activities.md) (with answers) and the [Test Bank](../Test%20bank%20Question_Answer/15_test-bank.md).

**References:** see [References and AI Usage](../References%20and%20AI%20Usage/15_references-and-ai-usage.md). All diagrams (Figures 1 to 5) are original drawings made for this module.
