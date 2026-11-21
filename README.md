# DE Lock-In: EEEN20050 Digital Electronics (final exam)

Cram notes for **EEEN20050 Digital Electronics: from Gate to System** (Dr Ruijia Liu), final on **Tuesday 8 December**. Built from Lectures 1 to 25 and the **2023 final**.

**▶ Practice site: https://lanceyprance.github.io/DE_Lock-In/** (exam drill, check-your-answer questions, the timed 2023 paper and mock finals). It reads the `questions/`, `papers/` and `mock/` md files directly, so editing them updates the site.

Start at **[TOPICS.md](TOPICS.md)** (progress tracker). Day-by-day plan to the exam: **[PLAN.md](PLAN.md)**.

- Everything to learn by heart (there's **no formula sheet**): **[formula-sheet.md](formula-sheet.md)**
- Confusing bits I asked about: **[questions-asked.md](questions-asked.md)**
- Past final: **[2023](papers/2023.md)**
- Mock finals: **[Mock 1](mock/final-1.md)** · **[Mock 2](mock/final-2.md)** · **[Mock 3](mock/final-3.md)**

## The exam

- **2 hours. 4 questions. Answer all. Equal marks (25 each).** 30% of the module.
- Calculator allowed. **No formula sheet.**
- The 2023 paper was:
  - Q1: a gate circuit → function, truth table, K-map, Σm / ΠM, two-level NAND.
  - Q2: a ripple count-down counter with D flip-flops, plus a static-1-hazard-free design.
  - Q3: a two-mode state machine with JK flip-flops (a whole question).
  - Q4: an asynchronous circuit: transition table, flow table, stability (a whole question).
- Assessment: labs 30%, assignments 30%, mid-term 10%, final 30%.

## Reading style (dyslexia-friendly)

- One idea per line. Short sentences.
- Big rules and equations on their own line.
- Lots of space between sections.
- Few brackets, little italics, no long bullet points.

## Notation (same as the slides)

| Write | Means | Say |
|---|---|---|
| x' | NOT x (a bar over x on the slides) | "x bar" or "not x" |
| xy or x·y | x AND y | "x and y" |
| x + y | x OR y | "x or y" |
| x ⊕ y | x XOR y | "x xor y" |
| Σm(…) | sum of minterms | "sum of m" |
| ΠM(…) | product of maxterms | "product of M" |
| Q_t+1 | the flip-flop output after the next clock | "Q next" |

## How each topic is built

- `notes/NN-topic.md`: slide diagrams with **"How to read this diagram"** in plain words, and **🧠 check questions** inline (answer before opening).
- **🎯 In the final**: how the topic was asked in 2023 (or that it wasn't).
- **⭐ Learn by heart**: the short list for that topic. All of them are collected in [formula-sheet.md](formula-sheet.md).
- **📐 boxes** for every rule and equation, numbered 1 to 59 across the whole repo: what each symbol means, why it works, **"use it when…"**.
- **Worked examples** of every 2023 question, **drawing checklists** for every sketch the exam asks for, and a **method table** at the end: "You're asked for… / Use…".
- `questions/NN-topic.md`: end-of-topic test.
  - Part A: the slide exercises and the 2023 final questions on that topic.
  - Part B: exam-style questions in other formats (true/false, multiple choice, design, explain).
- **Rule:** every answer cites the notes section (§) it comes from.

## Answers

- There are **no official answers** for the 2023 paper. Every answer here is my own working.
- Every K-map, flip-flop equation, counter sequence, hazard cover and transition table in Topics 13 to 23, the 2023 paper and the mocks is recomputed in Python: `python3 tools/check_numbers.py` (needs `pip install sympy`).
- Lecture 10 slide 3 has a typo in the mux select: see [questions-asked.md](questions-asked.md).

## Folders

```
notes/       one file per topic (1–23)
questions/   end-of-topic tests
papers/      the 2023 final with worked answers
mock/        three mock finals
img/NN/      snippets: sN.png = slide N of that topic's lecture. img/papers/ = 2023 figures
site/        the practice site (index.html at the root)
tools/       scripts that cut the snippets and check the answers and the site
```
