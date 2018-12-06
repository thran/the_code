def next_collatz(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1

def collatz_lenght(n):
    if n == 1: return 1

    return collatz_lenght(next_collatz(n)) + 1

m = 0
best = 0
for i in range(1, 10**6):
    l = collatz_lenght(i)
    if m < l:
        m = l
        best = i

print m, best