# Topic 17: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 19, slide 11)

How can a shift register be used as a sequence detector? Give the gate for the pattern 110.

<details><summary>Answer</summary>

A shift register always holds the **last n input bits**. Decode them with one AND gate.

For 110 in a 3-bit register (oldest bit Q₂, newest Q₀): Z = **Q₂ Q₁ Q₀'**.

Z = 1 exactly when the last three bits were 1, 1, 0.

From: §4

</details>

---

### S2 (Lecture 19, slides 13 and 14)

Register A = 1011 and register B = 0010. A's serial output feeds B's serial input and also A's own input. Give both registers after 4 shift pulses.

<details><summary>Answer</summary>

| | A | B |
|---|---|---|
| start | 1011 | 0010 |
| T₁ | 1101 | 1001 |
| T₂ | 1110 | 1100 |
| T₃ | 0111 | 0110 |
| T₄ | **1011** | **1011** |

B now holds A's word. A has its own word back, because its output was fed back to its input.

From: §6

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. A 6-bit shift register needs 6 clocks to load a word serially.
2. In a parallel load register, Load = 0 clears the register.
3. A serial adder for n-bit numbers needs n full adders.
4. In the universal shift register, s₁s₀ = 11 is parallel load.
5. All flip-flops in a register share one clock.

<details><summary>Answer</summary>

1. **True.** One bit per clock. (Rule 50)
2. **False.** Load = 0 **holds** the old value (D = Q). Clear is a separate input. (Rule 49)
3. **False.** **One** full adder, plus a D flip-flop for the carry. (§7)
4. **True.** (§8)
5. **True.** (§1)

</details>

---

### M2: Multiple choice

A 4-bit register shifts **right**. It holds 0110 and the serial input is 1. After one clock it holds:

- A. 1100
- B. 1011
- C. 0011
- D. 1101

<details><summary>Answer</summary>

**B.** The new bit 1 enters on the left. 0110 moves right one place and the last 0 drops out: **1011**.

From: Rule 50

</details>

---

### M3: Trace a shift register

A 4-bit right-shift register starts at 0000. The serial input gets 1, 1, 0, 1, 0, 0 (one bit per clock). Give the contents after each clock and the serial output bits.

<details><summary>Answer</summary>

| Clock | SI | Contents | SO (bit that drops out) |
|---|---|---|---|
| 1 | 1 | 1000 | 0 |
| 2 | 1 | 1100 | 0 |
| 3 | 0 | 0110 | 0 |
| 4 | 1 | 1011 | 0 |
| 5 | 0 | 0101 | 1 |
| 6 | 0 | 0010 | 1 |

From clock 5, the first bits in (1, 1) come out the other end.

From: Rule 50

</details>

---

### M4: One stage of a parallel load register

Write the D input of one stage. Draw it with gates.

<details><summary>Answer</summary>

**D = L·I + L'·Q**

Gates: one AND (L, I), one AND (L', Q), one OR of the two, into D. One NOT makes L' (shared by all stages).

It's a 2-to-1 mux with L as the select line.

From: Rule 49

</details>

---

### M5: Explain

Explain how a serial adder adds two 8-bit numbers.

<details><summary>Answer</summary>

The two numbers sit in two shift registers. On each clock, both shift out their **lowest** bit into one **full adder**.

The full adder's sum bit is shifted into a result register (or back into register A).

Its carry out is stored in a **D flip-flop**, and fed back as the carry in on the **next** clock.

After **8 clocks**, the whole sum is in the result register.

From: §7

</details>
