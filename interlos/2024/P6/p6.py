import numpy as np

los_count = 1234

shift = np.arange(1234) % 12
loses = np.zeros(1234, dtype=np.int8)
loses.fill(-1)
knows = np.zeros(1234, dtype=bool)
knows[0] = True

steps = 0
while not knows.all():
    steps += 1
    loses = (loses + 1 + shift) % 123
    for room in range(123):
        in_room = np.where(loses == room)[0]
        for new in np.where((loses == room) & ~knows)[0][: knows[in_room].sum()]:
            knows[new] = True
    print(steps, knows.sum())

print(steps)
