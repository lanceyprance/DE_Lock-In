# Mock Final 2

Same layout as the real paper: **2 hours, answer all four questions, 25 marks each.** The % next to each part is its share of that question.

Calculator allowed. No formula sheet.

This one adds the twists the 2023 paper didn't use: don't cares, NOR gates, a synchronous counter with unused states, static-0 hazards, a sequence detector and a race. Every answer was checked in Python (`tools/check_mocks.py`).

Timed, closed book.

---

## Questions

### Q1. K-maps with don't cares — 25 marks

F(A, B, C, D) = Σm(1, 3, 7, 11, 15). The input combinations 0, 2 and 5 never occur: d(0, 2, 5).

(a) Draw the Karnaugh map. (20%)

(b) Find the minimum sum of products, using the don't cares. (25%)

(c) Find the minimum product of sums, using the don't cares. (25%)

(d) Implement the minimum product of sums with two-level NOR gates. NOT gates can be used. (30%)

---

### Q2. Synchronous counter and static-0 hazards — 25 marks

(a) Design a synchronous counter with JK flip-flops A B C that goes through the sequence 000 → 010 → 011 → 101 → 110 → back to 000. Give the state table, the JK equations and the logic diagram. Show what happens if the counter powers up in an unused state. (60%)

(b) F(A, B, C, D) = (A + C)(A' + B)(B' + D'). Explain what a static-0 hazard is, find the static-0 hazards on the Karnaugh map, and give a hazard-free product of sums. (40%)

---

### Q3. Sequence detector — 25 marks

Design a Mealy sequence detector with one input X and one output Z. Z = 1 when the last four inputs were **1101**. Overlapping sequences must be detected. Use **JK** flip-flops.

Give the state diagram, the state table with the state assignment, the JK equations, the output equation and the logic diagram. Show the output for the input 1101101011. (100%)

---

### Q4. Asynchronous circuit with two state variables — 25 marks

An asynchronous circuit has one input x and two feedback loops:

Y₁ = x(y₁ + y₂')

Y₂ = x(y₁' + y₂)

(a) Derive the transition table and circle the stable states. (40%)

(b) Obtain the flow table, naming the states a = 00, b = 01, c = 11, d = 10. (20%)

(c) The circuit is stable with x = 0. Then x changes to 1. Explain what happens. Is there a race? Is it critical? (40%)

---

## Answers

<details><summary>Q1 answers</summary>

**(a)**

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | x | 1 | 1 | x |
| **01** | 0 | x | 1 | 0 |
| **11** | 0 | 0 | 1 | 0 |
| **10** | 0 | 0 | 1 | 0 |

From: Topic 9 §1

<br>

**(b)** Column CD = 11 (cells 3, 7, 15, 11) → **CD**. Row AB = 00 (cells 0, 1, 3, 2, using x at 0 and 2) → **A'B'**.

**F = CD + A'B'**

From: Topic 9 Rule 24

<br>

**(c)** Group the 0s (x at 0 and 2 now count as 0):

Columns CD = 00 and 10 (cells 0, 2, 4, 6, 8, 10, 12, 14) → D = 0 → **(D)**.

Cells 8, 9, 12, 13 (A = 1, C = 0) → **(A' + C)**.

**F = D(A' + C)**

(The two answers treat the don't cares differently. Both are correct for the cells that matter.)

From: Topic 8 Rule 23

<br>

**(d)** Two-level NOR (Topic 9 Rule 27):

Gate 1 = NOR(A', C) = (A' + C)'.

D goes straight to the output gate, so feed in **D'**.

Output = NOR(D', gate 1) = (D' + (A' + C)')' = **D(A' + C)** ✓.

2 NOR gates + NOT gates for A' and D'.

From: Topic 9 §10, Topic 9 Rule 27

</details>

<details><summary>Q2 answers</summary>

**(a)** Unused states: 001, 100, 111 → x.

| A B C | next | J_A K_A | J_B K_B | J_C K_C |
|---|---|---|---|---|
| 000 | 010 | 0 x | 1 x | 0 x |
| 010 | 011 | 0 x | x 0 | 1 x |
| 011 | 101 | 1 x | x 1 | x 0 |
| 101 | 110 | x 0 | 1 x | x 1 |
| 110 | 000 | x 1 | x 1 | 0 x |

K-maps (with the x's):

**J_A = C, K_A = C'**

**J_B = 1, K_B = A + C**

**J_C = A'B, K_C = B'**

Diagram: 3 JK flip-flops, one common clock. J_A from Q_C, K_A from Q_C'. J_B tied to 1. One OR (A, C) → K_B. One AND (A', B) → J_C. K_C from Q_B'.

<br>

**Unused states:**

001: J_A K_A = 10 → A = 1. J_B K_B = 11 → B = 1. J_C K_C = 01 → C = 0. → **110**.

100: J_A K_A = 01 → 0. J_B K_B = 11 → 1. J_C K_C = 01 → 0. → **010**.

111: J_A K_A = 10 → 1. J_B K_B = 11 → 0. J_C K_C = 00 → 1. → **101**.

All three go into the count. It **self-starts** ✓.

From: Topic 16 Rule 46, Topic 16 §5

<br>

**(b)** A **static-0 hazard**: the output should stay 0 but jumps to 1 for a moment, because two paths have different delays. It happens in POS (OR-AND) circuits.

The 0s: (A + C) at 0, 1, 4, 5. (A' + B) at 8, 9, 10, 11. (B' + D') at 5, 7, 13, 15.

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 0 | 0 | 1 | 1 |
| **01** | 0 | 0 | 0 | 1 |
| **11** | 1 | 0 | 0 | 1 |
| **10** | 0 | 0 | 0 | 0 |

Neighbouring 0s in different sum terms:

- 0 – 8 and 1 – 9 (A changes, B = C = 0) → add **(B + C)**.
- 9 – 13 and 11 – 15 (B changes, A = D = 1) → add **(A' + D')**.

**F = (A + C)(A' + B)(B' + D')(B + C)(A' + D')**

From: Topic 22 §5, Topic 22 Rule 58

</details>

<details><summary>Q3 answers</summary>

**States:** A = nothing (00), B = seen 1 (01), C = seen 11 (10), D = seen 110 (11).

**State diagram (input/output):**

A: 0/0 → A, 1/0 → B.

B: 0/0 → A, 1/0 → C.

C: 0/0 → D, 1/0 → C (111 still ends in 11).

D: 0/0 → A (1100 has none of the pattern left), **1/1 → B** (1101 found; the last 1 starts the next one).

<br>

**State table and JK inputs** (Q1 Q0):

| Q1 Q0 | X | next | J1 K1 | J0 K0 | Z |
|---|---|---|---|---|---|
| 00 | 0 | 00 | 0 x | 0 x | 0 |
| 00 | 1 | 01 | 0 x | 1 x | 0 |
| 01 | 0 | 00 | 0 x | x 1 | 0 |
| 01 | 1 | 10 | 1 x | x 1 | 0 |
| 10 | 0 | 11 | x 0 | 1 x | 0 |
| 10 | 1 | 10 | x 0 | 0 x | 0 |
| 11 | 0 | 00 | x 1 | x 1 | 0 |
| 11 | 1 | 01 | x 1 | x 0 | 1 |

<br>

**Equations:**

**J1 = Q0X. K1 = Q0.**

**J0 = Q1 ⊕ X. K0 = Q1' + X'.**

**Z = Q1Q0X**

Diagram: 2 JK flip-flops, one clock. One AND (Q0, X) → J1. K1 from Q0. One XOR (Q1, X) → J0. One NAND (Q1, X) → K0. One 3-input AND → Z.

<br>

**Input 1101101011:**

| X | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|
| Z | 0 | 0 | 0 | **1** | 0 | 0 | **1** | 0 | 0 | 0 |

The two 1101s overlap by one bit.

From: Topic 15 §3, Topic 15 Rule 43, Topic 15 Rule 44

</details>

<details><summary>Q4 answers</summary>

**(a)** With x = 0, both Y's are 0. With x = 1, Y₁ = y₁ + y₂' and Y₂ = y₁' + y₂.

| y₁y₂ \ x | 0 | 1 |
|---|---|---|
| **00** | (00) | 11 |
| **01** | 00 | (01) |
| **11** | 00 | (11) |
| **10** | 00 | (10) |

From: Topic 21 Rule 55

<br>

**(b)**

| \ x | 0 | 1 |
|---|---|---|
| **a** | (a) | c |
| **b** | a | (b) |
| **c** | a | (c) |
| **d** | a | (d) |

From: Topic 21 §4

<br>

**(c)** With x = 0 the only stable state is **a = 00**.

x goes to 1: row 00 says go to **11**. **Both** y₁ and y₂ must change: a **race**.

- If y₁ changes first: 00 → **10**. Row 10, x = 1 is stable. It stops in **d**.
- If y₂ changes first: 00 → **01**. Row 01, x = 1 is stable. It stops in **b**.
- If both change together: it reaches **11** (c), as intended.

It can end in three different stable states. It's a **critical race**.

Fix: choose a state assignment where every transition changes only one variable.

From: Topic 21 §7

</details>
