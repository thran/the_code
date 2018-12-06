import json
import re
import pandas as pd

import numpy as np
import pylab as plt
import time

numbers = ['745235478', '701001205', '605374214', '736637736', '608777010', '605658124', '700800100']
# times = []
times = json.load(open("times.json"))

if False:
    lat = np.empty((len(numbers), len(times)))
    lat[:] = np.nan
    long = np.empty((len(numbers), len(times)))
    long[:] = np.nan
    t = -1

    with open("P5-snaps.txt") as f:
        s = None
        for i, line in enumerate(f.readlines()):
            print i
            if line[:4] == "snap":
                # t = re.search("\[(.*)\]", line).group(1)
                # t = int(time.mktime(time.strptime(t, "%Y-%m-%d %H:%M:%S")))
                # times.append(t)
                t += 1
            else:
                r = re.search("\[(.*)\] \[\ (.*)  (.*)]", line).groups()
                lat[numbers.index(r[0]), t] = float(r[1])
                long[numbers.index(r[0]), t] = float(r[2])

    np.save("lat.npy", lat)
    np.save("long.npy", long)

# json.dump(times, open("times.json", "w"))
# print times
lat = np.load("lat.npy")
long = np.load("long.npy")


print long[3, 239*1000], lat[3, 239*1000]

for i, n in enumerate(numbers):
    plt.plot(times[::1000], lat[i][::1000]+0.0002*i, "-", label=n, alpha=0.5)
plt.legend(loc=0)

plt.figure()
for i, n in enumerate(numbers):
    plt.plot(range(len(times[::1000])), long[i][::1000]+0.0002*i, "-", label=n   )
# plt.show()

# 49.229624 16.591897
# 700800100ANOBAVORSKÁ