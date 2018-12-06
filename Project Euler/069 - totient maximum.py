from primes import phi, is_prime, primes

x = 1
for p in primes():
    if x * p > 10 ** 6:
        break
    x *= p

print x