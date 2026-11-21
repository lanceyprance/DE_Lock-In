# Recompute every answer in mock/final-1.md, final-2.md, final-3.md.
# Run through tools/check_numbers.py (it execs this file with its helpers loaded).

cols = ((0, 0), (0, 1), (1, 1), (1, 0))


def async_rows(Yf):
    return [[int(Yf(y, a, b)) for a, b in cols] for y in (0, 1)]


def run(step, s0, n=8):
    seq = [s0]
    for _ in range(n):
        seq.append(step(seq[-1]))
    return [format(s, '03b') for s in seq]


def jk_step(eqs):
    """eqs(A,B,C) -> (JA,KA,JB,KB,JC,KC); returns next-state function."""
    def step(s):
        a, b, c = (s >> 2) & 1, (s >> 1) & 1, s & 1
        ja, ka, jb, kb, jc, kc = eqs(a, b, c)
        return (jk(a, ja, ka) << 2) | (jk(b, jb, kb) << 1) | jk(c, jc, kc)
    return step


print('--- Mock 1')
# Q1: G1 = NOR(A, C), G2 = AND(B, D'), G3 = NAND(A, B', D), G4 = OR(G1, G2), F = AND(G3, G4)
f = lambda a, b, c, d: int((not (a and not b and d)) and ((not (a or c)) or (b and not d)))
m = mins_of(f, 4)
check('M1 Q1 minterms', m, [0, 1, 4, 5, 6, 12, 14])
check('M1 Q1 maxterms', [i for i in range(16) if i not in m], [2, 3, 7, 8, 9, 10, 11, 13, 15])
check('M1 Q1 SOP', str(sop([A, B, C, D], m)), '(B & ~D) | (~A & ~C)')
# Q2a: positive-edge JK (J = K = 1), next stage clocked from Q' -> counts up
Q = [0, 0, 0]; seq = []
for _ in range(9):
    seq.append(Q[2] * 4 + Q[1] * 2 + Q[0])
    o = 1 - Q[0]; Q[0] ^= 1          # Q0' before / after
    if o == 0 and 1 - Q[0] == 1:      # rising edge of Q0'
        o = 1 - Q[1]; Q[1] ^= 1
        if o == 0 and 1 - Q[1] == 1:
            Q[2] ^= 1
check('M1 Q2a count', seq, [0, 1, 2, 3, 4, 5, 6, 7, 0])
check('M1 Q2a 12 kHz divided', [12 / 2, 12 / 4, 12 / 8], [6.0, 3.0, 1.5])
# Q2b: F = A'(D' + BD) + ABD
f = lambda a, b, c, d: int((not a and ((not d) or (b and d))) or (a and b and d))
m = mins_of(f, 4)
check('M1 Q2b minterms', m, [0, 2, 4, 5, 6, 7, 13, 15])
check('M1 Q2b min SOP', str(sop([A, B, C, D], m)), '(B & D) | (~A & ~D)')
check('M1 Q2b hazard-free', hazard_free_sop(m, 4), ['-1-1', '0--0', '01--'])
# Q3: mode 1 000 -> 011 -> 101 -> 110 -> 000, mode 2 001 -> 010 -> 100 -> 111 -> 001 (JK)
nxt = {0: 3, 3: 5, 5: 6, 6: 0, 1: 2, 2: 4, 4: 7, 7: 1}
J, K = jk_table(nxt)
check('M1 Q3 JK', [str(sop([A, B, C], *J[b])) + ' / ' + str(sop([A, B, C], *K[b])) for b in (2, 1, 0)],
      ['B / B', 'True / True', '~B / ~B'])
st = jk_step(lambda a, b, c: (b, b, 1, 1, 1 - b, 1 - b))
check('M1 Q3 mode 1', run(st, 0, 4), ['000', '011', '101', '110', '000'])
check('M1 Q3 mode 2', run(st, 1, 4), ['001', '010', '100', '111', '001'])
# Q4: Y = A'B + By', z = A'y
check('M1 Q4 rows', async_rows(lambda y, a, b: (not a and b) or (b and not y)), [[0, 1, 1, 0], [0, 1, 0, 0]])

