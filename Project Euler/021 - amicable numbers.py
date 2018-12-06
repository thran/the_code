def proper_divisors_sum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

numbers = []
for i in range(1, 10000 +1):
    dn = proper_divisors_sum(i)
    if i == proper_divisors_sum(dn) and i != dn:
        numbers.append(i)

print numbers
print sum(numbers)