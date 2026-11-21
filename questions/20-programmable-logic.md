# Topic 20: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 22, slide 5)

Use a ROM as a look-up table for y = x² + 1, with x from 0 to 7. Give the table and the ROM size.

<details><summary>Answer</summary>

| x (A₂A₁A₀) | y | B₅…B₀ |
|---|---|---|
| 0 (000) | 1 | 000001 |
| 1 (001) | 2 | 000010 |
| 2 (010) | 5 | 000101 |
| 3 (011) | 10 | 001010 |
| 4 (100) | 17 | 010001 |
| 5 (101) | 26 | 011010 |
| 6 (110) | 37 | 100101 |
| 7 (111) | 50 | 110010 |

**8 × 6 ROM:** a 3 × 8 decoder and 6 OR gates.

From: §2

</details>

---

### S2 (Lecture 22, slides 7 to 11)

Explain the difference between a PROM, a PAL and a PLA.

<details><summary>Answer</summary>

**PROM:** fixed AND array (a full decoder: every minterm), programmable OR array.

**PAL:** programmable AND array, **fixed** OR array.

**PLA:** **both** arrays programmable. Most flexible, but harder to program.

From: Rule 54

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. In a PAL, the OR array is programmable.
2. A PLA can share one product term between two outputs.
3. PAL and PLA devices can implement sequential circuits on their own.
4. An FPGA logic block can implement any function of 4 variables.
5. ASICs have a lower development cost than FPGAs.

<details><summary>Answer</summary>

1. **False.** The PAL's OR array is **fixed**. (Rule 54)
2. **True.** (§5)
3. **False.** They're only gates. Sequential needs flip-flops: CPLD or FPGA. (§6)
4. **True.** Its look-up table has 4 inputs. (§7)
5. **False.** FPGAs have the low development cost. ASICs are cheaper only in high volume. (§9)

</details>

---

### M2: Multiple choice

Which device has a fixed AND array and a programmable OR array?

- A. PAL
- B. PLA
- C. PROM
- D. FPGA

<details><summary>Answer</summary>

**C.** The PROM's AND array is a fixed decoder.

From: Rule 54

</details>

---

### M3: A function on a PROM

Implement F₁ = Σm(1, 2, 4, 7) and F₂ = Σm(3, 5, 6, 7) on a PROM. What circuit is this?

<details><summary>Answer</summary>

A 3 × 8 decoder makes minterms 0 to 7.

OR gate F₁: connect decoder lines **1, 2, 4, 7**.

OR gate F₂: connect decoder lines **3, 5, 6, 7**.

It's a **full adder**: F₁ = S, F₂ = C (Topic 10).

From: §1

</details>

---

### M4: PLA sharing

F = AB + A'C and G = AB + BC'. How many AND gates does a PLA need? How many would two separate SOP circuits need?

<details><summary>Answer</summary>

Products: AB, A'C, BC'. AB is used by both.

PLA: **3** AND gates (AB shared) and 2 OR gates.

Separate circuits: 2 + 2 = **4** AND gates.

From: §5

</details>

---

### M5: Explain

What is inside an FPGA? Why would you choose an FPGA over an ASIC?

<details><summary>Answer</summary>

**Inside:** thousands of **configurable logic blocks** (each with a look-up table for any 4-variable function, muxes and flip-flops), **I/O blocks** round the edge, and **switch matrices** with wires that connect them.

**Why an FPGA:** it's bought off the shelf. Low development cost, short time to market, and it can be **reconfigured**. An ASIC only wins on performance, power, and cost in **high volume**.

From: §7, §8, §9

</details>
