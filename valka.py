import random


def battle(decks):
    won = [[] for _ in decks]
    while min(map(len, decks)) > 0:
        c1 = decks[0].pop(0)
        c2 = decks[1].pop(0)
        if c1 > c2:
            won[0].extend([c1, c2])
        elif c1 < c2:
            won[1].extend([c1, c2])
        else:
            while True:
                if len(decks[0]) == 0 or len(decks[1]) == 0:
                    won[0].append(c1)
                    won[1].append(c2)
                    return len(won[0]) > len(won[1]), len(won[0]) == len(won[1])
                tmp = [c1, c2]
                for _ in range(2):
                    if len(decks[0]) == 1 or len(decks[1]) == 1:
                        continue
                    tmp.append(decks[0].pop(0))
                    tmp.append(decks[1].pop(0))
                c1 = decks[0].pop(0)
                c2 = decks[1].pop(0)
                tmp.extend([c1, c2])
                if c1 > c2:
                    won[0].extend(tmp)
                    break
                elif c1 < c2:
                    won[1].extend(tmp)
                    break
    return len(won[0]) > len(won[1]), len(won[0]) == len(won[1])


def random_deck(size=4):
    deck = range(1, 15) * size
    random.shuffle(deck)
    return deck


def descent(size=4):
    deck = range(1, 15) * size
    deck.sort(reverse=True)
    return deck


def ascent(size=4):
    deck = range(1, 15) * size
    deck.sort()
    return deck


first_wons = 0.
draws = 0.
rounds = 100000
for _ in range(rounds):
    decks = [
        random_deck(),
        descent(),
    ]
    first, draw = battle(decks)
    if first:
        first_wons += 1
    if draw:
        draws += 1

print first_wons / rounds, " vs. ", (rounds - first_wons - draws) / rounds, "draws:", draws / rounds
