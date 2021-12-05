import numpy as np
import pandas as pd
from tqdm import tqdm
from icecream import ic

from utils import memoize

losi = pd.read_csv('losi-priklad.csv', index_col=0)
losice = pd.read_csv('losice-priklad.csv', index_col=0)
losi = pd.read_csv('losi.csv', index_col=0)
losice = pd.read_csv('losice.csv', index_col=0)


s = losi + losice
s[losi < 4 ] = None
s[losice < 4 ] = None
s = s.values

print(s.shape)

top = 0


@memoize
def possible_combinations(ns, m=0):
    global top
    if len(ns) == 1:
        v = s[-1, ns[0]]
        if pd.notna(v) and v + m > top:
            top = v + m
            print(top)
        return v

    results = []
    for i, n in sorted(enumerate(s[-len(ns), ns]), key=lambda x: -x[1]):
        if pd.notna(n):
            r = possible_combinations(ns[:i] + ns[i + 1:], m + n)
            if pd.notna(r):
                results.append(n + r)
    if results:
        return max(results)
    return np.nan


# ic(possible_combinations((0, )))
print(possible_combinations(tuple(range(len(s)))))
