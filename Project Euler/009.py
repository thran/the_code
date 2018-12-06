

for a in range(1, 5000):
    b = (10**6 - 2000 * a) / (-2. * a + 2000)
    if int(b) == b:
        print a, b, a**2+b**2, (1000-a-b)**2