print('--- Mock 2')
# Q1: F = sum m(1, 3, 7, 11, 15) + d(0, 2, 5)
ms, dc = [1, 3, 7, 11, 15], [0, 2, 5]
check('M2 Q1 SOP', str(sop([A, B, C, D], ms, dc)), '(C & D) | (~A & ~B)')
check('M2 Q1 POS', str(pos([A, B, C, D], ms, dc)), 'D & (C | ~A)')
# Q2a: JK counter 000 -> 010 -> 011 -> 101 -> 110 -> 000, unused 001, 100, 111
nxt = {0: 2, 2: 3, 3: 5, 5: 6, 6: 0}
J, K = jk_table(nxt)
dcs = [1, 4, 7]
eq = [str(sop([A, B, C], J[b][0], J[b][1] + dcs)) + ' / ' + str(sop([A, B, C], K[b][0], K[b][1] + dcs)) for b in (2, 1, 0)]
check('M2 Q2a JK', eq, ['C / ~C', 'True / A | C', 'B & ~A / ~B'])
st = jk_step(lambda a, b, c: (c, 1 - c, 1, int(a or c), int(b and not a), 1 - b))
check('M2 Q2a cycle', run(st, 0, 5), ['000', '010', '011', '101', '110', '000'])
check('M2 Q2a unused 001, 100, 111 go to', [format(st(s), '03b') for s in (1, 4, 7)], ['110', '010', '101'])
# Q2b: F = (A + C)(A' + B)(B' + D'): hazard-free POS via the 0s
fz = lambda a, b, c, d: int((a or c) and (not a or b) and (not b or not d))
z = [i for i in range(16) if i not in mins_of(fz, 4)]
check('M2 Q2b zeros', z, [0, 1, 4, 5, 7, 8, 9, 10, 11, 13, 15])
check('M2 Q2b min POS', str(pos([A, B, C, D], mins_of(fz, 4))), '(A | C) & (B | ~A) & (~B | ~D)')
check('M2 Q2b hazard-free (on the 0s)', hazard_free_sop(z, 4), ['-00-', '-1-1', '0-0-', '1--1', '10--'])
# Q3: 1101 Mealy detector, overlapping, JK. A=00 none, B=01 '1', C=10 '11', D=11 '110'
n = {(0, 0): (0, 0), (0, 1): (1, 0), (1, 0): (0, 0), (1, 1): (2, 0), (2, 0): (3, 0), (2, 1): (2, 0), (3, 0): (0, 0), (3, 1): (1, 1)}
J = {1: ([], []), 0: ([], [])}; K = {1: ([], []), 0: ([], [])}
for (s, x), (nx, zz) in n.items():
    r = s * 2 + x
    for b in (1, 0):
        q, q1 = (s >> b) & 1, (nx >> b) & 1
        if q == 0:
            (J[b][0] if q1 else []).append(r); K[b][1].append(r)
        else:
            J[b][1].append(r); (K[b][0] if not q1 else []).append(r)
check('M2 Q3 JK', [str(sop([Q1, Q0, X], *J[1])), str(sop([Q1, Q0, X], *K[1])), str(sop([Q1, Q0, X], *J[0])), str(sop([Q1, Q0, X], *K[0]))],
      ['Q0 & X', 'Q0', '(Q1 & ~X) | (X & ~Q1)', '~Q1 | ~X'])
# simulate the JK equations
def det_jk(bits):
    q1 = q0 = 0; out = []
    for x in bits:
        out.append(int(q1 and q0 and x))
        j1, k1, j0, k0 = q0 and x, q0, q1 ^ x, int(not q1 or not x)
        q1, q0 = jk(q1, j1, k1), jk(q0, j0, k0)
    return out
