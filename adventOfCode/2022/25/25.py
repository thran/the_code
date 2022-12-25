from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = '2=-1=0'

    DIGITS = '=-012'

    def part_one(self, lines) -> str:
        def from_snafu(snafu):
            number = 0
            for e, d in enumerate(snafu[::-1]):
                number += 5**e * (self.DIGITS.index(d) - 2)
            return number

        def to_snafu(number):
            snafu = []
            while number:
                digit = (number % 5 + 2) % 5 - 2
                number = (number - digit) // 5
                snafu.append(digit)

            return ''.join(self.DIGITS[i + 2] for i in snafu[::-1])

        return to_snafu(sum(from_snafu(l) for l in lines))


if __name__ == '__main__':
    Level().run()
