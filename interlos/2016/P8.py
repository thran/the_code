from primes import divisors

count = 19423091

fronta = range(1, count + 1)

c = 0
while len(fronta) > 1:
    c += 1
    to_remove = []
    l = len(fronta)
    for d in divisors(l):
        if d > 1:
            x = d
            while x <= l:
                to_remove.append(fronta[x-1])
                x += d
    to_remove = set(to_remove)
    new = []
    for f in fronta:
        if f not in to_remove:
            new.append(f)
    fronta = new
    print(c, len(fronta))
    if (len(fronta) < 100):
        print fronta

print(fronta, c)