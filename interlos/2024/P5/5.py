gates = {}
# with open('input.test.txt') as f:
with open('input.txt') as f:
    lines = list(f)
    for line in lines:
        line = line.strip()
        if line == '':
            break
        op, id, *inputs = line.split()
        if op != 'input':
            gates[int(id)] = op, tuple(map(int, inputs))

values = {}
for i, v in zip(map(int, lines[-3].split()[1:]), lines[-2].split()[1:]):
    values[i] = v == 'Los'

outputs = list(map(int, lines[-1].split()[1:]))
while any(o not in values for o in outputs):
    for id, (op, inputs) in gates.items():
        if id in values:
            continue
        try:
            if op == 'and':
                values[id] = all(values[i] for i in inputs)
            elif op == 'or':
                values[id] = any(values[i] for i in inputs)
            elif op == 'xor':
                values[id] = sum(values[i] for i in inputs) % 2 == 1
            else:
                assert False, op
        except KeyError:
            ...

    print(len(values))

# print(values)
print(''.join('Los' if values[o] else 'Sob' for o in outputs))
