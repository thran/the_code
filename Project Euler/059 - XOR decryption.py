from collections import Counter


with open("059 - XOR cipher.txt") as f:
    c = [int(l) for l in f.readline().split(",")]
    # print Counter(c)

    print

    # for i, l in enumerate(c):
    #     if l == 71:
    #         print i % 3

    print chr(71 ^ ord(" "))
    print chr(79 ^ ord(" "))
    print chr(68 ^ ord(" "))

    k = "god"

    m = ""
    s = 0
    for i, l in enumerate(c):
        m += chr(ord(k[i % 3]) ^ l)
        s += ord(k[i % 3]) ^ l

    print m
    print s