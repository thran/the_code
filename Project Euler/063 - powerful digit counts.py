n = 1
while True:
    # print n, len(str(9**n))
    if n > len(str(9**n)):
        break
    n+=1

hits = 0
for n in range(1, n+1):
    for a in range(1, 10):
        if n == len(str(a**n)):
            hits += 1

print hits