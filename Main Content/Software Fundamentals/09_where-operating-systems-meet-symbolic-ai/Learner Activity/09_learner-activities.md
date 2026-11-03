# Module 09 Learner Activities: Operating Systems Meet Symbolic AI

Back to: [Main Theory](../Main%20Theory/09_main-theory.md) · [Test Bank](../Test%20bank%20Question_Answer/09_test-bank.md)

## How to use these activities

- Read the matching section of the Main Theory first, then **try each activity before looking at the answers**. The **Answer Key** is at the end of this file.
- Each activity gives you all the information you need. You do not need to look anything up.
- Activities mix different skills: ordering steps, predicting outcomes, calculating, finding errors, comparing approaches, and designing.

| # | Activity | Skill practised | Main Theory section | Outcome |
|---|---|---|---|---|
| 1 | Order the steps of saving a file | Tracing a process | 5 | LO2 |
| 2 | Predict process state changes; find the error | Predicting, error finding | 6 | LO3 |
| 3 | FCFS vs Round Robin | Calculating, comparing, explaining | 7 | LO4 |
| 4 | Translate addresses; predict page faults | Calculating, predicting | 8 | LO5 |
| 5 | Decode file permissions | Applying rules | 9 | LO6 |
| 6 | Write a rule; trace forward and backward chaining | Representing, tracing | 11, 12 | LO8 |
| 7 | Find and fix flawed rules | Error finding | 12, 13 | LO8, LO9 |
| 8 | Choose the right tool and justify | Comparing, explaining a decision | 10, 14 | LO7, LO10 |
| 9 | Design a mini expert system | Applying, creating | 11 to 14 | LO8, LO9, LO10 |

---

## Activity 1: Order the steps (tracing a system call)

**Goal:** Trace what happens when a text editor saves a file.
**Time:** 10 minutes.

**Information:** Seven steps are listed below **in the wrong order**.

- (a) The kernel checks the request and whether the program is allowed to write to that location.
- (b) The user clicks **Save** in the text editor.
- (c) The CPU switches back to user mode and the editor carries on.
- (d) The kernel asks the disk's device driver to store the data.
- (e) The editor makes a system call asking the OS to write the data to a file.
- (f) The CPU switches to kernel mode.
- (g) The device driver reports that the data was written and the kernel returns "success" to the editor.

**Task**
1. Write the letters in the correct order.
2. Which steps happen in **user mode** and which in **kernel mode**?
3. *Explain:* Why can't the editor talk to the disk directly?

*(Simplification: real operating systems often keep written data in a memory cache first and write it to disk a little later. We ignore that here.)*

---

## Activity 2: Process states (predict and find the error)

**Goal:** Use the process state diagram ([Figure 2](../Diagrams%20and%20Pictures/09_fig2_process-states.svg)) to predict changes.
**Time:** 10 minutes.

**Part (a): Predict.** For each event, write the state change (for example, "Ready → Running").

1. A newly created process finishes being set up.
2. The scheduler picks a process from the Ready queue.
3. A music player is Running and its time slice ends.
4. A download manager is Running and must wait for network data.
5. The network data arrives for the download manager.
6. A Running process reaches the end of its instructions.

**Part (b): Which of these changes are NOT allowed in the diagram?** Say why for each one that is not allowed.

- (i) Waiting → Running
- (ii) Ready → Waiting
- (iii) Running → Terminated
- (iv) New → Running

**Part (c): Find the error.** A student says: *"My computer has one CPU core and is showing four processes in the Running state at the same time."* What is wrong with this statement?

---

## Activity 3: FCFS vs Round Robin

**Goal:** Calculate and compare two scheduling methods, then judge a claim.
**Time:** 20 minutes.

**Information:** Three processes arrive at time 0 in the order P1, P2, P3. Burst times: **P1 = 6, P2 = 3, P3 = 1**. Round Robin uses a **time slice of 2**. Ignore the cost of switching. (Use the formulas in Section 7.2.)

