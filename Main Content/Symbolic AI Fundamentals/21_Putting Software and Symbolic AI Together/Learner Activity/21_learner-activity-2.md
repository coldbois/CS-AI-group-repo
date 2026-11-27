# Try it: Python Troubleshooting Assistant (3.6)

**Time:** 25 min · **Group:** solo or pairs · **You need:** Python 3 or an online Python editor · Study Guide pp. 157–158

**Goal:** see how software inputs, conditions and outputs implement explicit rules, then extend them.

## Prepare

Open [troubleshooting_assistant.py](code/troubleshooting_assistant.py) and run it with `python troubleshooting_assistant.py`, or paste it into an online Python editor:

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

## Steps

1. **Predict** the output when the first answer is `no`. Run it.
2. Run it with `yes`, then `no`.
3. Type `maybe`. What happens?
4. Mark which lines are conditions (rules) and which display results.
5. Add a new rule: if the computer turns on but the sound isn't working, suggest checking the volume.

## Record

| Input | Output | Which condition chose it? |
| --- | --- | --- |
| on = no | | |
| on = yes, internet = no | | |
| maybe | | |
| your new case | | |

## Reflect

- Which values act as facts supplied by the user?
- What would this need before it could be a real support tool?

## Check it: expected results

We ran the script with each input to check these outputs.

| Input | Output | Condition |
| --- | --- | --- |
| `no` | Suggestion: check the power connection. | `if computer_on == "no"` |
| `yes`, then `no` | Suggestion: check the network connection. | `elif computer_on == "yes"`, then `if internet == "no"` |
| `yes`, then `yes` | The computer turns on and the internet is working. | `elif internet == "yes"` |
| `maybe` | Please enter yes or no for the first question. | the final `else` |

- **Conditions** = the `if` / `elif` lines; **outputs** = the `print` lines. The user's answers (`computer_on`, `internet`) are the facts.
- A new rule needs a new `input()` and a new `elif`. One possible answer, added inside the `elif computer_on == "yes":` block before the internet question:

  ```python
  sound = input("Is the sound working? (yes/no): ").strip().lower()
  if sound == "no":
      print("Suggestion: check the volume settings.")
  ```

- Compare this with [3.3](../../18_reasoning-and-expert-systems/Main%20Theory/18_main-theory.md): here the rules are mixed into the code, so the program can't explain itself. In the laptop expert system ([laptop_expert.py](../../18_reasoning-and-expert-systems/Learner%20Activity/code/laptop_expert.py)) the rules are kept in a separate list and an engine reasons with them, which is why it can answer WHY and HOW.
- A real tool needs many more tested rules, a separate knowledge base, good error handling and maintenance.
