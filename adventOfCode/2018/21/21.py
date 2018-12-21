from collections import defaultdict

from tqdm import tqdm


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

instructions = []
with open('input.txt') as f:
    for line in f:
        o, a, b, c = line.strip().split()
        instructions.append((ops[o], int(a), int(b), int(c)))
ipr = 5


register = [0] + [0] * 5
ip = 0
s = set()
with tqdm() as t:
    while ip < len(instructions):
        t.update()
        op, a, b, c = instructions[ip]
        op(register, a, b, c)
        print(ip, str(op)[10:14], a, b, c, register)
        # print([bin(r)[2:] for r in register])
        register[ipr] += 1
        ip = register[ipr]
        if ip == 6:
            print('----', ip, str(op)[10:14], a, b, c, register)
            # print([bin(r)[2:] for r in register])
        if t.n > 10000:
            break
register[ipr] -= 1


print(register)
