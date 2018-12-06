import re
import numpy as np
lights = np.zeros((1000, 1000))

with open("06.txt") as source:
    for line in source.readlines():
        g = re.match(r'(.*) (\d+),(\d+).* (\d+),(\d+)', line).groups()
        if g[0] == "turn on":
            lights[int(g[1]):int(g[3])+1, int(g[2]):int(g[4])+1] += 1
        if g[0] == "turn off":
            lights[int(g[1]):int(g[3])+1, int(g[2]):int(g[4])+1] -= 1
            lights[lights < 0] = 0
        if g[0] == "toggle":
            lights[int(g[1]):int(g[3])+1, int(g[2]):int(g[4])+1] += 2

print lights.sum()
