from primes import is_prime


def primes_row(a,b):
    n = 0
    count = 0
    while is_prime(n**2 + a * n + b):
        count += 1
        n += 1

    return count-1

max = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        c = primes_row(a, b)
        if max < c:
            max = c
            best = a,b

print best, max