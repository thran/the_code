def show(filed):
    for line in field:
        for x in line:
            print "#" if x else ".",
        print


def nb(field, x, y):
    s = 0
    for i, j in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
        try:
            if i < 0 or j < 0:
                raise IndexError
            s += field[i][j]
        except IndexError:
            pass
    return s

def corners(filed):
    field[0][0] = 1
    field[-1][0] = 1
    field[0][-1] = 1
    field[-1][-1] = 1

steps = 100

field = []

with open("18.txt") as f:
    for i, line in enumerate(f.readlines()):
        field.append([])
        for x in line[:-1]:
            field[i].append(0 if x == "." else 1)
corners(field)

for _ in range(steps):
    new_field = []
    for i, line in enumerate(field):
        new_field.append([])
        for j, x in enumerate(line):
            nbs = nb(field, i, j)
            new_field[i].append(1 if (x and (nbs == 2 or nbs == 3)) or (not x and nbs == 3) else 0)
    field = new_field
    corners(field)
    show(field)
    print

print sum(map(sum, field))