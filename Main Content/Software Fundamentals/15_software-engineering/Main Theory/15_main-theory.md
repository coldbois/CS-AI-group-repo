# 2.7 Software Engineering

![Dandroid frustrated that nothing works together](../../../assets/dandroid/dandroid-angry.png)

**Chapter 2 · Dandroid's Instructions** · Study Guide pp. 99–105 · Slide 31 · Test Bank T16, M16, O6

> **Mission.** Dandroid's team of 5 students has 4 weeks to build an app. Everyone codes their own way... and on Friday nothing works together. How do professionals avoid this?

**You will learn to**

- describe the software development life cycle
- compare Waterfall and Agile
- explain testing levels and version control

**Key words:** SDLC, requirements, Agile, sprint, unit test, Git, commit, branch

---

## Programming vs software engineering

Programming is cooking for yourself. **Software engineering** is running a restaurant kitchen: a plan, a team, quality checks and a process that works every day, even when people are ill or the menu changes.

## The software development life cycle (SDLC)

![Figure 2.7a](../Diagrams%20and%20Pictures/2-7_sdlc.png)

*Figure 2.7a. The software development life cycle (Study Guide p. 100; slide 31 shows the same six stages).*

| Stage | Question it answers |
| --- | --- |
| 1. Requirements | What do users really need? |
| 2. Design | How will it be structured, and what will the screens look like? |
| 3. Implementation | Write the code. |
| 4. Testing | Does it work? Where are the bugs? |
| 5. Deployment | Release it to users. |
| 6. Maintenance | Fix problems and add features over time. |

Maintenance usually lasts longest: most software spends years being fixed and improved after its first release. New requests from users then start the cycle again.

## Waterfall vs Agile

![Figure 2.7b](../Diagrams%20and%20Pictures/2-7_waterfall-vs-agile.png)

*Figure 2.7b. Waterfall vs Agile (Study Guide p. 101).*

| | **Waterfall** | **Agile** |
| --- | --- | --- |
| How | finish each stage completely before the next | build in short cycles called **sprints** (1–4 weeks) |
| Planning | plan everything up front | plan a little, adjust after each sprint |
| Users see it | only at the end | after every sprint, so feedback comes early |
| Good when | requirements are clear and fixed | needs change or are unclear |
| Risk | you find a big mistake too late | needs a customer who is willing to give regular feedback |

Agile in one line: "Build a little, show it, learn, improve, repeat."

> **Dandroid's tip.** Iterative and incremental models sit in between: build working versions early and add more each round.

## Testing and teamwork tools

![Figure 2.7c](../Diagrams%20and%20Pictures/2-7_testing-tools.png)

*Figure 2.7c. Testing and teamwork tools (Study Guide p. 102).*

**Levels of testing**

- **Unit test:** test one small piece on its own, for example `is_leap()` from [2.3](../../11_computer-programming/Main%20Theory/11_main-theory.md) with the years 2000, 1900, 2024 and 2023.
- **Integration test:** do the pieces work together?
- **System and acceptance test:** test the whole app; users confirm it meets their needs.
- **Regression test:** re-test after every change, so nothing that used to work breaks.

**Version control with Git.** Git tracks every change to a project, so a team can work on the same files without overwriting each other. GitHub hosts Git projects online. The words you need:

| Word | Meaning |
| --- | --- |
| repository | the project store, with its full history |
| commit | a saved snapshot of the files, with a message saying what changed |
| branch | a separate line of work, so you can try something without breaking the main version |
| merge | combine a branch back into the main version |

This module itself was built in a Git repository: each topic file has a history of commits that shows how it changed.

**Good design habits:** modularity (small parts), abstraction (hide the details), DRY (don't repeat yourself), separation of concerns, and documentation. **Team roles** often include a product owner, developers, a tester, a designer and a project manager.

## Try it

**Paper Airplane Sprints** (30 min, teams of 4–5): build paper planes for a "customer" twice, once Waterfall and once Agile, and see what happens when the customer changes their mind. Instructions and answers: [15_learner-activity.md](../Learner%20Activity/15_learner-activity.md).

## Going further (optional)

- **Scrum** is the most common Agile method. A *product backlog* lists everything the product needs. Each sprint starts with *sprint planning*, has a short *daily scrum* meeting, and ends with a *sprint review* (show the work) and a *retrospective* (improve the way the team works).
- **Pull requests.** On GitHub a developer pushes a branch and opens a pull request, so teammates can review the changes before they are merged into main.

## Check yourself

1. Put in order: testing, requirements, deployment, design.
2. What is a sprint?
3. Which kind of test re-checks old features after a change?

**Answers (try first, then peek)**
1. Requirements → design → testing → deployment.
2. A short Agile cycle (1–4 weeks) that ends with something working to show.
3. Regression testing.


More questions: [15_test-bank.md](../Test%20bank%20Question_Answer/15_test-bank.md)

## Remember

- SDLC: requirements → design → code → test → deploy → maintain.
- Agile = small cycles + feedback; Waterfall = one big plan.
- Test at many levels; use Git so teams don't overwrite each other.

## Watch and explore

**Crash Course Computer Science #16: Software Engineering** (PBS, YouTube). Shows how big teams split work, test and use version control. Write down three tools or practices the video mentions. There is some jargon: pause and check the [Glossary](../../../Glossary.md).

## References

- Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson. Chapters 2–3 and 8.
- Beck, K. et al. (2001). *Manifesto for Agile Software Development*. https://agilemanifesto.org
- Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. Free online at https://git-scm.com/book

---

Previous: [2.6 Databases](../../14_Databases/Main%20Theory/14_main-theory.md) · Next: [Chapter 3: Symbolic AI](../../../Symbolic%20AI%20Fundamentals/README.md) · Up: [Chapter 2 overview](../../README.md)
