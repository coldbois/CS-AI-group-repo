# 3.3 Test Bank: Reasoning and Expert Systems

T19, T20, M19, M20 and O7 are the same as in the *Dandroid's Logic Lab* Test Bank. V1 is the check question from our mini-lecture video. Q1–Q2 are extra practice. Answers are at the bottom.

## Questions

**T19 (True or False).** "If it rains, the ground is wet." The ground is wet. So it must have rained.

**T20 (True or False).** Forward chaining starts with the facts and works out what follows.

**M19 (choose ONE).** "The library was busy every Monday for 20 weeks, so next Monday it will be busy." What kind of reasoning is this?

- A. Random guessing
- B. Deduction (certain)
- C. Induction (a likely pattern)
- D. Abduction (best explanation)

**M20 (choose ONE).** Which part of an expert system applies the rules to the facts?

- A. The keyboard
- B. The printer
- C. The user interface
- D. The inference engine

**O7. Battery Detective** (about 100 words, 5 marks)

Dandroid's phone expert system has three rules:

R1 IF many_apps_open THEN advise_close_apps

R2 IF screen_bright THEN advise_dim_screen

R3 IF battery_old AND phone_hot THEN advise_check_battery

Case 1 facts: many_apps_open, screen_bright. Case 2 fact: battery_old (only).

(1) Which rules fire in Case 1? What does the system advise? (2) Why does the system say nothing in Case 2? (3) Suggest one way to improve the system.

Use these words: rule · fact · fires · AND · brittle

**V1 (mini-lecture video, choose ONE).** Using the six laptop rules on the [topic page](../Main%20Theory/18_main-theory.md), a laptop's power light is on but the screen stays black. Using forward chaining, which advice does the system give?

- A. Replace the charger
- B. Get the screen repaired
- C. Check the battery
- D. No rule fires

**Q1.** With the registration rules R1–R3 and the goal `may_register`, which facts does backward chaining need to check?

**Q2.** In the laptop example, the system asks "Is the light on the charger off?" and the user asks "Why?". What should the system answer?

---

## Answer key

| No. | Answer | Why |
| --- | --- | --- |
| T19 | **False** | This is a common thinking trap (affirming the consequent). Correct version: we cannot be sure; a sprinkler could also make the ground wet. |
| T20 | **True** | Facts → rules fire → new facts. Backward chaining starts from a goal instead. |
| M19 | **C** | Many examples → a likely pattern. It's based on evidence, not random (A); deduction gives a certain answer from a rule (B); abduction explains one observation (D). |
| M20 | **D** | The inference engine does the reasoning. The user interface (C) asks questions and shows answers; A and B are hardware. |
| V1 | **B** | R1 can't fire (the power light is on), so R2–R4 never start. R5 matches → display faulty → R6 → repair the screen. C is a trap: R3 needs "no power to laptop", which never appeared. |
| Q1 | prerequisite_passed and fees_paid | R3 needs prereq_ok and finance_ok; R1 needs prerequisite_passed; R2 needs fees_paid. |
| Q2 | Its reason | "Because I'm trying to prove that the charger is broken, using R2. I already know there's no power to the laptop, so if the charger light is off too, R2 is proven." |

**O7 sample answer (125 words).** In Case 1, the facts are many_apps_open and screen_bright. R1 fires, because its IF part (many_apps_open) is true, so the system advises closing apps. R2 fires too, because screen_bright is true, so it also advises dimming the screen. R3 does not fire. In Case 2, the only fact is battery_old. R3 needs battery_old AND phone_hot, and phone_hot is missing, so R3 cannot fire. No other rule matches, so the system says nothing, even though an old battery might be the real problem. This shows that rule-based systems are brittle: they only know what their rules cover. To improve it, the system could ask a follow-up question like "Is your phone hot?", or show a default message such as "No rule matched, please tell me more."

**O7 key points (1 mark each):** Case 1: R1 and R2 fire · advice: close apps and dim the screen · Case 2: R3 needs both facts (AND), so nothing fires · the system only knows what its rules cover (brittle) · a sensible improvement. *Also accept* the order R2 then R1; the order does not matter here.
