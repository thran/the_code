from itertools import cycle


class Marble:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Game:
    def __init__(self, players=493, max_marble=71863):
        self.players = [0] * players
        self.max_marble = max_marble

        self.current = None
        self.start = None

    def play(self):
        for player, value in zip(cycle(range(len(self.players))), range(self.max_marble + 1)):
            marble = Marble(value)
            if self.current is None:
                self.start = marble
                marble.prev = marble
                marble.next = marble
            else:
                if value % 23 == 0:
                    self.players[player] += value
                    to_remove = self.current
                    for _ in range(7):
                        to_remove = to_remove.prev
                    self.players[player] += to_remove.value
                    left = to_remove.prev
                    right = to_remove.next
                    left.next = right
                    right.prev = left
                    marble = right
                else:
                    left = self.current.next
                    right = left.next
                    left.next = marble
                    marble.prev = left
                    right.prev = marble
                    marble.next = right
            self.current = marble

    def __str__(self):
        s = ''
        m = self.start
        while True:
            s += f' {m.value} '
            m = m.next
            if s and m == self.start:
                break
        return s + f' | current: {self.current.value}'


game = Game()
game.play()
# print(game)
print(max(game.players))
