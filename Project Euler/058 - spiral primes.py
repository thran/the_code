from primes import is_prime

skip = 0
last = [1] * 3

side = 1
primes = 0
count = 1.

while True:
    count += 4
    side += 2
    for i in range(3):
        skip += 2
        last[i] += skip
    skip += 2
    for n in last:
        if is_prime(n):
            primes += 1

    print primes / count
    if primes / count < 0.1:
        print side
        break
