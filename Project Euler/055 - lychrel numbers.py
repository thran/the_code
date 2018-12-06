def do(n):
    return n + int(str(n)[::-1])


def is_palyndromic(n):
    return str(n) == str(n)[::-1]

def length(c):
    n = 1
    c = do(c)
    while n < 50:
        if is_palyndromic(c):
            return n
        n += 1
        c = do(c)
    return False


hits = 0
for i in range(1, 10**4):
    if not length(i):
        print i
        hits += 1

print hits