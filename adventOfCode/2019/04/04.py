from tqdm import tqdm


def is_good(number):
    last_digit = None
    adjacent = False
    adjacent_count = 1
    adjacent_counts = []

    for digit in str(number):
        if last_digit is not None and digit < last_digit:
            return False
        if last_digit == digit:
            adjacent = True
            adjacent_count += 1
        else:
            if last_digit is not None:
                adjacent_counts.append(adjacent_count)
                adjacent_count = 1
        last_digit = digit
    adjacent_counts.append(adjacent_count)
    return adjacent and 2 in adjacent_counts

goods = 0
for n in tqdm(range(231832, 767346 + 1)):
    if is_good(n):
        goods += 1
print(goods)
