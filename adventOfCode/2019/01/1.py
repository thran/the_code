def fuel(module):
    return max(0, module // 3 - 2)


def total_fuel(module):
    total = 0
    new = module
    while new > 0:
        new = fuel(new)
        total += new
    return total


s = 0
with open('input.txt') as f:
    for line in f:
        f = total_fuel(int(line.strip()))
        s += f

print(s)
