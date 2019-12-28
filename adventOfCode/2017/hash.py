from functools import reduce


def reverse(lst, position, length):
    assert length <= len(lst)
    lst = lst[position:] + lst[:position]
    lst = lst[:length][::-1] + lst[length:]
    lst = lst[-position:] + lst[:-position]
    return lst


def knot(data):
    size = 256
    lengths = list(map(ord, data)) + [17, 31, 73, 47, 23]

    s = list(range(size))

    position = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            s = reverse(s, position, length)
            position = (position + length + skip) % size
            skip += 1

    t = []
    for i in range(16):
        t.append(hex(reduce(lambda a, b: a ^ b, s[i * 16:(i + 1) * 16], 0))[2:])

    return ''.join([f'{u:0>2}' for u in t])
