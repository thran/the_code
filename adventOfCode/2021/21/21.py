from collections import defaultdict
from itertools import product

from core import AdventOfCode
from utils import memoize


move_distribution = defaultdict(int)
for rolls in product(*[(1, 2, 3)]*3):
    move_distribution[sum(rolls)] += 1


@memoize
def count_player1_wins(position1, score1, position2, score2, player1_moves):
    if score1 >= 21:
        return 1
    if score2 >= 21:
        return 0

    counts = 0
    for value, weight in move_distribution.items():
        if player1_moves:
            position = (position1 + value) % 10
            score = score1 + position + 1
            counts += weight * count_player1_wins(position, score, position2, score2, False)
        else:
            position = (position2 + value) % 10
            score = score2 + position + 1
            counts += weight * count_player1_wins(position1, score1, position, score, True)
    return counts


class Level(AdventOfCode):
    part_one_test_solution = 739785
    part_two_test_solution = 444356092776315

    def preprocess_input(self, lines):
        return int(lines[0][-1]) - 1, int(lines[1][-1]) - 1

    def roll_dice(self, dice, n=3):
        move = 0
        for _ in range(n):
            dice['rolled'] += 1
            dice['value'] = dice['value'] % 100 + 1
            move += dice['value']
        return move

    def part_one(self, position1, position2) -> int:
        player1 = {'position': position1, 'score': 0}
        player2 = {'position': position2, 'score': 0}
        dice = {'value': 0, 'rolled': 0}
        player, other_player = player1, player2
        while True:
            player['position'] = (player['position'] + self.roll_dice(dice)) % 10
            player['score'] += player['position'] + 1
            if player['score'] >= 1000:
                break
            player, other_player = other_player, player
        return other_player['score'] * dice['rolled']

    def part_two(self, position1, position2) -> int:
        return count_player1_wins(position1, 0, position2, 0, True)


Level().run()
