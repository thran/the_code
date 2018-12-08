from tqdm import tqdm
import numpy as np
import re

data = []
max_weight, max_height = 0, 0
with open('input.txt') as f:
    for line in f:
        id, left, top, width, height = re.match(f'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line.strip()).groups()
        data.append({
            'id': int(id),
            'left': int(left),
            'top': int(top),
            'width': int(width),
            'height': int(height),
        })
        h = int(top) + int(height)
        w = int(left) + int(width)

        if h > max_height:
            max_height = h
        if w > max_weight:
            max_weight = w


print(max_weight, max_height)


fabrik = np.zeros((max_weight, max_height))

for d in data:
    fabrik[d['left']:d['left']+d['width'], d['top']:d['top']+d['height']] += 1

overlaps = (fabrik > 1)
print(overlaps.sum())


for d in data:
    if overlaps[d['left']:d['left']+d['width'], d['top']:d['top']+d['height']].sum() == 0:
        print(d['id'])
