def fight(damage, armor, hp=100):
    boss_hp = 104
    boss_damage = 8
    boss_armor = 1

    while True:
        boss_hp -= max(1, damage - boss_armor)
        if boss_hp <= 0:
            return True
        hp -= max(1, boss_damage - armor)
        if hp <= 0:
            return False
weapons = [
    (8, 4),
    (10, 5),
    (25, 6),
    (40, 7),
    (74, 8)
]

armors= [
    (0, 0),
    (13, 1),
    (31, 2),
    (53, 3),
    (75, 4),
    (102, 5)
]

rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]

c = 0
for r1 in rings:
    for r2 in rings:
        if r1 == r2 and r1[0] != 0:
            continue
        print r1, r2
        c += 1
print c

costs = []
for w in weapons:
    for a in armors:
        for r1 in rings:
            for r2 in rings:
                if r1 == r2 and r1[0] != 0:
                    continue
                if not fight(w[1] + r1[1] + r2[1], a[1] + r1[2] + r2[2]):
                    costs.append(w[0] + r1[0] + r2[0] + a[0])

print len(costs), max(costs)