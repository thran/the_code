def permutations(l):
    if len(l) == 1:
        yield l
    for pre in l:
        list_without = l[:]
        list_without.remove(pre)
        posts = permutations(list_without)
        for post in posts:
            yield [pre] + post


def rotations(l):
    for i in range(len(l)):
        yield l[i:]+l[0:i]


def is_permutation(a, b):
    return sorted(a) == sorted(b)
