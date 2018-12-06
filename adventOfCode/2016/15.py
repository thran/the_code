disc = (
    (5, 2),
    (13, 7),
    (17, 10),
    (3, 2),
    (19, 9),
    (7, 0),
    (11, 0),
)

t = 0
while True:
    for i, (positions, start) in enumerate(disc):
        if (start + t + i + 1) % positions != 0:
            break
    else:
        print(t)
        break
    t += 1