**Task**
- **(a)** Draw the timeline for FCFS and for Round Robin.
- **(b)** For each method, calculate the **average waiting time** and the **average response time**.
- **(c)** A student says: *"Round Robin is always better than FCFS because its average waiting time was lower."* Test this claim using three processes that each need **4** time units (same arrival, same time slice of 2). Compare **average turnaround time** for FCFS and RR.
- **(d)** *Explain a decision:* A computer is used mainly for typing and web browsing. Which would you prefer, FCFS or RR, and why?

---

## Activity 4: Address translation and page faults

**Goal:** Translate virtual addresses and predict what the OS does.
**Time:** 15 minutes.

**Information:** Page size = **4096 bytes**. The process has **pages 0 to 3** only. Page table:

| Page | Location |
|---|---|
| 0 | Frame 5 |
| 1 | Frame 2 |
| 2 | Frame 7 |
| 3 | Not in RAM (stored on disk) |

Formulas: page = address ÷ 4096 (whole part); offset = remainder; physical address = frame × 4096 + offset.

**Task**
- **(a)** Translate these virtual addresses, or state what happens: **100**, **5000**, **12300**, **20000**.
- **(b)** For the address that causes a *legal* page fault, suppose the OS loads that page into **frame 9**. What is the physical address after that?
- **(c)** *Explain:* Is a page fault always an error? Give a reason for each address in (a) that does not translate immediately.

---

## Activity 5: Decode file permissions

**Goal:** Apply the "first matching class" rule.
**Time:** 10 minutes.

**Information:** Users: **alex** (owner of all files below, member of group staff), **sam** (member of group staff, not an owner), **kim** (not in staff, not an owner).

| File | Permissions | Owner | Group |
|---|---|---|---|
| f1 | `-rw-r-----` | alex | staff |
| f2 | `-rwxr-xr-x` | alex | staff |
| f3 | `drwx------` | alex | staff |
| f4 | `----rw----` | **sam** | staff |

**Task**
1. Who can **read** f1? Who can **write** f1?
2. Who can **run** f2?
3. What does the first letter of f3 mean? Who can enter or use it?
4. **Challenge:** sam owns f4 and is also in the group staff, which has `rw`. Can sam read f4? Explain, using the "first matching class" rule.

---

## Activity 6: Write a rule, then trace forward and backward chaining

**Goal:** Represent knowledge and reason with it.
**Time:** 25 minutes.

**Information (rule base: "Can this user open the file?")**

| Rule | Definition |
|---|---|
| R1 | IF `user_cannot_open_file` AND `file_exists` THEN `suspect_permission_problem` |
| R2 | IF `suspect_permission_problem` AND `user_not_owner` THEN `check_group_permissions` |
| R3 | IF `suspect_permission_problem` AND `user_is_owner` THEN `check_owner_permission_bits` |
| R4 | IF `check_group_permissions` AND `user_in_group` AND `group_has_no_read` THEN `recommend_add_group_read` |

**Known facts:** `user_cannot_open_file`, `file_exists`, `user_not_owner`, `user_in_group`, `group_has_no_read`

**Task**
- **(a) Write a rule.** Translate into IF-THEN form: *"If the user is the owner and the owner's permission bits include write, then the user can edit the file."* (Use names like `user_is_owner`, `owner_has_write`, `user_can_edit`.)
- **(b) Forward chaining.** Trace the reasoning in a table (cycle, rules that fire, new fact added). Which final recommendation is reached?
- **(c)** Which rule(s) did **not** fire, and why?
- **(d) Backward chaining.** Take the goal `check_owner_permission_bits`. Show the sub-goals. Can the goal be proven from the known facts?

---

## Activity 7: Find and fix flawed rules

**Goal:** Spot problems in a rule base.
**Time:** 15 minutes.

**Information:** A student wrote these rules for a "slow computer" expert system.

