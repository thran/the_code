from intcode import IntCode
from itertools import combinations


class Robot:
    def __init__(self):
        memory = list(map(int, open('input.txt').readlines()[0].split(',')))

        self.bot = IntCode(memory.copy())
        outputs = self.bot.run(inputs=[], halt_on_missing_input=True)
        self.show(outputs)

    def show(self, outputs):
        print(''.join(map(chr, outputs)))

    def run(self, command):
        outputs = self.bot.run(inputs=map(ord, command + '\n'), halt_on_missing_input=True)
        self.show(outputs)

    def solve(self, items):
        for count in range(1, len(items)):
            for its in combinations(items, count):
                for it in its:
                    self.run(f'take {it}')
                self.run('west')
                outputs = self.bot.run(inputs=map(ord, 'west\n'), halt_on_missing_input=True)
                outputs = ''.join(map(chr, outputs))
                if 'Alert' not in outputs:
                    self.run('inv')
                    return
                for it in its:
                    self.run(f'drop {it}')


bot = Robot()
# bot.run('take giant electromagnet')
# bot.run('north')
# bot.run('east')
# bot.run('west')
bot.run('south')
bot.run('take space law space brochure')
bot.run('south')
bot.run('take mouse')
bot.run('west')
bot.run('north')
bot.run('north')
bot.run('take wreath')
bot.run('south')
bot.run('west')
# bot.run('take infinite loop') Navigation
bot.run('east')
bot.run('south')
bot.run('east')
bot.run('south')
bot.run('take astrolabe')
bot.run('south')
bot.run('take mug')
bot.run('north')
bot.run('north')
bot.run('north')
# sick bay
bot.run('west')
bot.run('take sand')
bot.run('north')
bot.run('take manifold')
bot.run('south')
bot.run('west')
bot.run('take monolith')
bot.run('west')
bot.run('inv')
bot.run('drop monolith')
bot.run('drop wreath')
bot.run('drop mug')
bot.run('drop astrolabe')
bot.run('drop manifold')
bot.run('drop sand')
bot.run('drop mouse')
bot.run('drop space law space brochure')
bot.solve(['monolith', 'wreath', 'mug', 'astrolabe', 'manifold', 'sand', 'mouse', 'space law space brochure'])
# bot.run('west')

