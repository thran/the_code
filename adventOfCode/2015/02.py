from itertools import combinations

total = 0
ribon = 0
with open("02.txt") as source:
    for line in source:
        sides = []
        sizes = sorted(map(int, line.split("x")))
        for x, y in combinations(sizes, 2):
            sides.append(x*y)
        total += 2 * sum(sides) + min(sides)
        ribon += 2 * (sizes[0] + sizes[1]) + sizes[0]*sizes[1]*sizes[2]

print total, ribon