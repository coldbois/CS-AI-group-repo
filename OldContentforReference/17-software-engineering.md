# Section 14 — Software Engineering

Software engineering is the organised process of planning, building, testing, and maintaining software. The aim is to make programs that work well and are practical to change later. It is a bit like building a house: find out what is needed, make a plan, build it, inspect it, and fix problems as they appear.

## The software development life cycle

The software development life cycle (SDLC) is often described in five stages:

1. **Requirements:** Work out what users need and write it down. A banking app might need secure sign-in and quick transactions.
2. **Design:** Plan how the system will fit together. The app might have separate login, payment, and dashboard parts. Diagrams can show how components and data connect.
3. **Development:** Write the code, follow shared conventions, and use tools such as Git to track changes.
4. **Testing:** Check that the pieces work individually and that the whole system works together.
5. **Maintenance:** Fix bugs, improve security, adapt to changes, and add features after release.

Real teams often revisit these stages instead of doing them exactly once. Maintenance can be **corrective** (fixing bugs), **adaptive** (adjusting to a changed environment), **perfective** (adding or improving features), or **preventive** (reducing future problems).

## Why the process matters

The source uses the launch problems of HealthCare.gov in 2013 as an example of how unclear requirements, planning issues, deadlines, and limited testing can hurt a large project. It also mentions the 1999 Mars Climate Orbiter loss, where a mismatch between metric and imperial units contributed to the failure. These examples show why teams need clear agreements and tests across different parts of a system. Regular software updates are another everyday example of maintenance.

## Different development models

**Waterfall** moves through stages in a fixed order. It is easy to understand, but changing direction late can be difficult.

**Agile** works in short cycles, often called sprints. Each cycle aims to deliver a small working improvement and collect feedback. Agile still benefits from good documentation; it does not mean “no planning.”

**Spiral** repeats planning, risk analysis, development, and review. It pays special attention to risks, but it can be more complicated to manage.

**DevOps** encourages development and operations teams to work together, often using automation to test and release changes more frequently.

## Four useful principles

- **Modularity:** Split a program into smaller pieces that are easier to work on separately.
- **Reusability:** Reuse code or services instead of building the same thing repeatedly.
- **Scalability:** Plan for more users or data as the system grows.
- **Maintainability:** Keep the software understandable enough to fix and update later.

Software engineering is not just about getting the first version working. It is about making software that can be checked, changed, and supported over time.
