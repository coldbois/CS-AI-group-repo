# Module 09 References and AI Usage

Back to: [Main Theory](../Main%20Theory/09_main-theory.md)

---

## 1. References

> **Before submitting:** open or look up every reference below and confirm that it exists and supports the claim listed beside it. Add edition details, page or chapter numbers, and a DOI or URL where available. Record your check in the "Verified by" column.

| # | Reference | Used to support (Main Theory section) | Verified by |
|---|---|---|---|
| 1 | Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. | Processes and process states, PCB, CPU scheduling (FCFS, Round Robin, waiting and turnaround time), paging and page faults, thrashing (Sections 6, 7, 8) | [ ] |
| 2 | Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson. | Kernel, user and kernel mode, system calls, threads, virtual memory, file permissions (Sections 4, 5, 6, 8, 9) | [ ] |
| 3 | Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. | Definition of AI, knowledge-based agents, logic and rules, forward and backward chaining (Sections 10, 11, 12) | [ ] |
| 4 | Newell, A., & Simon, H. A. (1976). Computer science as empirical inquiry: Symbols and search. *Communications of the ACM, 19*(3), 113 to 126. | Physical symbol system hypothesis (Section 10.1) | [ ] |
| 5 | Haugeland, J. (1985). *Artificial Intelligence: The Very Idea*. MIT Press. | The term "GOFAI" (Section 10.1) | [ ] |
| 6 | Buchanan, B. G., & Shortliffe, E. H. (Eds.). (1984). *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*. Addison-Wesley. | MYCIN: rule-based diagnosis, certainty factors, research use (Section 13.2) | [ ] |
| 7 | McDermott, J. (1982). R1: A rule-based configurer of computer systems. *Artificial Intelligence, 19*(1), 39 to 88. | XCON/R1: configuring VAX computer orders with rules (Sections 13.2, 14.3) | [ ] |
| 8 | The Linux man-pages project. Manual pages for `chmod(1)` and `inode(7)`. https://man7.org/linux/man-pages/ | Read, write and execute bits; owner, group and others (Section 9) | [ ] |

**Claims that need a second look when you check sources**
- Section 13.2 says MYCIN used "several hundred rules" and was "never adopted for routine clinical use". Check the exact wording against reference 6 or a reliable history of expert systems.
- Section 13.2 says XCON "grew to thousands of rules". Check against reference 7 and later accounts.
- Section 14.4 says Lisp machines "faded commercially" as ordinary workstations and PCs improved. Find a source for the dates and cause (for example, a history of AI or computing) and add it here.
- Section 10.1 credits "GOFAI" to John Haugeland. Confirm in reference 5.

---

## 2. Attribution of Images and Borrowed Material

| Item | Source / attribution |
|---|---|
| Figures 1 to 5 (`09_fig1` to `09_fig5`, SVG) | **Original diagrams** created for this module. The *ideas* shown (OS layers, process states, expert system parts) are standard textbook concepts (see references 1, 2, 3); the drawings themselves were not copied. |
| Scheduling example (P1 = 8, P2 = 2, P3 = 1) and the practice data | Original numbers made for this module; the *methods* (FCFS, Round Robin) are standard (reference 1). |
| Rule bases ("slow computer", file permission, phone battery) | Original examples written for this module. |
| Analogies (restaurant manager, kitchen, recipe) | Original teaching analogies. |
| MYCIN and XCON descriptions | Summarised in our own words from references 6 and 7. |

---

## 3. AI Usage Record

> **This is a record to complete honestly.** The Shared Assignment Rules require significant AI use to be recorded in the project and personal logs, with verification, decisions and learning placed beside or below the relevant entry. Copy the entries below into your personal log, then complete every "[To be completed]" cell **yourself**.

### Entry 1: Drafting the Module 09 content

| Field | Record |
|---|---|
| **Date** | 2026-11-03 |
| **AI tool** | Claude (Anthropic) |
| **Who used it** | [Your name] |
| **What was asked** | To draft a beginner-friendly Study Guide section for Module 09 (operating systems and symbolic AI) following the Stage 2 Markdown V2.0 instructions, matching our repository folder structure. |
| **What the AI produced** | First drafts of: the Main Theory file, Learner Activities with answers, Test Bank with answers, five SVG diagrams, this references file, a teammate-review template and a content status file. |
| **Verification you did** | [To be completed. Examples: recomputed every calculation by hand (scheduling, address translation, forward and backward chaining); checked each reference exists and supports its claim; viewed all five figures in the rendered Markdown; compared the content with our course materials and agreed scope.] |
| **Errors, gaps or doubtful points found** | [To be completed] |
| **Decisions and changes you made** | [To be completed. Examples: what you rewrote in your own words, what you removed, what you added from the course materials.] |
| **What you learned** | [To be completed] |

### Entry 2: Teammate review (when it happens)

| Field | Record |
|---|---|
| **Date** | [To be completed] |
| **AI used?** | [Yes/No. If yes, describe.] |
| **Summary** | [Link to the completed [Teammate Review](../Teammate_review/09_teammate-review.md)] |

### Honest note on the draft's limits
The draft was written without access to our course materials, the agreed scope, or Stage 1 feedback. Those must be checked by a human before the content is submitted (see [Content Status and Mapping](../09_content-status-and-mapping.md)).
