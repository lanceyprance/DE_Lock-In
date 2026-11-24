# Handoff: building the next subject's Lock-In repo

For the next Claude Code session. Read all of this before you touch anything.

You are building **one more cram repo for one more subject**, the same way these were built:

| Repo | Subject | Exam | Storage prefix | Notes |
|---|---|---|---|---|
| `lanceyprance/mathlockin` | MATH20290 Multivariable Calculus | Sat 5 Dec | `m20290:` | no formula sheet in the exam |
| `lanceyprance/DE_Lock-In` | EEEN20050 Digital Electronics | Tue 8 Dec | `de:` | no formula sheet, one past paper, **no official answers** |
| `lanceyprance/SSD_Lock-In` | EEEN20070 Solid State Devices | Wed 16 Dec | `ssd:` | formula sheet given, 5 past papers **with official answers** |

Later all subjects get joined into one hub site, so **follow the formats below exactly**: the hub reads them.

---

## 0. Which repo to use as the template

- **Use `lanceyprance/DE_Lock-In`** (the newest) if the subject has **no tutorial sheets**, **no formula sheet**, **no official answers**, or is design / logic heavy (truth tables, diagrams, procedures). Its site accepts slide-exercise tags and "Rule N" boxes as well as "Equation N".
- **Use `lanceyprance/SSD_Lock-In`** if the subject is calculation heavy, has a formula sheet, and has tutorials and past papers with official answers.
- Both have the same file formats (§5). The differences are in `site/app.js` (§6) and the tools.

---

## 1. Who the user is and how they work

- A UCD engineering student cramming for finals in **Nov–Dec 2026**, roughly 70% understanding fast, with no lectures attended.
- **Dyslexia-friendly writing everywhere:** one idea per line, short sentences, big equations on their own line, lots of space, few brackets, little italics, no long bullet points. Plain words, no waffle.
- They send material **5 files at a time** and say when they're done. **Don't start building until they say "that's all".** After each batch, reply in a few lines: what you got, what's still missing.
- Ask your questions **once, early, in a numbered list** (§3). Then work without stopping to ask. If they don't answer one (DE: study hours), pick a sensible default, say so, and offer to redo it.
- Keep chat replies short. Findings go in the repo, not in chat.
- Never tick a topic ✅ in `TOPICS.md` unless the user says it's done. Log every confusion question they ask in `questions-asked.md` under its topic (short answer + link to the notes §). Don't edit the notes for it unless they ask.
- They may already have a **half-built repo** (DE had a mid-term pack for Lectures 1–10). Then: keep the content, convert it to the formats in §5, and add the rest.

---

## 2. Set up

1. Clone the template read-only (call the `add_repo` tool first if the session needs it; public repos clone anonymously):
   `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/lanceyprance/DE_Lock-In ~/ref/template`
2. Your own repo is whatever the session gives you. Copy from the template: `site/`, `index.html`, `.nojekyll`, `tools/` (`check_links.py`, `check_site_parse.js`, `contact_sheet.py`, `crops.py`, `grid.py`), and the **structure** (not the content) of every md file.
3. Tools: `pdftoppm`, `pdftotext`, `soffice` (pptx → pdf), Pillow, Node are installed. Run `pip install sympy` (needed by `check_numbers.py` for K-maps / algebra).
4. Put every upload and every rendered page in the **scratchpad**, never in the repo. Only cropped snippets go in `img/`.
5. Uploads arrive in `/root/.claude/uploads/<session>/` with random prefixes. Copy each to the scratchpad with a short name (`L5.pdf`, `exam2023.pdf`) straight away.

---

## 3. Questions to ask the user (once, before building)

1. Subject name and module code. Final exam **date**, **length**, and **layout** (number of questions, marks each, choice or answer-all).
2. Is a **formula sheet** given? If yes, get a copy. That decides every "Learn by heart" list.
3. **Past papers**, and do **answers** exist? Which years?
4. Tutorials or assignments: which chapters, and do the answers exist?
5. Is there an existing repo for this subject to redo, or start from scratch?
6. Rough study hours per day, for `PLAN.md`. (Remind them of their other exam dates: the plan must go light around them.)
7. Confirm the Pages URL: `https://lanceyprance.github.io/<Repo>/`.

Don't ask about anything you can find in the files.

**The UCD module page answers a lot of this** (exam length, assessment split, syllabus, learning outcomes): `https://hub.ucd.ie/usis/!W_HU_MENU.P_PUBLISH?p_tag=MODULE&MODULE=<CODE>`. It may be blocked by the session's network at first. The user can allow it. Then fetch it with `curl` and strip the HTML in Python (the web-fetch agent failed on DNS while it was blocked). A past paper's front page gives the layout too.

---

## 4. Building it, in order

### 4.1 Extract the material