| Rule | Definition |
|---|---|
| X1 | IF `process_uses_high_cpu` THEN `end_that_process` |
| X2 | IF `memory_full` THEN `suspect_thrashing` |
| X3 | IF `suspect_thrashing` THEN `memory_full` |

**Task**
1. Rule X1 would end a video export you started on purpose, or a virus scan. What is wrong, and how would you improve it? Write an improved version.
2. Rule X2 diagnoses thrashing every time memory is full. Using Section 8.5, what condition is missing? Rewrite it.
3. Look at X2 and X3 together. What problem do they cause for the inference engine's reasoning, and why is X3 not useful knowledge?
4. Which limitation of expert systems (Section 13.4) does problem 1 illustrate?

---

## Activity 8: Choose the right tool and justify

**Goal:** Decide between three approaches and explain your reasoning.
**Time:** 15 minutes.

**Information:** Three approaches:
- **(OS)** A fixed OS mechanism or policy (for example, a permission check or a scheduling algorithm)
- **(SYM)** Symbolic AI rule-based reasoning with an explanation facility
- **(ML)** Machine learning from examples

**Task:** For each task, choose the best approach and give **one reason**. There can be more than one defensible answer if your reason is good.

1. Decide whether user *sam* may open `report.txt`.
2. Recognise handwritten digits in thousands of photographs.
3. Help a technician diagnose why a printer fails, following a documented troubleshooting procedure, and show *why* each suggestion is made.
4. Choose which of five Ready processes gets the CPU next.

---

## Activity 9: Design a mini expert system

**Goal:** Apply everything: build and test a small rule base.
**Time:** 30 minutes.

**Scenario:** Build a "Why does my phone's battery drain quickly?" expert system.

**Facts the user can report:** `screen_brightness_high`, `many_background_apps`, `battery_older_than_2_years`, `phone_hot`

**Task**
1. Write **five IF-THEN rules** using these facts (you may add intermediate conclusions such as `suspect_background_processes`). At least **one rule must chain** (its conclusion is used by another rule), and at least **one must use AND**.
2. **Test case 1:** facts `many_background_apps` and `screen_brightness_high`. Use forward chaining. What does your system recommend?
3. **Test case 2:** the only fact is `battery_older_than_2_years`. What does your system say?
4. Write **two sentences** explaining one weakness your test cases reveal, and how you would fix it.
5. Add a sentence linking your system to the OS: which *OS concept* from Part A does the rule about background apps relate to?

---

# Answer Key

## Answer 1
1. **b → e → f → a → d → g → c**
2. **User mode:** (b), (e) and (c). **Kernel mode:** (f), (a), (d) and (g) (the kernel runs these steps after the switch in (f) and until the return in (c)).
3. Direct access would let any program corrupt files or other programs' data. The OS keeps hardware control in kernel mode for protection, and the editor must go through a system call so the kernel can check permission first.

## Answer 2
**(a)**
1. New → Ready
2. Ready → Running
3. Running → Ready
4. Running → Waiting
5. Waiting → Ready
6. Running → Terminated

**(b)** Not allowed: **(i)** Waiting → Running (a process whose I/O has finished must first become Ready, and the scheduler decides who runs), **(ii)** Ready → Waiting (a Ready process is not executing, so it cannot start waiting for an I/O request), **(iv)** New → Running (a new process becomes Ready first). **(iii)** Running → Terminated **is** allowed.

**(c)** At most **one** process can be Running per CPU core. The others must be Ready or Waiting. (A four-core CPU could have four Running.)

## Answer 3
**(a) Timelines**

FCFS: P1 runs 0 to 6, P2 runs 6 to 9, P3 runs 9 to 10.

Round Robin (slice 2):

