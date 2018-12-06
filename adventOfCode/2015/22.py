def fight(mana, spells, hp=50):
    boss_hp = 51
    boss_damage = 9

    effects = {
        "A": 0,
        "P": 0,
        "R": 0,
    }

    def decay():
        for k, v in effects.items():
            effects[k] = max(v - 1, 0)

    spend = 0

    for spell in spells:
        hp -= 1
        if hp <= 0:
           return False

        # players turn
        if effects["P"]: boss_hp -= 3
        if effects["R"]: mana += 101
        decay()

        if spell == "M":
            mana -= 53
            spend += 53
            boss_hp -= 4
        if spell == "D":
            mana -= 73
            spend += 73
            boss_hp -= 2
            hp += 2
        if spell == "S":
            mana -= 113
            spend += 113
            if effects["A"]:
                return False
            effects["A"] = 6
        if spell == "P":
            mana -= 173
            spend += 173
            if effects["P"]:
                return False
            effects["P"] = 6
        if spell == "R":
            mana -= 229
            spend += 229
            if effects["R"]:
                return False
            effects["R"] = 5
        if mana < 0:
            return False

        if boss_hp <= 0:
            return spend

        # boss turn
        if effects["P"]: boss_hp -= 3
        if boss_hp <= 0:
            return spend
        if effects["R"]: mana += 101
        armor = 7 if effects["A"] else 0
        decay()
        hp -= max(1, boss_damage - armor)
        if hp <= 0:
            return False

    print "Not finished"



def spells(n, ss="RSDPM"):
    if n == 1:
        for s in ss:
            yield s
        return
    for suf in spells(n - 1, ss):
        for s in ss:
            yield s + suf


spends = []
for spell in spells(8):
    result = fight(500, spell)
    if result:
        spends.append(result)

print len(spends), min(spends)