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
def prde(r, a, b, c): r[c] = r[c] = r[a] // b
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
    'prde': prde,
    'nono': None,
}

instructions = []
with open('input.txt') as f:
    for line in f:
        o, a, b, c = line.strip().split()
        instructions.append((ops[o], int(a), int(b), int(c)))
ipr = 5


register = [0] + [0] * 5
ip = 0
li = []
with tqdm(total=11545) as t:
    while ip < len(instructions):
        op, a, b, c = instructions[ip]
        op(register, a, b, c)
        # print(ip, str(op)[10:14], a, b, c, register)
        register[ipr] += 1
        ip = register[ipr]
        if ip == 29:
            if register[3] in li:
                print(li[-1], len(li))
                break
            li.append(register[3])
            t.update()
register[ipr] -= 1


print(register)
print(li[-1])