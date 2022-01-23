import abc
import json
import random
from collections import Counter, defaultdict
from operator import itemgetter
from pathlib import Path

from typing import Optional

from icecream import ic
from scipy.stats import entropy
from tqdm import tqdm

from wordle import LetterState, WordWordle, compere_words, Wordle, hash_comparison, ManualWordle


class GuessKnowledge:

    def __init__(self, word: str = None, comparison: tuple[LetterState] = None):
        self.unplaced_letters = Counter()
        self.excluded_letters = set()
        self.positions = None

        if word is None:
            return

        self.positions = [{} for _ in word]

        for i, (letter, letter_state) in enumerate(zip(word, comparison)):
            if letter_state == LetterState.HIT:
                self.positions[i]['known'] = letter

        for i, (letter, letter_state) in enumerate(zip(word, comparison)):
            if letter_state == LetterState.BAD_POSITION:
                self.unplaced_letters[letter] += 1
                self.positions[i]['excluded'] = {letter}

        for i, (letter, letter_state) in enumerate(zip(word, comparison)):
            if letter_state == LetterState.MISS:
                if letter in self.unplaced_letters:
                    self.positions[i]['excluded'] = {letter}
                    continue
                self.excluded_letters.add(letter)

    def is_matching(self, word) -> bool:
        unused_letters = list(word)
        for i, (position, letter) in enumerate(zip(self.positions, word)):
            if 'known' in position:
                if position['known'] != letter:
                    return False
                unused_letters[i] = None
            if 'excluded' in position:
                if letter in position['excluded']:
                    return False

        if any(excluded_letter in unused_letters for excluded_letter in self.excluded_letters):
            return False

        for unplaced_letter, count in self.unplaced_letters.items():
            if unused_letters.count(unplaced_letter) < count:
                return False

        return True

    def __add__(self, other: 'GuessKnowledge') -> 'GuessKnowledge':
        new = GuessKnowledge()
        new.positions = [{} for _ in self.positions]
        self_extra_known = Counter()
        other_extra_known = Counter()

        new.excluded_letters = self.excluded_letters | other.excluded_letters

        for i, (s, o) in enumerate(zip(self.positions, other.positions)):
            if 'known' in s and 'known' in o:
                assert s['known'] == o['known']
                new.positions[i]['known'] = s['known']
                continue
            if 'known' in s:
                assert s['known'] not in other.excluded_letters
                assert s['known'] not in o.get('excluded', [])
                new.positions[i]['known'] = s['known']
                self_extra_known[s['known']] += 1
                continue
            if 'known' in o:
                assert o['known'] not in self.excluded_letters
                assert o['known'] not in s.get('excluded', [])
                new.positions[i]['known'] = o['known']
                other_extra_known[o['known']] += 1
                continue

            if 'excluded' in s or 'excluded' in o:
                excluded = (s.get('excluded', set()) | o.get('excluded', set())) - new.excluded_letters
                if excluded:
                    new.positions[i]['excluded'] = excluded

        self_unplaced_letters = self.unplaced_letters - other_extra_known
        other_unplaced_letters = other.unplaced_letters - self_extra_known
        for unplaced_letter in set(self_unplaced_letters) | set(other_unplaced_letters):
            new.unplaced_letters[unplaced_letter] = max(
                self_unplaced_letters.get(unplaced_letter, 0),
                other_unplaced_letters.get(unplaced_letter, 0),
            )
        return new

    def __repr__(self):
        return str(self)

    def __str__(self):
        positions = []
        for position in self.positions:
            if 'known' in position:
                positions.append(position['known'].upper())
                continue
            if 'excluded' in position:
                positions.append('-' + ''.join(position['excluded']))
                continue
            positions.append('_')

        return f'  {",".join(positions)}\n' \
               f'  unplaced: {dict(self.unplaced_letters)}\n' \
               f'  excluded: {self.excluded_letters}'


