import re

with open("05.txt") as source:
    lines = source.readlines()
    # lines = filter(lambda x: re.match(r"(.*[aeiou].*){3}", x), lines)
    # lines = filter(lambda x: re.match(r".*(.)\1", x), lines)
    # lines = filter(lambda x: not re.match(r".*(ab|cd|pq|xy)", x), lines)
    lines = filter(lambda x: re.match(r".*(..).*\1", x), lines)
    lines = filter(lambda x: re.match(r".*(.).\1", x), lines)


print len(lines)
print lines