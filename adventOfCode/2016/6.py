from collections import Counter

with open('6.txt') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]

data = ['' for i in  range(len(lines[0]))]

for line in lines:
    for i, l in enumerate(line):
        data[i] += l

r = ''
for x in data:
    c = Counter(x)
    print(c)
    r += c.most_common()[-1][0]

print(r)
