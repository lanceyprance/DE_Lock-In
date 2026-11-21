# Mock Final 3

Same layout as the real paper: **2 hours, answer all four questions, 25 marks each.** The % next to each part is its share of that question.

Calculator allowed. No formula sheet.

This one mixes in NOR logic, a count-down counter with T flip-flops, a D flip-flop state machine that turns out to be a Johnson counter, and a stable asynchronous latch. Every answer was checked in Python (`tools/check_mocks.py`).

Timed, closed book.

---

## Questions

### Q1. Combinational logic — 25 marks

A circuit has inputs X, Y, Z and output F:

- G1 = NAND(X, Y)
- G2 = OR(Y, Z')
- F = AND(G1, G2)

(a) Write a Boolean function for F. (10%)

(b) Draw the truth table and the Karnaugh map. (30%)

(c) Express F as a sum of minterms and as a product of maxterms, in shorthand. (20%)

(d) Find the minimum product of sums and implement it with two-level NOR gates. NOT gates can be used. Also give the minimum sum of products. (40%)

---

### Q2. Ripple counter and hazards — 25 marks

(a) Design a three-bit binary ripple **count-down** counter with **positive-edge-triggered T** flip-flops. Show the logic diagram and the waveforms. The clock is 1 MHz: give the frequency at each output. (50%)

(b) What is the difference between a static hazard and a dynamic hazard? Implement F(A, B, C, D) = B'C' + BD without static-1 hazards, using a minimum number of gates. (50%)

---

### Q3. Two-mode D flip-flop state machine — 25 marks

(a) Use **D** flip-flops to design a 3-bit synchronous state machine with two modes in one circuit block:

| Mode 1 | Mode 2 |
|---|---|
| 000 → 001 → 011 → 111 → 110 → 100 → back to 000 | 010 → 101 → back to 010 |

Give the state table, the D equations and the logic diagram. (70%)

(b) What well-known counter is this circuit? If you only wanted Mode 1, what problem would Mode 2 cause, and how do you fix it? (30%)

---

### Q4. Asynchronous sequential circuit — 25 marks

An asynchronous circuit has inputs A and B, one internal state y and output z:

Y = By + AB'

z = Ay

(a) Derive the transition table and show it on a Karnaugh map. (40%)

(b) Obtain the flow table, with the output. (20%)

(c) Is the circuit stable? Describe what the circuit does. (40%)

---

## Answers

<details><summary>Q1 answers</summary>

**(a)** **F = (XY)' · (Y + Z')**

From: Topic 6 §6

<br>

**(b)** (XY)' is 0 at 110, 111. (Y + Z') is 0 at 001, 101.

| X | Y | Z | F |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |

| X \ YZ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 1 | 0 | 1 | 1 |
| **1** | 1 | 0 | 0 | 0 |

From: Topic 8 §3

<br>

**(c)** **F = Σm(0, 2, 3, 4) = ΠM(1, 5, 6, 7)**

From: Topic 7 Rule 20

<br>

