from collections import defaultdict

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 13
    part_two_test_solution = 30

    def preprocess_input(self, lines):
        cards = []
        for line in lines:
            card, numbers = line.split(':')
            winning_numbers, have_numbers = numbers.split(' | ')
            cards.append(
                (
                    int(card.split()[-1]),
                    len(set(map(int, winning_numbers.split())) & set(map(int, have_numbers.split()))),
                )
            )
        return cards

    def part_one(self, cards) -> int:
        return sum(2 ** (hits - 1) for _, hits in cards if hits)

    def part_two(self, cards) -> int:
        wins = defaultdict(int)
        card_count = len(cards)
        for card_number, hits in cards:
            wins[card_number] += 1
            for win in range(card_number + 1, min(card_number + hits, card_count) + 1):
                wins[win] += wins[card_number]
        return sum(wins.values())


if __name__ == '__main__':
    Level().run()
