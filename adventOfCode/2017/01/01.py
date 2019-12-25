number = str(open('input.txt').readlines()[0])
print(number)

s = 0
for i, d in enumerate(number):
    if number[(i+1)%len(number)] == d:
        s += int(d)

print(s)


s = 0
for i, d in enumerate(number):
    if number[(i + len(number) // 2) % len(number)] == d:
        s += int(d)

print(s)