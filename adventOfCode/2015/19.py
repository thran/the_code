import re
from collections import defaultdict


def replace_by_1(s, sub, replacement):
    parts = s.split(sub)
    for i in range(1, len(parts)):
        yield sub.join(parts[:i]) + replacement + sub.join(parts[i:])
        return


def step(mols):
    results = []
    for mol in mols:
        for atom in rules.keys():
            for replacement in rules[atom]:
                for result in replace_by_1(mol, atom, replacement):
                    results.append(result)
    return set(results)


mol = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

rules = defaultdict(lambda: [])

with open("19.txt") as f:
    for line in f.readlines():
        gs = re.match(r'(\w+) => (\w+)', line).groups()
        rules[gs[1]].append(gs[0])


mols = [mol]
s = 0
while True:
    s += 1
    mols = step(mols)
    mols = [sorted(mols, key=len)[0]]
    print len(mols), min(map(len, mols))
    if "e" in mols:
        print s
        break