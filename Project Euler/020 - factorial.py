def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


print sum([int(d) for d in str(factorial(100))])