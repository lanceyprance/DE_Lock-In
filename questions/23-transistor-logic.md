# Topic 23: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 25, slides 15 to 18)

Explain how the CMOS NAND and the CMOS NOR gate work, case by case.

<details><summary>Answer</summary>

**NAND** (PMOS parallel on top, NMOS series below):

A = B = 1: both NMOS on, both PMOS off. Y connects to ground: **Y = 0**.

A or B = 0: one NMOS off (no path to ground), one PMOS on: **Y = 1**.

<br>

**NOR** (PMOS series on top, NMOS parallel below):

A = B = 0: both PMOS on, both NMOS off: **Y = 1**.

A or B = 1: one NMOS on, so Y connects to ground. The series PMOS path is broken: **Y = 0**.

From: §6, §7, Rule 59

</details>

---

### S2 (Lecture 25, slide 20)

How does the transmission-gate XOR work, and how many transistors does it use?

<details><summary>Answer</summary>

B controls the two transmission gates. When B = 0, TG1 closes and passes **A**. When B = 1, TG2 closes and passes **A'**.

So Y = A when B = 0, and Y = A' when B = 1: **Y = A ⊕ B**.

**8** transistors: 2 TGs (2 each) and 2 inverters (2 each).

From: §9

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. An NMOS transistor conducts when its gate is low.
2. In a CMOS NAND, the NMOS transistors are in series.
3. A CMOS inverter draws current all the time its output is low.
4. In negative logic, a high voltage means 0.
5. A 3-input CMOS NOR uses 6 transistors.

<details><summary>Answer</summary>

1. **False.** NMOS conducts when the gate is **high**. (Rule 59)
2. **True.** (§6)
3. **False.** One transistor is always off, so no steady current. That's the NMOS inverter's problem. (§5)
4. **True.** (§1)
5. **True.** 2n = 6. (§7)

</details>

---

### M2: Multiple choice

In a CMOS NOR gate, the PMOS transistors are connected:

- A. in parallel, between V_DD and the output
- B. in series, between V_DD and the output
- C. in series, between the output and ground
- D. in parallel, between the output and ground

<details><summary>Answer</summary>

**B.** NOR: PMOS in **series** on top (pull-up), NMOS in parallel below (pull-down).

From: §7

</details>

---

### M3: Transistor counts

Using CMOS, how many transistors for: a 2-input AND? A 4-input NAND? An inverter? A transmission-gate D latch?

<details><summary>Answer</summary>

2-input AND = NAND + NOT = 4 + 2 = **6** (2n + 2).

4-input NAND = **8** (2n).

Inverter = **2**.

D latch with transmission gates = **10** (from the slides).

From: §9, Topic 9 Rule 25

</details>

---

### M4: Analyse an NMOS circuit

An NMOS circuit has a load from V_DD to Y, and two NMOS transistors in series from Y to ground, with inputs A and B. Make the voltage table (H/L) and say which gate it is in positive logic and in negative logic.

<details><summary>Answer</summary>

Y is low only when **both** transistors are on, so A and B both high.

| A | B | Y |
|---|---|---|
| L | L | H |
| L | H | H |
| H | L | H |
| H | H | L |

**Positive logic** (H = 1): Y = 0 only for 11 → **NAND**.

**Negative logic** (H = 0): Y = 1 only for 00 → (A + B)' → **NOR**.

From: §1, §4

</details>

---

### M5: Explain

What is a transmission gate and why does it use both an NMOS and a PMOS?

<details><summary>Answer</summary>

A transmission gate is a **switch** made from an NMOS and a PMOS in parallel between two points X and Y.

N high and P low: both conduct, so X and Y are connected. N low and P high: both off, so they're disconnected.

Both types are used because together they pass **both** logic levels well (NMOS pulls down well, PMOS pulls up well), and the signal can go **either** way.

From: §8, Rule 59

</details>
