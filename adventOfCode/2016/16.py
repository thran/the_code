def step(a):
    b = a[::-1]
    b = b.replace('0', '#').replace('1', '0').replace('#', '1')
    return a + '0' + b


def checksum(s):
    if len(s) % 2 == 1:
        return s
    c = ''
    for i in range(0, len(s), 2):
        if s[i] == s[i + 1]:
            c += '1'
        else:
            c += '0'
    return checksum(c)


data = '10001110011110000'
size = 35651584

while len(data) < size:
    data = step(data)

data = data[:size]

print(checksum(data))
