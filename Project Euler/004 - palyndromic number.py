def is_palyndromic(n):
    return str(n) == str(n)[::-1]


for sum in range(999*2, 999, -1):
    for x in range(999, sum-999 - 1 , -1):
        y = sum - x
        if is_palyndromic(x * y):
            print x * y
            exit()