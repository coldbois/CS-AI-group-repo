# The "laptop won't turn on" expert system from our mini-lecture video (topic 3.3).
# It shows forward chaining, backward chaining, a WHY explanation and a HOW explanation.
# Run:  python laptop_expert.py            (uses Dandroid's answers from the video)
#       python laptop_expert.py --ask      (backward chaining asks YOU the questions)
import sys

RULES = [
    ("R1", ["power_light_off", "charger_plugged_in"], "no_power_to_laptop"),
    ("R2", ["no_power_to_laptop", "charger_light_off"], "charger_broken"),
    ("R3", ["no_power_to_laptop", "charger_light_on"], "battery_or_port_faulty"),
    ("R4", ["charger_broken"], "advice_replace_charger"),
    ("R5", ["power_light_on", "screen_stays_black"], "display_faulty"),
    ("R6", ["display_faulty"], "advice_repair_screen"),
]


def forward_chain(facts):
    """Data-driven: keep firing the first rule that adds something new, until nothing changes."""
    memory = list(facts)
    why = {}                                    # conclusion -> rule that produced it
    passes = 0
    while True:
        passes += 1
        for name, conditions, conclusion in RULES:
            if conclusion not in memory and all(c in memory for c in conditions):
                memory.append(conclusion)
                why[conclusion] = name
                print(f"  pass {passes}: {name} fires -> add {conclusion}")
                break
        else:
            print(f"  pass {passes}: nothing new can fire -> STOP")
            return memory, why


def backward_chain(goal, answer, known, stack=()):
    """Goal-driven: find a rule that concludes the goal, then try to prove its conditions."""
    if goal in known:
        return known[goal]
    rules = [r for r in RULES if r[2] == goal]
    if not rules:                               # a basic fact: no rule concludes it, so ask
        known[goal] = answer(goal, stack)
        return known[goal]
    for name, conditions, conclusion in rules:
        if all(backward_chain(c, answer, known, stack + ((name, conclusion),)) for c in conditions):
            known[goal] = True
            print(f"  {name} proven: {conclusion}")
            return True
    known[goal] = False
    return False


def scripted(fact, stack):
    # Dandroid's answers in the video: power light off, plugged in, charger light off.
    reply = fact in ("power_light_off", "charger_plugged_in", "charger_light_off")
    print(f"  ASK: is {fact}?")
    if fact == "charger_light_off":            # the moment Dandroid asks WHY
        rule, conclusion = stack[-1]
        print(f"     Dandroid: why are you asking me that?")
        print(f"     System: because I am trying to prove {conclusion} using {rule}.")
    print(f"     Dandroid: {'yes' if reply else 'no'}")
    return reply


def interactive(fact, stack):
    while True:
        reply = input(f"  Is it true that {fact.replace('_', ' ')}? (yes/no/why) ").strip().lower()
        if reply == "why":
            rule, conclusion = stack[-1]
            print(f"  Because I am trying to prove {conclusion} using {rule}.")
        elif reply in ("yes", "no"):
            return reply == "yes"


def explain_how(conclusion, why, depth=0):
    rule = why.get(conclusion)
    pad = "  " * (depth + 1)
    if rule is None:
        print(f"{pad}{conclusion}: you told me")
        return
    conditions = next(r[1] for r in RULES if r[0] == rule)
    print(f"{pad}{conclusion}: by {rule}, because {' and '.join(conditions)}")
    for c in conditions:
        explain_how(c, why, depth + 1)


if __name__ == "__main__":
    print("FORWARD CHAINING with Dandroid's facts")
    memory, why = forward_chain(["power_light_off", "charger_plugged_in", "charger_light_off"])
    print("\nHOW did you decide to replace the charger?")
    explain_how("advice_replace_charger", why)

    print("\nBACKWARD CHAINING: goal = charger_broken")
    asker = interactive if "--ask" in sys.argv else scripted
    print("  Goal proven!" if backward_chain("charger_broken", asker, {}) else "  Goal NOT proven.")

    print("\nYOUR TURN (video check question): power light on, screen stays black")
    forward_chain(["power_light_on", "screen_stays_black"])
