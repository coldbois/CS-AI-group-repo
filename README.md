# DanD Disciples: Software and Symbolic AI

![Dandroid](Main%20Content/assets/dandroid/dandroid-happy.png)

This is our team's repository for the **Software and Symbolic AI** module. Our learning module is called **Dandroid's Logic Lab**: a robot called Dandroid learns how a computer runs (operating systems), how to follow instructions (software) and how to think with rules (Symbolic AI).

The Markdown in this repository is the base for our Study Guide and Test Bank, our slides and our mini-lecture video.

- **Version:** 3.0 (final, Stage 3), November 2026
- **Repository:** https://github.com/coldbois/CS-AI-group-repo

## Where to start

Open **[Main Content/00_Start_Here.md](Main%20Content/00_Start_Here.md)**. It explains who the module is for, what you need before you start, what you will learn and the order to read things in.

Reading order:

1. [Start Here](Main%20Content/00_Start_Here.md)
2. [Operating Systems](Main%20Content/Operating%20Systems%20%E2%80%94%20Essential%20Foundations/README.md) (topics 01–08)
3. [Software Fundamentals](Main%20Content/Software%20Fundamentals/README.md) (topics 09–15)
4. [Symbolic AI Fundamentals](Main%20Content/Symbolic%20AI%20Fundamentals/README.md) (topics 16–21)
5. [Final Mission](Main%20Content/Final_Mission.md) (a short escape-room review)

## Our team

| Name | GitHub | Role |
| --- | --- | --- |
| Malik Talgat | @Bro920 | Quality Lead |
| Aaron Neupane | @Pikolet141 | Project Coordinator |
| Raphael Agnello Wresniwira | @coldbois | Visual Lead, repository owner |
| Baristha Neupane | @Bari-1 | CTO, submissions |
| Gerrard Edgar Joseph | @iblendkids | General Assistant |
| Angele Wang | @gigeeyn | Video Lead |
| Isaac Yong Yee Jay | @YeeJ77 | Content Lead |

More about roles is in the [project plan](About%20Us%20and%20the%20project/ProjectPlan/project_plan.md).

## What the project is for

- **Purpose:** teach Software and Symbolic AI to complete beginners with one checked set of content, and use it to make our Study Guide, Test Bank, slides and video.
- **Who it is for:** first-year university students from any major. You don't need any programming or AI experience.
- **Learning goals:** explain how an operating system runs a computer, write and test small programs, pick algorithms and data structures, use a simple database, write knowledge as facts and rules, trace forward and backward chaining and search, and decide when rule-based AI is a good idea. The full list is in Start Here.

## How the folders work

```
CS-AI-group-repo/
  README.md                      this page
  Main Content/
    00_Start_Here.md             overview, learners, outcomes, how to run the code
    Operating Systems — Essential Foundations/     topics 01–08
    Software Fundamentals/                          topics 09–15
    Symbolic AI Fundamentals/                       topics 16–21
    Final_Mission.md, Glossary.md, Resource_Map.md, References.md
    images/, assets/             pictures for Start Here and the Dandroid stickers
  About Us and the project/      project plan and progress report
  AI_usage_record/               AI usage records for each member
```

Every topic folder (01 to 21) has the same five folders:

| Folder | What is inside |
| --- | --- |
| Main Theory | the lesson |
| Diagrams and Pictures | the pictures the lesson uses (most are the same as in our Study Guide and slides) |
| Learner Activity | the hands-on activity with expected answers, plus a `code` folder for topics with programs |
| Test bank Question_Answer | questions and an answer key |
| Teammate_review | the review sheet for the topic, checked by a teammate who did not write it |

The topic numbers match the Study Guide like this: 01–08 are sections 1.1–1.8, 09–15 are 2.1–2.7 and 16–21 are 3.1–3.6. [Resource_Map.md](Main%20Content/Resource_Map.md) shows where each topic is used in the guide, test bank, slides and video.

## Running the code

- **Python** (topics 11–14, 18, 19, 21): you only need Python 3. Go into the topic's `Learner Activity/code` folder and run for example `python laptop_expert.py`.
- **C** (topic 08): `gcc hello.c -o hello`, then run `hello`. Or paste the code into OnlineGDB.
- **Prolog** (topic 21): paste `family.pl` into a new program at swish.swi-prolog.org.
- **SQL** (topic 14): `python books_starter.py` makes the Books table and runs the activity queries.

Every online activity also has an offline option written on the activity page.

## Our other resources

- Study Guide and Test Bank (*Dandroid's Logic Lab*, 57 questions): handed in with the Study Guide assignment.
- Slides (`DanDDisciples_Stage2_PPT_V1`): handed in with the PPT assignment.
- Mini-lecture video (`DanD_Disciples_MiniLecture_ExpertSystem.mp4`): handed in with the mini-lecture assignment. It is too big to keep on GitHub.

## Versions

- **1.0** (October 2026): first notes.
- **2.0** (7 November 2026): Stage 2, 21 topic folders with theory, diagrams, activities and test banks.
- **3.0** (November 2026): Stage 3 final. All topics checked against the Study Guide, slides and Test Bank, every folder filled in, pictures taken from our own guide and slides, all 57 Test Bank questions added, mini-lecture example added to topic 18, code tested. Old placeholder files and the old reference folder were removed (they are still in the Git history).

## Known limitations

- We could not run the Prolog activity on our own computers, so its answers come from the Study Guide and normal SWI-Prolog behaviour.
- Some online tools might be blocked on school networks. Each activity has an offline option.
- Only the mini-lecture video is linked to the content (topic 18, plus the expert-system part of topic 16).
