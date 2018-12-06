import math


def is_pentagonal_number(n):
    x = int(math.sqrt(2 * n / 3)+1)
    return x*(3*x-1)/2 == n


def is_triangle_number(n):
    x = int(math.sqrt(2 * n))
    return x*(x+1)/2 == n


def is_hexagonal_number(n):
    x = int(math.sqrt(n / 2) + 1)
    return x*(2*x-1) == n


def hexagonal_numbers(n=1):
    while True:
        yield n * (2 * n - 1)
        n += 1


hits = 0
for n in hexagonal_numbers():
    if is_pentagonal_number(n) and is_triangle_number(n):
        print n
        hits += 1

    if hits >= 3:
        break