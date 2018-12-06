def digits(n):
    s = list(str(n))
    s.sort()
    return "".join(s)


def check(n):
    s = digits(n)
    for i in range(2, 7):
        if s != digits(i * n):
            return False
    return True


i = 1
while True:
    if check(i):
        print i
        break
    i += 1
