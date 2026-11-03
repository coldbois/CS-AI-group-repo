# Activity 3 — Build a Small Rule-Based Troubleshooting Assistant

**Related chapter:** Chapter 3 — Putting Software and Symbolic AI Together  
**Difficulty:** Beginner–Intermediate  
**Suggested time:** 20–30 minutes  

## Goal

See how software input, conditions and output can implement a small set of explicit rules.

## Preparation

- A computer.
- Python installed, or an accessible online Python environment approved by your instructor.
- Basic familiarity with running a Python program. If needed, ask your instructor to provide the environment.

## Scenario

You are prototyping a simple troubleshooting assistant. It asks whether the computer turns on and, if it does, whether the internet is working. It then displays a suggestion based on the answers.

## Starter code

```python
computer_on = input("Does your computer turn on? (yes/no): ").strip().lower()

if computer_on == "no":
    print("Suggestion: check the power connection.")
elif computer_on == "yes":
    internet = input("Is your internet working? (yes/no): ").strip().lower()

    if internet == "no":
        print("Suggestion: check the network connection.")
    elif internet == "yes":
        print("The computer turns on and the internet is working.")
    else:
        print("Please enter yes or no for the internet question.")
else:
    print("Please enter yes or no for the first question.")
```

## Task

1. Read the program before running it. Predict what it will display when the first answer is `no`.
2. Run it with `no` as the first answer.
3. Run it with `yes` for the first answer and `no` for the internet question.
4. Test an unexpected answer such as `maybe`.
5. Identify which lines represent conditions and which lines display results.
6. Add one new rule, such as: if the computer turns on but the sound is not working, suggest checking the volume settings.

## Observation record

| Input tested | Output observed | Which condition selected the output? |
|---|---|---|
| computer_on = no | | |
| computer_on = yes, internet = no | | |
| unexpected input | | |
| your added case | | |

## Reflection

- Which values act as facts supplied by the user?
- Which statements act as rules?
- What does the software do when an input is not recognized?
- What additional knowledge or tests would be needed before using this as a real support tool?

## Hint

`if`, `elif` and `else` control which branch runs. The `and` operator is not needed in this starter example because the program checks the questions in sequence.

## Expected outcome and feedback

- If the computer does not turn on, the program suggests checking the power connection.
- If the computer turns on but the internet does not work, it suggests checking the network connection.
- If both answers are yes, it reports that both are working.
- Unexpected answers are handled by the final `else` branches.
- A new troubleshooting case needs an additional input and a condition that checks it.

**Important distinction:** This short script demonstrates how software executes explicit rules. A production expert system would need a carefully developed knowledge base, richer reasoning, tested coverage, suitable error handling and ongoing maintenance.
