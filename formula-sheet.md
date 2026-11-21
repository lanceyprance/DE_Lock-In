# Learn by heart (no formula sheet in the exam)

The EEEN20050 final gives **no formula sheet**. Only a calculator.

**So learn this whole page by heart.** It's every "Learn by heart" list from the topics, on one page.

Read it the night before. Each line is explained in the topic linked next to it. Rule and equation numbers match the 📐 boxes in the notes.

---

## Numbers (Topics 2 to 4)

**Powers of 2**

| 2⁰ | 2¹ | 2² | 2³ | 2⁴ | 2⁵ | 2⁶ | 2⁷ | 2⁸ | 2⁹ | 2¹⁰ |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |

| 2⁻¹ | 2⁻² | 2⁻³ | 2⁻⁴ | 2⁻⁵ |
|---|---|---|---|---|
| 0.5 | 0.25 | 0.125 | 0.0625 | 0.03125 |

<br>

**Hex digits:** A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.

<br>

**Decimal → any base b** ([Topic 2](notes/02-number-systems.md))

Whole part: divide by b. Read the remainders **upward**.

Fraction part: multiply by b. Read the whole parts **downward**.

<br>

**Binary → octal or hex** ([Topic 2](notes/02-number-systems.md))

Group outward from the point. 3 bits for octal, 4 bits for hex.

Pad zeros at the **outer ends only**.

<br>

**Binary arithmetic** ([Topic 3](notes/03-binary-arithmetic.md))

1 + 1 = 10. 1 + 1 + 1 = 11. 0 − 1 = 1, borrow 1.

Multiply = shift and add.

<br>

**Negative numbers** ([Topic 4](notes/04-signed-numbers.md))

| System | Make it negative | Zeros | n-bit range |
|---|---|---|---|
| Signed magnitude | flip the sign bit | two | −(2ⁿ⁻¹ − 1) to +(2ⁿ⁻¹ − 1) |
| 1's complement | flip every bit | two | −(2ⁿ⁻¹ − 1) to +(2ⁿ⁻¹ − 1) |
| 2's complement | flip every bit, add 1 | one | −2ⁿ⁻¹ to +(2ⁿ⁻¹ − 1) |

2's complement shortcut: from the right, copy up to and including the first 1. Flip the rest.

1's complement add: carry out of the left → add it back on the right.

2's complement add: carry out of the left → throw it away.

Overflow: two numbers with the **same sign** give an answer with the **other sign**.

<br>

**Codes** ([Topic 5](notes/05-binary-codes.md))

BCD: 4 bits per decimal digit. Gray: neighbours differ by 1 bit. One-hot: one bit per value.

---

## Boolean logic (Topics 6 to 9)

**Key laws** ([Topic 6](notes/06-boolean-algebra.md))

$$x + x' = 1 \qquad x \cdot x' = 0$$

$$x + yz = (x + y)(x + z)$$

$$(x + y)' = x'y' \qquad (xy)' = x' + y'$$

$$x + xy = x \qquad x + x'y = x + y$$

<br>

**Minterm and maxterm** ([Topic 7](notes/07-minterms-maxterms.md))

Minterm: bit 0 → x', bit 1 → x.

Maxterm: bit 0 → x, bit 1 → x'.

Σm(rows where f = 1) = ΠM(rows where f = 0).

<br>

**K-map** ([Topic 8](notes/08-karnaugh-maps.md))

Order the rows and columns 00, 01, **11, 10**.

Groups of 1, 2, 4, 8 or 16. Make them as big as possible. Edges wrap.

A group of 2ᵏ cells removes k variables.

SOP: group the 1s. POS: group the 0s.

<br>

**Don't cares** ([Topic 9](notes/09-dont-cares-nand-nor.md))

Use an x as a 1 only if it makes a group bigger.

<br>

**NAND-NAND / NOR-NOR** ([Topic 9](notes/09-dont-cares-nand-nor.md))

NAND-NAND from the minimum SOP. NOR-NOR from the minimum POS.

Swap every gate. Complement any single letter going into the output gate.

<br>

**CMOS transistors** ([Topic 9](notes/09-dont-cares-nand-nor.md))

NAND and NOR: 2n. AND and OR: 2n + 2. NOT: 2.

---

## Combinational logic (Topics 10 to 12)

**Adders** ([Topic 10](notes/10-adders.md))

$$\text{Half adder: } S = X \oplus Y \qquad C = XY$$

$$\text{Full adder: } S = X \oplus Y \oplus Z \qquad C = XY + XZ + YZ = XY + (X \oplus Y)Z$$

Ripple carry delay: about 2n gate delays.

<br>

**Carry lookahead** ([Topic 10](notes/10-adders.md))

$$P_i = A_i \oplus B_i \qquad G_i = A_i B_i$$

$$S_i = P_i \oplus C_i \qquad C_{i+1} = G_i + P_i C_i$$

<br>

**Subtraction** ([Topic 10](notes/10-adders.md))

Half subtractor: D = X ⊕ Y, B = X'Y.

Or use 2's complement: A − B = A + B' + 1.

<br>

**Shifts:** left = × 2. Right = ÷ 2.

<br>

**Decoder** ([Topic 11](notes/11-decoders-encoders.md))

Active-high outputs are minterms → OR the ones in Σm.

Active-low outputs are maxterms → AND the ones in ΠM.

<br>

**Encoder** ([Topic 11](notes/11-decoders-encoders.md))

Assumes exactly one input is on. Priority encoder: highest number wins.

