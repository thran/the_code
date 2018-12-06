from permutations import permutations
from primes import is_prime

digits = list("7654321")

for p in permutations(digits):
    if is_prime(int("".join(p))):
        print "".join(p)
        exit()