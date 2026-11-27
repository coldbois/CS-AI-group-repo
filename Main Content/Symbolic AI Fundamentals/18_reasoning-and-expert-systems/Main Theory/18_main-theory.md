# 3.3 Reasoning and Expert Systems

![Dandroid worried about its laptop](../../../assets/dandroid/dandroid-nervous.png)

**Chapter 3 · Dandroid's Brain** · Study Guide pp. 124–131 · Slides 37–39 · Test Bank T19, T20, M19, M20, O7 · **Mini-lecture video:** *How does an expert system reach and explain a conclusion?*

> **Mission.** Dandroid's laptop won't turn on, and the assignment is due at midnight. A human technician would ask a few questions and suggest a fix. Can Dandroid reason like that expert?

**You will learn to**

- tell deduction, induction and abduction apart
- trace forward and backward chaining
- describe the parts and limits of an expert system

**Key words:** deduction, induction, abduction, modus ponens, forward chaining, backward chaining, expert system

---

## Three ways to reason (detective edition)

![Figure 3.3a](../Diagrams%20and%20Pictures/3-3_three-ways.png)

*Figure 3.3a. Three ways to reason (Study Guide p. 125).*

| Kind | How it works | Example | How sure? |
| --- | --- | --- | --- |
| **Deduction** | rule + fact → conclusion | Every enrolled student has a record. Asha is enrolled → Asha has a record. | certain (if the rule and fact are true) |
| **Induction** | many observations → a pattern | The library was busy every Monday → it'll be busy next Monday. | likely (unless it's a holiday!) |
| **Abduction** | an observation → the best explanation | The battery is empty → maybe the charger wasn't plugged in... or the battery is faulty. | a guess to test |

> **Bug alert.** A likely explanation is not a proven cause. Remember that whenever a system "diagnoses" something.

## Valid and invalid patterns

An inference engine creates new facts by applying **valid** patterns again and again.

| Pattern | Form | Example | Valid? |
| --- | --- | --- | --- |
| **Modus ponens** | P → Q, P, so Q | If a file is saved, it appears in the folder. It was saved → it appears. | ✓ yes |
| **Modus tollens** | P → Q, not Q, so not P | If online, the page loads. It didn't load → not online (if the rule is strict). | ✓ yes |
| **Affirming the consequent** | P → Q, Q, so P? | If it rained, the ground is wet. It's wet → it rained? | ✗ no: maybe a sprinkler! |

This last one is the class question on slides 38–39 and Test Bank T19. It looks like logic, but it isn't.

## Inside an expert system

An **expert system** is a program that captures a human expert's knowledge as rules and uses it to give advice, like a technician, a doctor or a repair manual that can talk back.

![Figure 3.3b](../Diagrams%20and%20Pictures/3-3_expert-system.png)

*Figure 3.3b. Inside an expert system (Study Guide p. 127).*

| Part | Job | In the restaurant picture |
| --- | --- | --- |
| **Knowledge base** | the expert's rules, written by people | the recipe book |
| **Working memory** | the facts about *this* case | today's order |
| **Inference engine** | matches rules to facts and fires them | the chef |
| **User interface** | asks questions, shows answers | the waiter |
| **Explanation facility** | shows *why*: which rules fired | the receipt |

The mini-lecture video sums these up as "rules, facts, a thinker, and a receipt".

Famous examples: **MYCIN** (Stanford, 1970s, suggested antibiotics for serious blood infections and could answer *why* and *how* questions), **DENDRAL** (worked out chemical structures) and **XCON** (configured computer orders, see [2.1](../../../Software%20Fundamentals/09_where-operating-systems-meet-symbolic-ai/Main%20Theory/09_main-theory.md)).

## Forward vs backward chaining

The inference engine can work in two directions. We use the course-registration rules from the Study Guide and slide 37:

- **R1** IF prerequisite_passed THEN prereq_ok
- **R2** IF fees_paid THEN finance_ok
- **R3** IF prereq_ok AND finance_ok THEN may_register

![Figure 3.3c](../Diagrams%20and%20Pictures/3-3_forward-vs-backward.png)

*Figure 3.3c. Forward vs backward chaining (Study Guide p. 128).*

| | **Forward chaining** (data-driven) | **Backward chaining** (goal-driven) |
| --- | --- | --- |
| Starts from | the facts | a goal (a question) |
| Steps | fire every rule whose IF part is true, add the new facts, repeat until nothing changes | find a rule that concludes the goal, then try to prove each of its conditions, asking the user when no rule can |
| Registration example | facts → R1 adds prereq_ok → R2 adds finance_ok → R3 adds may_register ✓ | may_register? → R3 needs prereq_ok and finance_ok → R1: prerequisite_passed ✓ → R2: fees_paid ✓ → proven |
| Like... | following clues to see where they lead | a detective testing a theory |
| Good for | monitoring: new facts keep arriving and you want everything they lead to | diagnosis: you have a suspicion and want to ask only the questions that matter |

## Worked example: the laptop that won't turn on (from our mini-lecture video)

Our mini-lecture video builds a small troubleshooting expert system for this topic's mission. It has six rules:

| Rule | IF | THEN |
| --- | --- | --- |
| R1 | power light off AND charger plugged in | no power to laptop |
| R2 | no power to laptop AND charger light off | charger is broken |
| R3 | no power to laptop AND charger light on | battery or port faulty |
| R4 | charger is broken | **replace the charger** |
| R5 | power light on AND screen stays black | display is faulty |
| R6 | display is faulty | **repair the screen** |

Notice that some rules conclude exactly what other rules need (R1 feeds R2 and R3; R2 feeds R4; R5 feeds R6). That is what lets the engine *chain* them.

