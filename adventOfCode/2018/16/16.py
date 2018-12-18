
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


ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

op_map = {i: set(ops) for i in range(len(ops))}

good = 0
with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        before = eval(line.strip()[8:])
        o, a, b, c = map(int, f.readline().strip().split())
        after = eval(f.readline().strip()[8:])
        f.readline()

        count = 0
        for op in ops:
            registr = list(before)
            op(registr, a, b, c)
            if registr == after:
                count += 1
            else:
                op_map[o] -= {op}

        if count >= 3:
            good += 1


print(good)
print()

for _ in range(16):
    for i, os, in op_map.items():
        if len(os) == 1:
            for j in op_map:
                if j != i:
                    op_map[j] -= {list(os)[0]}

# for i, os, in op_map.items():
#     print(i, len(os))

registr = [0, 0, 0, 0]
with open('input2.txt') as f:
    for line in f:
        o, a, b, c = map(int, line.strip().split())
        op = list(op_map[o])[0]
        op(registr, a, b, c)

print(registr)
