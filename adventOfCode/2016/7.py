with open('7.txt') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]


def check(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


def ABA(s, rev):
    ab = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            ab.append((s[i], s[i + 1]) if not rev else (s[i + 1], s[i]))
    return ab

c = 0
for line in lines:
    parts = line.replace(']', '[').split('[')
    ok = False
    nok = False
    for i, part in enumerate(parts):
        if i % 2 == 1:
            if check(part):
                nok = True
                break
        else:
            if check(part):
                ok = True
    if ok and not nok:
        c += 1

c = 0
for line in lines:
    parts = line.replace(']', '[').split('[')
    inside = []
    outside = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            inside += ABA(part, False)
        else:
            outside += ABA(part, True)

    if len(set(outside) & set(inside)) > 0:
        c += 1

print(c)
