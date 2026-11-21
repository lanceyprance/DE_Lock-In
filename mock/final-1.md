# Mock Final 1

Same layout as the real paper: **2 hours, answer all four questions, 25 marks each.** The % next to each part is its share of that question.

Calculator allowed. No formula sheet.

New numbers and new circuits, built on the 2023 questions. Every answer was checked in Python (`tools/check_mocks.py`).

Do it **after** the topics and the 2023 paper. Timed, closed book.

---

## Questions

### Q1. Combinational logic — 25 marks

A circuit has inputs A, B, C, D and output F. Its gates are:

| Gate | Type | Inputs |
|---|---|---|
| G1 | NOR | A, C |
| G2 | AND | B, D' |
| G3 | NAND | A, B', D |
| G4 | OR | G1, G2 |
| F | AND | G3, G4 |

(a) Write a Boolean function for F in terms of A, B, C, D. (10%)

(b) Draw the truth table and the Karnaugh map. (30%)

(c) Express F as a sum of minterms and as a product of maxterms, in shorthand. (20%)

(d) Simplify F with the Karnaugh map and implement it with two-level NAND gates. NOT gates can be used. Comment on gate G3. (40%)

---

### Q2. Ripple counter and static hazards — 25 marks

(a) Design a three-bit binary ripple **count-up** counter using **positive-edge-triggered JK** flip-flops. Show the logic diagram and draw the output waveforms. The clock is 12 kHz: give the frequency at each output. (60%)

(b) Implement the function below without static-1 hazards, using a minimum number of gates. Show where the hazards are on the Karnaugh map.

F(A, B, C, D) = A'(D' + BD) + ABD (40%)

---

### Q3. Two-mode JK state machine — 25 marks

Use JK flip-flops and external gates to design a 3-bit synchronous state machine with two modes, set by its initial state:

| Mode 1 | Mode 2 |
|---|---|
| 000 → 011 → 101 → 110 → back to 000 | 001 → 010 → 100 → 111 → back to 001 |

Both modes must run on **one** circuit block. Show the design procedure, the state table, the logic functions and the logic diagram. Use the minimum number of flip-flops and external gates. (100%)

---

### Q4. Asynchronous sequential circuit — 25 marks

An asynchronous circuit has inputs A and B, one internal state y and an output z. Its logic is:

- AND gate 1: A' and B.
- AND gate 2: B and y'.
- OR gate: AND 1 and AND 2. Its output is Y, which is fed back as y.
- AND gate 3: A' and y. Its output is z.

(a) Derive the transition table and show it on a Karnaugh map. (40%)

(b) Obtain the flow table, with the output. (20%)

(c) Is there a stability issue? If so, where, and what happens? (40%)

---

## Answers

<details><summary>Q1 answers</summary>

**(a)** G1 = (A + C)'. G2 = BD'. G3 = (AB'D)'. G4 = (A + C)' + BD'.

**F = (AB'D)' · ((A + C)' + BD')**

From: Topic 6 §6

<br>

**(b)** (A + C)' = A'C'. So F = (AB'D)'(A'C' + BD').

Truth table (F = 1 rows only; all others 0): ABCD = 0000, 0001, 0100, 0101, 0110, 1100, 1110.

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 1 | 1 | 0 | 0 |
| **01** | 1 | 1 | 0 | 1 |
| **11** | 1 | 0 | 0 | 1 |
| **10** | 0 | 0 | 0 | 0 |

From: Topic 8 §4

<br>

**(c)** **F = Σm(0, 1, 4, 5, 6, 12, 14)**

**F = ΠM(2, 3, 7, 8, 9, 10, 11, 13, 15)**

From: Topic 7 §9, Topic 7 Rule 20

<br>

**(d)** Groups: cells 0, 1, 4, 5 → **A'C'**. Cells 4, 6, 12, 14 (columns 00 and 10 wrap) → **BD'**.

**F = A'C' + BD'**

Two-level NAND: G1 = NAND(A', C'), G2 = NAND(B, D'), F = NAND(G1, G2). Plus NOT gates for A', C', D'.

**G3 is redundant.** G3' = AB'D is never 1 when A'C' + BD' is 1 (A'C' needs A = 0, BD' needs D = 0). So F = G4, and G3 can be removed.