| Time | 0 to 2 | 2 to 4 | 4 to 5 | 5 to 7 | 7 to 8 | 8 to 10 |
|---|---|---|---|---|---|---|
| Running | P1 | P2 | P3 | P1 | P2 | P1 |
| Left to do | P1: 4 | P2: 1 | P3: 0 | P1: 2 | P2: 0 | P1: 0 |

**(b)**

| | FCFS | Round Robin |
|---|---|---|
| Completion | P1 = 6, P2 = 9, P3 = 10 | P3 = 5, P2 = 8, P1 = 10 |
| Waiting (completion − burst) | 0, 6, 9 → average 15 ÷ 3 = **5.0** | P1 = 4, P2 = 5, P3 = 4 → average 13 ÷ 3 ≈ **4.33** |
| Response (first start) | 0, 6, 9 → average 15 ÷ 3 = **5.0** | 0, 2, 4 → average 6 ÷ 3 = **2.0** |

RR has a slightly lower average waiting time and a much lower average response time.

**(c)** Three processes of 4 units each, slice 2.
- FCFS: completions at 4, 8, 12 → average turnaround = 24 ÷ 3 = **8.0**.
- RR: P1 0 to 2, P2 2 to 4, P3 4 to 6, P1 6 to 8 (done at 8), P2 8 to 10 (done at 10), P3 10 to 12 (done at 12) → completions 8, 10, 12 → average turnaround = 30 ÷ 3 = **10.0**.

RR is **worse** here (and it would also pay extra switching costs), so the claim "RR is always better" is **false**.

**(d)** Model answer: Prefer **Round Robin**. With interactive work, low response time matters so that typing and clicks feel instant, and RR gives every process regular turns. FCFS could freeze the browser behind a long background job. *(Any reasoned answer that refers to response time and responsiveness is acceptable.)*

## Answer 4
**(a)**
- **100:** page 0, offset 100 → frame 5 → 5 × 4096 + 100 = 20480 + 100 = **20580**.
- **5000:** page 1 (5000 − 4096 = 904), offset 904 → frame 2 → 2 × 4096 + 904 = 8192 + 904 = **9096**.
- **12300:** page 3 (3 × 4096 = 12288), offset 12 → page 3 is not in RAM → **page fault** (legal address; the OS loads the page).
- **20000:** page 4 (4 × 4096 = 16384), offset 3616 → page 4 does not exist for this process → **illegal access**; the OS stops the process (segmentation fault).

**(b)** Frame 9: 9 × 4096 + 12 = 36864 + 12 = **36876**.

**(c)** No. The page fault at 12300 is **normal**: the page exists and the OS simply fetches it from disk. The access at 20000 is a different case: it is an **error** because the process has no page 4, so the OS ends the process.

## Answer 5
1. **Read f1:** alex (owner `rw-`) and sam (group `r--`). kim is in "others" (`---`) → no. **Write f1:** only alex.
2. **Run f2:** all three. Owner `rwx`, group `r-x`, others `r-x` all include x.
3. `d` means **directory**. Owner `rwx` only, so only **alex** can enter and use it.
4. **No, sam cannot read f4.** sam is the owner, so the OS applies only the **owner** class, which is `---` (the first three characters after the type). The group's `rw-` is never consulted. (As the owner, sam could change the permissions with `chmod`, but cannot read the file until then.)

## Answer 6
**(a)**
```
IF  user_is_owner AND owner_has_write
THEN user_can_edit
```

**(b)**

| Cycle | Rule(s) that fire | New fact added |
|---|---|---|
| 1 | R1 (`user_cannot_open_file` and `file_exists` are true) | `suspect_permission_problem` |
| 2 | R2 (`suspect_permission_problem` and `user_not_owner` true) | `check_group_permissions` |
| 3 | R4 (`check_group_permissions`, `user_in_group`, `group_has_no_read` all true) | `recommend_add_group_read` |
| 4 | Nothing new | Stop |

**Final recommendation: `recommend_add_group_read`.**

**(c)** **R3** did not fire because it needs `user_is_owner`, which is not known (`user_not_owner` is the known fact).

