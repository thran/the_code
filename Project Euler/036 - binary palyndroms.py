
found = []
for i in range(1, 10**6):
    if str(i) == str(i)[::-1]:
        b = "{:#b}".format(i)[2:]
        if b == b[::-1]:
            print i
            found.append(i)

print sum(found)
