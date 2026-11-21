# Topic 13: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

The slides set no exercises here. Part A is built from the slide examples.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 11/12, slides 10 and 11)

A NOR SR latch starts with Q = 0, Q' = 1. Then S = 1, R = 0.

1. Which output changes first?
2. How many gate delays until Q = 1?
3. What happens after that?

<details><summary>Answer</summary>

1. **Q'** changes first. S = 1 forces Q' = (1 + Q)' = 0.
2. **Two** gate delays. Q' falls after one. Then Q = (R + Q')' = (0 + 0)' = 1 after the second.
3. It **stays** there. Q = 1, Q' = 0 is a stable state until S or R changes.

From: §2, Rule 38

</details>

---

### S2 (Lecture 11/12, slide 13)

Explain why S = R = 1 must be avoided in a NOR latch.

<details><summary>Answer</summary>

With S = R = 1, **both** Q and Q' become 0. They are no longer complements.

If S and R then drop to 0 **together**, both gates see 0 + 0 and both outputs go to 1. Then both see a 1 and go to 0. The latch **oscillates** forever.

So the state is **indeterminate**.

From: §3, Rule 38

</details>

---

### S3 (Lecture 11/12, slides 34 to 36)

Use the JK characteristic equation to find Q_t+1 for J = K = 0 and for J = K = 1.

<details><summary>Answer</summary>

Q_t+1 = JQ' + K'Q.

J = K = 0: Q_t+1 = 0·Q' + 1·Q = **Q** (no change).

J = K = 1: Q_t+1 = 1·Q' + 0·Q = **Q'** (toggle).

From: §10, Equation 39

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. A latch changes only on a clock edge.
2. In a NAND latch, S' = R' = 1 holds the stored value.
3. A JK flip-flop with J = K = 1 toggles on each clock edge.
4. A D flip-flop has a forbidden input combination.
5. A master-slave flip-flop built as on the slides changes on the falling clock edge.
6. A T flip-flop can be made from a JK by tying J and K together.

<details><summary>Answer</summary>

1. **False.** A latch follows its inputs for the whole time it's enabled. That's a flip-flop's job. (§6, Rule 40)
2. **True.** Active-low inputs: 1 means "do nothing". (§5)
3. **True.** (§10)
4. **False.** D feeds S, and D' feeds R, so S = R = 1 can't happen. (§8)
5. **True.** The slave copies the master when the clock goes 1 → 0. (§7)
6. **True.** J = K = T. (§11)

</details>

---

### M2: Multiple choice

Q = 1. A JK flip-flop has J = 0, K = 1. After the clock edge, Q is:

- A. 1
- B. 0
- C. it toggles to 0, then back to 1
- D. indeterminate

<details><summary>Answer</summary>

**B.** JK = 01 is **reset**: Q = 0 whatever it was before.

From: §10

</details>

---

### M3: Fill the table

A T flip-flop starts at Q = 0. Give Q after each clock edge for T = 1, 1, 0, 1, 0, 1.

<details><summary>Answer</summary>

T = 1 toggles, T = 0 holds.

| Edge | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| T | 1 | 1 | 0 | 1 | 0 | 1 |
| Q | 1 | 0 | 0 | 1 | 1 | 0 |

**Q = 1, 0, 0, 1, 1, 0**

From: §11, Equation 39

</details>

---

### M4: Build one flip-flop from another

1. Make a T flip-flop from a D flip-flop.
2. Make a D latch from an SR latch.

<details><summary>Answer</summary>

**1.** T toggles when T = 1. So D must equal Q' when T = 1, and Q when T = 0.

**D = T ⊕ Q** (one XOR gate in front of the D flip-flop).

<br>

**2.** Feed D to S, and D through an inverter to R. Add an enable C with two AND gates.

**S = CD, R = CD'**. Now S = R = 1 can't happen.

From: §8, §11

</details>

---

### M5: Explain

1. What is the difference between combinational and sequential logic?
2. Why does level triggering cause problems, and how does a master-slave flip-flop fix it?

<details><summary>Answer</summary>

**1.** Combinational: the outputs depend **only** on the inputs now. Sequential: the outputs depend on the inputs **and** the stored state (memory).

<br>

**2.** A level-triggered latch is enabled for the whole time the clock is high. Its output can change **several times** in one clock period, in an unpredictable way.

A master-slave flip-flop uses two latches and an inverter, so only one is enabled at a time. The master takes the input while the clock is high. The slave copies it when the clock falls. The output changes **once**, on the edge.

From: §1, §6, §7, Rule 40

</details>
