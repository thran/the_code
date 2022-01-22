import abc
from enum import Enum


STATE_REPR = {0: '|', 1: 'o', 2: 'x'}

class LetterState(Enum):

    HIT = 0
    BAD_POSITION = 1
    MISS = 2

    def __str__(self):
        return STATE_REPR[self.value]


def hash_comparison(comparison: tuple[LetterState]):
    return ''.join(map(str, comparison))


def compere_words(guess: str, target: str) -> tuple[LetterState]:
    result = []
    unused_target = list(target)
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            unused_target[i] = None

    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            result.append(LetterState.HIT)
            continue
        if g in unused_target:
            unused_target[unused_target.index(g)] = None
            result.append(LetterState.BAD_POSITION)
        else:
            result.append(LetterState.MISS)
    return tuple(result)


class Wordle:

    def __init__(self):
        self.guesses = 0

    def guesses_word(self, word) -> tuple[bool, tuple[LetterState]]:
        self.guesses += 1
        comparison = self.get_comparison(word)
        if all(position == LetterState.HIT for position in comparison):
            return True, comparison
        return False, comparison

    @abc.abstractmethod
    def get_comparison(self, word: str) -> tuple[LetterState]:
        pass


class WordWordle(Wordle):

    def __init__(self, target):
        super().__init__()
        self.target = target

    def get_comparison(self, word):
        return compere_words(word, self.target)


class ManualWordle(Wordle):

    def get_comparison(self, word: str):
        print(f'insert {word.upper()}')
        result = input('green: 0; yellow: 1; gray: 2: ')
        assert len(result) == len(word)
        return tuple(LetterState(int(r)) for r in result)