check('M2 Q3 JK circuit on 1101101011', det_jk([1, 1, 0, 1, 1, 0, 1, 0, 1, 1]), [0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
check('M2 Q3 Z', str(sop([Q1, Q0, X], [s * 2 + x for (s, x), (nx, zz) in n.items() if zz])), 'Q0 & Q1 & X')
# simulate the detector on a test string
def det(bits):
    s, out = 0, []
    for x in bits:
        nx, zz = n[(s, x)]; out.append(zz); s = nx
    return out
check('M2 Q3 on 1101101011', det([1, 1, 0, 1, 1, 0, 1, 0, 1, 1]), [0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
# Q4: Y1 = x y1 + x y2', Y2 = x y1' + x y2
tt = {(y1, y2, x): (int(x and (y1 or not y2)), int(x and (not y1 or y2))) for y1, y2 in product((0, 1), repeat=2) for x in (0, 1)}
check('M2 Q4 table rows 00, 01, 11, 10 (x = 0 | x = 1)',
      [''.join(f'{tt[(y1, y2, x)][0]}{tt[(y1, y2, x)][1]}' for x in (0, 1)) for y1, y2 in ((0, 0), (0, 1), (1, 1), (1, 0))],
      ['0011', '0001', '0011', '0010'])

print('--- Mock 3')
# Q1: G1 = NAND(X, Y), G2 = OR(Y, Z'), F = AND(G1, G2)
f = lambda x, y, z: int(not ((x and y) or not (y or not z)))
m = mins_of(f, 3)
check('M3 Q1 minterms', m, [0, 2, 3, 4])
check('M3 Q1 SOP', str(sop([X, Y, Z], m)), '(Y & ~X) | (~Y & ~Z)')
check('M3 Q1 POS', str(pos([X, Y, Z], m)), '(Y | ~Z) & (~X | ~Y)')
# Q2a: positive-edge T flip-flops (T = 1), clocked from Q: counts down
Q = [0, 0, 0]; seq = []
for _ in range(9):
    seq.append(Q[2] * 4 + Q[1] * 2 + Q[0])
    o = Q[0]; Q[0] ^= 1
    if o == 0 and Q[0] == 1:
        o = Q[1]; Q[1] ^= 1
        if o == 0 and Q[1] == 1:
            Q[2] ^= 1
check('M3 Q2a count', seq, [0, 7, 6, 5, 4, 3, 2, 1, 0])
check('M3 Q2a 1 MHz divided (kHz)', [1000 / 2, 1000 / 4, 1000 / 8], [500.0, 250.0, 125.0])
# Q2b: F = B'C' + BD
m = mins_of(lambda a, b, c, d: int((not b and not c) or (b and d)), 4)
check('M3 Q2b minterms', m, [0, 1, 5, 7, 8, 9, 13, 15])
check('M3 Q2b hazard-free', hazard_free_sop(m, 4), ['--01', '-00-', '-1-1'])
# Q3: D flip-flops, mode 1 000 -> 001 -> 011 -> 111 -> 110 -> 100 -> 000, mode 2 010 -> 101 -> 010
nxt = {0: 1, 1: 3, 3: 7, 7: 6, 6: 4, 4: 0, 2: 5, 5: 2}
check('M3 Q3 D', [str(sop([A, B, C], [s for s in nxt if (nxt[s] >> b) & 1])) for b in (2, 1, 0)], ['B', 'C', '~A'])
check('M3 Q3 JK', [str(sop([A, B, C], *jk_table(nxt)[0][b])) + ' / ' + str(sop([A, B, C], *jk_table(nxt)[1][b])) for b in (2, 1, 0)],
      ['B / ~B', 'C / ~C', '~A / A'])
# Q4: Y = By + AB', z = Ay
check('M3 Q4 rows', async_rows(lambda y, a, b: (b and y) or (a and not b)), [[0, 0, 0, 1], [0, 1, 1, 1]])
check('M3 Q4 z rows', async_rows(lambda y, a, b: a and y), [[0, 0, 0, 0], [0, 0, 1, 1]])
