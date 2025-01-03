import math


def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f, **kwargs):
            super(memodict, self).__init__(**kwargs)
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret

    return memodict(f)


def is_square(n):
    return int(math.sqrt(n)) ** 2 == n


def binary_search(fce, goal, lower, upper=None, upper_search_increment=lambda x: x * 2):
    if upper is None:
        upper = lower
        while fce(upper) < goal:
            upper = upper_search_increment(upper)

    while lower < upper - 1:
        mid = (lower + upper) // 2
        value = fce(mid)
        if value > goal:
            upper = mid
        elif value < goal:
            lower = mid
        else:
            return mid
    if fce(lower) == goal:
        return lower
    if fce(upper) == goal:
        return upper
    return lower, upper


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y
