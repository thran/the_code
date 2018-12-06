# n = 5
n = 3012210

elves = [i + 1 for i in range(n)]

current = -1
count = n
d = 0
while len(elves) > 1:
    print(len(elves))
    tr = (1 + current + len(elves) // 2) % len(elves)
    to_remove = set()
    for _ in range(len(elves) // 2):
        current = (current + 1) % len(elves)
        to_remove.add(elves[tr])
        # print(elves[current], d, elves[tr])
        tr = (tr + 1 + d) % len(elves)
        d = (d + 1) % 2

    current = elves[current]
    elves = sorted(list(set(elves) - to_remove))
    current = elves.index(current)

    # print(elves, sorted(to_remove), current)

print(elves)