Dandroid checks the laptop. **Facts:** power light off, charger plugged in, charger light off.

**Forward chaining.** The engine scans the rules and fires the first one whose IF part is completely true:

| Pass | What happens | New fact |
| --- | --- | --- |
| 1 | R1 matches (power light off ✓, plugged in ✓) and fires | no power to laptop |
| 2 | R2 matches (no power ✓, charger light off ✓). R3 can't: the charger light isn't on. | charger is broken |
| 3 | R4 fires | replace the charger |
| 4 | nothing new can fire, so the engine **stops** | |

![Figure 3.3d](../Diagrams%20and%20Pictures/3-3_video-forward-chaining.jpg)

*Figure 3.3d. Forward chaining in the mini-lecture video.*

**Backward chaining.** Now suppose a repair expert suspects the charger. The goal is *"is the charger broken?"* The engine finds R2, which needs *no power* and *charger light off*. *No power* is concluded by R1, so that becomes a new goal, which needs *power light off* and *charger plugged in*. No rule concludes those: they are basic facts, so the system simply **asks**.

> **System:** Is the power light off? **Dandroid:** Yes.
>
> **System:** Is the charger plugged in? **Dandroid:** Yep. *(R1 is proven.)*
>
> **System:** Is the light on the charger off?
>
> **Dandroid:** Wait... why are you asking me that?
>
> **System:** Because I'm trying to prove the charger is broken, using rule two. I already know there's no power. So if the charger light is off too, rule two is proven.
>
> **Dandroid:** Fair enough. Yes, it's off. *(Goal proven.)*

That answer to **WHY** is the explanation facility at work. Notice also what backward chaining *never* asked: nothing about the screen. It only asks what it needs.

![Figure 3.3e](../Diagrams%20and%20Pictures/3-3_video-backward-chaining.jpg)

*Figure 3.3e. Backward chaining and the WHY question in the mini-lecture video.*

**HOW did it decide?** Once it has an answer, you can ask the system how it got there. It replays the rules it used, from the answer back to your own facts, like a receipt:

```
replace the charger      by R4, because the charger is broken
the charger is broken    by R2, because no power to laptop + charger light off
no power to laptop       by R1, because power light off + charger plugged in
those three facts        you told me
```

Every step points to a rule, and every rule points to facts you gave it. Nothing is hidden, so a person can check it and trust it. MYCIN worked exactly like this.

You can run this whole example, including the WHY and HOW explanations, with [laptop_expert.py](../Learner%20Activity/code/laptop_expert.py) (Python 3 only). Add `--ask` to answer the questions yourself and type `why` at any question.

**Check question from the video.** A friend's laptop has a new problem: the power light is **on**, but the screen stays black. Using forward chaining on the same six rules, which advice does the system give? *A* replace the charger, *B* get the screen repaired, *C* check the battery, or *D* no rule fires?

**Answer**
**B.** R1 can't fire, because the power light is on, not off, and without R1, rules R2, R3 and R4 never get started. But R5 matches (power light on, screen black), so *display is faulty*; then R6 fires: get the screen repaired.

If you picked **C**, here's the trap: R3 needs *no power to laptop*, and that fact never appeared.


## Try it

**Battery Detective Expert System** (30 min, groups of 3): write, test and break a small rule base for a phone whose battery drains quickly. Instructions and answers: [18_learner-activity.md](../Learner%20Activity/18_learner-activity.md).

## Limits of expert systems

- **Knowledge is hard to collect.** Experts often can't say exactly how they decide.
- **Brittle.** A case the rules don't cover gets no answer, or a silly one.
- **Rules can conflict** as the rule base grows.
- **Weak with uncertainty.** Plain rules are yes/no; real evidence is often "maybe". (MYCIN added *certainty factors* for this.)

[3.5](../../20_advantages-and-limitations-of-symbolic-ai/Main%20Theory/20_main-theory.md) looks at these limits in more detail.

## Check yourself

1. "All my 20 Mondays were busy, so next Monday will be." Which kind of reasoning is this?
2. Which chaining method starts from a goal?
3. Name two limitations of expert systems.

**Answers (try first, then peek)**
1. Induction (a likely pattern, not guaranteed).
2. Backward chaining.
3. Any two: knowledge is hard to collect, brittle on new cases, rules can conflict, weak with uncertainty.


More questions: [18_test-bank.md](../Test%20bank%20Question_Answer/18_test-bank.md)

## Remember

- Deduction = certain; induction and abduction = likely.
- Forward: facts → conclusions. Backward: goal → needed facts.
- Expert system = knowledge base + inference engine + explanation. Same rules, two directions, and always a receipt.

## Watch and explore

- **Our mini-lecture video** (*DanD_Disciples_MiniLecture_ExpertSystem.mp4*, about 8 minutes, submitted with the mini-lecture assignment). Pause during the 10-second "Think!" countdown and answer the check question before the reveal.
- **Yale CS lecture notes: "Rule Based Systems"**. Short notes on IF-THEN rules and MYCIN. Find one MYCIN-style rule and rewrite it in plain English. It is a university-level page: skim the examples only.

## References

- Buchanan, B. G., & Shortliffe, E. H. (Eds.). (1984). *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*. Addison-Wesley.
- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. Chapter 7 (forward and backward chaining).
- McDermott, J. (1982). R1: A rule-based configurer of computer systems. *Artificial Intelligence, 19*(1), 39–88.

---

Previous: [3.2 Knowledge Representation](../../17_knowledge-representation/Main%20Theory/17_main-theory.md) · Next: [3.4 Planning and Problem Solving](../../19_planning-and-problem-solving/Main%20Theory/19_main-theory.md) · Up: [Chapter 3 overview](../../README.md)
