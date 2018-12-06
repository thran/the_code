from permutations import permutations


digits = list("987654321")

for p in permutations(digits):
    for i in range(1, 5):
        n = int("".join(p[:i]))
        x = 1
        y = ""
        while len(y) < 9:
            y += str(n * x)
            x += 1
        if y == "".join(p):
            print y, n, x-1
            exit()