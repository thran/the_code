from tqdm import tqdm

n1 = 512
n2 = 191
f1 = 16807
f2 = 48271
m = 2147483647

c = 0
for _ in tqdm(range(5 * 10 ** 6)):
    n1 = (n1 * f1) % m
    n2 = (n2 * f2) % m
    while n1 % 4 != 0:
        n1 = (n1 * f1) % m
    while n2 % 8 != 0:
        n2 = (n2 * f2) % m

    if bin(n1)[-16:] == bin(n2)[-16:]:
        c += 1

print(c)