```bash
soffice --headless --convert-to pdf deck.pptx            # slides → PDF
pdftoppm -r 100 -png deck.pdf sl/L5/s                     # pages → sl/L5/s-01.png ...
pdftotext -layout deck.pdf txt_L5.txt                     # text, if the PDF has any
python3 tools/contact_sheet.py sl/L5 cs/L5_1.png 1 16     # 4×4 grid of slides with numbers
```

- Read **all** slide text first (`grep -v` the header/footer lines), then look at the contact sheets to see the diagrams. That's much faster than reading slides one by one.
- Past papers are sometimes **scanned**: pdftotext gives nothing. Render them (`-r 90` to read, `-r 200` to read small circuit figures) and **read the images**.
- **Transcribe every past paper into a scratch file** as you read it. You'll need it for topics, papers and mocks.
- Map every tutorial and past-paper question to a topic **before** writing anything. The exam drives the topic list and the weights. Anything nothing touches goes in "Skip / skim".

### 4.2 Solve and verify before writing

- **Compute every answer in Python first** (sympy `SOPform`/`POSform` for K-maps, simulate flip-flops and counters, recompute every number).
- Put those checks in `tools/check_numbers.py` (topics + papers) and `tools/check_mocks.py` (mocks). Template: DE's versions.
- **Never write a "want" value from your head.** Compute it, then hand-check the computed value, then write it in. On DE, the guessed values were wrong six times. The computed ones were right every time.
- Compare sympy output **order-independently** (DE's `check()` has a `_norm` helper): term order changes between runs.

### 4.3 Cut the snippets

```bash
python3 tools/crops.py jobs.txt        # each line: src.png dst.png [x0 y0 x1 y1] (fractions)
```

- Fast option that worked on DE: **whole-slide crops without the header and footer**. Decks come in different page sizes, and each size needs its own box. DE used `0 0.062 1 0.905` for 1170×827 slides and `0 0.072 1 0.918` for 1000×750. A slide whose text runs to the bottom needs `y1 ≈ 0.96`.
- For a single diagram, read the crop box off `tools/grid.py`'s overlay of **that page alone**.
- **Always look at your crops** on one check sheet (thumbnails of every crop, 8 per row) before using them. Fix any that cut off a title, axis, label or last line.
- Names: `img/NN/sPAGE.png` (slide of topic NN), `img/papers/YYYY-figN.png` (past-paper figures), `img/NN/ans-...png` (official answers).

### 4.4 Write the files (formats in §5 are fixed)

1. `site/app.js` port (§6) and `index.html`.
2. `formula-sheet.md`: the exam's own sheet, plus "Learn by heart (NOT on the sheet)". **No sheet in the exam?** Then the page is all learn-by-heart (DE's is the model). Keep the file name: the site and hub expect it.
3. Topics: `notes/NN-slug.md` then `questions/NN-slug.md`. **Commit and push after every 2–3 topics.**
4. `TOPICS.md`, `README.md`, `PLAN.md`.
5. `papers/YYYY.md` for every past final.
6. `mock/final-1.md` … `final-3.md`.
7. `questions-asked.md`: one `## Topic N — Title` heading per topic, "(none yet)".
8. Checks (§7). Commit, push, and **ask the user before merging to `main`**.

---

## 5. File formats (the site parses these, don't improvise)

### `notes/NN-slug.md`

```
# Topic N: Title

Tutorial questions: Ch3 Q1, Q2 · Past finals: 2018 Q1a        (or: Slide exercises: L5 s23–27 · Past finals: 2023 Q1b)

Slides: DECK, pages a to b.

---

## The big idea
(3 to 8 short lines)

---

**How to use these notes:**
When you see 🧠, stop.
Answer it on paper first.
Then click to check.

---

## 🎯 In the final
(how this topic is actually asked, with years and marks. Not asked? Say so, and say where it's used.)

---

## ⭐ Learn by heart from this topic
(only what is NOT on the formula sheet; everything if there's no sheet; a memory hook at the end)

---

## 1. Section title

![What it shows](../img/NN/s12.png)

**How to read this diagram:**
- plain-word bullets, one idea each

### 🧠 Check
Question.

<details><summary>Answer</summary>

Answer.

</details>

---

### 📐 Equation K: name (on / NOT on the formula sheet)      (or: ### 📐 Rule K: name)
$$...$$
| Symbol | Means | Units / value |
**What it means:** … **Use it when:** … (and when not)

## Worked example: Final YYYY QZ
## Drawing checklist: ...   (numbered steps for every sketch the exam asks for)
## Method: ...              (table: "You're asked for | Use")

---

Next: [End-of-topic test](../questions/NN-slug.md)
```