From: Topic 9 §11, Topic 9 Rule 26

</details>

<details><summary>Q2 answers</summary>

**(a)** Three positive-edge JK flip-flops, **J = K = 1** (toggle).

Positive edge, counting **up**: clock each stage from the previous **Q'** (Topic 16 Rule 47).

| Flip-flop | J, K | Clock |
|---|---|---|
| FF0 (Q₀) | 1, 1 | CLK |
| FF1 (Q₁) | 1, 1 | Q₀' |
| FF2 (Q₂) | 1, 1 | Q₁' |

Sequence 000 → 001 → 010 → ... → 111 → 000.

```
CLK  __‾‾__‾‾__‾‾__‾‾__‾‾__‾‾__‾‾__‾‾
Q0   __‾‾‾‾____‾‾‾‾____‾‾‾‾____‾‾‾‾__
Q1   ______‾‾‾‾‾‾‾‾________‾‾‾‾‾‾‾‾__
Q2   ______________‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾__
```

Frequencies: Q₀ = 12/2 = **6 kHz**, Q₁ = **3 kHz**, Q₂ = **1.5 kHz**.

From: Topic 16 §8, Topic 16 Rule 47, Topic 16 Equation 48

<br>

**(b)** F = A'D' + A'BD + ABD = Σm(0, 2, 4, 5, 6, 7, 13, 15).

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 1 | 0 | 0 | 1 |
| **01** | 1 | 1 | 1 | 1 |
| **11** | 0 | 1 | 1 | 0 |
| **10** | 0 | 0 | 0 | 0 |

Minimum SOP: **A'D' + BD**.

Hazards: cells 4–5 and 6–7 (D changes, A = 0, B = 1) are neighbours in different groups.

Add **A'B** (cells 4, 5, 6, 7).

**F = A'D' + BD + A'B**: 3 AND gates + 1 OR gate.

From: Topic 22 Rule 57

</details>

<details><summary>Q3 answers</summary>

**Step 1.** The two cycles use all 8 codes. One machine, start state picks the mode. **3** JK flip-flops A B C.

**Step 3.** Excitation:

| A B C | next | J_A K_A | J_B K_B | J_C K_C |
|---|---|---|---|---|
| 000 | 011 | 0 x | 1 x | 1 x |
| 001 | 010 | 0 x | 1 x | x 1 |
| 010 | 100 | 1 x | x 1 | 0 x |
| 011 | 101 | 1 x | x 1 | x 0 |
| 100 | 111 | x 0 | 1 x | 1 x |
| 101 | 110 | x 0 | 1 x | x 1 |
| 110 | 000 | x 1 | x 1 | 0 x |
| 111 | 001 | x 1 | x 1 | x 0 |

**Step 4.**

**J_A = K_A = B**

**J_B = K_B = 1**

**J_C = K_C = B'**

<br>

**Step 5.** One common clock. J_B = K_B tied to logic 1: B toggles every clock. J_A and K_A both wired to Q_B. J_C and K_C both wired to **Q_B'** (the flip-flop's own complement output).

**3 flip-flops, no external gates** (or one NOT gate if Q' isn't used).

Check: 000 → B toggles to 1, A holds (B = 0), C toggles (B' = 1) → 011 ✓.

From: Topic 15 §12, Topic 15 Rule 44

</details>

<details><summary>Q4 answers</summary>

**(a)** Y = A'B + By'. z = A'y.

| y \ AB | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | (0) | 1 | 1 | (0) |
| **1** | 0 | (1) | 0 | 0 |

From: Topic 21 Rule 55

<br>

**(b)** a = (y = 0), b = (y = 1). "next state, z" (z = A'y):

| \ AB | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **a** | (a), 0 | b, 0 | b, 0 | (a), 0 |
| **b** | a, 1 | (b), 1 | a, 0 | a, 0 |

From: Topic 21 §4

<br>

**(c)** **Yes**, in column **AB = 11**: in a, Y = 1 → b. In b, Y = By' = 0 → a. No stable state.

With A = B = 1 the circuit **oscillates** between a and b. The period is twice the delay round the loop.

Example: stable in b with AB = 01. A goes to 1 → AB = 11 → it oscillates.

From: Topic 21 Rule 56

</details>
