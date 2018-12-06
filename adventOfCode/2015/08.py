import re
from collections import defaultdict

import numpy as np

s = 0

with open("08.txt") as source:
    for line in source.readlines():
        line = line.replace("\n", "")
        # s += len(line) - len(eval(re.sub(r'\\x\d\d', 'x', line)))
        s += 2 + len(line.replace('"', r'%%').replace('\\', r'%%')) - len(line)
print s
