import math
from primes import factorization

n = 600851475143
# primes = []
# while n > 1:
#     for i in range(2, int(math.sqrt(n))):
#         if n % i == 0:
#             primes.append(i)
#             n /= i
#             break

# print primes

print factorization(n)

