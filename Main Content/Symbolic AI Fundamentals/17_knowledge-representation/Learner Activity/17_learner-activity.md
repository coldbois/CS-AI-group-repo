# Try it: Sticky-Note Knowledge Graph (3.2)

**Time:** 20 min · **Group:** pairs · **You need:** sticky notes, a big sheet of paper, pens · Study Guide pp. 121–122

**Goal:** turn sentences into triples and a graph Dandroid can follow, then pick the best representation for different jobs.

## Prepare

The facts:

- Kai is a student.
- Kai studies Mathematics.
- Kai attends North College.
- North College is located in Beijing.

## Steps

1. List every **entity** (thing). Write each on its own sticky note.
2. Stick the notes on the sheet and draw a **labelled arrow** for each relationship.
3. Write each fact as a triple: *(subject, predicate, object)*.
4. Ask your partner: **"Which city is Kai's college in?"** They may answer *only* by following arrows.
5. **Bonus:** which representation suits (a) course prerequisites, (b) laptop specs, (c) a university's shared vocabulary?

## Record

- Your 4 triples.
- The path of arrows you followed to answer the question.

## Reflect

- Why is putting names next to each other not enough?
- What could go wrong if two people use different labels for the same link (e.g. "attends" vs "goes_to")?

## Check it: expected results

- **Entities:** Kai, Student, Mathematics, North College, Beijing.
- **Triples:**
  - (Kai, type, Student)
  - (Kai, studies, Mathematics)
  - (Kai, attends, North_College)
  - (North_College, located_in, Beijing)
- **Path:** Kai → attends → North College → located_in → **Beijing**.
- **Bonus:** (a) IF-THEN rules or logic, (b) a frame, (c) an ontology.
- Names next to each other don't say *how* they are related. The labelled arrow is the knowledge.
- Different labels for the same idea confuse the system: a question about "attends" won't find a "goes_to" arrow. That's why ontologies agree on a shared vocabulary.

This is the same structure as Mina's graph in Figure 3.2b and Test Bank question M18.
