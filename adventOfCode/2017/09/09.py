import re

x = open('input.txt').readline().strip()

x = re.sub('!.', '', x)
l1 = len(x)
x = re.sub('\<.*?\>', '69', x)
l2 = len(x)
x = x.replace('{', '[').replace('}', ']')
x = eval(x)


def groups(y):
    if y is None or y == 69:
        return 0
    return 1 + sum(groups(i) for i in y)


def score(y, s=1):
    if y is None or y == 69:
        return 0
    return s + sum(score(i, s + 1) for i in y)


# print(groups(x))
print(score(x))
print(l1 - l2)