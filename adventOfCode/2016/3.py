import numpy as np

with open('3.txt') as f:
    lines = [list(map(int, l.replace('\n', '').split())) for l in f.readlines()]


lines2 = []
for i in range(0, len(lines), 3):
    for j in [0, 1, 2]:
        lines2.append([lines[i][j], lines[i + 1][j], lines[i + 2][j]])


c = 0
for line in lines2:
    a = np.argmax(line)
    if line[a] < line[(a + 1) % 3] + line[(a + 2) % 3]:
        c += 1

print(c)