<br>

**Mux** ([Topic 12](notes/12-multiplexers.md))

2-to-1: Y = S'I₀ + SI₁.

n-variable function on a mux with n − 1 select lines: each pair of rows gives 0, 1, v or v'.

---

## Sequential logic (Topics 13 to 15)

**Flip-flops** ([Topic 13](notes/13-latches-flip-flops.md))

SR latch (NOR): 00 hold, 01 reset, 10 set, **11 not allowed**. NAND latch: active low, 00 not allowed.

JK: 00 hold, 01 reset, 10 set, 11 **toggle**. T: 0 hold, 1 toggle. D: Q next = D.

$$Q_{t+1} = JQ' + K'Q \qquad Q_{t+1} = D \qquad Q_{t+1} = T \oplus Q$$

Latch = level (changes while enabled). Flip-flop = edge. Master-slave = negative edge. Bubble on C = negative edge.

<br>

**Analysis** ([Topic 14](notes/14-sequential-analysis.md))

Input equations → flip-flop inputs for every row → characteristic table → next state.

n flip-flops → 2ⁿ states. m inputs → 2ᵐ arrows out of each state. Mealy arrows: input/output.

<br>

**Design** ([Topic 15](notes/15-state-machine-design.md))

1. State diagram and table. 2. Codes (log₂ n flip-flops, round up). 3. Excitation table. 4. K-maps (unused = x). 5. Circuit.

| Q → Q next | D | J K | T |
|---|---|---|---|
| 0 → 0 | 0 | 0 x | 0 |
| 0 → 1 | 1 | 1 x | 1 |
| 1 → 0 | 0 | x 1 | 1 |
| 1 → 1 | 1 | x 0 | 0 |

Moore: output from the state only (in the circle). Mealy: output from state and input (on the arrow).

Two modes in one circuit: one state diagram holding both cycles. The start state picks the mode.

---

## Counters and registers (Topics 16 to 18)

**Counters** ([Topic 16](notes/16-counters.md))

Synchronous: Topic 15 with no input. **Check every unused state** leads back.

Ripple: every flip-flop toggles (T = 1, J = K = 1, D = Q').

| Trigger edge | next clock from Q | from Q' |
|---|---|---|
| negative | up | down |
| positive | down | up |

Stage k divides by 2ᵏ: f/2, f/4, f/8. BCD counter: 0 to 9.

<br>

**Registers** ([Topic 17](notes/17-registers.md))

Parallel load: D = L·I + L'·Q. Shift register: one place per clock, n clocks for n bits.

Universal shift register s₁s₀: 00 hold, 01 right, 10 left, 11 load.

Serial adder: two shift registers + one full adder + one D flip-flop for the carry.

<br>

**Ring and Johnson** ([Topic 18](notes/18-ring-johnson.md))

Ring: last Q → first D, n flip-flops → n states, start 1000.

Johnson: last **Q'** → first D, k flip-flops → **2k** states. Decode each with one 2-input AND (A'E', AB', BC', CE', AE, A'B, B'C, C'E). Reset at power-up.

---

## Memory and programmable logic (Topics 19 and 20)

**Memory** ([Topic 19](notes/19-memory.md))

2ᵏ words × n bits → k address lines. 1 k = 2¹⁰.

One k × 2ᵏ decoder = 2ᵏ ANDs of k inputs. Two-dimensional: 2 × 2^(k/2) ANDs of k/2 inputs.

SRAM: latch, 6 transistors. DRAM: 1 transistor + 1 capacitor, needs refresh. Both volatile.

PROM: fuses once. EPROM: UV erase. EEPROM: electrical erase. Flash: in-circuit, floating gate.

<br>

**Programmable logic** ([Topic 20](notes/20-programmable-logic.md))

PROM: fixed AND, programmable OR. PAL: programmable AND, fixed OR. PLA: both programmable.

CPLD: PLDs + switch matrix + I/O blocks, macrocells with flip-flops. FPGA: CLBs (4-input look-up table + flip-flops), IOBs, switch matrix (6 switches → 64 ways).

---

## Asynchronous logic and hazards (Topics 21 and 22)

**Asynchronous** ([Topic 21](notes/21-asynchronous-circuits.md))

Y = next (excitation), y = present (secondary). Transition table: y rows, inputs columns (Gray), circle Y = y.

A column with **no** circle → oscillates (period = 2 × loop delay).

Flow table: letters for states, ", output" in each cell.

Fundamental mode: one input change at a time, only when stable.

Race: two state variables change at once. Critical = can end in different states. Avoid with an assignment that changes one bit per transition.

<br>

**Hazards** ([Topic 22](notes/22-hazards.md))

Cause: different path delays (a signal and its inverted copy).

Static-1 (SOP): every pair of neighbouring 1s must share a group. Static-0 (POS): same with the 0s.

Consensus: xy + x'z → add yz. (x + y)(x' + z) → add (y + z).

Dynamic hazard: three or more changes instead of one.

---

## Transistor logic (Topic 23)

**CMOS** ([Topic 23](notes/23-transistor-logic.md))

NMOS on when gate high. PMOS on when gate low.

Inverter: 2 transistors. NAND: PMOS parallel, NMOS series. NOR: PMOS series, NMOS parallel.

Transmission gate: NMOS + PMOS side by side, a two-way switch. XOR = 8 transistors, D latch = 10, 4-to-1 mux = 16.

Positive logic: high = 1. Negative logic: high = 0.
