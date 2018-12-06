
skip = 0
s = 1
last = [1] * 4
for _ in range(1, (1001+1) / 2):
    for i in range(4):
        skip += 2
        last[i] += skip
    s += sum(last)

print s

