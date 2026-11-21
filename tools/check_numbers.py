"""Recompute every worked answer in Topics 13-23, papers/2023.md and mock/final-*.md.
Run: python3 tools/check_numbers.py   (needs sympy: pip install sympy)
Prints each result; compare with the md files. Any 'FAIL' line is a mismatch."""
from itertools import product
from sympy import symbols, SOPform, POSform

A, B, C, D, X, Y, Z = symbols('A B C D X Y Z')


def mins_of(f, n):
    return [i for i, v in enumerate(product([0, 1], repeat=n)) if f(*v)]


def sop(vars_, ms, dc=()):
    b = lambda m: [int(c) for c in f'{m:0{len(vars_)}b}']
    return SOPform(vars_, [b(m) for m in ms], [b(m) for m in dc])


def pos(vars_, ms, dc=()):
    b = lambda m: [int(c) for c in f'{m:0{len(vars_)}b}']
    return POSform(vars_, [b(m) for m in ms], [b(m) for m in dc])


def _norm(v):
    """Make sympy strings order-independent: '(a) | (b)' == '(b) | (a)'."""
    if isinstance(v, str):
        return tuple(sorted(t.strip().strip('()') for t in v.split(' | ')))
    if isinstance(v, (list, tuple)):
        return type(v)(_norm(x) for x in v)
    if isinstance(v, dict):
        return {k: _norm(x) for k, x in v.items()}
    return v


def check(label, got, want):
    ok = _norm(got) == _norm(want)
    print(('ok   ' if ok else 'FAIL ') + f'{label}: {got}' + ('' if ok else f'  (want {want})'))


def jk(q, j, k):
    return int((j and not q) or (not k and q))


def jk_table(nxt, nbits=3):
    """Excitation for JK. nxt: dict state->next. Returns per-bit (ones, dcs) lists for J and K."""
    J = {b: ([], []) for b in range(nbits)}; K = {b: ([], []) for b in range(nbits)}
    for s, n in nxt.items():
        for b in range(nbits):
            q, q1 = (s >> b) & 1, (n >> b) & 1
            if q == 0:
                (J[b][0] if q1 else []).append(s); K[b][1].append(s)
            else:
                J[b][1].append(s); (K[b][0] if not q1 else []).append(s)
    return J, K


def hazard_free_sop(ms, n):
    """Smallest set of prime implicants that covers every 1 and every adjacent pair of 1s."""
    from itertools import combinations
    cubes = []
    for pat in product('01-', repeat=n):
        cov = [int(''.join(p), 2) for p in product(*[(c,) if c != '-' else ('0', '1') for c in pat])]
        if all(c in ms for c in cov):
            cubes.append(''.join(pat))
    covers = lambda a, b: all(x == '-' or x == y for x, y in zip(a, b))
    primes = [c for c in cubes if not any(o != c and covers(o, c) for o in cubes)]
    inc = lambda p, m: covers(p, f'{m:0{n}b}')
    pairs = [(a, b) for a in ms for b in ms if a < b and bin(a ^ b).count('1') == 1]
    for k in range(1, len(primes) + 1):
        for S in combinations(primes, k):
            if all(any(inc(p, m) for p in S) for m in ms) and all(any(inc(p, a) and inc(p, b) for p in S) for a, b in pairs):
                return sorted(S)


# ------------------------------------------------------------------ Final 2023
print('--- Final 2023')
f = lambda x, y, z: int((not x and not y) or not ((x or y) and not z))
m = mins_of(f, 3)
check('Q1 minterms', m, [0, 1, 3, 5, 7])
check('Q1 SOP', str(sop([X, Y, Z], m)), 'Z | (~X & ~Y)')
f = lambda a, b, c, d: int((a and not b and ((not d) or (c and d))) or (not a and (b or (c and d))) or (not a and c and not d))
m = mins_of(f, 4)
check('Q2b minterms', m, [2, 3, 4, 5, 6, 7, 8, 10, 11])
check('Q2b min SOP', str(sop([A, B, C, D], m)), '(B & ~A) | (C & ~B) | (A & ~B & ~D)')
check('Q2b hazard-free primes', hazard_free_sop(m, 4), ['-01-', '0-1-', '01--', '10-0'])
nxt = {0b011: 0b001, 0b001: 0b010, 0b010: 0b000, 0b000: 0b100, 0b100: 0b011, 0b111: 0b110, 0b110: 0b101, 0b101: 0b111}
J, K = jk_table(nxt)
res = {f'J{n}': str(sop([A, B, C], *J[b])) for b, n in ((2, 'A'), (1, 'B'), (0, 'C'))}
res.update({f'K{n}': str(sop([A, B, C], *K[b])) for b, n in ((2, 'A'), (1, 'B'), (0, 'C'))})
check('Q3 JK', res, {'JA': '~B & ~C', 'JB': 'A | C', 'JC': 'A', 'KA': '~B & ~C', 'KB': '~A | ~C', 'KC': '(A & B) | (~A & ~B)'})
# Q2a ripple count-down: negative-edge D flip-flops, D = Q', next stage clocked from Q'
Q = [0, 0, 0]; seq = []
for _ in range(9):
    seq.append(Q[2] * 4 + Q[1] * 2 + Q[0])
    old0 = 1 - Q[0]; Q[0] ^= 1
    if old0 == 1 and 1 - Q[0] == 0:
        old1 = 1 - Q[1]; Q[1] ^= 1
        if old1 == 1 and 1 - Q[1] == 0:
            Q[2] ^= 1
