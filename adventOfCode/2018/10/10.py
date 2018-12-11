import re
import pandas as pd
import seaborn as sns
import pylab as plt
from tqdm import tqdm

with open('input.txt') as f:
    data = []
    for line in f:
        x, y, dx, dy = re.match(r'position=< ?(-?\d+),  ?(-?\d+)> velocity=< ?(-?\d+),  ?(-?\d+)>', line.strip()).groups()
        data.append({
            'x': int(x),
            'y':  int(y),
            'dx':  int(dx),
            'dy':  int(dy),
        })

df = pd.DataFrame(data)


# vs = []
# steps = 12000
# for i in tqdm(range(steps)):
#     df.x += df.dx
#     df.y += df.dy
#     vs.append(sum(abs(df.x) + abs(df.y)))
#
# plt.plot(range(steps), vs)
# plt.show()
# hit = pd.np.argmin(vs)
#
# print(hit)

hit = 10710

df = pd.DataFrame(data)
while True:
    plt.plot(df.x + df.dx * hit, df.y + df.dy * hit, '.')
    print(hit)
    plt.show()
    hit -= 1
    input()
