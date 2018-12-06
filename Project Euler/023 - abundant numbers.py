from math import sqrt


def proper_divisors_sum(n):
    suma = 0
    for i in range(1, int(sqrt(n)+1)):
        if n % i == 0:
            if i ** 2 == n or i == 1:
                suma += i
            else:
                suma += i + n / i
    return suma

abundants = []
for n in range(1, 28123 + 1):
    if proper_divisors_sum(n) > n:
        abundants.append(n)


candidates = range(28124)

for a in abundants:
    for b in abundants:
        if a+b < 28124:
            candidates[a+b] = 0

print sum(candidates)