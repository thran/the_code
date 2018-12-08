import re


visited = {0}
current = 0
found = False
while not found:
    numbers = []
    with open('input.txt') as f:
        for line in f:
            n = int(line.strip())
            numbers.append(n)
            current += n
            if current in visited and not found:
                print(current, n)
                found = True
            visited.add(current)

    print(sum(numbers))
