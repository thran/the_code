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
with tqdm() as t:
    while ip < len(instructions):
        t.update()
        op, a, b, c = instructions[ip]

        if False and op == gtrr:
            h = hash(register, a, b)
            if h in history:
                hist = history[h]
                if hist is not None:
                    if hist[a] == register[a]:
                        assert False
                    if hist[b] == register[b]:
                        assert register[a] - hist[a] == 1
                        if a == 2 and register[a] < register[4] // register[5]:
                            print(register)
                            register[a] = register[4] // register[5] - 1
                            print(register)
                        else:
                            register[a] = register[b]
                        del history[h]
                    print(h, register, hist)
                    history[h] = None
            else:
                history[h] = tuple(register)

        # print(ip, register, end=' ')
        op(register, a, b, c)
        register[ipr] += 1
        ip = register[ipr]
        print(str(op)[10:14], a, b, c, register)
register[ipr] -= 1
print(history)
print(register)
