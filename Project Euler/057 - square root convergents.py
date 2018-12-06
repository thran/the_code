from fractions import Fraction

f = Fraction(1, 2)
hits = 0

for i in range(1000):
    if len(str((1 + f).denominator)) < len(str((1 + f).numerator)):
        hits += 1
        print 1 + f
    f = 1 / (2 + f)

print hits
