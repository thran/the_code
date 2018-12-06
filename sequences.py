import math


def is_triangle_number(n):
    x = int(math.sqrt(2 * n))
    return x*(x+1)/2 == n


def is_pentagonal_number(n):
    x = int(math.sqrt(2 * n / 3) + 1)
    return x*(3*x-1)/2 == n


def is_hexagonal_number(n):
    x = int(math.sqrt(n / 2) + 1)
    return x*(2*x-1) == n


def is_heptagonal_number(n):
    x = int(math.sqrt(2 * n / 5) + 1)
    return x*(5*x-3)/2 == n


def is_octagonal_number(n):
    x = int(math.sqrt(n / 3) + 1)
    return x*(3*x-2) == n


def seq_numbers(k):
    n = 1
    while True:
        yield n * ((k-2)*n - k + 4)/2
        n += 1


# for i, n in enumerate(seq_numbers(8)):
#     if i > 20:
#         break
#     print n, is_octagonal_number(n)