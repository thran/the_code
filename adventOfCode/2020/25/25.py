# start 9:36, 1. 10:02
from pathlib import Path


with Path('input.txt').open() as file:
    pub1, pub2 = [int(line.strip()) for line in file]

p = 20201227
sn1 = 7


ls1 = 0
v1 = 1
v2 = 1
while True:
    v1 = (v1 * sn1) % p
    v2 = (v2 * pub2) % p
    if v1 == pub1:
        break

print(v2)
