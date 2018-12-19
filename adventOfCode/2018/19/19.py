from collections import defaultdict


def addr(r, a, b, c): r[c] = r[a] + r[b]
def addi(r, a, b, c): r[c] = r[a] + b
def mulr(r, a, b, c): r[c] = r[a] * r[b]
def muli(r, a, b, c): r[c] = r[a] * b
def banr(r, a, b, c): r[c] = r[a] & r[b]
def bani(r, a, b, c): r[c] = r[a] & b
def borr(r, a, b, c): r[c] = r[a] | r[b]
def bori(r, a, b, c): r[c] = r[a] | b
def setr(r, a, b, c): r[c] = r[a]
def seti(r, a, b, c): r[c] = a
def gtir(r, a, b, c): r[c] = 1 if a > r[b] else 0
def gtri(r, a, b, c): r[c] = 1 if r[a] > b else 0
def gtrr(r, a, b, c): r[c] = 1 if r[a] > r[b] else 0
def eqir(r, a, b, c): r[c] = 1 if a == r[b] else 0
def eqri(r, a, b, c): r[c] = 1 if r[a] == b else 0
def eqrr(r, a, b, c): r[c] = 1 if r[a] == r[b] else 0
ops = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
}


ipr = 3

instructions = []
register = [1] + [0] * 5
with open('input.txt') as f:
    for line in f:
        o, a, b, c = line.strip().split()
        instructions.append((ops[o], int(a), int(b), int(c)))


hash = lambda reg, a, b: tuple([r if i != a and i != b else '?' for i, r in enumerate(reg)])

ip = 0
history = {}
prdel = defaultdict(int)
while ip < len(instructions):
    op, a, b, c = instructions[ip]

    if op == gtrr:
        h = hash(register, a, b)
        if h in history and prdel[h] > 100:
            hist = history[h]
            if hist is not None:
                if hist[a] == register[a]:
                    assert False
                if hist[b] == register[b]:
                    assert register[a] - hist[a] == 1
                    # print('ended b', register[a] - hist[a])
                    register[a] = register[b] - 100
                    del history[h]
                print(h, register, hist)
                history[h] = None
        else:
            history[h] = tuple(register)
            prdel[h] += 1

    print(ip, register, end=' ')
    op(register, a, b, c)
    register[ipr] += 1
    ip = register[ipr]
    print(str(op)[10:14], a, b, c, register)
register[ipr] -= 1
print(history)
print(register)


# 0 [1, 0, 0, 0, 0, 0] addi 3 16 3 [1, 0, 0, 17, 0, 0]
# 17 [1, 0, 0, 17, 0, 0] addi 4 2 4 [1, 0, 0, 18, 2, 0]
# 18 [1, 0, 0, 18, 2, 0] mulr 4 4 4 [1, 0, 0, 19, 4, 0]
# 19 [1, 0, 0, 19, 4, 0] mulr 3 4 4 [1, 0, 0, 20, 76, 0]
# 20 [1, 0, 0, 20, 76, 0] muli 4 11 4 [1, 0, 0, 21, 836, 0]
# 21 [1, 0, 0, 21, 836, 0] addi 1 6 1 [1, 6, 0, 22, 836, 0]
# 22 [1, 6, 0, 22, 836, 0] mulr 1 3 1 [1, 132, 0, 23, 836, 0]
# 23 [1, 132, 0, 23, 836, 0] addi 1 21 1 [1, 153, 0, 24, 836, 0]
# 24 [1, 153, 0, 24, 836, 0] addr 4 1 4 [1, 153, 0, 25, 989, 0]
# 25 [1, 153, 0, 25, 989, 0] addr 3 0 3 [1, 153, 0, 27, 989, 0]
# 27 [1, 153, 0, 27, 989, 0] setr 3 4 1 [1, 27, 0, 28, 989, 0]
# 28 [1, 27, 0, 28, 989, 0] mulr 1 3 1 [1, 756, 0, 29, 989, 0]
# 29 [1, 756, 0, 29, 989, 0] addr 3 1 1 [1, 785, 0, 30, 989, 0]
# 30 [1, 785, 0, 30, 989, 0] mulr 3 1 1 [1, 23550, 0, 31, 989, 0]
# 31 [1, 23550, 0, 31, 989, 0] muli 1 14 1 [1, 329700, 0, 32, 989, 0]
# 32 [1, 329700, 0, 32, 989, 0] mulr 1 3 1 [1, 10550400, 0, 33, 989, 0]
# 33 [1, 10550400, 0, 33, 989, 0] addr 4 1 4 [1, 10550400, 0, 34, 10551389, 0]
# 34 [1, 10550400, 0, 34, 10551389, 0] seti 0 3 0 [0, 10550400, 0, 35, 10551389, 0]
# 35 [0, 10550400, 0, 35, 10551389, 0] seti 0 7 3 [0, 10550400, 0, 1, 10551389, 0]

