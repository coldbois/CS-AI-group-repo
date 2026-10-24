# Section 14: Software Engineering

## 1. What is software engineering?

**Software engineering** is a systematic way to plan, design, build, test, release, and maintain software. The goal is to create software that works correctly, meets users' needs, can be maintained, and is worth the time and money spent developing it.

A useful comparison is building a house. Before construction, the builders need to understand what the family needs, make plans, build the structure, inspect it, and repair it when necessary. Software projects benefit from the same discipline. Skipping planning or testing can make problems more expensive to fix later.

One common framework for organizing this work is the **software development life cycle (SDLC)**. The source presents five main phases.

## 2. The five SDLC phases

| Phase | Main question | Typical activities | Example from the source |
|---|---|---|---|
| 1. Requirements analysis | What must the software do? | Collect users' needs and write them down clearly. | A banking app needs secure login, transactions processed within two seconds, and basic offline use. |
| 2. Design | How should we build it? | Divide the system into modules, plan data flow, and draw diagrams. | Plan a login module, payment module, and dashboard before building them. |
| 3. Development | How do we turn the design into working software? | Write code, follow coding standards, use version control such as Git, and run unit tests. | A hospital system may have separate Patient Management and Billing teams. |
| 4. Testing | Does it work as intended? | Test individual pieces, connections between pieces, and the complete system; find and fix problems before release. | Check that different teams' systems work together. |
| 5. Maintenance | How do we keep it useful and reliable? | Fix bugs, adapt to new environments, improve features, and reduce future problems. | Release regular security updates. |

### Phase 1: Requirements analysis

A **requirement** describes something the software must do or a condition it must meet. Requirements should be specific enough that the team and users can agree on what success means. For example, “the app must be fast” is vague; “a transaction should be processed within two seconds under the stated test conditions” is more measurable.

### Phase 2: Design

Design is the plan for how the software will be organized. A system may be split into **modules**, which are smaller parts responsible for particular jobs. Modules can make large projects easier to understand, test, and develop in parallel.

The source mentions **Unified Modeling Language (UML)** diagrams. These are standardized drawings that help people describe a software system. Examples include:

- **Use-case diagrams:** show how users or other systems interact with the software.
- **Class diagrams:** show classes, their data, and relationships between them.
- **Sequence diagrams:** show how interactions happen over time.

### Phase 3: Development

Developers implement the design by writing code. **Version control**, such as Git, tracks changes to files so a team can review work, compare versions, and coordinate contributions. A **unit test** checks one small part of the program, such as a function, in isolation.

### Phase 4: Testing

Testing helps determine whether the software behaves as expected and exposes defects before release.

- **Unit testing:** tests a small component on its own.
- **Integration testing:** tests whether components work correctly together.
- **System testing:** tests the complete system as a whole.

Testing cannot prove that a complex program has no possible defects, but it can uncover many important problems and reduce risk.

### Phase 5: Maintenance

Software usually continues to change after its first release. The source groups maintenance into four kinds:

| Kind | Meaning | Example |
|---|---|---|
| Corrective | Fix a defect that has already occurred. | Repair a crash caused by a bug. |
| Adaptive | Adjust software to a changed environment. | Update a program so it works with a new operating-system version. |
| Perfective | Add a feature or improve existing behavior. | Add message reactions to a messaging app. |
| Preventive | Make changes that lower the chance of future problems. | Refactor difficult code or improve monitoring before a failure occurs. |

**Maintainability** means how easily the software can be understood, repaired, and changed. It matters throughout the software's life, not only at the beginning.

## 3. Real-world cases in the source

- **HealthCare.gov (2013):** The source describes the U.S. healthcare website as experiencing serious launch problems and connects them to poor planning, unclear requirements, unrealistic deadlines, and limited testing. The lesson is that a weak requirements and preparation process can affect even a large project.
- **Mars Climate Orbiter (1999):** The source states that one team used metric units while another used imperial units, and that the spacecraft was lost, at a cost of about $125 million. The lesson is that interfaces between components must agree on assumptions and units, and integration testing matters.
- **Patch Tuesday:** Microsoft commonly releases scheduled updates for Windows and other products. Security fixes, bug fixes, and improvements are examples of maintenance.

These cases illustrate the source's central point: software failures may result not only from a mistake in one line of code, but also from unclear requirements, coordination failures, or inadequate testing.

## 4. Common SDLC models

An **SDLC model** is a way to organize the phases of software development. Different models suit different projects and constraints.

| Model | How it works | Strength | Limitation or note |
|---|---|---|---|
| Waterfall | Work proceeds through phases in a mostly fixed sequence. A phase is generally completed before the next begins. | Simple, orderly, and easy to describe. | Changing direction later can be difficult or costly. |
| Agile | Work is divided into short cycles, often called **sprints**. Each cycle produces a small working part that can be reviewed. | Frequent feedback and flexibility; often useful where needs change. | Agile does not eliminate the need for planning or documentation. It aims to keep feedback and working software frequent. |
| Spiral | Teams repeat cycles of planning, risk analysis, development, and review. | Risk is considered repeatedly, rather than only at the beginning. | Can be more complex to manage. |
| DevOps | Development and operations teams collaborate, using automation and frequent integration and deployment. | Can support faster, more frequent releases. | Requires appropriate tools, automation, teamwork, and operational practices. |

**Continuous integration (CI)** means frequently combining developers' changes and automatically checking whether they work together. **Continuous deployment/delivery** refers to automating the steps that prepare and release changes; the exact distinction between deployment and delivery depends on the team's process.

## 5. Core software-engineering principles

| Principle | Meaning | Example from the source |
|---|---|---|
| Modularity | Divide software into smaller parts with clear responsibilities. Teams can build and test some parts independently. | A product may separate inbox, chat, and calendar features. |
| Reusability | Use existing components where appropriate instead of rewriting the same functionality. This can save time and keep behavior consistent. | A sign-in service may be reused across different platforms. |
| Scalability | Design a system so it can handle growth in users, data, or workload. | A shopping service needs to handle unusually high traffic during major sales. |
| Maintainability | Keep the software understandable and practical to fix or update over time. | A widely maintained project such as Linux depends on code that contributors can understand and improve. |

## 6. Key takeaways

- Software engineering is the organized process of developing and maintaining software.
- Requirements describe what the system must do; design plans how to organize it; development builds it; testing checks it; maintenance keeps it useful.
- Testing includes unit, integration, and system testing.
- Waterfall follows a more fixed sequence, Agile works in short feedback cycles, Spiral repeatedly analyzes risk, and DevOps emphasizes collaboration and automation.
- Modularity, reusability, scalability, and maintainability help software remain manageable as it grows.
