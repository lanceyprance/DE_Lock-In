# Topic 22: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 23/24, slides 33 to 36)

Y = x₁x₂ + x₂'x₃. Show where the static-1 hazard is and remove it.

<details><summary>Answer</summary>

On the K-map, x₁x₂ covers 110, 111. x₂'x₃ covers 001, 101.

Cells **111** and **101** are neighbours (x₂ changes) but in different groups. With x₁ = x₃ = 1, when x₂ falls, gate x₁x₂ turns off before x₂'x₃ turns on: Y glitches to 0.

Add the term covering both: **x₁x₃**.

**Y = x₁x₂ + x₂'x₃ + x₁x₃**

From: §3, §4, Rule 57

</details>

---

### S2 (Lecture 23/24, slide 38)

Y = (x₁ + x₂')(x₂ + x₃). Remove the static-0 hazard.

<details><summary>Answer</summary>

The 0s: (x₁ + x₂') is 0 at 010, 011. (x₂ + x₃) is 0 at 000, 100.

Cells **000** and **010** are neighbouring 0s in different sum terms. With x₁ = x₃ = 0, a change of x₂ can make Y spike to 1.

Add the sum term covering both: **(x₁ + x₃)**.

**Y = (x₁ + x₂')(x₂ + x₃)(x₁ + x₃)**

From: §5, Rule 58

</details>

---

### F2023-2b (Final 2023 Q2b)

Briefly explain what causes static hazards in digital circuits. Implement the function below without static-1 hazards, using a minimum number of gates: F(A, B, C, D) = AB'(D' + CD) + A'(B + CD) + A'CD' [40%]

<details><summary>Answer</summary>

**Cause:** different paths have different **propagation delays**, especially a signal and its inverted copy. When an input changes, one product term can turn off before another turns on, so the output dips to 0 for a moment when it should stay 1.

<br>

**K-map** (AB rows, CD columns):

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 0 | 0 | 1 | 1 |
| **01** | 1 | 1 | 1 | 1 |
| **11** | 0 | 0 | 0 | 0 |
| **10** | 1 | 0 | 1 | 1 |

F = Σm(2, 3, 4, 5, 6, 7, 8, 10, 11).

Minimum SOP: **A'B + B'C + AB'D'**.

Hazards: pairs 2–6 and 3–7 are neighbours in different groups.

Add **A'C** (cells 2, 3, 6, 7).

**F = A'B + B'C + AB'D' + A'C**

4 AND gates + 1 OR gate (plus inverters).

From: §6, Rule 57

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. A static-1 hazard is a momentary 0 when the output should stay at 1.
2. Static-1 hazards are typical of POS circuits.
3. Adding a redundant term changes the Boolean function.
4. A dynamic hazard changes the output three or more times.
5. Hazards are caused by unequal delays on different paths.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **False.** Static-1 hazards come from **SOP** (AND-OR). POS gives static-0. (§5)
3. **False.** The function stays the same. The term only fixes the timing. (§4)
4. **True.** (§1)
5. **True.** (§2)

</details>

---

### M2: Multiple choice

F = AB' + BC. Which term removes its static-1 hazard?

- A. AB
- B. AC
- C. B'C
- D. A'C

<details><summary>Answer</summary>

**B.** Consensus of AB' and BC (B is the variable that flips): **AC**.

From: Rule 57

</details>

---

### M3: Hazard-free SOP

F(A, B, C) = A'B' + BC. Find any static-1 hazard and give a hazard-free circuit.

<details><summary>Answer</summary>

K-map (A rows, BC columns):

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 1 | 1 | 1 | 0 |
| **1** | 0 | 0 | 1 | 0 |

A'B' covers 000, 001. BC covers 011, 111.

**001** and **011** are neighbours (B changes, A = 0, C = 1) in different groups. Hazard.

Add **A'C** (covers 001, 011).

**F = A'B' + BC + A'C**

3 AND gates + 1 OR gate.

From: Rule 57

</details>

---

### M4: Hazard-free POS

F = (A + B)(A' + C). Find the static-0 hazard and remove it.

<details><summary>Answer</summary>

The 0s: (A + B) = 0 at 000, 001. (A' + C) = 0 at 100, 110.

**000** and **100** are neighbouring 0s (A changes, B = C = 0) in different sum terms. Hazard.

Add the consensus **(B + C)** (0 at 000 and 100).

**F = (A + B)(A' + C)(B + C)**

From: Rule 58

</details>

---

### M5: Explain

Why do hazards matter more in asynchronous circuits than in synchronous ones?

<details><summary>Answer</summary>

In a **synchronous** circuit, flip-flops only look at their inputs on the clock edge. A short glitch between edges is usually ignored, as long as it has settled by the edge.

In an **asynchronous** circuit there's no clock. A glitch on a feedback line is seen **straight away** and can send the circuit to the **wrong state**.

From: §1, Topic 21 §8

</details>
