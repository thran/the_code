def iterate_mask(mask):
    this = None
    for i, m in enumerate(mask):
        if m == 1:
            last = this
            this = i
            if last is not None:
                yield last, this


def reduce(polymer):
    mask = [1] * len(polymer)
    no_change = False
    while not no_change:
        print(sum(mask))
        for i, j in iterate_mask(mask):
            if polymer[i].swapcase() == polymer[j]:
                mask[i] = mask[j] = 0
                break
        else:
            no_change = True
    return sum(mask)


with open('input.txt') as f:
    polymer = f.read().strip()

print(reduce(polymer))

exit()

letters = sorted(set(polymer.lower()))
results = {}
for letter in letters:
    print(letter)
    r = reduce(''.join([l for l in polymer if l.lower() != letter]))
    print(r)
    results[letter] = r

for letter, length in sorted(results.items(), key=lambda x: x[1]):
    print(letter, length)
