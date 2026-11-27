# Try it: Battery Detective Expert System (3.3)

**Time:** 30 min · **Group:** groups of 3 · **You need:** paper and rule cards · Study Guide pp. 129–130 · Linked Test Bank question: O7

**Goal:** write, test and improve a small rule base, like a real knowledge engineer.

## Prepare

**Problem:** "Why does my phone battery drain quickly?"

Facts users can report: `screen_bright`, `many_background_apps`, `battery_old`, `phone_hot`.

## Steps

1. Write **5 IF-THEN rules** on cards. At least one must use **AND**, and one must **chain** (its THEN part feeds another rule's IF part).
2. **Test case 1:** facts `many_background_apps` + `screen_bright`. Forward-chain: what does your system advise?
3. **Test case 2:** the only fact is `battery_old`. What does it say?
4. Swap rule sets with another group and try to break theirs with a tricky case.
5. Write one improvement.

## Record

Trace test case 1:

| Cycle | Rule that fires | New fact added |
| --- | --- | --- |
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

## Reflect

- What did your system say when no rule matched?
- Which limitation of expert systems did the other group expose?

## Check it: a model answer

Your rules will be different. Here is one good rule set (the same as the Study Guide model answer):

| Rule | IF | THEN |
| --- | --- | --- |
| R1 | many_background_apps | suspect_background |
| R2 | suspect_background | advise_close_apps |
| R3 | screen_bright | advise_dim_screen |
| R4 | battery_old AND phone_hot | suspect_worn_battery |
| R5 | suspect_worn_battery | advise_check_battery |

R4 uses AND; R1 → R2 and R4 → R5 are chains.

| Cycle | Rule that fires | New fact added |
| --- | --- | --- |
| 1 | R1 | suspect_background |
| 2 | R2 | advise_close_apps |
| 3 | R3 | advise_dim_screen |
| 4 | none | (stop) |

- **Case 1** → R1, R2, R3 fire: close background apps and dim the screen.
- **Case 2** → R4 also needs `phone_hot`, so **nothing fires**: the system is silent, even though an old battery might be the real problem.
- **Fix:** ask a follow-up question ("Is your phone hot?"), which is backward chaining, or add a default message such as "No rule matched, please tell me more." Going silent outside its rules is called **brittleness**.

**Link to the Test Bank.** Test Bank question O7 uses a shorter three-rule version of the same system (`R1 IF many_apps_open THEN advise_close_apps`, `R2 IF screen_bright THEN advise_dim_screen`, `R3 IF battery_old AND phone_hot THEN advise_check_battery`). It has no chains, and it calls the first fact `many_apps_open` instead of `many_background_apps`, but the advice for both test cases is the same.