# 1 [0, 10550400, 0, 1, 10551389, 0] seti 1 2 5 [0, 10550400, 0, 2, 10551389, 1]
# 2 [0, 10550400, 0, 2, 10551389, 1] seti 1 3 2 [0, 10550400, 1, 3, 10551389, 1]
# 3 [0, 10550400, 1, 3, 10551389, 1] mulr 5 2 1 [0, 1, 1, 4, 10551389, 1]
# 4 [0, 1, 1, 4, 10551389, 1] eqrr 1 4 1 [0, 0, 1, 5, 10551389, 1]
# 5 [0, 0, 1, 5, 10551389, 1] addr 1 3 3 [0, 0, 1, 6, 10551389, 1]
# 6 [0, 0, 1, 6, 10551389, 1] addi 3 1 3 [0, 0, 1, 8, 10551389, 1]
# 8 [0, 0, 1, 8, 10551389, 1] addi 2 1 2 [0, 0, 2, 9, 10551389, 1]
# 9 [0, 0, 2, 9, 10551389, 1] gtrr 2 4 1 [0, 0, 2, 10, 10551389, 1]
# 10 [0, 0, 2, 10, 10551389, 1] addr 3 1 3 [0, 0, 2, 11, 10551389, 1]
# 11 [0, 0, 2, 11, 10551389, 1] seti 2 5 3 [0, 0, 2, 3, 10551389, 1]
# 3 [0, 0, 2, 3, 10551389, 1] mulr 5 2 1 [0, 2, 2, 4, 10551389, 1]
# 4 [0, 2, 2, 4, 10551389, 1] eqrr 1 4 1 [0, 0, 2, 5, 10551389, 1]
# 5 [0, 0, 2, 5, 10551389, 1] addr 1 3 3 [0, 0, 2, 6, 10551389, 1]
# 6 [0, 0, 2, 6, 10551389, 1] addi 3 1 3 [0, 0, 2, 8, 10551389, 1]
# 8 [0, 0, 2, 8, 10551389, 1] addi 2 1 2 [0, 0, 3, 9, 10551389, 1]
# (0, 0, '?', 9, '?', 1) [0, 0, 10551387, 9, 10551389, 1] (0, 0, 2, 9, 10551389, 1)

# 9 [0, 0, 10551387, 9, 10551389, 1] gtrr 2 4 1 [0, 0, 10551387, 10, 10551389, 1]
# 10 [0, 0, 10551387, 10, 10551389, 1] addr 3 1 3 [0, 0, 10551387, 11, 10551389, 1]
# 11 [0, 0, 10551387, 11, 10551389, 1] seti 2 5 3 [0, 0, 10551387, 3, 10551389, 1]
# 3 [0, 0, 10551387, 3, 10551389, 1] mulr 5 2 1 [0, 10551387, 10551387, 4, 10551389, 1]
# 4 [0, 10551387, 10551387, 4, 10551389, 1] eqrr 1 4 1 [0, 0, 10551387, 5, 10551389, 1]
# 5 [0, 0, 10551387, 5, 10551389, 1] addr 1 3 3 [0, 0, 10551387, 6, 10551389, 1]
# 6 [0, 0, 10551387, 6, 10551389, 1] addi 3 1 3 [0, 0, 10551387, 8, 10551389, 1]
# 8 [0, 0, 10551387, 8, 10551389, 1] addi 2 1 2 [0, 0, 10551388, 9, 10551389, 1]

# 9 [0, 0, 10551388, 9, 10551389, 1] gtrr 2 4 1 [0, 0, 10551388, 10, 10551389, 1]
# 10 [0, 0, 10551388, 10, 10551389, 1] addr 3 1 3 [0, 0, 10551388, 11, 10551389, 1]
# 11 [0, 0, 10551388, 11, 10551389, 1] seti 2 5 3 [0, 0, 10551388, 3, 10551389, 1]
# 3 [0, 0, 10551388, 3, 10551389, 1] mulr 5 2 1 [0, 10551388, 10551388, 4, 10551389, 1]
# 4 [0, 10551388, 10551388, 4, 10551389, 1] eqrr 1 4 1 [0, 0, 10551388, 5, 10551389, 1]
# 5 [0, 0, 10551388, 5, 10551389, 1] addr 1 3 3 [0, 0, 10551388, 6, 10551389, 1]
# 6 [0, 0, 10551388, 6, 10551389, 1] addi 3 1 3 [0, 0, 10551388, 8, 10551389, 1]
# 8 [0, 0, 10551388, 8, 10551389, 1] addi 2 1 2 [0, 0, 10551389, 9, 10551389, 1]

# 9 [0, 0, 10551389, 9, 10551389, 1] gtrr 2 4 1 [0, 0, 10551389, 10, 10551389, 1]
# 10 [0, 0, 10551389, 10, 10551389, 1] addr 3 1 3 [0, 0, 10551389, 11, 10551389, 1]
# 11 [0, 0, 10551389, 11, 10551389, 1] seti 2 5 3 [0, 0, 10551389, 3, 10551389, 1]
# 3 [0, 0, 10551389, 3, 10551389, 1] mulr 5 2 1 [0, 10551389, 10551389, 4, 10551389, 1]
# 4 [0, 10551389, 10551389, 4, 10551389, 1] eqrr 1 4 1 [0, 1, 10551389, 5, 10551389, 1]
# 5 [0, 1, 10551389, 5, 10551389, 1] addr 1 3 3 [0, 1, 10551389, 7, 10551389, 1]
# 7 [0, 1, 10551389, 7, 10551389, 1] addr 5 0 0 [1, 1, 10551389, 8, 10551389, 1]
# 8 [1, 1, 10551389, 8, 10551389, 1] addi 2 1 2 [1, 1, 10551390, 9, 10551389, 1]

