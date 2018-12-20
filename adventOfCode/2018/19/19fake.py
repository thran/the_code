n = 10551389
# n = 989

s = 0
for a in range(1, n +1):
    if n / a == n // a:
        s += a
print(s)
