from collections import defaultdict

map = {
    'A':  ['GCT', 'GCC', 'GCA', 'GCG'],
    'L':  ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'R':  ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'K':  ['AAA', 'AAG'],
    'N':  ['AAT', 'AAC'],
    'M':  ['ATG'],
    'D':  ['GAT', 'GAC'],
    'F':  ['TTT', 'TTC'],
    'C':  ['TGT', 'TGC'],
    'P':  ['CCT', 'CCC', 'CCA', 'CCG'],
    'Q':  ['CAA', 'CAG'],
    'S':  ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'E':  ['GAA', 'GAG'],
    'T':  ['ACT', 'ACC', 'ACA', 'ACG'],
    'G':  ['GGT', 'GGC', 'GGA', 'GGG'],
    'W':  ['TGG'],
    'H':  ['CAT', 'CAC'],
    'Y':  ['TAT', 'TAC'],
    'I':  ['ATT', 'ATC', 'ATA'],
    'V':  ['GTT', 'GTC', 'GTA', 'GTG'],
    '$': ['TRA', 'TAG'],
}

seq = 'ATGAATGCTCCGATCAGCTTTATTAACGCCTTGAATATACGTGAATCTGAGAACATTGCCCTGTGTCATTATATGATATCCACGGCGTAA'

reverse_map = defaultdict(lambda: '?')

for k, vs in map.items():
    for v in vs:
        reverse_map[v] = k

shift = 0

s = seq[shift:] + seq[:shift]
result = ''
for i in range(len(s) // 3):
    sub = s[i*3:i*3+3]
    result += reverse_map[sub]

print(result)
