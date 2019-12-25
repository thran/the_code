s = 0
s2 = 0
with open('input.txt') as f:
    for line in f:
        numbers = list(map(int, line.strip().split()))
        s += max(numbers) - min(numbers)
        for n1 in numbers:
            for n2 in numbers:
                if n1 != n2 and n1 % n2 == 0:
                    s2 += n1 // n2

print(s)
print(s2)
