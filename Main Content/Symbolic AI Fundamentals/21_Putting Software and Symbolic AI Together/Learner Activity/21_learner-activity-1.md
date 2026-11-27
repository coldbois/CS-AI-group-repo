# Try it: Prolog Family Lab on SWISH (3.6)

**Time:** 30 min · **Group:** pairs · **You need:** a browser (swish.swi-prolog.org) · Study Guide pp. 155–156

**Goal:** build and query a tiny knowledge base, then extend it with your own rule.

## Prepare

Open **swish.swi-prolog.org** and create a new **Program** (no account is needed to try it). Paste the contents of [family.pl](code/family.pl) into the program panel on the left:

```prolog
parent(john, mary).
parent(mary, alice).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
```

Queries go in the query box on the bottom right, *without* the `?-`.

No internet or SWISH blocked? Do the predictions on paper and use the answers below.

## Steps

1. **Predict, then run:** `grandparent(john, alice).`
2. **Predict, then run:** `grandparent(john, Who).` (a capital W makes it a variable!)
3. Add the fact `parent(alice, tom).` to the program. Then ask: `grandparent(mary, tom).`
4. Add your own rule: `sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.` Add facts to test it, for example `parent(mary, bob).`, then ask `sibling(alice, Who).`
5. **Break it:** write `Parent(john, mary).` with a capital P. What happens?

## Record

| Query | My prediction | SWISH answer |
| --- | --- | --- |
| `grandparent(john, alice)` | | |
| `grandparent(john, Who)` | | |
| `grandparent(mary, tom)` | | |
| my sibling query | | |

## Reflect

- How did Prolog find `Who` without you writing a loop?
- Why does `X \= Y` matter in the sibling rule?

## Check it: expected results

1. `true.`
2. `Who = alice.`
3. `true.` (Mary → Alice → Tom)
4. With `parent(mary, bob)` added, `sibling(alice, Who)` gives `Who = bob`. Without `X \= Y` ("X is not the same as Y"), everyone would also be their own sibling: `Who = alice` would appear too!
5. A capital P makes `Parent` a variable, not a name, so SWISH reports a **syntax error**. Fact and rule names start with a lowercase letter.

Prolog found `Who` by **searching**: it tried each `parent` fact for Z until both parts of the rule were true. That's the inference engine from [3.3](../../18_reasoning-and-expert-systems/Main%20Theory/18_main-theory.md), built into the language (Prolog uses backward chaining).

**Hint:** every fact and rule ends with a full stop. A missing full stop is the most common error.
