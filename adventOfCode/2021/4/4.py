# start: 9:38
# 1.:    9:57
# 2.:   10:00
import numpy as np

from core import AdventOfCode

MARKED_NUMBER = -1


class Level(AdventOfCode):
    part_one_test_solution = 4512
    part_two_test_solution = 1924

    def preprocess_input(self, lines):
        numbers = map(int, lines[0].strip().split(','))
        boards = []
        rows = []
        for line in lines[1:]:
            if not line.strip():
                continue
            rows.append(list(map(int, line.split())))
            if len(rows) == len(line.split()):
                boards.append(np.array(rows))
                rows = []
        return numbers, boards

    def check_win(self, board):
        for i in range(len(board)):
            if all(board[i] == MARKED_NUMBER) or all(board[:, i] == MARKED_NUMBER):
                return True
        return False

    def compute_score(self, board):
        b = np.array(board)
        b[b == MARKED_NUMBER] = 0
        return b.sum()

    def part_one(self, input_) -> int:
        numbers, boards = input_
        for number in numbers:
            for board in boards:
                board[board == number] = -1
            for board in boards:
                if self.check_win(board):
                    return number * self.compute_score(board)

    def part_two(self, input_) -> int:
        numbers, boards = input_
        for number in numbers:
            for board in boards:
                board[board == number] = -1
            for i, board in enumerate(boards):
                if self.check_win(board):
                    if len(boards) == 1:
                        return number * self.compute_score(board)
                    del boards[i]


Level().run()