**(d)** Group the 0s: cells 001, 101 (Y = 0, Z = 1) → **(Y + Z')**. Cells 110, 111 (X = 1, Y = 1) → **(X' + Y')**.

**F = (Y + Z')(X' + Y')**

Two-level NOR: G1 = NOR(Y, Z'), G2 = NOR(X', Y'), F = NOR(G1, G2). NOT gates make Z', X', Y'.

Check: ((Y + Z')' + (X' + Y')')' = (Y + Z')(X' + Y') ✓.

Minimum SOP (group the 1s): cells 000, 100 → Y'Z'. Cells 010, 011 → X'Y. **F = X'Y + Y'Z'**.

From: Topic 9 §10, Topic 9 Rule 27, Topic 8 Rule 23

</details>

<details><summary>Q2 answers</summary>

**(a)** Three positive-edge T flip-flops, **T = 1** (toggle).

Positive edge, counting **down**: clock each stage from the previous **Q** (Topic 16 Rule 47).

| Flip-flop | T | Clock |
|---|---|---|
| FF0 (Q₀) | 1 | CLK |
| FF1 (Q₁) | 1 | Q₀ |
| FF2 (Q₂) | 1 | Q₁ |

Sequence 000 → 111 → 110 → 101 → 100 → 011 → 010 → 001 → 000.

```
CLK  __‾‾__‾‾__‾‾__‾‾__‾‾__‾‾__‾‾__‾‾
Q0   __‾‾‾‾____‾‾‾‾____‾‾‾‾____‾‾‾‾__
Q1   __‾‾‾‾‾‾‾‾________‾‾‾‾‾‾‾‾______
Q2   __‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾______________
```

Frequencies: Q₀ = **500 kHz**, Q₁ = **250 kHz**, Q₂ = **125 kHz**.

From: Topic 16 Rule 47, Topic 16 Equation 48

<br>

**(b)** **Static hazard:** the output should **not** change, but glitches once (1 → 0 → 1 or 0 → 1 → 0). **Dynamic hazard:** the output should change **once**, but changes three or more times (1 → 0 → 1 → 0).

F = B'C' + BD = Σm(0, 1, 5, 7, 8, 9, 13, 15).

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 1 | 1 | 0 | 0 |
| **01** | 0 | 1 | 1 | 0 |
| **11** | 0 | 1 | 1 | 0 |
| **10** | 1 | 1 | 0 | 0 |

Hazards: cells 1–5 and 9–13 (B changes, C = 0, D = 1) are in different groups.

Add **C'D** (cells 1, 5, 9, 13).

**F = B'C' + BD + C'D**: 3 AND gates + 1 OR gate.

From: Topic 22 §1, Topic 22 Rule 57

</details>

<details><summary>Q3 answers</summary>

**(a)** The two cycles use all 8 codes: one machine, the start state picks the mode.

D = next state:

| A B C | next A B C |
|---|---|
| 000 | 001 |
| 001 | 011 |
| 011 | 111 |
| 111 | 110 |
| 110 | 100 |
| 100 | 000 |
| 010 | 101 |
| 101 | 010 |

K-maps:

**D_A = B**

**D_B = C**

**D_C = A'**

Diagram: 3 D flip-flops, one clock. Q_B → D_A, Q_C → D_B, Q_A' → D_C. **No gates.**

From: Topic 15 §8, Topic 15 Rule 43

<br>

**(b)** It's a **3-bit Johnson counter** (switch-tail ring counter): a shift register (C → B → A) with the **complement** of the last stage (A') fed back into the first (C). 3 flip-flops → 6 states in Mode 1.

**Problem:** Mode 2 is the Johnson counter's **unused-state loop**. If it powers up in 010 or 101, it gets stuck there and never reaches the Mode 1 count.

**Fix:** reset all flip-flops to 000 at power-up (asynchronous reset), or add logic that sends 010 / 101 into the main cycle.

From: Topic 18 §3, Topic 18 §5

</details>

<details><summary>Q4 answers</summary>

**(a)**

| y \ AB | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | (0) | (0) | (0) | 1 |
| **1** | 0 | (1) | (1) | (1) |

From: Topic 21 Rule 55

<br>

**(b)** a = (y = 0), b = (y = 1). "next state, z" with z = Ay:

| \ AB | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **a** | (a), 0 | (a), 0 | (a), 0 | b, 0 |
| **b** | a, 0 | (b), 0 | (b), 1 | (b), 1 |

From: Topic 21 §4

<br>

**(c)** **Stable:** every column has at least one circled state.

It's a **latch**:
- AB = 10 **sets** y to 1.
- AB = 00 **resets** y to 0.
- B = 1 (AB = 01 or 11) **holds** y.

The output z = Ay is 1 only when the latch is set and A = 1.

From: Topic 21 Rule 56

</details>
