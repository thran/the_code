import json
import re

if False:
    s = 0
    with open("12.json") as source:
        for line in source.readlines():
            r = re.search(r'-?\d+', line)
            if r:
                print int(r.group(0))
                s += int(r.group(0))


s = 0


def traverse(a):
    if type(a) == dict:
        if "red" in a.values():
            return
        for value in a.values():
            traverse(value)
        return
    if type(a) == list:
        for value in a:
            traverse(value)
        return
    if type(a) == int:
        global s
        s += a
        return

d = json.load(open("12.json"))

traverse(d)
print s