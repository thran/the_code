import pandas as pd
from munkres import Munkres  # assigment problem

losi = pd.read_csv('losi-priklad.csv', index_col=0)
losice = pd.read_csv('losice-priklad.csv', index_col=0)
losi = pd.read_csv('losi.csv', index_col=0)
losice = pd.read_csv('losice.csv', index_col=0)


s = losi + losice
s[losi < 4 ] = -10000
s[losice < 4 ] = -10000
m = 20 - s.values

total = 0
for match in Munkres().compute(m):
    total += s.values[match]

print(total)
