# 1.7 Security and Access Control

![Dandroid nervous about a strange email](../../../assets/dandroid/dandroid-nervous.png)

**Chapter 1 · Dandroid's Body** · Study Guide pp. 40–45 · Slides 15–17 · Test Bank T7, M7, O3

> **Mission.** Someone is trying to log in as Dandroid, and a strange email says "Click here or your account will be closed!" How do the OS (and you) keep Dandroid safe?

**You will learn to**

- explain the CIA triad
- tell authentication from authorization
- read file permissions and spot common threats

**Key words:** confidentiality, integrity, availability, authentication, permissions, least privilege

---

## Three security goals: CIA

Security people check everything against three goals, known as the **CIA triad**:

| Goal | Meaning | Example |
| --- | --- | --- |
| **Confidentiality** | only the right people can see it | your exam marks |
| **Integrity** | nobody can secretly change it | your bank balance |
| **Availability** | it works when you need it | the course website the night before the deadline |

![Figure 1.7a](../Diagrams%20and%20Pictures/1-7_cia-and-login.png)

*Figure 1.7a. Keeping Dandroid safe (slide 15).*

## Who are you, and what may you do?

When you log in, the OS asks two different questions, in this order:

1. **Authentication:** *who are you?* You prove it with something you know (a password), something you have (your phone) or something you are (a fingerprint). Using two of these together is **two-factor authentication (2FA)**.
2. **Authorization:** *what may you do?* Once the OS knows who you are, it checks what you are allowed to open, change or delete.

Typing your password is authentication. Being allowed to read a class file but not change it is authorization.

## Reading permissions: `-rwxr-x---`

Linux and macOS show permissions as a row of 10 characters. Each file has an **owner**, a **group** and **everyone else**, and each of them may **read (r)**, **write (w)** or **execute (x)** the file.

![Figure 1.7b](../Diagrams%20and%20Pictures/1-7_permissions.png)

*Figure 1.7b. Reading `-rwxr-x---` (Study Guide p. 42).*

- The 1st character is the type: `-` = file, `d` = folder (directory).
- The next three are the owner, then three for the group, then three for everyone else.
- A dash `-` means "not allowed".

So `-rwxr-x---` means the owner can read, change and run the file, group members can read and run it, and everyone else can do nothing.

**Least privilege:** give each user or app only the permissions it really needs. A photo-editing app doesn't need your contacts; a private diary doesn't need to be readable by the group.

## Layers of defence

The OS protects you in layers: user mode and kernel mode (1.1), separate memory for each process (1.4), permissions, sandboxing apps, and firewalls. No single layer stops every attack, so we use several.

The weakest layer is often the person. **Phishing** emails trick you into handing over a password. Typical red flags:

- a sender address that only *looks* real (`micros0ft` with a zero)
- urgent threats ("CLOSED in 1 hour!")
- a link that doesn't go to the real website
- asking for your password or a code (real companies never do this by email)
- spelling mistakes and SHOUTING

> **Dandroid's tip.** Use long, unique passwords (a password manager helps), turn on 2FA, install updates and keep a separate backup. These four habits stop most everyday attacks.

## Try it

**Phishing Spotter & Permission Decoder** (15 min, pairs): find the red flags in a fake email, then decide who may open `report.txt`. Instructions and answers: [07_learner-activity.md](../Learner%20Activity/07_learner-activity.md).

## Going further (optional)

- **Encryption** protects confidentiality: even if a laptop is stolen, an encrypted drive (BitLocker, FileVault) is unreadable without the key.
- **Hashing passwords.** The OS does not store your password. It stores a *hash*, a scrambled fingerprint of it, and compares hashes when you log in.
- **Sandboxes, containers and virtual machines** keep programs apart. A virtual machine runs a whole separate OS; a container shares the host's kernel but has its own files and processes. Both limit the damage one program can do.
- **Ransomware** encrypts your files and demands payment. It attacks availability (and often confidentiality). The best defence is a backup that the ransomware can't reach.

## Check yourself

1. Which CIA goal is broken if someone secretly changes your grade?
2. Fingerprint unlock: authentication or authorization?
3. What does the `x` mean in `-rwx------`?

**Answers (try first, then peek)**
1. Integrity.
2. Authentication (proving who you are).
3. Execute: the owner may run the file as a program.


More questions: [07_test-bank.md](../Test%20bank%20Question_Answer/07_test-bank.md)

## Remember

- CIA = confidentiality, integrity, availability.
- Authenticate (who are you?) → authorize (what may you do?).
- Least privilege, updates, backups and 2FA stop most everyday attacks.

## Watch and explore

**Crash Course Computer Science #31: Cybersecurity** (PBS, YouTube). A clear introduction to authentication, access control and least privilege. Pause at each attack type and name the CIA goal it targets. It is fast-paced, so captions are recommended.

## References

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Chapters 16–17.
- National Cyber Security Centre (UK). (n.d.). *Phishing attacks: defending your organisation*. https://www.ncsc.gov.uk/guidance/phishing

---

Previous: [1.6 Files](../../06_File%20Systems%20and%20Storage/Main%20Theory/06_main-theory.md) · Next: [1.8 Basic C](../../08_Basic%20C%20for%20Operating%20System%20Ideas/Main%20Theory/08_main-theory.md) · Up: [Chapter 1 overview](../../README.md)
