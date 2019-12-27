lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(line.strip().split())

c = 0
for passphrase in lines:
    if len(passphrase) == len(set(passphrase)):
        c += 1

print(c)


c = 0
for passphrase in lines:
    passphrase = [''.join(sorted(p)) for p in passphrase]
    if len(passphrase) == len(set(passphrase)):
        c += 1

print(c)
