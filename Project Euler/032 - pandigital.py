from permutations import permutations

def check(m1, m2, p):
    m1 = int("".join(map(str, m1)))
    m2 = int("".join(map(str, m2)))
    p = int("".join(map(str, p)))
    if m1 * m2 == p:
        print m1, m2, p
        return p
    return False

s = []
for digits in permutations(range(1, 10)):
    for eq in [5]:
        for times in range(1, 3):
            # print digits[:times], digits[times:eq], digits[eq:]
            result = check(digits[:times], digits[times:eq], digits[eq:])
            if result:
                s.append(result)

print s, sum(set(s))


def check2(i,j,k):
    digits = str(i)+str(j)+str(k)
    return len(digits) == 9 and 9 == len(set(digits)) and "0" not in digits

for i in range(1,99):
    for j in range(1,9888):
        if check2(i,j,i*j):
            print i, j, i*j