import numpy as np
from tqdm import tqdm

grid_serial_number = 9306


def get_fuel(x, y):
    x = x + 1
    y = y + 1

    rack_id = x + 10
    fuel = rack_id * y
    fuel += grid_serial_number
    fuel *= rack_id
    fuel = fuel // 100 % 10
    fuel -= 5
    return fuel

grid = np.zeros((300, 300))
for x in range(300):
    for y in range(300):
        grid[x, y] = get_fuel(x, y)

m = None
best = None
for size in tqdm(range(1, 300)):
    for i in range(300 - size + 1):
        for j in range(300 - size + 1):
            s = grid[i:i+size,j:j+size].sum()
            if m is None or s > m:
                m = s
                best = i + 1, j + 1, size

print(m, best)
