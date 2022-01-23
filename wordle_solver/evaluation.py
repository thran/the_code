import json
from collections import Counter
from pathlib import Path

import numpy as np
import seaborn as sns
from icecream import ic
from matplotlib import pyplot as plt
from tqdm import tqdm

from wordle import WordWordle
from wordle_solver import RandomSolver, MaxInformationSolver


def evaluate(language):
    solvers = {
        'random': lambda wordle: RandomSolver(wordle, language),
        'entropy_hard': lambda wordle: MaxInformationSolver(wordle, language),
        # 'entropy_soft': lambda wordle: MaxInformationSolver(wordle, language, hard_mode=False),
    }

    results = {}
    for name, solver in solvers.items():
        stats = Counter()
        results[name] = stats
        with (Path('dictionaries') / f'{language}.test.txt').open() as f:
            for line in tqdm(f, desc=name):
                word = line.strip()

                wordle = WordWordle(word)
                solver(wordle).solve(verbose=False)
                stats[wordle.guesses] += 1

        json.dump(stats, Path(f'evaluation/{language}.{name}.evaluation.json').open('w'))
    return results


def show(language):
    files = sorted(Path('evaluation').glob(f'{language}.*.evaluation.json'))
    plt.figure(figsize=(9, 3))
    for i, file in enumerate(files):
        name = file.name.split('.')[1]
        stats = json.load(file.open())
        stats = np.array([(int(k), v) for k, v in stats.items()])
        mean = np.average(stats[:,0], weights=stats[:,1])

        plt.subplot(1, len(files), i + 1)
        plt.title(f'{name}: {mean:.2f}')
        sns.barplot(stats[:,0], stats[:,1])
    plt.savefig(Path('evaluation') / f'{language}.png')
    plt.show()



if __name__ == '__main__':
    language = 'en'

    # ic(evaluate(language))
    show(language)