**(d)** Goal `check_owner_permission_bits` → concluded by **R3** → sub-goals `suspect_permission_problem` and `user_is_owner`.
- `suspect_permission_problem` can be proven by R1 (its facts are known) ✔
- `user_is_owner` is not a known fact and no rule concludes it ✘

So the goal **cannot** be proven from the known facts. (An interactive system could ask the user; but in this case the known fact says the user is *not* the owner.)

## Answer 7
1. **Problem:** the rule is too broad. High CPU use is normal for useful work. The system lacks the context to know whether the process is a problem. **Improved rule:** `IF process_uses_high_cpu AND process_not_responding AND NOT system_process THEN recommend_end_that_process`. (Even better: *recommend*, and let the user confirm.)
2. **Missing condition:** `disk_activity_high`. Memory can be full without heavy paging. Rewrite: `IF memory_full AND disk_activity_high THEN suspect_thrashing`.
3. X2 and X3 form a **circle**: each one's conclusion is the other's condition. No new knowledge is gained and the reasoning can go round and round, and X3 is not even true (thrashing is not the only reason memory is full). A conclusion must add *new*, justified information.
4. **Brittleness** (and the related difficulty of capturing context). The rule works only in the situation its writer imagined.

## Answer 8
1. **OS.** A fixed permission check against owner, group and mode is exact and fast; no learning or flexible reasoning is needed.
2. **ML.** Handwriting varies enormously; writing rules by hand would be impractical, but many labelled examples let a program learn patterns.
3. **SYM.** The procedure is documented knowledge that can be written as rules, and the rule trace gives the "why". *(A defensible alternative: a plain flowchart or an OS-independent help guide.)*
4. **OS.** Choosing the next process is the scheduler's job, done by a fixed scheduling algorithm. Remember: IF-THEN *shape* alone does not make it AI.

## Answer 9 (model answer and marking guide)
**Model rules**

| Rule | Definition |
|---|---|
| R1 | IF `many_background_apps` THEN `suspect_background_processes` |
| R2 | IF `suspect_background_processes` THEN `recommend_close_or_restrict_background_apps` |
| R3 | IF `screen_brightness_high` THEN `recommend_lower_brightness` |
| R4 | IF `battery_older_than_2_years` AND `phone_hot` THEN `suspect_worn_battery` |
| R5 | IF `suspect_worn_battery` THEN `recommend_check_battery_health_or_replace` |

- **Chaining:** R1 → R2 and R4 → R5. **AND:** R4.
- **Test case 1:** R1 and R3 are ready first. R1 adds `suspect_background_processes`, which lets R2 fire and add `recommend_close_or_restrict_background_apps`. R3 adds `recommend_lower_brightness`. (The order in which R2 and R3 fire depends on conflict resolution, but the final facts are the same.) Result: two recommendations: lower the brightness, and close or restrict background apps.
- **Test case 2:** R4 needs both conditions, and `phone_hot` is not known, so it does not fire. **No rule fires and the system gives no advice.**
- **Weakness and fix:** The system says nothing when the facts do not match any rule (incompleteness, a form of brittleness). Fix: ask the user follow-up questions, as backward chaining would, or add a rule such as `IF battery_older_than_2_years THEN recommend_check_battery_health`, and add a default message when no rule fires.
- **OS link:** Background apps are **processes** sharing the CPU and memory (Sections 6 and 7); many processes in the Ready or Running state use CPU time and power.

**Marking guide (self-check):** ☐ Five rules written in IF-THEN form ☐ At least one chain ☐ At least one AND ☐ Test case 1 traced step by step ☐ Test case 2 result matches your own rules ☐ Weakness identified and a fix suggested ☐ OS concept named correctly.

---

*Answers have been calculated twice. A teammate who is not the author should re-check them and record the result in the [Teammate Review](../Teammate_review/09_teammate-review.md).*
