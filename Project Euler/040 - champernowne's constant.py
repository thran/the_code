s = ""
i = 0
while len(s) <= 10 ** 6:
    s += str(i)
    i += 1

p = 1
for i in range(7):
    p *= int(s[10**i])

print p