class WordleSolver(abc.ABC):
    DICTIONARIES_PATH = Path('dictionaries')

    def __init__(self, wordle: Wordle, language):
        self.wordle = wordle
        self.language = language
        self.dictionary, self.guess_dictionary = self.load_dictionary(language)

        self.knowledge: Optional[GuessKnowledge] = None
        self._prepare()

    def load_dictionary(self, language):
        solutions = []
        with (self.DICTIONARIES_PATH / f'{language}.solutions.txt').open() as file:
            for line in file:
                solutions.append(line.strip())

        guesses = []
        guesses_path = (self.DICTIONARIES_PATH / f'{language}.guesses.txt')
        if not guesses_path.exists():
            return solutions, solutions

        with guesses_path.open() as file:
            for line in file:
                guesses.append(line.strip())
        return solutions, solutions + guesses

    def _prepare(self):
        pass

    def solve(self, verbose=True):
        while True:
            guess = self._get_guess()
            if verbose:
                print(f'Guessing {guess.upper()}')
            solved, comparison = self.wordle.guesses_word(guess)
            if verbose:
                print('Result  ', hash_comparison(comparison))
            if solved:
                if verbose:
                    print(f'\nSolved in {wordle.guesses} guesses')
                return
            new_knowledge = GuessKnowledge(guess, comparison)
            if self.knowledge:
                self.knowledge += new_knowledge
            else:
                self.knowledge = new_knowledge
            if verbose and self.knowledge:
                print('Current knowledge:')
                print(self.knowledge)
            self._after_guess()

            if verbose:
                print()

    @abc.abstractmethod
    def _get_guess(self) -> str:
        pass

    def _after_guess(self):
        pass


class ManualSolver(WordleSolver):

    def _get_guess(self):
        return input('your guess: ').lower()


class PruningSolver(WordleSolver, abc.ABC):

    def _after_guess(self):
        self.dictionary = [
            word
            for word in self.dictionary
            if self.knowledge.is_matching(word)
        ]
        print(f'Dictionary pruned to {len(self.dictionary)} words')
        if len(self.dictionary) <= 5:
            print('    ', ', '.join(self.dictionary))


class RandomSolver(PruningSolver):

    def _get_guess(self) -> str:
        guess = random.choice(self.dictionary)
        return guess


class MaxInformationSolver(PruningSolver):

    CHOICE_COUNT = 5

    def __init__(self, wordle: Wordle, language, hard_mode=True, interactive=False):
        self.hard_mode = hard_mode
        self.interactive = interactive
        super().__init__(wordle, language)

    def _prepare(self):
        cache_path = self.DICTIONARIES_PATH / f'{self.language}.info_matrix.json'
        if cache_path.exists():
            self.info_matrix = json.load(cache_path.open())
            return

        self.info_matrix = defaultdict(dict)
        for guess in tqdm(self.guess_dictionary, desc='Preparing'):
            for word in self.dictionary:
                self.info_matrix[guess][word] = hash_comparison(compere_words(guess, word))

        json.dump(self.info_matrix, cache_path.open('w'))

    def _get_guess(self) -> str:

        option_entropy = {}
        options = self.dictionary if self.hard_mode else self.info_matrix.keys()
        for option in options:
            counts = Counter()
            comparisons = self.info_matrix[option]
            for target in self.dictionary:
                counts[comparisons[target]] += 1
            boost = 1 / len(self.dictionary) if option in self.dictionary else 0
            # boost is hack for preferring to pick a word with chance to be solution
            option_entropy[option] = entropy(list(counts.values())) + boost

        if self.interactive:
            choices = sorted(option_entropy.items(), key=itemgetter(1), reverse=True)[:self.CHOICE_COUNT]
            print('Select guess:')
            for i, (choice, e) in enumerate(choices):
                print(f'{i + 1:>2}: {choice.upper()} ({e:.3f})')
            answer = input('insert number: ')
            if answer.isnumeric():
                return choices[int(answer) - 1][0]
            else:
                return answer

        best_option, _ = max(option_entropy.items(), key=itemgetter(1))
        return best_option


if __name__ == '__main__':
    # wordle = WordWordle('wince')
    wordle = ManualWordle()

    language = 'en'
    # solver = ManualSolver(wordle, language)
    # solver = RandomSolver(wordle, language)
    solver = MaxInformationSolver(wordle, language, hard_mode=False, interactive=True)
    solver.solve()


