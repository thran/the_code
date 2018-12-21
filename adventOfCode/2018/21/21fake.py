def split(n):
    while n > 0:
        yield n & 255
        n = n // 256


three = 0

se = set()
li = []

while True:
    two = three | (2 ** 16)
    three = 832312
    for s in split(two):
        three += s
        three *= 65899
        three &= (2**24 - 1)
    if three in li:
        print(li[-1])
        break
    li.append(three)
    # print(three)

