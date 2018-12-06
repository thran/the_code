from primes import primes, is_prime

l = 6
while True:
    print l
    stack = []

    for p in primes():
        if sum(stack) > 10 ** 6:
            break

        stack.append(p)
        if len(stack) > l:
            stack.pop(0)

        if len(stack) == l and is_prime(sum(stack)):
            print stack, sum(stack)
            found = p
            break
    l += 1