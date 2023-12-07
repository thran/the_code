from collections import Counter

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 6440
    part_two_test_solution = 5905
    CARDS1 = '23456789TJQKA'
    CARDS2 = 'J23456789TQKA'

    def preprocess_input(self, lines):
        return [(line[:5], int(line[6:])) for line in lines]

    def get_hand_score(self, hand, with_jokers=False) -> tuple:
        if type(hand) is tuple:
            hand = hand[0]

        card_order = self.CARDS2 if with_jokers else self.CARDS1
        counts = Counter(hand)
        if with_jokers and 'J' in counts and hand != 'JJJJJ':
            joker_count = counts.pop('J')
            values = sorted(counts.values())
            values[-1] += joker_count
        else:
            values = counts.values()

        cards = [card_order.index(card) for card in hand]

        if 5 in values:
            return 7, cards
        if 4 in values:
            return 6, cards
        if 3 in values and 2 in values:
            return 5, cards
        if 3 in values:
            return 4, cards
        if 2 in values and len(values) == 3:
            return 3, cards
        if 2 in values:
            return 2, cards
        return 1, cards

    def part_one(self, hands, with_jokers=False) -> int:
        winnings = 0
        for i, (hand, bid) in enumerate(sorted(hands, key=lambda h: self.get_hand_score(h, with_jokers)), start=1):
            winnings += bid * i
        return winnings

    def part_two(self, hands) -> int:
        return self.part_one(hands, with_jokers=True)


if __name__ == '__main__':
    Level().run()