- **Box numbers (Equation K / Rule K) are global across the repo**, one counter for both kinds (DE runs 1 to 59). The site jumps "Rule 18" / "Equation 18" to the right box.
- A reference to a box in **another** topic must say `Topic N Rule K`. A bare "Rule K" is looked up in the current topic. (DE has a script that checks this: see §7.)
- Converting an old repo with per-topic numbers? Renumber with a script that maps (topic, kind, k) → global n and rewrites headings and every reference, including "Rules 1 to 3" and "Topic 6 Rule 1". Skip the 📐 heading lines when rewriting references, or they get renumbered twice.
- Every 📐 box says whether it's on the formula sheet (if there is one).
- Any slip in a slide or official answer gets a ⚠️ note with the corrected value.

### `questions/NN-slug.md`

```
# Topic N: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Tutorial and past-final questions        (DE: "Slide exercises and past-final questions")

### Q5 (Tutorial Ch2 Q5)          (DE: ### S1 (Lecture 5, slides 23 to 25))
question
<details><summary>Answer</summary>

answer (bold the final answers)

From: §3, Equation 18

</details>

---

### F2023-1a (Final 2023 Q1a)
...

## Part B: Exam-style questions

### M1: True or false
1. statement
<details><summary>Answer</summary>

1. **True.** why (§2)

</details>

### M2: Multiple choice
- A. option
- B. option
<details><summary>Answer</summary>

**B.** why

</details>

### M3: Calculate / Design   ### M4: Sketch   ### M5: Explain
```

Rules the parser depends on:
- Heading IDs must match `^[A-Za-z]*\d+(-\d+[a-z]*)?[a-z]*`: `Q5`, `S1`, `M3`, `F2023-1a`, `F2014-3biii`. **Unique within a file.**
- The bracket tag must start with `Tutorial` or `Final` (SSD site) — or also `Lecture` / `Study guide` (DE site) — for the question to count in the drill.
- Every answer ends with a `From:` line naming § / Topic N § / Equation N / Rule N / drawing checklist / Method.
- True/false and multiple-choice answers must use exactly the bold patterns above.
- A topic with no Part A questions still needs the `## Part B: Exam-style questions` heading, or everything counts as Part A.

### `papers/YYYY.md` and `mock/final-N.md`

```
# Final 2023          (or: # Mock Final 1)

(intro: how to use it, constants, whether the answers are official)

---

## Questions

### Q1. Title — 25 marks
parts with (marks or %)

---

## Answers

<details><summary>Q1 answers</summary>

... each part ends with "From: Topic N §M" ...

</details>
```

- The em dash and "N marks" in the `### Q` heading are parsed for the score. One `<details><summary>QN answers</summary>` per question.
- Mocks copy the real layout (number of questions, marks) with new numbers, new circuits and twists. No figures? Describe a circuit as a gate table (DE mocks do this).

### `TOPICS.md` (the site builds the whole home page from this)

```
**Exam:** Tuesday 8 December. **2 hours. 4 questions, answer all ...**      ← first lines: the hub reads the date here

## 🔁 Relearn
(none yet)

## Chapter 1: Numbers and codes (Lectures 1 to 3)

| # | Topic | Slides | Tutorial and past-final Qs | Weight | Notes | Qs done |
|---|---|---|---|---|---|---|
| 1 | [Title](notes/01-slug.md) | L1 all | [L2 s22 · 2023 Q1a](questions/01-slug.md) | ●● | ☐ | ☐ |

## Past finals
| [Final 2023](papers/2023.md) (what's in it) | ☐ |

## Mock finals
| [Mock Final 1](mock/final-1.md) | ☐ |

## Skip / skim
...

---
**Progress:** 0 / N topics
```

- Chapter headings must be `## Chapter N: Title`. No `|` and no `[` inside the slides column or the link text.
- Paper and mock rows start with `|`, and their link text contains **Mock**, **Final** or **Wrap**.
- Weight: ●●● must know · ●● should know · ● skim · ✗ skip, from the tutorials **and** past finals. Only one past paper? Say the weights are a best guess.
- Update `tools/check_site_parse.js`'s chapter list (`[1,2,...,8]`) to your number of chapters.

### `PLAN.md`

Day-by-day tables from tomorrow to the exam: date, links, hours, ☐. Topics first, then past finals timed, then mocks, then a light last day ("stop by 8 pm"). **Go light around the user's other exams.** End with "If you fall behind, cut in this order" and "Never cut". **Check weekdays with Python.**

---

## 6. Porting the site

Copy `site/` and `index.html` from the template, then change:

