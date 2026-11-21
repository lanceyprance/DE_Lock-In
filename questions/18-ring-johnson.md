# Topic 18: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 20, slide 10)

Use a 3-bit Johnson counter and external gates to design a binary counter counting 0 to 5. Show the design procedure and give the circuit.

<details><summary>Answer</summary>

**Johnson sequence** (A B C, C' → A): 000, 100, 110, 111, 011, 001. Map these to 0 to 5. Codes 010, 101 never happen (x).

| A B C | Q₂ Q₁ Q₀ |
|---|---|
| 000 | 000 |
| 100 | 001 |
| 110 | 010 |
| 111 | 011 |
| 011 | 100 |
| 001 | 101 |

<br>

K-maps with the two x's:

**Q₂ = A'C**

**Q₁ = AB**

**Q₀ = AB' + B'C + AC**

<br>

Circuit: 3 D flip-flops (D_A = C', D_B = A, D_C = B, one clock, reset to 000), plus 2 two-input ANDs for Q₂ and Q₁, and 3 two-input ANDs + one 3-input OR for Q₀.

From: §6

</details>

---

### S2 (Lecture 20, slides 6 and 8)

Give the state sequence of a 4-bit Johnson counter (A B C E) starting at 0000, and the 2-input AND gate that decodes each state.

<details><summary>Answer</summary>

| State | A B C E | Gate |
|---|---|---|
| t₀ | 0000 | A'E' |
| t₁ | 1000 | AB' |
| t₂ | 1100 | BC' |
| t₃ | 1110 | CE' |
| t₄ | 1111 | AE |
| t₅ | 0111 | A'B |
| t₆ | 0011 | B'C |
| t₇ | 0001 | C'E |

Then back to 0000.

From: §3, Rule 51

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. A 4-bit ring counter has 4 states.
2. A 5-bit Johnson counter has 10 states.
3. A Johnson counter feeds the last Q back to the first D.
4. Each state of a Johnson counter can be decoded with a 2-input AND gate.
5. A ring counter starting at 0000 counts correctly.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **True.** 2 × 5. (Rule 51)
3. **False.** The last **Q'**. Feeding Q makes a ring counter. (§3)
4. **True.** (Rule 51)
5. **False.** It must start with **one** 1 (1000). From 0000 it just shifts 0s forever. (§1)

</details>

---

### M2: Multiple choice

You need 12 timing signals. The fewest flip-flops if you use a Johnson counter is:

- A. 3
- B. 4
- C. 6
- D. 12

<details><summary>Answer</summary>

**C.** 2k = 12, so k = **6**. (A ring counter would need 12. A binary counter + decoder would need 4, plus a 4-to-16 decoder.)

From: Rule 51

</details>

---

### M3: Trace a Johnson counter

A 3-bit Johnson counter (A B C, C' fed to A) powers up in state 010. What happens? How do you fix it?

<details><summary>Answer</summary>

Next = (C', A, B).

010 → (1, 0, 1) = **101** → (0, 1, 0) = **010** → ...

It loops between **010 and 101** and never reaches the normal count.

**Fix:** reset all flip-flops to 000 at power-up (asynchronous reset, Topic 13 §13). Or add logic that forces the unused codes back into the main cycle.

From: §5

</details>

---

### M4: Ring counter waveforms

Sketch the outputs of a 4-bit ring counter that starts at 1000.

<details><summary>Answer</summary>

Each output is high for **one** clock period, one after the other:

```
CLK  ‾|_|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_|
T0   ‾‾‾‾____________‾‾‾‾____________
T1   ____‾‾‾‾____________‾‾‾‾________
T2   ________‾‾‾‾____________‾‾‾‾____
T3   ____________‾‾‾‾____________‾‾‾‾
```

Each Tᵢ repeats every 4 clocks.

From: §1

</details>

---

### M5: Explain

Compare three ways to make 8 timing signals: ring counter, Johnson counter, binary counter + decoder.

<details><summary>Answer</summary>

| Way | Flip-flops | Extra gates |
|---|---|---|
| Ring counter | 8 | none: outputs are already one-hot |
| Johnson counter | 4 | 8 two-input ANDs |
| Binary counter + decoder | 3 | a 3-to-8 decoder (8 three-input ANDs) |

Fewer flip-flops means more decoding gates.

From: §1, §2, Rule 51

</details>
