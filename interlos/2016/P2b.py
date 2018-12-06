n = 8

def place(number, x):
    if x == 0:
        print ''.join(map(str, number))
        return
    for p in range(2 * n - x):
        if number[p] == 0 and number[p + x] == 0:
            new = number[:]
            new[p] = new[p + x] = x
            place(new, x - 1)

import time

x = time.time()
place([0] * n * 2, n)
print(time.time() - x)
