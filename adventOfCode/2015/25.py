def get_number(row, column):
    return sum(range(column + row)) - row + 1


def code(row, column):
    n = get_number(row, column)
    r = 20151125
    for _ in range(n - 1):
        r = (r * 252533) % 33554393

    return r

print code(2947, 3029)
