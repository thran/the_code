import random
from queue import Queue

import seaborn as sns
from icecream import ic
from matplotlib import pyplot as plt
from tqdm import trange


class Deck:

    def __init__(self, cards):
        self.deck = Queue()
        self.desk = []

        self.put(cards)


    @property
    def is_empty(self):
        return self.deck.empty()

    def get(self):
        card = self.deck.get()
        self.desk.append(card)
        return card

    def get_war(self, count=3):
        for _ in range(count):
            if self.is_empty:
                return self.desk[-1]
            card = self.get()
        return card

    def collect(self):
        cards = self.desk
        self.desk = []
        return cards

    def put(self, cards):
        for card in cards:
            self.deck.put(card)

    def __bool__(self):
        return not self.is_empty

    def __str__(self):
        nd = Queue()
        cs = []
        while not self.deck.empty():
            c = self.deck.get()
            nd.put(c)
            cs.append(str(c))
        self.deck = nd
        return ', '.join(cs)


def simulation(dec_count=1):
    cards = list(range(1, 14)) * 4 * dec_count
    random.shuffle(cards)

    d1 = Deck(cards[:len(cards) // 2])
    d2 = Deck(cards[len(cards) // 2:])

    rounds = 0
    while d1 and d2:
        rounds += 1
        c1, c2 = d1.get(), d2.get()
        while c1 == c2:
            c1, c2 = d1.get_war(), d2.get_war()

        desk = d1.collect() + d2.collect()
        random.shuffle(desk)
        if c1 > c2:
            d1.put(desk)
        else:
            d2.put(desk)

    return rounds

if __name__ == '__main__':
    runs = []
    for _ in trange(10000):
        runs.append(simulation(1))

    sns.distplot(runs)
    plt.show()
    ic(max(runs))
    ic(min(runs))
    ic(sum(runs) / len(runs))