check('Q2a count sequence', seq, [0, 7, 6, 5, 4, 3, 2, 1, 0])
# Q4: Y = AB + A y', z = A + Y
tt = {(a, b, y): int((a and b) or (a and not y)) for a, b, y in product([0, 1], repeat=3)}
check('Q4 row y=0 (AB=00,01,11,10)', [tt[(a, b, 0)] for a, b in ((0, 0), (0, 1), (1, 1), (1, 0))], [0, 0, 1, 1])
check('Q4 row y=1 (AB=00,01,11,10)', [tt[(a, b, 1)] for a, b in ((0, 0), (0, 1), (1, 1), (1, 0))], [0, 0, 1, 0])
check('Q4 column AB=10 has no stable state', [tt[(1, 0, y)] == y for y in (0, 1)], [False, False])

# ------------------------------------------------------------------ Topic 14 slide example
print('--- Topic 14')
rows = []
for q1, q0, x in product([0, 1], repeat=3):
    J1, K1, J0, K0 = int(not x and q0), int(x or q0), int(x or q1), int(not x)
    rows.append(f'{jk(q1, J1, K1)}{jk(q0, J0, K0)}{int(q1 and q0 and x)}')
check('L13 next state + Z rows', rows, ['000', '010', '100', '010', '110', '010', '000', '011'])

# Part B M3 (D: DA = Bx + Ax', DB = A'x + Bx', z = AB') and M4 (T: TA = Bx, TB = x)
rows = [f'{int((b and x) or (a and not x))}{int((not a and x) or (b and not x))}{int(a and not b)}' for a, b, x in product([0, 1], repeat=3)]
check('T14 M3 next+z', rows, ['000', '010', '010', '110', '101', '001', '110', '100'])
rows = [f'{a ^ (b & x)}{b ^ x}' for a, b, x in product([0, 1], repeat=3)]
check('T14 M4 next', rows, ['00', '01', '01', '10', '10', '11', '11', '00'])

# ------------------------------------------------------------------ Topic 15 slide examples
print('--- Topic 15')
nxt = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 1, (2, 0): 3, (2, 1): 1, (3, 0): 0, (3, 1): 1}
m1 = [s * 2 + x for (s, x), n in nxt.items() if n & 2]; m0 = [s * 2 + x for (s, x), n in nxt.items() if n & 1]
Q1, Q0 = symbols('Q1 Q0')
check('1001 D1', str(sop([Q1, Q0, X], m1)), '(Q0 & ~Q1 & ~X) | (Q1 & ~Q0 & ~X)')
check('1001 D0', str(sop([Q1, Q0, X], m0)), 'X | (Q1 & ~Q0)')

# 1001 detector with JK: recompute equations from the state table
nxt4 = {}
for (st, xx), n in nxt.items():
    nxt4[st * 2 + xx] = n
J = {1: ([], []), 0: ([], [])}; K = {1: ([], []), 0: ([], [])}
for r, n in nxt4.items():
    st = r >> 1
    for b in (1, 0):
        q, q1 = (st >> b) & 1, (n >> b) & 1
        if q == 0:
            (J[b][0] if q1 else []).append(r); K[b][1].append(r)
        else:
            J[b][1].append(r); (K[b][0] if not q1 else []).append(r)
check('1001 JK', [str(sop([Q1, Q0, X], *J[1])), str(sop([Q1, Q0, X], *K[1])), str(sop([Q1, Q0, X], *J[0])), str(sop([Q1, Q0, X], *K[0]))],
      ['Q0 & ~X', 'Q0 | X', 'Q1 | X', '~X'])
