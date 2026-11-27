# Try it: Guess My Number & Human Bubble Sort (2.4)

**Time:** 20 min · **Group:** pairs, then whole class · **You need:** paper; VisuAlgo (optional) · Study Guide pp. 81–82 · Slides 25–26

**Goal:** experience why binary search is fast, and how bubble sort works step by step.

## Prepare

Partner A secretly picks a number from 1 to 100 and writes it down. Optional: open visualgo.net/en/sorting.

## Steps

1. **Random round.** Partner B guesses. A replies only "higher", "lower" or "correct". Count the guesses.
2. **Middle round.** Play again with a new number, but this time B always guesses the middle of what is left (50, then 25 or 75, ...). Count again.
3. **Human bubble sort.** Six volunteers stand in a row in random height order. Only neighbours may swap. Walk along the row from left to right: if two neighbours are in the wrong order, they swap. Repeat the walk until a full pass has no swaps. The class counts the swaps.
4. Optional: run bubble sort on VisuAlgo with 6 numbers and compare.

## Record

| Round | Guesses / swaps |
| --- | --- |
| Random guessing | |
| Middle strategy | |
| Human bubble sort | |

## Reflect

- What is the most guesses the middle strategy can ever need for 1–100?
- Why would bubble sort be slow for a class of 300?

## Check it: expected results

- The middle strategy never needs more than **7 guesses** for 1–100. Each guess halves what's left: 100 → 50 → 25 → 13 → 7 → 4 → 2 → 1. That is binary search: O(log n).
- Random guessing has no guaranteed limit: you could need many more.
- Bubble sort compares neighbours again and again. Doubling the number of people roughly **quadruples** the work (O(n²)), so 300 people would take a very long time.
- Your swap count depends on the starting order. For six people the most possible is 15 swaps (when they start in exactly reverse order). As a check, the order 5, 2, 6, 1, 4, 3 (heights ranked 1 = shortest) takes 9 swaps.
