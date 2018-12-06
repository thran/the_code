with open('20.txt') as f:
    ranges = [list(map(int, line.split('-'))) for line in f.readlines()]

c = 0
s = 0
for mn, mx in  sorted(ranges):
    print(mn, mx)
    if mn <= c:
        pass
    else:
        s += mn - c
    c = max(c, mx + 1)
print(s)