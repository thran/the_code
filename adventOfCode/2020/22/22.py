# start 8:19, 1. 8:28, 2. 8:50
from collections import deque
from pathlib import Path


def load_decks():
    deck1 = deque()
    deck2 = deque()
    with Path('input.txt').open() as file:
        for deck in (deck1, deck2):
            file.readline()
            while line := file.readline().strip():
              deck.append(int(line))
    return deck1, deck2


deck1, deck2 = load_decks()
while deck1 and deck2:
    card1 = deck1.popleft()
    card2 = deck2.popleft()
    win_deck = deck1 if card1 > card2 else deck2
    for card in sorted((card1, card2), reverse=True):
        win_deck.append(card)

print(sum((len(win_deck) - i) * card for i, card in enumerate(win_deck)))


def hash(deck1, deck2):
    return ','.join(map(str, deck1)) + '#' + ','.join(map(str, deck2))


def play(deck1, deck2):
    played_situations = set()
    while deck1 and deck2:
        h = hash(deck1, deck2)
        if h in played_situations:
            return 1
        played_situations.add(h)

        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 > len(deck1) or card2 > len(deck2):
            if card1 > card2:
                win_deck, win_card, loose_card = deck1, card1, card2
            else:
                win_deck, win_card, loose_card = deck2, card2, card1
        else:
            if play(deque(list(deck1)[:card1]), deque(list(deck2)[:card2])) == 1:
                win_deck, win_card, loose_card = deck1, card1, card2
            else:
                win_deck, win_card, loose_card = deck2, card2, card1

        win_deck.append(win_card)
        win_deck.append(loose_card)

    return 1 if deck1 else 2


deck1, deck2 = load_decks()
win_deck = deck1 if play(deck1, deck2) == 1 else deck2
print(sum((len(win_deck) - i) * card for i, card in enumerate(win_deck)))
