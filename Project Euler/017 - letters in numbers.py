to9 = len("onetwothreefourfivesixseveneightnine")
to19 = to9 + len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")

tens = len("twentythirtyfortyfiftysixtyseventyeightyninety")

to99 = to19 + tens*10 + to9*8
to999 = 100*to9 + 900*10 -9*3 + to99 * 10


print to999 + 11