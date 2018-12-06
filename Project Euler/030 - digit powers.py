s = 0
for i in range(2, 9**5 * 6):
    if i == sum([int(d)**5 for d in str(i)]):
        s += i

print s
