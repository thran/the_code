i = 0
j = 1
this = 0

sum = 0

while this < 4 * 10 ** 6:
    this = i + j

    if this % 2 == 0:
        sum += this

    i = j
    j = this

print sum
