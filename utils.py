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


def binary_search(fce, goal, lower, upper=None):
    if upper is None:
        upper = lower
        while fce(upper) < goal:
            upper *= 2

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