# 9 [1, 1, 10551390, 9, 10551389, 1] gtrr 2 4 1 [1, 1, 10551390, 10, 10551389, 1]
# 10 [1, 1, 10551390, 10, 10551389, 1] addr 3 1 3 [1, 1, 10551390, 12, 10551389, 1]
# 12 [1, 1, 10551390, 12, 10551389, 1] addi 5 1 5 [1, 1, 10551390, 13, 10551389, 2]
# 13 [1, 1, 10551390, 13, 10551389, 2] gtrr 5 4 1 [1, 0, 10551390, 14, 10551389, 2]
# 14 [1, 0, 10551390, 14, 10551389, 2] addr 1 3 3 [1, 0, 10551390, 15, 10551389, 2]
# 15 [1, 0, 10551390, 15, 10551389, 2] seti 1 2 3 [1, 0, 10551390, 2, 10551389, 2]
# 2 [1, 0, 10551390, 2, 10551389, 2] seti 1 3 2 [1, 0, 1, 3, 10551389, 2]
# 3 [1, 0, 1, 3, 10551389, 2] mulr 5 2 1 [1, 2, 1, 4, 10551389, 2]
# 4 [1, 2, 1, 4, 10551389, 2] eqrr 1 4 1 [1, 0, 1, 5, 10551389, 2]
# 5 [1, 0, 1, 5, 10551389, 2] addr 1 3 3 [1, 0, 1, 6, 10551389, 2]
# 6 [1, 0, 1, 6, 10551389, 2] addi 3 1 3 [1, 0, 1, 8, 10551389, 2]
# 8 [1, 0, 1, 8, 10551389, 2] addi 2 1 2 [1, 0, 2, 9, 10551389, 2]
# 9 [1, 0, 2, 9, 10551389, 2] gtrr 2 4 1 [1, 0, 2, 10, 10551389, 2]
# 10 [1, 0, 2, 10, 10551389, 2] addr 3 1 3 [1, 0, 2, 11, 10551389, 2]
# 11 [1, 0, 2, 11, 10551389, 2] seti 2 5 3 [1, 0, 2, 3, 10551389, 2]
# 3 [1, 0, 2, 3, 10551389, 2] mulr 5 2 1 [1, 4, 2, 4, 10551389, 2]
# 4 [1, 4, 2, 4, 10551389, 2] eqrr 1 4 1 [1, 0, 2, 5, 10551389, 2]
# 5 [1, 0, 2, 5, 10551389, 2] addr 1 3 3 [1, 0, 2, 6, 10551389, 2]
# 6 [1, 0, 2, 6, 10551389, 2] addi 3 1 3 [1, 0, 2, 8, 10551389, 2]
# 8 [1, 0, 2, 8, 10551389, 2] addi 2 1 2 [1, 0, 3, 9, 10551389, 2]

# (1, 0, '?', 9, '?', 2) [1, 0, 10551387, 9, 10551389, 2] (1, 0, 2, 9, 10551389, 2)

# 9 [1, 0, 10551387, 9, 10551389, 2] gtrr 2 4 1 [1, 0, 10551387, 10, 10551389, 2]
# 10 [1, 0, 10551387, 10, 10551389, 2] addr 3 1 3 [1, 0, 10551387, 11, 10551389, 2]
# 11 [1, 0, 10551387, 11, 10551389, 2] seti 2 5 3 [1, 0, 10551387, 3, 10551389, 2]
# 3 [1, 0, 10551387, 3, 10551389, 2] mulr 5 2 1 [1, 21102774, 10551387, 4, 10551389, 2]
# 4 [1, 21102774, 10551387, 4, 10551389, 2] eqrr 1 4 1 [1, 0, 10551387, 5, 10551389, 2]
# 5 [1, 0, 10551387, 5, 10551389, 2] addr 1 3 3 [1, 0, 10551387, 6, 10551389, 2]
# 6 [1, 0, 10551387, 6, 10551389, 2] addi 3 1 3 [1, 0, 10551387, 8, 10551389, 2]
# 8 [1, 0, 10551387, 8, 10551389, 2] addi 2 1 2 [1, 0, 10551388, 9, 10551389, 2]

# 9 [1, 0, 10551388, 9, 10551389, 2] gtrr 2 4 1 [1, 0, 10551388, 10, 10551389, 2]
# 10 [1, 0, 10551388, 10, 10551389, 2] addr 3 1 3 [1, 0, 10551388, 11, 10551389, 2]
# 11 [1, 0, 10551388, 11, 10551389, 2] seti 2 5 3 [1, 0, 10551388, 3, 10551389, 2]
# 3 [1, 0, 10551388, 3, 10551389, 2] mulr 5 2 1 [1, 21102776, 10551388, 4, 10551389, 2]
# 4 [1, 21102776, 10551388, 4, 10551389, 2] eqrr 1 4 1 [1, 0, 10551388, 5, 10551389, 2]
# 5 [1, 0, 10551388, 5, 10551389, 2] addr 1 3 3 [1, 0, 10551388, 6, 10551389, 2]
# 6 [1, 0, 10551388, 6, 10551389, 2] addi 3 1 3 [1, 0, 10551388, 8, 10551389, 2]
# 8 [1, 0, 10551388, 8, 10551389, 2] addi 2 1 2 [1, 0, 10551389, 9, 10551389, 2]

