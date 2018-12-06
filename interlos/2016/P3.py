s = """...........
.....###...
.....#.##..
.....#..#..
....##..##.
...##....#.
..##.....##
.##........
.#.........
.#.........
.##........
..#####....
......#....
"""

field = []
for line in s.split('\n'):
    l = []
    for z in line:
        l.append(z)
    field.append(l)

print(field)


def in_range(a, b, x, y):
    if abs(a - x) > 2 or abs(b - y) > 2:
        return False
    if abs(a - x) == 2 and abs(b - y) == 2:
        return False
    return True

def place_S(field):
    for line in enumerate(i, field):