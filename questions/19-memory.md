# Topic 19: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises and past-final questions

### S1 (Lecture 21, slide 5)

A memory holds 1024 words of 16 bits. How many address lines and data lines does it need? How many bits does it store?

<details><summary>Answer</summary>

1024 = 2¹⁰ → **10** address lines.

16 data lines (in and out).

1024 × 16 = **16,384** bits.

From: §2, Rule 52

</details>

---

### S2 (Lecture 21, slide 13)

Compare a 10 × 1024 decoder with two 5 × 32 decoders for a 1K-word memory.

<details><summary>Answer</summary>

One 10 × 1024 decoder: **1024** AND gates, each with **10** inputs.

Two 5 × 32 decoders: 2 × 32 = **64** AND gates, each with **5** inputs.

Two-dimensional selection is far cheaper.

From: §5, Rule 53

</details>

---

### S3 (Lecture 21, slides 23 to 25)

What does a 32 × 8 ROM contain inside? What does it output for address 00011 if word 3 is programmed as 10110010?

<details><summary>Answer</summary>

Inside: a **5 × 32 decoder** (5 address lines) and **8 OR gates** with **32** inputs each.

Address 00011 → only decoder output 3 is high. Each OR gate outputs 1 if its cross point on line 3 is connected.

Output: **10110010**.

From: §8

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. DRAM is non-volatile.
2. A DRAM cell uses one transistor and one capacitor.
3. EPROM is erased with ultraviolet light.
4. A memory with 16 address lines has 65,536 words.
5. In a PROM, a blown fuse stores a 1.
6. Flash memory stores charge on a floating gate.

<details><summary>Answer</summary>

1. **False.** DRAM loses its data with no power. It's volatile. (§7)
2. **True.** (§6)
3. **True.** (§9)
4. **True.** 2¹⁶ = 65,536. (Rule 52)
5. **False.** Blown = **0**. Intact = 1. (§9)
6. **True.** (§10)

</details>

---

### M2: Multiple choice

How many address lines does a 256K × 8 memory need?

- A. 8
- B. 16
- C. 18
- D. 256

<details><summary>Answer</summary>

**C.** 256K = 2⁸ × 2¹⁰ = 2¹⁸ → **18** address lines. (The 8 is the word width.)

From: Rule 52

</details>

---

### M3: Memory sizes

1. How many 8-bit words fit in 4 kB? How many address lines?
2. A 64K × 8 memory uses two-dimensional decoding with two equal decoders. What size is each decoder, and how many AND gates in total?

<details><summary>Answer</summary>

**1.** 4 kB = 4 × 1024 = **4096** words. 4096 = 2¹² → **12** address lines.

<br>

**2.** 64K = 2¹⁶, so k = 16. Two decoders of 8 inputs: **8 × 256** each.

Gates: 2 × 256 = **512** AND gates of 8 inputs. (One 16 × 65,536 decoder would need 65,536 gates of 16 inputs.)

From: Rule 52, Rule 53

</details>

---

### M4: Read and write

Explain what happens in the binary storage cell for: Select = 0; Select = 1, Read/Write = 0; Select = 1, Read/Write = 1.

<details><summary>Answer</summary>

**Select = 0:** the latch is forced to "no change" and the output is 0. The cell does nothing.

**Select = 1, R/W = 0:** **write**. The data input goes into the latch.

**Select = 1, R/W = 1:** **read**. The latch's value goes to the output.

From: §3

</details>

---

### M5: Explain

Give two differences between SRAM and DRAM, and say where flash memory fits.

<details><summary>Answer</summary>

**SRAM:** a latch of about 6 transistors per bit. Holds its data while powered. Bigger, faster.

**DRAM:** 1 transistor + 1 capacitor per bit. About a quarter of the area. The charge leaks, so it must be **refreshed**.

Both are **volatile**.

**Flash** is **non-volatile**. It's like EEPROM, but can be erased and reprogrammed **in the circuit**. Each bit is a floating-gate transistor.

From: §6, §7, §10

</details>
