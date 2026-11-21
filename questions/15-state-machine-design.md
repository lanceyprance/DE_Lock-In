# Topic 15: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Excitation (Rule 44): D = next. T = 1 if the bit changes. JK: 0→0 = 0x, 0→1 = 1x, 1→0 = x1, 1→1 = x0.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 14/15/16, slides 6 to 20)

Design a Mealy sequence detector for **1001** (overlapping allowed) with JK flip-flops. One input X, one output Z.

Give the state diagram, state table, JK equations and Z.

<details><summary>Answer</summary>

**States:** A = nothing (00), B = 1 (01), C = 10 (10), D = 100 (11).

**Arrows:** A: 0/0 → A, 1/0 → B. B: 0/0 → C, 1/0 → B. C: 0/0 → D, 1/0 → B. D: 0/0 → A, **1/1 → B**.

<br>

| Q1 Q0 | X | next | J1 K1 | J0 K0 | Z |
|---|---|---|---|---|---|
| 00 | 0 | 00 | 0 x | 0 x | 0 |
| 00 | 1 | 01 | 0 x | 1 x | 0 |
| 01 | 0 | 10 | 1 x | x 1 | 0 |
| 01 | 1 | 01 | 0 x | x 0 | 0 |
| 10 | 0 | 11 | x 0 | 1 x | 0 |
| 10 | 1 | 01 | x 1 | 1 x | 0 |
| 11 | 0 | 00 | x 1 | x 1 | 0 |
| 11 | 1 | 01 | x 1 | x 0 | 1 |

<br>

**J1 = X'Q0. K1 = X + Q0. J0 = X + Q1. K0 = X'. Z = Q1Q0X.**

From: §3 to §7, Rule 43, Rule 44

</details>

---

### S2 (Lecture 14/15/16, slides 21 to 24)

Build the same 1001 detector with D flip-flops.

<details><summary>Answer</summary>

D = the next-state column of S1.

D1 = 1 in rows 010, 100. D0 = 1 in rows 001, 011, 100, 101, 111.

**D1 = Q1Q0'X' + Q1'Q0X'**

**D0 = X + Q1Q0'**

**Z = Q1Q0X**

From: §8

</details>

---

### S3 (Lecture 14/15/16, slides 26 to 32)

Why does the Moore version of the 1001 detector need 5 states and 3 flip-flops, when the Mealy version needs 4 states and 2?

<details><summary>Answer</summary>

A Moore output depends on the **state only**. So "1001 has just been seen" must be its **own state** (E, output 1).

The Mealy version puts the output on the D → B arrow instead, so it doesn't need E.

5 states need log₂ 5 → **3** flip-flops. The 3 unused codes (101, 110, 111) become don't cares.

From: §1, §9, Rule 45

</details>

---

### S4 (Lecture 14/15/16, slides 33 to 35)

A Mealy circuit has one input and two outputs. It outputs 01 when it sees **1011** and 10 when it sees **1110** (overlapping allowed), and 00 otherwise. Give the state meanings and the arrows out of D (seen 101) and H (seen 111).

<details><summary>Answer</summary>

States: **A** nothing, **B** 1, **C** 10, **D** 101, **G** 11, **H** 111.

From D: on 0 → **C**, output 00 (1010 ends in 10). On 1 → **G**, output **01** (1011 found; it ends in 11).

From H: on 0 → **C**, output **10** (1110 found; it ends in 10). On 1 → **H**, output 00 (1111 ends in 111).

6 states → 3 flip-flops.

From: §11

</details>

---

### F2023-3 (Final 2023 Q3)

Use JK flip-flops and external gates to design a 3-bit synchronous binary state machine with two modes, depending on its initial state.

Mode 1: initial state 011. It cycles 011 → 001 → 010 → 000 → 100 → back to 011.

Mode 2: initial state 111. It cycles 111 → 110 → 101 → back to 111.

The two modes must use **one** circuit block. Show the design procedure, give the state table and logic functions, and sketch the logic diagram. Use the minimum number of flip-flops and gates. [100%]

<details><summary>Answer</summary>

**Step 1.** The two cycles use all 8 codes once. So one state diagram holds both. The start state picks the mode.

**Step 2.** 8 states → **3** JK flip-flops, A B C.

<br>

**Step 3.**

| A B C | next | J_A K_A | J_B K_B | J_C K_C |
|---|---|---|---|---|
| 000 | 100 | 1 x | 0 x | 0 x |
| 001 | 010 | 0 x | 1 x | x 1 |
| 010 | 000 | 0 x | x 1 | 0 x |
| 011 | 001 | 0 x | x 1 | x 0 |
| 100 | 011 | x 1 | 1 x | 1 x |
| 101 | 111 | x 0 | 1 x | x 0 |
| 110 | 101 | x 0 | x 1 | 1 x |
| 111 | 110 | x 0 | x 0 | x 1 |

<br>

**Step 4.** K-maps:

**J_A = K_A = B'C'** = (B + C)'

