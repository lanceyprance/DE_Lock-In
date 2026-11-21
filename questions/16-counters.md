# Topic 16: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 17/18, slides 4 to 8)

Design a synchronous modulo-5 counter (000 → 001 → 010 → 011 → 100 → 000) with JK flip-flops A B C.

<details><summary>Answer</summary>

| A B C | next | J_A K_A | J_B K_B | J_C K_C |
|---|---|---|---|---|
| 000 | 001 | 0 x | 0 x | 1 x |
| 001 | 010 | 0 x | 1 x | x 1 |
| 010 | 011 | 0 x | x 0 | 1 x |
| 011 | 100 | 1 x | x 1 | x 1 |
| 100 | 000 | x 1 | 0 x | 0 x |

States 101, 110, 111 are x.

**J_A = BC, K_A = 1. J_B = C, K_B = C. J_C = A', K_C = 1.**

All three clock inputs on one common clock.

From: §2 to §4, Rule 46

</details>

---

### S2 (Lecture 17/18, slides 9 and 10)

For the S1 counter, where do the unused states 101, 110 and 111 go? Is that OK?

<details><summary>Answer</summary>

Put each into the equations:

101: J_A K_A = 01 → A = 0. J_B K_B = 11 → B toggles to 1. J_C K_C = 01 → C = 0. Next **010**.

110: J_A K_A = 01 → 0. J_B K_B = 00 → B stays 1. J_C K_C = 01 → 0. Next **010**.

111: J_A K_A = 11 → 0. J_B K_B = 11 → 0. J_C K_C = 01 → 0. Next **000**.

All three go into the main count. **OK**: the counter can't get stuck.

From: §5

</details>

---

### S3 (Lecture 17/18, slide 16)

How would the ripple counter change to count **down**? How would you build it with D flip-flops? With JK flip-flops?

<details><summary>Answer</summary>

**Down** (negative-edge flip-flops): clock each stage from the previous **Q'** instead of Q.

**D flip-flops:** wire **D = Q'** on each one, so it toggles.

**JK flip-flops:** tie **J = K = 1**, so it toggles.

From: Rule 47

</details>

---

### F2023-2a (Final 2023 Q2a)

Design a three-bit binary ripple count-down counter using D flip-flops. Show the logic diagram, draw the output waveforms and briefly explain how this circuit can be used as a frequency divider. [60%]

<details><summary>Answer</summary>

**Logic diagram:** three negative-edge D flip-flops. Each has **D = Q'** (toggles).

| Flip-flop | D | Clock |
|---|---|---|
| FF0 (Q₀) | Q₀' | CLK |
| FF1 (Q₁) | Q₁' | **Q₀'** |
| FF2 (Q₂) | Q₂' | **Q₁'** |

Common Reset to start at 000. (Positive-edge flip-flops: clock from Q₀ and Q₁ instead.)

<br>

**Sequence:** 000 → 111 → 110 → 101 → 100 → 011 → 010 → 001 → 000. That's **0, 7, 6, 5, 4, 3, 2, 1, 0**.

<br>

**Waveforms:**

```
CLK  ‾‾__‾‾__‾‾__‾‾__‾‾__‾‾__‾‾__‾‾__
Q0   __‾‾‾‾____‾‾‾‾____‾‾‾‾____‾‾‾‾__
Q1   __‾‾‾‾‾‾‾‾________‾‾‾‾‾‾‾‾______
Q2   __‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾______________
```

<br>

**Frequency divider:** each stage toggles half as often as the one before. Q₀ = **f/2**, Q₁ = **f/4**, Q₂ = **f/8**. Take the output from the stage you need.

From: §8, Rule 47, Equation 48

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. In a synchronous counter, every flip-flop gets the same clock.
2. A ripple counter made of D flip-flops needs D = Q on every stage.
3. Negative-edge flip-flops, each clocked from the previous Q, count up.
4. A 4-bit ripple counter divides the clock by 16 at its last stage.
5. A BCD counter has 16 states.
6. In a ripple counter, all outputs change at exactly the same moment.

<details><summary>Answer</summary>

1. **True.** (§2)
2. **False.** D = **Q'**, so it toggles. (Rule 47)
3. **True.** (Rule 47)
4. **True.** f₀/2⁴ = f₀/16. (Equation 48)
5. **False.** **10** states: 0 to 9. (§9)
6. **False.** Each stage waits for the one before it, so the changes ripple through with a small delay each. (§6)

</details>

---

### M2: Multiple choice

A 3-bit ripple counter uses positive-edge JK flip-flops with J = K = 1. Each stage is clocked from the previous Q'. It:

- A. counts up 0 to 7
- B. counts down 7 to 0
- C. counts up 0 to 5
- D. holds its value

<details><summary>Answer</summary>

**A.** Positive edge + clock from Q' counts **up** (Rule 47). 3 bits → 0 to 7.

From: Rule 47

</details>

---

### M3: Design a synchronous modulo-6 counter

Design a counter that goes 000 → 001 → 010 → 011 → 100 → 101 → 000 with T flip-flops A B C. Check the unused states.

<details><summary>Answer</summary>

T = 1 where the bit changes.

| A B C | next | T_A T_B T_C |
|---|---|---|
| 000 | 001 | 0 0 1 |
| 001 | 010 | 0 1 1 |
| 010 | 011 | 0 0 1 |
| 011 | 100 | 1 1 1 |
| 100 | 101 | 0 0 1 |
| 101 | 000 | 1 0 1 |

110, 111 → x.

<br>

**T_A = AC + BC**

**T_B = A'C**

**T_C = 1**

<br>

**Unused states:**

110: T_A T_B T_C = 0 0 1 → **111**.

111: T_A T_B T_C = 1 0 1 → **010**.

110 → 111 → 010, which is in the count. It self-starts ✓.

From: §5, Rule 46

</details>

---

### M4: Frequency divider

A 16 MHz clock drives a 4-bit binary ripple counter. What frequency comes out of each stage? How many flip-flops would you need to get 250 kHz?

<details><summary>Answer</summary>

f_k = 16 MHz / 2ᵏ:

Q₀ = **8 MHz**. Q₁ = **4 MHz**. Q₂ = **2 MHz**. Q₃ = **1 MHz**.

<br>

16 MHz / 250 kHz = 64 = 2⁶. So **6** flip-flops.

From: Equation 48

</details>

---

### M5: Explain

Give one advantage and one disadvantage of a ripple counter compared with a synchronous counter.

<details><summary>Answer</summary>

**Advantage:** it's very **simple**. No design or gates: each flip-flop just toggles and clocks the next.

**Disadvantage:** it's **slow**. The clock ripples through the flip-flops one after another, so the delay grows with every bit. While it ripples, the outputs pass through **wrong values** for a moment.

A synchronous counter changes all bits on the same edge, and can count **any** sequence.

From: §6, §2

</details>