# 9 [1, 0, 10551389, 9, 10551389, 2] gtrr 2 4 1 [1, 0, 10551389, 10, 10551389, 2]
# 10 [1, 0, 10551389, 10, 10551389, 2] addr 3 1 3 [1, 0, 10551389, 11, 10551389, 2]
# 11 [1, 0, 10551389, 11, 10551389, 2] seti 2 5 3 [1, 0, 10551389, 3, 10551389, 2]
# 3 [1, 0, 10551389, 3, 10551389, 2] mulr 5 2 1 [1, 21102778, 10551389, 4, 10551389, 2]
# 4 [1, 21102778, 10551389, 4, 10551389, 2] eqrr 1 4 1 [1, 0, 10551389, 5, 10551389, 2]
# 5 [1, 0, 10551389, 5, 10551389, 2] addr 1 3 3 [1, 0, 10551389, 6, 10551389, 2]
# 6 [1, 0, 10551389, 6, 10551389, 2] addi 3 1 3 [1, 0, 10551389, 8, 10551389, 2]
# 8 [1, 0, 10551389, 8, 10551389, 2] addi 2 1 2 [1, 0, 10551390, 9, 10551389, 2]

# 9 [1, 0, 10551390, 9, 10551389, 2] gtrr 2 4 1 [1, 1, 10551390, 10, 10551389, 2]
# 10 [1, 1, 10551390, 10, 10551389, 2] addr 3 1 3 [1, 1, 10551390, 12, 10551389, 2]
# 12 [1, 1, 10551390, 12, 10551389, 2] addi 5 1 5 [1, 1, 10551390, 13, 10551389, 3]

# (1, 1, 10551390, 13, '?', '?') [1, 1, 10551390, 13, 10551389, 10551387] (1, 1, 10551390, 13, 10551389, 2)

