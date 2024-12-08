from collections import defaultdict

from adventOfCode.utils import BFS, SearchAll, PrioritySearch

prices = {}
stations = defaultdict(list)
with open('input.txt') as f:
    # with open('input.test.txt') as f:
    fp = True
    for i, line in enumerate(f):
        line = line.strip()
        if line == '':
            fp = False
            continue
        if fp:
            prices[i] = tuple(map(int, line.split()))
        else:
            f, t, time = tuple(map(int, line.split()))
            stations[f].append((t, time))


start, goal = 64, 60
# start, goal = 3, 0


# print(stations)

# for i, ps in prices.items():
#     print(i, ps)
# exit()


# state = station, ppm, fm, spent
class Search(PrioritySearch):
    def __init__(self):
        super().__init__([(0, 1000000, 1000000, start)])
        self.goal = goal
        self.best = None

    def next_states(self, state):
        spent, ppm, fm, station = state
        if ppm != 1000000:
            for st, length in stations[station]:
                for_free = min(length, fm)
                yield spent + (length - for_free) * ppm, ppm, fm - for_free, st

        borrow, fm, ppm = prices[station]
        for st, length in stations[station]:
            for_free = min(length, fm)
            yield spent + borrow + (length - for_free) * ppm, ppm, fm - for_free, st

    def end_condition(self, state) -> bool:
        return state[-1] == self.goal

    def on_found(self, state):
        price = state[0]
        if self.best is None or price < self.best:
            print(price, state)
            self.best = price


Search()()
