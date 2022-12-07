from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 95437
    part_two_test_solution = 24933642

    def preprocess_input(self, lines):
        disk = {'parent': None, 'files': {}, 'dirs': {}}
        current_dir = None
        for line in lines:
            match line.split():
                case '$', 'cd', '/':
                    current_dir = disk
                case '$', 'cd', '..':
                    current_dir = current_dir['parent']
                case '$', 'cd', dir_name:
                    current_dir = current_dir['dirs'][dir_name]
                case '$', ls:
                    pass
                case 'dir', dir_name:
                    current_dir['dirs'][dir_name] = {'parent': current_dir, 'files': {}, 'dirs': {}}
                case size, file_name if size.isnumeric():
                    current_dir['files'][file_name] = int(size)
                case _:
                    assert False

        return disk

    @staticmethod
    def get_dir_sizes(disk):
        sizes = []

        def _compute_dir_size(dir_) -> int:
            size = sum(dir_['files'].values()) + sum(_compute_dir_size(sd) for sd in dir_['dirs'].values())
            sizes.append(size)
            return size

        _compute_dir_size(disk)
        return sizes

    def part_one(self, disk, max_size=100_000) -> int:
        return sum(s for s in self.get_dir_sizes(disk) if s <= max_size)

    def part_two(self, disk, total_size=70_000_000, required_size=30_000_000) -> int:
        sizes = sorted(self.get_dir_sizes(disk))
        free_size = total_size - sizes[-1]
        for size in sizes:
            if free_size + size >= required_size:
                return size


Level().run()
