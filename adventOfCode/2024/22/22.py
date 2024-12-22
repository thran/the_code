import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 37990510
    part_two_test_solution = 23

    def preprocess_input(self, lines):
        return np.array(super().preprocess_input(lines), dtype=np.uint32)

    def hash(self, secret):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        return secret

    def hash_n(self, secret, n):
        for _ in range(n):
            secret = self.hash(secret)
        return secret

    def part_one(self, secrets, n=2000) -> int:
        return sum(self.hash_n(secrets, n))

    def part_two(self, secrets, n=2000) -> int:
        def seq_hash(seq):
            return (seq * [1, 19, 19**2, 19**3]).sum(axis=1)

        diffs = np.zeros((n, len(secrets)), dtype=np.int8)

        sequence_prices = np.zeros(19**4, dtype=int)  # seq -> int
        used_sequences = np.zeros((19**4, len(secrets)), dtype=bool)  # seq x monkey_id-> bool
        monkey_indexes = np.arange(len(secrets))

        def update_prices(prices, step):
            if step < 3:
                return
            diff_hashes = seq_hash(diffs[step - 3 : step + 1].T)
            np.add.at(sequence_prices, diff_hashes, prices * ~used_sequences[diff_hashes, np.arange(len(secrets))])
            used_sequences[diff_hashes, monkey_indexes] = True

        last_price = secrets % 10
        for i in range(n):
            secrets = self.hash(secrets)
            price = secrets % 10
            diffs[i] = price - last_price
            update_prices(price, i)
            last_price = price
        return sequence_prices.max()


if __name__ == '__main__':
    Level().run()
