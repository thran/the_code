import re

obs = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def comp(o, v):
    if o == "cats" or o == "trees":
        return obs[o] <= v
    if o == "pomeranians" or o == "goldfish":
        return obs[o] >= v
    return obs[o] == v

with open("16.txt") as source:
    for line in source.readlines():
        r = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line).groups()
        if comp(r[1], int(r[2])) and comp(r[3], int(r[4])) and comp(r[5], int(r[6])):
            print r[0]