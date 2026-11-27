# Glossary

The same definitions as the Study Guide glossary (pp. 165–167), with a few extra terms used in this module. "See" gives the topic where the term is explained.

## Chapter 1: Operating Systems

| Term | Meaning | See |
| --- | --- | --- |
| Operating system (OS) | Software that manages the hardware and shares it between programs | 1.1 |
| Kernel | The core of the OS, with full control of the hardware | 1.1 |
| User mode / kernel mode | Limited mode for apps / full-power mode for the kernel | 1.1 |
| System call | A program's request for a service from the kernel | 1.1 |
| UEFI / BIOS | Firmware that starts first and checks the hardware (BIOS is the older name) | 1.2 |
| POST | Power-On Self-Test: the hardware check at start-up | 1.2 |
| Bootloader | Small program that loads the OS kernel into memory | 1.2 |
| Process | A program that is running | 1.3 |
| Thread | A smaller unit of work inside a process | 1.3 |
| Scheduler | The OS part that picks which process runs next | 1.3 |
| Time slice | The short turn each process gets in Round Robin | 1.3 |
| Context switch | Saving one process's place and loading the next one | 1.3 |
| Deadlock | Processes stuck waiting for each other's resources | 1.3 |
| RAM | Fast working memory that is cleared when the power goes off | 1.4 |
| Virtual memory | Private addresses for each program, mapped to RAM or disk | 1.4 |
| Page / frame | An equal-sized block of a program's memory / the space in RAM that holds one | 1.4 |
| Page fault | A needed page isn't in RAM yet, so the OS loads it | 1.4 |
| Swap / thrashing | Moving pages to the drive / spending more time swapping than working | 1.4 |
| Device driver | Software that lets the OS control a device | 1.5 |
| Interrupt | A signal that tells the CPU something needs attention | 1.5 |
| DMA | Direct memory access: a device copies data straight into RAM | 1.5 |
| Buffer / cache | A waiting area for data on its way / a fast copy of data used again | 1.5 |
| File system | How the OS organises and finds files on storage | 1.6 |
| Path | The address of a file or folder | 1.6 |
| CIA triad | Confidentiality, integrity, availability | 1.7 |
| Authentication | Checking who you are | 1.7 |
| Authorization | Checking what you are allowed to do | 1.7 |
| Least privilege | Give only the permissions that are needed | 1.7 |
| Phishing | A fake message that tries to trick you into giving away a password or money | 1.7 |
| Ransomware | Malware that locks or encrypts your files and asks for money to unlock them | 1.7 |
| Variable | A named box that stores a value | 1.8 |

## Chapter 2: Software

| Term | Meaning | See |
| --- | --- | --- |
| Policy rule | A fixed OS decision rule, e.g. a permission check; not AI | 2.1 |
| Software | Instructions that tell hardware what to do | 2.2 |
| Source code / machine code | Human-readable program instructions / the 0s and 1s the CPU runs | 2.2 |
| Compiler / interpreter | Translates a whole program first / line by line | 2.2 |
| Open source | Software whose code anyone can read and change | 2.2 |
| Syntax / runtime / logic error | Breaks the language rules / crashes while running / runs but gives a wrong answer | 2.3 |
| Function | A named, reusable block of code | 2.3 |
| Edge case | A tricky input at the boundary of a rule, like the year 1900 | 2.3 |
| Algorithm | A finite list of clear steps that solves a problem | 2.4 |
| Binary search | Finding an item in a sorted list by halving | 2.4 |
| Big-O | How the amount of work grows as the input grows | 2.4 |
| Recursion | Solving a problem by solving smaller copies of it; needs a base case | 2.4 |
| Data structure | A way to organise data so operations are efficient | 2.5 |
| Stack / queue | LIFO pile / FIFO line | 2.5 |
| Hash table | Key → value store with very fast lookup | 2.5 |
| Database / DBMS | Organised, lasting data / the software that manages it | 2.6 |
| Primary / foreign key | Unique row ID / a link to another table's key | 2.6 |
| SQL | Language for querying relational databases | 2.6 |
| Transaction | Steps that happen all together or not at all | 2.6 |
| SDLC | Requirements → design → code → test → deploy → maintain | 2.7 |
| Agile / sprint | Building in short cycles with feedback / one such cycle (1–4 weeks) | 2.7 |
| Git: commit / branch / merge | Saved snapshot / separate line of work / combine work | 2.7 |
| Backlog / retrospective | The to-do list of features for a project / the meeting after a sprint where the team talks about what to improve | 2.7 |

## Chapter 3: Symbolic AI

| Term | Meaning | See |
| --- | --- | --- |
| Symbolic AI | AI that reasons with human-readable symbols and rules | 3.1 |
| Fact / rule | Something stored as true / IF condition THEN conclusion | 3.1 |
| Knowledge base | The stored facts and rules | 3.1 |
| Inference engine | Applies rules to facts to reach conclusions | 3.1 |
| Machine learning | AI that learns patterns from many examples | 3.1 |
| Triple / knowledge graph | Subject–predicate–object link / a network of them | 3.2 |
| Frame | A form with slots and values describing an object | 3.2 |
| Ontology | A shared, formal vocabulary of concepts and relations | 3.2 |
| Deduction / induction / abduction | Certain conclusion / likely pattern / best-guess explanation | 3.3 |
| Modus ponens | P → Q and P, so Q (a valid pattern) | 3.3 |
| Affirming the consequent | P → Q and Q, so P? (an invalid pattern) | 3.3 |
| Forward / backward chaining | Facts → conclusions / goal → needed facts | 3.3 |
| Working memory | The facts about the current case | 3.3 |
| Explanation facility | The part of an expert system that answers WHY and HOW | 3.3 |
| Expert system | A program that applies expert rules in a narrow area | 3.3 |
| State / action / goal test | A situation / a move / how you know you're done | 3.4 |
| BFS / DFS | Search level by level with a queue / deep first with a stack | 3.4 |
| Heuristic | An estimate that guides search | 3.4 |
| A* search | Expands the lowest f(n) = g(n) + h(n) | 3.4 |
| STRIPS | Actions described by preconditions, add and delete lists | 3.4 |
| CSP | Constraint satisfaction problem: find values that break no rules | 3.4 |
| Brittleness | Failing badly on cases the rules didn't expect | 3.5 |
| Knowledge bottleneck | Turning experts' know-how into rules is slow and costly | 3.5 |
| Prolog | A logic programming language: describe facts and rules, then ask | 3.6 |
| Neuro-symbolic AI | Combining neural learning with symbolic reasoning | 3.6 |

Back to [Start Here](00_Start_Here.md)
