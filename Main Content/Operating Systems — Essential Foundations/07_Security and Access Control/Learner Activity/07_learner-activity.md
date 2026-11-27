# Try it: Phishing Spotter & Permission Decoder (1.7)

**Time:** 15 min · **Group:** pairs · **You need:** this page and the mock email · Study Guide pp. 43–44 · Linked Test Bank question: O3

**Goal:** spot the warning signs of a fake message, and decide who can open a file.

## The mock email

This is a harmless example the team made up. It is not a real company's email.

![A mock phishing email from support@micros0ft-help.example with the](../Diagrams%20and%20Pictures/1-7_fake-email.png)

*The same mock email as slide 16.*

## Steps

1. Find **3 red flags** in the email (sender, link, urgency, spelling...).
2. The file `report.txt` has permissions `-rw-r-----`. The owner is **alex** and the group is **staff**. Can **sam** (who is in staff) read it? Write to it?
3. Can **kim** (not in staff) read it?
4. **Least privilege:** a private diary file is set to `-rwxrwxrwx`. Which permissions would you remove?

Use Figure 1.7b on the [topic page](../Main%20Theory/07_main-theory.md) to decode the permissions.

## Record

- Your 3 red flags.
- Yes or no for: sam reads · sam writes · kim reads.
- The diary's new permissions.

## Reflect

- Why do attackers try to make you hurry?
- Which CIA goal does a ransomware attack break?

## Check it: expected results

- **Red flags:** a strange sender address (`micros0ft` uses a zero), urgent threats ("CLOSED in 1 hour"), a link that doesn't match the real website, shouting in capitals and extra "!!!", and asking for a password. Any three are correct.
- What to do instead: don't click. Delete or report it, and if you are worried, type the real website address yourself (slide 17).
- **sam:** read **yes** (group has `r--`), write **no**.
- **kim:** **no access** (others have `---`).
- **Diary:** remove everything from the group and others, and execute from the owner (a diary isn't a program): `-rw-------`.
- Attackers make you hurry so you act before you think.
- **Ransomware** breaks **availability** (you can't open your files) and often confidentiality too. Defences: separate backups and updates.