# Moore 1001 with T flip-flops (5 states, 101/110/111 unused)
Q2 = symbols('Q2')
nm = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 1, (2, 0): 3, (2, 1): 1, (3, 0): 0, (3, 1): 4, (4, 0): 2, (4, 1): 1}
Tm = {b: [st * 2 + xx for (st, xx), n in nm.items() if ((st ^ n) >> b) & 1] for b in range(3)}
dcm = [st * 2 + xx for st in (5, 6, 7) for xx in (0, 1)]
check('Moore T2 T1 T0', [str(sop([Q2, Q1, Q0, X], Tm[b], dcm)) for b in (2, 1, 0)],
      ['Q2 | (Q0 & Q1 & X)', '(Q0 & ~X) | (Q1 & X) | (Q2 & ~X)', 'Q1 | (Q0 & ~X) | (X & ~Q0)'])
# Part B M3: 101 Mealy detector with D flip-flops (S0=00, S1=01, S2=10, 11 unused)
n101 = {(0, 0): (0, 0), (0, 1): (1, 0), (1, 0): (2, 0), (1, 1): (1, 0), (2, 0): (0, 0), (2, 1): (1, 1)}
dd = [6, 7]
check('101 D1 D0 Z', [str(sop([Q1, Q0, X], [st * 2 + xx for (st, xx), (n, z) in n101.items() if n & 2], dd)),
                      str(sop([Q1, Q0, X], [st * 2 + xx for (st, xx), (n, z) in n101.items() if n & 1], dd)),
                      str(sop([Q1, Q0, X], [st * 2 + xx for (st, xx), (n, z) in n101.items() if z], dd))],
      ['Q0 & ~X', 'X', 'Q1 & X'])
# Part B M4: two modes with D flip-flops
n2 = {0: 1, 1: 3, 3: 2, 2: 0, 4: 6, 6: 7, 7: 5, 5: 4}
check('two-mode D', [str(sop([A, B, C], [st for st in n2 if (n2[st] >> b) & 1])) for b in (2, 1, 0)],
      ['A', '(A & ~C) | (C & ~A)', '(A & B) | (~A & ~B)'])

# ------------------------------------------------------------------ Topic 16 mod-5 counter
print('--- Topic 16')
def step5(s):
    a, b, c = (s >> 2) & 1, (s >> 1) & 1, s & 1
    return (jk(a, b and c, 1) << 2) | (jk(b, c, c) << 1) | jk(c, not a, 1)
check('mod-5 cycle', [format(s, '03b') for s in (0, step5(0), step5(1), step5(2), step5(3))], ['000', '001', '010', '011', '100'])
check('mod-5 step from 100', format(step5(4), '03b'), '000')
check('unused 101,110,111 go to', [format(step5(s), '03b') for s in (5, 6, 7)], ['010', '010', '000'])
# mod-6 synchronous up counter with T flip-flops (Part B M3)
nxt6 = {s: (s + 1) % 6 for s in range(6)}
T = {b: [s for s in range(6) if ((s ^ nxt6[s]) >> b) & 1] for b in range(3)}
res = {f'T{n}': str(sop([A, B, C], T[b], [6, 7])) for b, n in ((2, 'A'), (1, 'B'), (0, 'C'))}
check('mod-6 T', res, {'TA': '(A & C) | (B & C)', 'TB': 'C & ~A', 'TC': 'True'})
def step6(s):
    a, b, c = (s >> 2) & 1, (s >> 1) & 1, s & 1
    ta, tb = (a and c) or (b and c), (c and not a)
    return ((a ^ ta) << 2) | ((b ^ tb) << 1) | (c ^ 1)
check('mod-6 unused 110, 111 go to', [format(step6(s), '03b') for s in (6, 7)], ['111', '010'])
# 3-bit ripple up counter, negative-edge T (T=1), clocked from Q: counts up
Q = [0, 0, 0]; seq = []
for _ in range(9):
    seq.append(Q[2] * 4 + Q[1] * 2 + Q[0])
    o = Q[0]; Q[0] ^= 1
    if o == 1 and Q[0] == 0:
        o = Q[1]; Q[1] ^= 1
        if o == 1 and Q[1] == 0:
            Q[2] ^= 1
check('ripple up (neg edge, clock from Q)', seq, [0, 1, 2, 3, 4, 5, 6, 7, 0])
check('divider 16 MHz, 4 stages', [16 / 2 ** k for k in range(1, 5)], [8.0, 4.0, 2.0, 1.0])

# ------------------------------------------------------------------ Topic 18 Johnson exercise
print('--- Topic 18')
s = (0, 0, 0); seqj = []
for _ in range(7):
    seqj.append(''.join(map(str, s))); s = (1 - s[2], s[0], s[1])
check('3-bit Johnson sequence ABC', seqj, ['000', '100', '110', '111', '011', '001', '000'])
cnt = {int(st, 2): k for k, st in enumerate(seqj[:6])}
outs = {}
for b, n in ((2, 'Q2'), (1, 'Q1'), (0, 'Q0')):
    outs[n] = str(sop([A, B, C], [st for st, k in cnt.items() if (k >> b) & 1], [2, 5]))
