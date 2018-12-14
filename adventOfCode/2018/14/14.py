from itertools import count

from tqdm import tqdm

recps = [3, 7]
n = list(map(int, "165061"))
first = 0
second = 1


def is_subsequence(b, a):
    for i in range(len(a)):
        for j in range(len(b)):
            if i + j >= len(a) or a[i + j] != b[j]:
                break
        else:
            return True
    return False


for i in tqdm(count()):
    new = recps[first] + recps[second]
    if new < 10:
        recps.append(new)
    else:
        recps.append(new // 10)
        recps.append(new % 10)

    first = (recps[first] + first + 1) % len(recps)
    second = (recps[second] + second + 1) % len(recps)

    if i % 1000000 == 0 and is_subsequence(n, recps):
        print(''.join(map(str, recps)).index(''.join(map(str, n))))
        # print(recps, i)
        break
