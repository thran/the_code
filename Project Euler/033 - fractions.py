def remove_digit(n, r):
    return float("".join([d for d in str(n) if d!= str(r)]))

for i in range(10, 99):
    for j in range(i+1, 100):
        for r in str(i):
            try:
                if r != "0" and float(i) / j == remove_digit(i, r) / remove_digit(j, r):
                    print i, j, r, remove_digit(i, r), remove_digit(j, r)
            except:
                pass
