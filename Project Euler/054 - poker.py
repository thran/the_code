from collections import Counter


def get_value(hand):
    hand = [(int(c[:-1].replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "20")), c[-1]) for c in hand]
    hand.sort(key=lambda c: c[:-1])

    suits = [c for _, c in hand]
    values = [c for c, _ in hand]
    counts = Counter(values)

    # 10 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    # 9  Straight Flush: All cards are consecutive values of same suit.
    if len(set(suits)) == 1 and len(set(map(lambda (i, v): v - i, enumerate(values)))) == 1:
        return 10, values[-1], 0, 0, 0, 0

    # 8  Four of a Kind: Four cards of the same value.
    if 4 in counts.values():
        return 8, counts.most_common()[0][0], 0, 0, 0, 0

    # 7  Full House: Three of a kind and a pair.
    if counts.values() == [2, 3] or counts.values() == [3, 2]:
        return 7, counts.most_common()[0][0], 0, 0, 0, 0

    # 6  Flush: All cards of the same suit.
    if len(set(suits)) == 1:
        values.reverse()
        return (6, ) + tuple(values)

    # 5  Straight: All cards are consecutive values.
    if len(set(map(lambda (i, v): v - i, enumerate(values)))) == 1:
        return 5, values[-1], 0, 0, 0, 0

    # 4  Three of a Kind: Three cards of the same value.
    if 3 in counts.values():
        return 4, counts.most_common()[0][0], 0, 0, 0, 0

    # 3  Two Pairs: Two different pairs.
    c = counts.values()
    c.sort()
    if c[1] == 2 and c[2] == 2:
        return 3, values[3], values[1], counts.most_common()[2][0], 0, 0

    # 2  One Pair: Two cards of the same value.
    if 2 in counts.values():
        values.remove(counts.most_common()[0][0])
        values.remove(counts.most_common()[0][0])
        values.reverse()
        return (2, counts.most_common()[0][0]) + tuple(values) + (0, )

    # 1  High Card: Highest value card.
    values.reverse()
    return (1, ) + tuple(values)


def first_wins(h1, h2):
    return get_value(h1.split()) > get_value(h2.split())


hits = 0
with open("054 - poker.txt") as f:
    for line in f.readlines():
        if first_wins(line[:14], line[15:]):
            hits += 1

print hits














