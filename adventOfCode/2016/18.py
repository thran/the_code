def step(row):
    new = []
    for i in range(len(row)):
        l = row[i - 1] if i > 0 else False
        c = row[i]
        r = row[i + 1] if i + 1 < len(row) else False
        n = (l and c and not r) or (not l and c and r) or (l and not c and not r) or (not l and not c and r)
        new.append(n)
    return new

row = [t == '^' for t in '^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.']
s = 0
for _ in range(400000):
    # print(''.join(['^' if t else '.' for t in row]))
    s += len(row) - sum(row)
    row = step(row)

print(s)

