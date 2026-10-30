# Section 15 — Introduction to Symbolic AI

Symbolic AI is an approach to artificial intelligence that represents knowledge with symbols, facts, and rules. Instead of learning everything from examples, it uses information people have written down and applies logic to it. It is sometimes called **Good Old-Fashioned AI (GOFAI)**.

Think of symbolic AI as a system following a rulebook. Machine learning is more like learning patterns after seeing lots of examples. A rulebook is easier to inspect, but it cannot cover every situation unless someone has thought to include it.

## A little history

In the 1950s and 1960s, researchers explored whether intelligence could be modelled using symbols and logic. John McCarthy helped establish AI as a field and created Lisp, a language associated with early AI. Alan Turing proposed the Turing Test as one way to discuss machine intelligence. Marvin Minsky helped build the MIT AI Lab and worked on frames and simplified “microworlds.” Allen Newell and Herbert Simon built early reasoning programs such as the Logic Theorist and General Problem Solver.

Later, expert systems used stored rules to imitate parts of specialist decision-making in medicine, engineering, and business.

## How it works

A symbolic system stores facts and rules, then uses them to draw conclusions. A toy rule could be `IF Fever AND Cough THEN Consider respiratory illness`. This only shows the format of a rule; it is not a reliable medical diagnosis.

Symbolic systems tend to be predictable: if the facts, rules, and settings stay the same, the result usually stays the same too. But the answer is only as good as the information and rules provided.

Symbolic AI has been used in decision support, rule-based analysis, and robot planning. MYCIN is a classic medical expert system built around rules. It is different from systems that primarily learn patterns from large amounts of data.

## Symbolic AI today

Many systems combine symbolic reasoning with machine learning. For example, a model could examine an image and label an object. A symbolic component can use that label with other facts and rules to decide what to do and potentially show which rules supported the decision.

This is called **neuro-symbolic AI**. Machine learning handles patterns in images, audio, or text, while symbolic reasoning handles structured facts and rules. AlphaGeometry is a known example that combines learning with symbolic methods.

The basic idea is that machine learning is often good at recognising patterns, while symbolic AI is useful when rules and reasoning steps need to be explicit. Neither approach is best for every job.
