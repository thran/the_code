from collections import defaultdict

centers = {}
orbiters = defaultdict(list)
neighbours = defaultdict(list)

with open('input.txt') as f:
    for line in f:
        center, orbiter = line.strip().split(')')
        centers[orbiter] = center
        orbiters[center].append(orbiter)
        neighbours[center].append(orbiter)
        neighbours[orbiter].append(center)


checksum = 0
for orbiter in centers.keys():
    current = orbiter
    while current in centers:
        checksum += 1
        current = centers[current]

print(checksum)


currents = ['YOU']
steps = 0

visited = set()
while True:
    new = []
    for current in currents:
        if current == 'SAN':
            print(steps - 2)
            exit()
        for n in neighbours[current]:
            if n not in visited:
                new.append(n)
                visited.add(n)
    currents = new
    steps += 1
