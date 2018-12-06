import re

with open('9.txt') as f:
    seq = f.read()




def get_len(seq):
    if '(' not in seq:
        return len(seq)

    i = 0
    s = 0
    while i < len(seq):
        # print(i, seq)
        if seq[i] == '(':
            g = re.search('^(\d+)x(\d+)\)', seq[i + 1:]).groups()
            l = int(g[0])
            r = int(g[1])
            after = i + len(g[0]) + len(g[1]) + 3
            s += get_len(seq[after:after + l]) * r
            i += after - i + l
        else:
            i += 1
            s += 1
    return s

print(get_len(seq))