check('Johnson -> count 0..5', outs, {'Q2': 'C & ~A', 'Q1': 'A & B', 'Q0': '(A & C) | (A & ~B) | (C & ~B)'})
# 4-bit Johnson: decoding gate for each state
check('4-bit Johnson states', 2 * 4, 8)

# ------------------------------------------------------------------ Topic 19 memory sizes
print('--- Topic 19')
check('1024 x 16: address lines', (1024).bit_length() - 1, 10)
check('64K x 8: address lines, bits', ((64 * 1024).bit_length() - 1, 64 * 1024 * 8), (16, 524288))
check('10x1024 decoder AND gates / inputs', (2 ** 10, 10), (1024, 10))
check('two 5x32 decoders AND gates / inputs', (2 * 2 ** 5, 5), (64, 5))
check('32 x 8 ROM: decoder, OR gates, OR inputs', ('5x32', 8, 32), ('5x32', 8, 32))
check('ROM y = x^2 + 1 table', [x * x + 1 for x in range(8)], [1, 2, 5, 10, 17, 26, 37, 50])
check('4K x 8 ROM: address lines', (4096).bit_length() - 1, 12)

# ------------------------------------------------------------------ Topic 20
print('--- Topic 20')
check('switch matrix point: 6 switches', 2 ** 6, 64)

# ------------------------------------------------------------------ Topic 21 slide examples
print('--- Topic 21')
x1x2 = ((0, 0), (0, 1), (1, 1), (1, 0))
t = {(y, a, b): int((not a and b) or (not y and b)) for y in (0, 1) for a, b in x1x2}
check('L23 s19 Y = x1\'x2 + y\'x2, row y=0', [t[(0, a, b)] for a, b in x1x2], [0, 1, 1, 0])
check('L23 s19 row y=1', [t[(1, a, b)] for a, b in x1x2], [0, 1, 0, 0])
x = (0, 1)
t2 = {(y1, y2, xx): (int((xx and y1) or (not xx and y2)), int((xx and not y1) or (not xx and y2))) for y1, y2 in product((0, 1), repeat=2) for xx in x}
check('L23 s15 transition table rows y1y2=00,01,11,10 x=0,1',
      [''.join(f'{t2[(y1, y2, xx)][0]}{t2[(y1, y2, xx)][1]}' for xx in x) for y1, y2 in ((0, 0), (0, 1), (1, 1), (1, 0))],
      ['0001', '1101', '1110', '0010'])

# Part B M3: Y = x1x2' + x2'y
t3 = {(y, a, b): int((a and not b) or (not b and y)) for y in (0, 1) for a, b in x1x2}
check('T21 M3 rows', [[t3[(y, a, b)] for a, b in x1x2] for y in (0, 1)], [[0, 0, 0, 1], [1, 0, 0, 1]])
# slide 17: Y = x1x2' + x1y, z = x1x2y
t4 = {(y, a, b): int((a and not b) or (a and y)) for y in (0, 1) for a, b in x1x2}
check('L23 s17 rows', [[t4[(y, a, b)] for a, b in x1x2] for y in (0, 1)], [[0, 0, 0, 1], [0, 0, 1, 1]])

# ------------------------------------------------------------------ Topic 22 slide example
print('--- Topic 22')
m = mins_of(lambda a, b, c: int((a and b) or (not b and c)), 3)
check('Y = x1x2 + x2\'x3 hazard-free', hazard_free_sop(m, 3), ['-01', '1-1', '11-'])

check('T22 M3 A\'B\' + BC hazard-free', hazard_free_sop(mins_of(lambda a, b, c: int((not a and not b) or (b and c)), 3), 3), ['-11', '0-1', '00-'])
check('T22 M2 AB\' + BC hazard-free', hazard_free_sop(mins_of(lambda a, b, c: int((a and not b) or (b and c)), 3), 3), ['-11', '1-1', '10-'])
# static-0: hazard-free POS = hazard-free SOP of the complement
zeros = lambda f, n: [m for m in range(2 ** n) if m not in mins_of(f, n)]
check('T22 S2 0s', zeros(lambda a, b, c: int((a or not b) and (b or c)), 3), [0, 2, 3, 4])
check('T22 S2 hazard-free (on the 0s)', hazard_free_sop(zeros(lambda a, b, c: int((a or not b) and (b or c)), 3), 3), ['-00', '0-0', '01-'])
check('T22 M4 hazard-free (on the 0s)', hazard_free_sop(zeros(lambda a, b, c: int((a or b) and (not a or c)), 3), 3), ['-00', '00-', '1-0'])

# ------------------------------------------------------------------ Mocks: imported from the mock check file
exec(open(__file__.replace('check_numbers.py', 'check_mocks.py')).read())