**J_B = A + C**

**K_B = A' + C'** = (AC)'

**J_C = A**

**K_C = AB + A'B'** = (A ⊕ B)'

<br>

**Step 5.** 3 JK flip-flops on one clock. One NOR (B, C) feeds J_A and K_A. One OR (A, C) → J_B. One NAND (A, C) → K_B. J_C wired to Q_A. One XNOR (A, B) → K_C. **4 gates.**

<br>

**Check:** analysing it back gives 011 → 001 → 010 → 000 → 100 → 011 and 111 → 110 → 101 → 111.

From: §12, Rule 43, Rule 44

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. A JK flip-flop going from 0 to 1 needs J = 1, K = 1.
2. A T flip-flop needs T = 1 whenever its bit changes.
3. In a Moore machine, the output is written on the arrows.
4. A machine with 6 states needs at least 3 flip-flops.
5. Unused states can be treated as don't cares in the K-maps.
6. D flip-flops usually give more don't cares than JK flip-flops.

<details><summary>Answer</summary>

1. **False.** J = 1, K = **x**. Set (10) or toggle (11) both work. (Rule 44)
2. **True.** (Rule 44)
3. **False.** Moore outputs go **inside** the circles. Mealy outputs go on arrows. (Rule 45)
4. **True.** log₂ 6 ≈ 2.6, round up to 3. (Rule 43)
5. **True.** But check they lead back into the cycle. (§10)
6. **False.** JK gives the don't cares. D has none. (§8)

</details>

---

### M2: Multiple choice

A flip-flop must go from Q = 1 to Q = 1. Which inputs are right?

- A. D = 0
- B. J = x, K = 0
- C. T = 1
- D. J = 1, K = x

<details><summary>Answer</summary>

**B.** 1 → 1 with JK: hold (00) or set (10). K = 0 in both, J can be anything.

(D would need D = 1. T would need T = 0.)

From: Rule 44

</details>

---

### M3: Design a 101 detector

Design a Mealy circuit with input X and output Z. Z = 1 when the last three inputs were **101**. Overlapping is allowed. Use D flip-flops.

<details><summary>Answer</summary>

**Step 1.** States: S0 = nothing, S1 = seen 1, S2 = seen 10.

S0: 0/0 → S0, 1/0 → S1.

S1: 0/0 → S2, 1/0 → S1.

S2: 0/0 → S0, **1/1 → S1** (101 found; the last 1 can start the next one).

<br>

**Step 2.** 3 states → 2 flip-flops. S0 = 00, S1 = 01, S2 = 10. Code 11 is unused (x).

<br>

**Step 3.**

| Q1 Q0 | X | next = D1 D0 | Z |
|---|---|---|---|
| 00 | 0 | 00 | 0 |
| 00 | 1 | 01 | 0 |
| 01 | 0 | 10 | 0 |
| 01 | 1 | 01 | 0 |
| 10 | 0 | 00 | 0 |
| 10 | 1 | 01 | 1 |
| 11 | x | xx | x |

<br>

**Step 4.**

**D1 = Q0X'**

**D0 = X**

**Z = Q1X**

<br>

**Check the unused state 11:** X = 0 → D1D0 = 10 (S2). X = 1 → 01 (S1). It returns to the cycle ✓.

From: §3, §8, §10, Rule 43

</details>

---

### M4: Two modes with D flip-flops

Design a 3-bit synchronous machine with D flip-flops and one circuit block.

Mode 1 cycles 000 → 001 → 011 → 010 → 000.

Mode 2 cycles 100 → 110 → 111 → 101 → 100.

<details><summary>Answer</summary>

**Step 1.** The two cycles use all 8 codes. One machine, the start state picks the mode.

<br>

**Step 3.** D = next state.

| A B C | next A B C |
|---|---|
| 000 | 001 |
| 001 | 011 |
| 010 | 000 |
| 011 | 010 |
| 100 | 110 |
| 101 | 100 |
| 110 | 111 |
| 111 | 101 |

<br>

**Step 4.** K-maps:

D_A: next A = A in every row. **D_A = A** (a wire: A never changes).

D_B: 1 at 001, 011, 100, 110 → A'C + AC'. **D_B = A ⊕ C**

D_C: 1 at 000, 001, 110, 111 → A'B' + AB. **D_C = (A ⊕ B)'**

<br>

**Step 5.** 3 D flip-flops, one common clock. D_A from Q_A. One XOR (A, C) → D_B. One XNOR (A, B) → D_C. **2 gates.**

From: §8, §12, Rule 43

</details>

---

### M5: Explain

1. Why do JK flip-flops often give simpler input equations than D flip-flops?
2. Why are D flip-flops still used more in practice?

<details><summary>Answer</summary>

**1.** The JK excitation table has an **x** in every row. Half the K-map cells are don't cares, so groups get bigger and terms get shorter.

**2.** D has **one** input instead of two. There's **no excitation table** (D = next state). And a D flip-flop needs slightly **less hardware**.

From: §8

</details>