# 13 [1, 1, 10551390, 13, 10551389, 10551387] gtrr 5 4 1 [1, 0, 10551390, 14, 10551389, 10551387]
# 14 [1, 0, 10551390, 14, 10551389, 10551387] addr 1 3 3 [1, 0, 10551390, 15, 10551389, 10551387]
# 15 [1, 0, 10551390, 15, 10551389, 10551387] seti 1 2 3 [1, 0, 10551390, 2, 10551389, 10551387]
# 2 [1, 0, 10551390, 2, 10551389, 10551387] seti 1 3 2 [1, 0, 1, 3, 10551389, 10551387]
# 3 [1, 0, 1, 3, 10551389, 10551387] mulr 5 2 1 [1, 10551387, 1, 4, 10551389, 10551387]
# 4 [1, 10551387, 1, 4, 10551389, 10551387] eqrr 1 4 1 [1, 0, 1, 5, 10551389, 10551387]
# 5 [1, 0, 1, 5, 10551389, 10551387] addr 1 3 3 [1, 0, 1, 6, 10551389, 10551387]
# 6 [1, 0, 1, 6, 10551389, 10551387] addi 3 1 3 [1, 0, 1, 8, 10551389, 10551387]
# 8 [1, 0, 1, 8, 10551389, 10551387] addi 2 1 2 [1, 0, 2, 9, 10551389, 10551387]
# 9 [1, 0, 2, 9, 10551389, 10551387] gtrr 2 4 1 [1, 0, 2, 10, 10551389, 10551387]
# 10 [1, 0, 2, 10, 10551389, 10551387] addr 3 1 3 [1, 0, 2, 11, 10551389, 10551387]
# 11 [1, 0, 2, 11, 10551389, 10551387] seti 2 5 3 [1, 0, 2, 3, 10551389, 10551387]
# 3 [1, 0, 2, 3, 10551389, 10551387] mulr 5 2 1 [1, 21102774, 2, 4, 10551389, 10551387]
# 4 [1, 21102774, 2, 4, 10551389, 10551387] eqrr 1 4 1 [1, 0, 2, 5, 10551389, 10551387]
# 5 [1, 0, 2, 5, 10551389, 10551387] addr 1 3 3 [1, 0, 2, 6, 10551389, 10551387]
# 6 [1, 0, 2, 6, 10551389, 10551387] addi 3 1 3 [1, 0, 2, 8, 10551389, 10551387]
# 8 [1, 0, 2, 8, 10551389, 10551387] addi 2 1 2 [1, 0, 3, 9, 10551389, 10551387]
# (1, 0, '?', 9, '?', 10551387) [1, 0, 10551387, 9, 10551389, 10551387] (1, 0, 2, 9, 10551389, 10551387)
# 9 [1, 0, 10551387, 9, 10551389, 10551387] gtrr 2 4 1 [1, 0, 10551387, 10, 10551389, 10551387]
# 10 [1, 0, 10551387, 10, 10551389, 10551387] addr 3 1 3 [1, 0, 10551387, 11, 10551389, 10551387]
# 11 [1, 0, 10551387, 11, 10551389, 10551387] seti 2 5 3 [1, 0, 10551387, 3, 10551389, 10551387]
# 3 [1, 0, 10551387, 3, 10551389, 10551387] mulr 5 2 1 [1, 111331767623769, 10551387, 4, 10551389, 10551387]
# 4 [1, 111331767623769, 10551387, 4, 10551389, 10551387] eqrr 1 4 1 [1, 0, 10551387, 5, 10551389, 10551387]
# 5 [1, 0, 10551387, 5, 10551389, 10551387] addr 1 3 3 [1, 0, 10551387, 6, 10551389, 10551387]
# 6 [1, 0, 10551387, 6, 10551389, 10551387] addi 3 1 3 [1, 0, 10551387, 8, 10551389, 10551387]
# 8 [1, 0, 10551387, 8, 10551389, 10551387] addi 2 1 2 [1, 0, 10551388, 9, 10551389, 10551387]
# 9 [1, 0, 10551388, 9, 10551389, 10551387] gtrr 2 4 1 [1, 0, 10551388, 10, 10551389, 10551387]
# 10 [1, 0, 10551388, 10, 10551389, 10551387] addr 3 1 3 [1, 0, 10551388, 11, 10551389, 10551387]
# 11 [1, 0, 10551388, 11, 10551389, 10551387] seti 2 5 3 [1, 0, 10551388, 3, 10551389, 10551387]
# 3 [1, 0, 10551388, 3, 10551389, 10551387] mulr 5 2 1 [1, 111331778175156, 10551388, 4, 10551389, 10551387]
# 4 [1, 111331778175156, 10551388, 4, 10551389, 10551387] eqrr 1 4 1 [1, 0, 10551388, 5, 10551389, 10551387]
# 5 [1, 0, 10551388, 5, 10551389, 10551387] addr 1 3 3 [1, 0, 10551388, 6, 10551389, 10551387]
# 6 [1, 0, 10551388, 6, 10551389, 10551387] addi 3 1 3 [1, 0, 10551388, 8, 10551389, 10551387]
# 8 [1, 0, 10551388, 8, 10551389, 10551387] addi 2 1 2 [1, 0, 10551389, 9, 10551389, 10551387]
# 9 [1, 0, 10551389, 9, 10551389, 10551387] gtrr 2 4 1 [1, 0, 10551389, 10, 10551389, 10551387]
# 10 [1, 0, 10551389, 10, 10551389, 10551387] addr 3 1 3 [1, 0, 10551389, 11, 10551389, 10551387]
# 11 [1, 0, 10551389, 11, 10551389, 10551387] seti 2 5 3 [1, 0, 10551389, 3, 10551389, 10551387]
# 3 [1, 0, 10551389, 3, 10551389, 10551387] mulr 5 2 1 [1, 111331788726543, 10551389, 4, 10551389, 10551387]
# 4 [1, 111331788726543, 10551389, 4, 10551389, 10551387] eqrr 1 4 1 [1, 0, 10551389, 5, 10551389, 10551387]
# 5 [1, 0, 10551389, 5, 10551389, 10551387] addr 1 3 3 [1, 0, 10551389, 6, 10551389, 10551387]
# 6 [1, 0, 10551389, 6, 10551389, 10551387] addi 3 1 3 [1, 0, 10551389, 8, 10551389, 10551387]
# 8 [1, 0, 10551389, 8, 10551389, 10551387] addi 2 1 2 [1, 0, 10551390, 9, 10551389, 10551387]
# 9 [1, 0, 10551390, 9, 10551389, 10551387] gtrr 2 4 1 [1, 1, 10551390, 10, 10551389, 10551387]
# 10 [1, 1, 10551390, 10, 10551389, 10551387] addr 3 1 3 [1, 1, 10551390, 12, 10551389, 10551387]
# 12 [1, 1, 10551390, 12, 10551389, 10551387] addi 5 1 5 [1, 1, 10551390, 13, 10551389, 10551388]
# 13 [1, 1, 10551390, 13, 10551389, 10551388] gtrr 5 4 1 [1, 0, 10551390, 14, 10551389, 10551388]
# 14 [1, 0, 10551390, 14, 10551389, 10551388] addr 1 3 3 [1, 0, 10551390, 15, 10551389, 10551388]
# 15 [1, 0, 10551390, 15, 10551389, 10551388] seti 1 2 3 [1, 0, 10551390, 2, 10551389, 10551388]
# 2 [1, 0, 10551390, 2, 10551389, 10551388] seti 1 3 2 [1, 0, 1, 3, 10551389, 10551388]
# 3 [1, 0, 1, 3, 10551389, 10551388] mulr 5 2 1 [1, 10551388, 1, 4, 10551389, 10551388]
# 4 [1, 10551388, 1, 4, 10551389, 10551388] eqrr 1 4 1 [1, 0, 1, 5, 10551389, 10551388]
# 5 [1, 0, 1, 5, 10551389, 10551388] addr 1 3 3 [1, 0, 1, 6, 10551389, 10551388]
# 6 [1, 0, 1, 6, 10551389, 10551388] addi 3 1 3 [1, 0, 1, 8, 10551389, 10551388]
# 8 [1, 0, 1, 8, 10551389, 10551388] addi 2 1 2 [1, 0, 2, 9, 10551389, 10551388]
# 9 [1, 0, 2, 9, 10551389, 10551388] gtrr 2 4 1 [1, 0, 2, 10, 10551389, 10551388]
# 10 [1, 0, 2, 10, 10551389, 10551388] addr 3 1 3 [1, 0, 2, 11, 10551389, 10551388]
# 11 [1, 0, 2, 11, 10551389, 10551388] seti 2 5 3 [1, 0, 2, 3, 10551389, 10551388]
# 3 [1, 0, 2, 3, 10551389, 10551388] mulr 5 2 1 [1, 21102776, 2, 4, 10551389, 10551388]
# 4 [1, 21102776, 2, 4, 10551389, 10551388] eqrr 1 4 1 [1, 0, 2, 5, 10551389, 10551388]
# 5 [1, 0, 2, 5, 10551389, 10551388] addr 1 3 3 [1, 0, 2, 6, 10551389, 10551388]
# 6 [1, 0, 2, 6, 10551389, 10551388] addi 3 1 3 [1, 0, 2, 8, 10551389, 10551388]
# 8 [1, 0, 2, 8, 10551389, 10551388] addi 2 1 2 [1, 0, 3, 9, 10551389, 10551388]
# (1, 0, '?', 9, '?', 10551388) [1, 0, 10551387, 9, 10551389, 10551388] (1, 0, 2, 9, 10551389, 10551388)
# 9 [1, 0, 10551387, 9, 10551389, 10551388] gtrr 2 4 1 [1, 0, 10551387, 10, 10551389, 10551388]
# 10 [1, 0, 10551387, 10, 10551389, 10551388] addr 3 1 3 [1, 0, 10551387, 11, 10551389, 10551388]
# 11 [1, 0, 10551387, 11, 10551389, 10551388] seti 2 5 3 [1, 0, 10551387, 3, 10551389, 10551388]
# 3 [1, 0, 10551387, 3, 10551389, 10551388] mulr 5 2 1 [1, 111331778175156, 10551387, 4, 10551389, 10551388]
# 4 [1, 111331778175156, 10551387, 4, 10551389, 10551388] eqrr 1 4 1 [1, 0, 10551387, 5, 10551389, 10551388]
# 5 [1, 0, 10551387, 5, 10551389, 10551388] addr 1 3 3 [1, 0, 10551387, 6, 10551389, 10551388]
# 6 [1, 0, 10551387, 6, 10551389, 10551388] addi 3 1 3 [1, 0, 10551387, 8, 10551389, 10551388]
# 8 [1, 0, 10551387, 8, 10551389, 10551388] addi 2 1 2 [1, 0, 10551388, 9, 10551389, 10551388]
# 9 [1, 0, 10551388, 9, 10551389, 10551388] gtrr 2 4 1 [1, 0, 10551388, 10, 10551389, 10551388]
# 10 [1, 0, 10551388, 10, 10551389, 10551388] addr 3 1 3 [1, 0, 10551388, 11, 10551389, 10551388]
# 11 [1, 0, 10551388, 11, 10551389, 10551388] seti 2 5 3 [1, 0, 10551388, 3, 10551389, 10551388]
# 3 [1, 0, 10551388, 3, 10551389, 10551388] mulr 5 2 1 [1, 111331788726544, 10551388, 4, 10551389, 10551388]
# 4 [1, 111331788726544, 10551388, 4, 10551389, 10551388] eqrr 1 4 1 [1, 0, 10551388, 5, 10551389, 10551388]
# 5 [1, 0, 10551388, 5, 10551389, 10551388] addr 1 3 3 [1, 0, 10551388, 6, 10551389, 10551388]
# 6 [1, 0, 10551388, 6, 10551389, 10551388] addi 3 1 3 [1, 0, 10551388, 8, 10551389, 10551388]
# 8 [1, 0, 10551388, 8, 10551389, 10551388] addi 2 1 2 [1, 0, 10551389, 9, 10551389, 10551388]
# 9 [1, 0, 10551389, 9, 10551389, 10551388] gtrr 2 4 1 [1, 0, 10551389, 10, 10551389, 10551388]
# 10 [1, 0, 10551389, 10, 10551389, 10551388] addr 3 1 3 [1, 0, 10551389, 11, 10551389, 10551388]
# 11 [1, 0, 10551389, 11, 10551389, 10551388] seti 2 5 3 [1, 0, 10551389, 3, 10551389, 10551388]
# 3 [1, 0, 10551389, 3, 10551389, 10551388] mulr 5 2 1 [1, 111331799277932, 10551389, 4, 10551389, 10551388]
# 4 [1, 111331799277932, 10551389, 4, 10551389, 10551388] eqrr 1 4 1 [1, 0, 10551389, 5, 10551389, 10551388]
# 5 [1, 0, 10551389, 5, 10551389, 10551388] addr 1 3 3 [1, 0, 10551389, 6, 10551389, 10551388]
# 6 [1, 0, 10551389, 6, 10551389, 10551388] addi 3 1 3 [1, 0, 10551389, 8, 10551389, 10551388]
# 8 [1, 0, 10551389, 8, 10551389, 10551388] addi 2 1 2 [1, 0, 10551390, 9, 10551389, 10551388]
# 9 [1, 0, 10551390, 9, 10551389, 10551388] gtrr 2 4 1 [1, 1, 10551390, 10, 10551389, 10551388]
# 10 [1, 1, 10551390, 10, 10551389, 10551388] addr 3 1 3 [1, 1, 10551390, 12, 10551389, 10551388]
# 12 [1, 1, 10551390, 12, 10551389, 10551388] addi 5 1 5 [1, 1, 10551390, 13, 10551389, 10551389]
# 13 [1, 1, 10551390, 13, 10551389, 10551389] gtrr 5 4 1 [1, 0, 10551390, 14, 10551389, 10551389]
# 14 [1, 0, 10551390, 14, 10551389, 10551389] addr 1 3 3 [1, 0, 10551390, 15, 10551389, 10551389]
# 15 [1, 0, 10551390, 15, 10551389, 10551389] seti 1 2 3 [1, 0, 10551390, 2, 10551389, 10551389]
# 2 [1, 0, 10551390, 2, 10551389, 10551389] seti 1 3 2 [1, 0, 1, 3, 10551389, 10551389]
# 3 [1, 0, 1, 3, 10551389, 10551389] mulr 5 2 1 [1, 10551389, 1, 4, 10551389, 10551389]
# 4 [1, 10551389, 1, 4, 10551389, 10551389] eqrr 1 4 1 [1, 1, 1, 5, 10551389, 10551389]
# 5 [1, 1, 1, 5, 10551389, 10551389] addr 1 3 3 [1, 1, 1, 7, 10551389, 10551389]
# 7 [1, 1, 1, 7, 10551389, 10551389] addr 5 0 0 [10551390, 1, 1, 8, 10551389, 10551389]
# 8 [10551390, 1, 1, 8, 10551389, 10551389] addi 2 1 2 [10551390, 1, 2, 9, 10551389, 10551389]
# 9 [10551390, 1, 2, 9, 10551389, 10551389] gtrr 2 4 1 [10551390, 0, 2, 10, 10551389, 10551389]
# 10 [10551390, 0, 2, 10, 10551389, 10551389] addr 3 1 3 [10551390, 0, 2, 11, 10551389, 10551389]
# 11 [10551390, 0, 2, 11, 10551389, 10551389] seti 2 5 3 [10551390, 0, 2, 3, 10551389, 10551389]
# 3 [10551390, 0, 2, 3, 10551389, 10551389] mulr 5 2 1 [10551390, 21102778, 2, 4, 10551389, 10551389]
# 4 [10551390, 21102778, 2, 4, 10551389, 10551389] eqrr 1 4 1 [10551390, 0, 2, 5, 10551389, 10551389]
# 5 [10551390, 0, 2, 5, 10551389, 10551389] addr 1 3 3 [10551390, 0, 2, 6, 10551389, 10551389]
# 6 [10551390, 0, 2, 6, 10551389, 10551389] addi 3 1 3 [10551390, 0, 2, 8, 10551389, 10551389]
# 8 [10551390, 0, 2, 8, 10551389, 10551389] addi 2 1 2 [10551390, 0, 3, 9, 10551389, 10551389]
# 9 [10551390, 0, 3, 9, 10551389, 10551389] gtrr 2 4 1 [10551390, 0, 3, 10, 10551389, 10551389]
# 10 [10551390, 0, 3, 10, 10551389, 10551389] addr 3 1 3 [10551390, 0, 3, 11, 10551389, 10551389]
# 11 [10551390, 0, 3, 11, 10551389, 10551389] seti 2 5 3 [10551390, 0, 3, 3, 10551389, 10551389]
# 3 [10551390, 0, 3, 3, 10551389, 10551389] mulr 5 2 1 [10551390, 31654167, 3, 4, 10551389, 10551389]
# 4 [10551390, 31654167, 3, 4, 10551389, 10551389] eqrr 1 4 1 [10551390, 0, 3, 5, 10551389, 10551389]
# 5 [10551390, 0, 3, 5, 10551389, 10551389] addr 1 3 3 [10551390, 0, 3, 6, 10551389, 10551389]
# 6 [10551390, 0, 3, 6, 10551389, 10551389] addi 3 1 3 [10551390, 0, 3, 8, 10551389, 10551389]
# 8 [10551390, 0, 3, 8, 10551389, 10551389] addi 2 1 2 [10551390, 0, 4, 9, 10551389, 10551389]
# (10551390, 0, '?', 9, '?', 10551389) [10551390, 0, 10551387, 9, 10551389, 10551389] (10551390, 0, 3, 9, 10551389, 10551389)
# 9 [10551390, 0, 10551387, 9, 10551389, 10551389] gtrr 2 4 1 [10551390, 0, 10551387, 10, 10551389, 10551389]
# 10 [10551390, 0, 10551387, 10, 10551389, 10551389] addr 3 1 3 [10551390, 0, 10551387, 11, 10551389, 10551389]
# 11 [10551390, 0, 10551387, 11, 10551389, 10551389] seti 2 5 3 [10551390, 0, 10551387, 3, 10551389, 10551389]
# 3 [10551390, 0, 10551387, 3, 10551389, 10551389] mulr 5 2 1 [10551390, 111331788726543, 10551387, 4, 10551389, 10551389]
# 4 [10551390, 111331788726543, 10551387, 4, 10551389, 10551389] eqrr 1 4 1 [10551390, 0, 10551387, 5, 10551389, 10551389]
# 5 [10551390, 0, 10551387, 5, 10551389, 10551389] addr 1 3 3 [10551390, 0, 10551387, 6, 10551389, 10551389]
# 6 [10551390, 0, 10551387, 6, 10551389, 10551389] addi 3 1 3 [10551390, 0, 10551387, 8, 10551389, 10551389]
# 8 [10551390, 0, 10551387, 8, 10551389, 10551389] addi 2 1 2 [10551390, 0, 10551388, 9, 10551389, 10551389]
# 9 [10551390, 0, 10551388, 9, 10551389, 10551389] gtrr 2 4 1 [10551390, 0, 10551388, 10, 10551389, 10551389]
# 10 [10551390, 0, 10551388, 10, 10551389, 10551389] addr 3 1 3 [10551390, 0, 10551388, 11, 10551389, 10551389]
# 11 [10551390, 0, 10551388, 11, 10551389, 10551389] seti 2 5 3 [10551390, 0, 10551388, 3, 10551389, 10551389]
# 3 [10551390, 0, 10551388, 3, 10551389, 10551389] mulr 5 2 1 [10551390, 111331799277932, 10551388, 4, 10551389, 10551389]
# 4 [10551390, 111331799277932, 10551388, 4, 10551389, 10551389] eqrr 1 4 1 [10551390, 0, 10551388, 5, 10551389, 10551389]
# 5 [10551390, 0, 10551388, 5, 10551389, 10551389] addr 1 3 3 [10551390, 0, 10551388, 6, 10551389, 10551389]
# 6 [10551390, 0, 10551388, 6, 10551389, 10551389] addi 3 1 3 [10551390, 0, 10551388, 8, 10551389, 10551389]
# 8 [10551390, 0, 10551388, 8, 10551389, 10551389] addi 2 1 2 [10551390, 0, 10551389, 9, 10551389, 10551389]
# 9 [10551390, 0, 10551389, 9, 10551389, 10551389] gtrr 2 4 1 [10551390, 0, 10551389, 10, 10551389, 10551389]
# 10 [10551390, 0, 10551389, 10, 10551389, 10551389] addr 3 1 3 [10551390, 0, 10551389, 11, 10551389, 10551389]
# 11 [10551390, 0, 10551389, 11, 10551389, 10551389] seti 2 5 3 [10551390, 0, 10551389, 3, 10551389, 10551389]
# 3 [10551390, 0, 10551389, 3, 10551389, 10551389] mulr 5 2 1 [10551390, 111331809829321, 10551389, 4, 10551389, 10551389]
# 4 [10551390, 111331809829321, 10551389, 4, 10551389, 10551389] eqrr 1 4 1 [10551390, 0, 10551389, 5, 10551389, 10551389]
# 5 [10551390, 0, 10551389, 5, 10551389, 10551389] addr 1 3 3 [10551390, 0, 10551389, 6, 10551389, 10551389]
# 6 [10551390, 0, 10551389, 6, 10551389, 10551389] addi 3 1 3 [10551390, 0, 10551389, 8, 10551389, 10551389]
# 8 [10551390, 0, 10551389, 8, 10551389, 10551389] addi 2 1 2 [10551390, 0, 10551390, 9, 10551389, 10551389]
# 9 [10551390, 0, 10551390, 9, 10551389, 10551389] gtrr 2 4 1 [10551390, 1, 10551390, 10, 10551389, 10551389]
# 10 [10551390, 1, 10551390, 10, 10551389, 10551389] addr 3 1 3 [10551390, 1, 10551390, 12, 10551389, 10551389]
# 12 [10551390, 1, 10551390, 12, 10551389, 10551389] addi 5 1 5 [10551390, 1, 10551390, 13, 10551389, 10551390]
# 13 [10551390, 1, 10551390, 13, 10551389, 10551390] gtrr 5 4 1 [10551390, 1, 10551390, 14, 10551389, 10551390]
# 14 [10551390, 1, 10551390, 14, 10551389, 10551390] addr 1 3 3 [10551390, 1, 10551390, 16, 10551389, 10551390]
# 16 [10551390, 1, 10551390, 16, 10551389, 10551390] mulr 3 3 3 [10551390, 1, 10551390, 257, 10551389, 10551390]
# {(0, 0, '?', 9, '?', 1): None, (1, 1, '?', 9, '?', 1): (1, 1, 10551390, 9, 10551389, 1), (1, 0, '?', 9, '?', 2): None, (1, 1, 10551390, 13, '?', '?'): None, (1, 0, '?', 9, '?', 10551387): None, (1, 0, '?', 9, '?', 10551388): None, (10551390, 1, '?', 9, '?', 10551389): (10551390, 1, 2, 9, 10551389, 10551389), (10551390, 0, '?', 9, '?', 10551389): None, (10551390, 1, 10551390, 13, '?', '?'): (10551390, 1, 10551390, 13, 10551389, 10551390)}
# [10551390, 1, 10551390, 256, 10551389, 10551390]