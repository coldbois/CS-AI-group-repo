# Try it: Chat with ELIZA: Find the Cracks (3.5)

**Time:** 15 min · **Group:** solo · **You need:** a browser · Study Guide pp. 148–149

**Goal:** investigate a famous 1966 rule-based chatbot and discover what pattern rules can (and can't) do.

## Prepare

Open an online ELIZA, for example the "Try ELIZA" link on the ELIZA historical project site (elizagen.org). Write down which version you use, because replies differ between versions.

No internet? Read the sample conversation in "Check it" and answer the reflection questions from that.

## Steps

1. Type: **"I am sad about my exams."** Note the reply.
2. Type: **"My mother cooks well."** Then: **"My robot cooks well."**
3. Predict the reply to **"I am happy"** before you send it.
4. Try to break it: ask a factual question ("What is 2 + 2?") or use sarcasm.
5. Write down 3 patterns ELIZA seems to follow.

## Record

| I typed | ELIZA replied | Smart ✓ or broken ✗? |
| --- | --- | --- |
| | | |

## Reflect

- Does ELIZA understand you? What is your evidence?
- Which limitation from [3.5](../Main%20Theory/20_main-theory.md) did you find?

## Check it: what to look for

- ELIZA (Joseph Weizenbaum, MIT, 1966) matches **keywords and patterns**, for example "I am X" → a question about X, and swaps words such as "my" → "your" and "I" → "you".
- "Mother" is a keyword in the original script, so it usually gets a special reply about your family. "Robot" isn't, so the same sentence with "robot" gets a generic reply. The *pattern* matters, not the meaning.
- It has no knowledge of the world, so factual questions and sarcasm break it.
- It shows **brittleness**, and the gap between *matching symbols* and *understanding*.
- Replies vary between ELIZA versions, so your exact output may differ. A typical exchange looks like this:

  > **You:** I am sad about my exams.
  >
  > **ELIZA:** Why do you say you are sad about your exams?