| What | Where |
|---|---|
| `REPO_BLOB` | `https://github.com/lanceyprance/<Repo>/blob/main/` |
| **storage prefix** | `'de:'` → a **unique** short prefix (e.g. `'ce:'`). Replace every occurrence, including `'xx:pref:'`. |
| `FALLBACK_TOPICS` | `[n, title, slug, chapter]` |
| hero title and subtitle | in `viewHome`: subject, exam date, layout, formula sheet or not |
| drill subtitle | in `viewHome` |
| `tutOrder` | sort key for the drill: matches your tag style (`ChN QN`, `Lecture N, slide M`, `Final YYYY QN`) |
| tag regex in `finish()` | `(?:Tutorial|Final|Lecture|Study guide)`: add any new tag word you use |
| Past finals / mock subtitles | in `viewHome` ("official answers" or not, "formula sheet only" or "calculator only") |
| timer | 120 minutes by default; change if the exam length differs |
| `REP_SEED` | the user's 🔁 Relearn keys, or `[]` |
| `index.html` | `<title>`, description, logo letters (2 characters), brand text, the formula-sheet button label, the Periodic table tab only if relevant |
| `site/scramble.js` | start with `window.SCRAMBLE = {}; window.SCRAMBLE_FMT = x => String(x);` |

DE's other site changes (already in its `app.js`): references accept `Rule N` as well as `Equation N`; the "check your number" box only appears when the bold answer is a plain number (it would otherwise trip over Boolean expressions).

Run `node --check site/app.js` after editing.

---

## 7. Checks before you finish

```bash
python3 tools/check_links.py            # every relative link/image exists, <details> balanced
node tools/check_site_parse.js .        # site parsers over TOPICS, questions, papers, mocks: no NO ANSWER, no DUP
python3 tools/check_numbers.py          # rewritten for the new subject: every answer recomputed, no FAIL
grep -rni "midterm\|ssd\|EEEN20070\|EEEN20050\|digital" --include=*.md --include=*.js --include=*.html .   # template leftovers
```

Also check, with a short script (DE did this inline):
- every 📐 number is unique, and every `Rule N` / `Equation N` cited exists **in the topic it points to**;
- every true/false and multiple-choice question parses as `tf` / `mcq` (run `parseQuestions` from `app.js` in Node, as `check_site_parse.js` does).

**Things that were blocked in past sessions:**
- **`python3 -m http.server`** (both SSD and DE). Don't try. Use `check_site_parse.js` and tell the user you couldn't load the site in a browser.
- A long `python3 - <<'EOF' ... EOF` heredoc was once refused by a safety check that misread it. If that happens, write the script to the scratchpad with the Write tool and run the file.

---

## 8. Git and publishing

- Work on the branch the session names. Commit after each batch with a clear message, and push.
- **Ask the user before merging to `main`.** When they say yes: `git fetch origin main`, check `git merge-base --is-ancestor origin/main HEAD`, then `git push origin HEAD:main`.
- GitHub Pages: tell them Settings → Pages → branch `main`, folder `/ (root)`. You can't change that from the session.
- If the repo is public, warn once that it contains copyrighted slides and past papers.

---

## 9. Lessons (save yourself the time)

- **Past finals were the best material** on both SSD and DE. Put every past-final question into its topic's Part A, a worked example in its notes, and build mocks from them with new numbers and twists.
- **No official answers** (DE)? Write your own, verify them in Python, and say clearly in the paper's intro and the README that they're yours.
- **Read the slide's own text before writing a learn-by-heart list.** On DE, a list written from memory got the integration-scale numbers wrong. The notes had them right.
- Look for **hidden structure** in exam answers and say it: DE's 2023 Q3 reduced to one NOR + OR + NAND + XNOR; a mock's "two modes" turned out to be a Johnson counter; a gate in Q1 was redundant. Students remember these.
- Watch for slide typos (DE Lecture 10 slide 3 mux select) and constant mismatches (SSD ε values). Flag them with ⚠️ and log them in `questions-asked.md`.
- When a chapter has **no tutorial**, build its topics from the slides and the past-final questions, and say so in `TOPICS.md`.
- Name the student's files neutrally (`questions-asked.md`), not after a person.

---

## 10. The hub (next step after all subjects exist)

Not part of this job, but don't break it:

- All the Pages sites share one origin, `https://lanceyprance.github.io`, so a hub can `fetch('/<Repo>/TOPICS.md')` and every question file directly.
- The hub needs from each repo: the `TOPICS.md` format above, a **unique storage prefix**, and the exam date in the first lines of `TOPICS.md` (`**Exam:** Tuesday 8 December. …`).
- Tag words differ between repos (`Tutorial` / `Final` in SSD, also `Lecture` / `Study guide` in DE). The hub's parser should accept all of them.
- The user wants one **combined day plan** across all exams, giving the most time to the nearest exam.
- Probably a Computer Engineering subject next (the old SSD site linked to a CE site on albinjoby82's account): ask the user whether they want their own copy. The other remaining subject is unknown: ask.
