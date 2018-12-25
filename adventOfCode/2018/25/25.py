import queue

import pandas as pd
import numpy as np


df = pd.read_csv('input.txt', header=None)

distances = df.loc[:, :4]

df['selected'] = False
df['constellation'] = None

value = 3

c = 0
while (~df.selected).sum() > 0:
    x = df.index[~df.selected][0]
    q = queue.Queue()
    q.put(x)
    c += 1
    df.loc[x, 'selected'] = True
    df.loc[x, 'constellation'] = c

    while not q.empty():
        i = q.get()
        d = df.loc[i]
        new = (np.abs(distances - d[:4]).sum(axis=1) <= 3) & ~df.selected
        df.loc[new, 'selected'] = True
        df.loc[new, 'constellation'] = c
        for n in df[new].index.values:
            q.put(n)

print(df)
print(len(df.constellation.unique()))
