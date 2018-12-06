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
