import numpy as np
from tqdm import tqdm

size = 50
court = np.zeros((size, size))

with open('input.txt') as f:
    for x, line in enumerate(f):
        for y, p in enumerate(line.strip()):

            court[x][y] = 0 if p == '.' else (1 if p == '|' else 2)


def s(court):
    r = ''
    for row in court:
        for f in row:
            if f == 0:
                r += '.'
            if f == 1:
                r += '|'
            if f == 2:
                r += '#'
        r += '\n'
    return r


def step(court):
    new = np.zeros(shape=court.shape)
    for x in range(size):
        for y in range(size):
            c = court[x][y]
            area = court[max(0, x-1):min(x+2,size), max(0,y-1):min(y+2,size)]
            if c == 0 and (area == 1).sum() >= 3:
                new[x][y] = 1
            elif c == 1 and (area == 2).sum() >= 3:
                new[x][y] = 2
            elif c == 2 and ((area == 2).sum() == 1 or (area == 1).sum() == 0):
                new[x][y] = 0
            else:
                new[x][y] = c
    return new


history = {}
s(court)
for i in tqdm(range((1000000000 - 518) % (546 - 518) + 518)):
    court = step(court)
    rep = s(court)
    if rep in history:
        print(i, history[rep])      # 546 518
        exit()
    history[rep] = i
    # print(rep)

print((court == 1).sum() * (court == 2).sum())
