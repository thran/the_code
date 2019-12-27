import numpy as np

# inpt = [0, 2, 7, 0]
inpt = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

states = []
steps = 0
while True:
    state = tuple(inpt)
    if state in states:
        steps -= states.index(state)
        break
    states.append(state)
    i = np.argmax([(v, -i) for i, v in enumerate(inpt)], axis=0)[0]
    v = inpt[i]
    inpt[i] = 0

    for j in range(i + 1, i + v + 1):
        inpt[j % len(inpt)] += 1
    steps += 1
    print(inpt)

print(steps)
