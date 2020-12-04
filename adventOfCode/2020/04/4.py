from pathlib import Path

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def is_valid(passport):
    return all(field in passport for field in fields)


def is_valid2(passport):
    for field in fields:
        if field not in passport:
            return False

        value: str = passport[field]

        if field == 'byr':
            if not (value.isdigit() and 1920 <= int(value) <= 2002):
                return False

        if field == 'iyr':
            if not (value.isdigit() and 2010 <= int(value) <= 2020):
                return False

        if field == 'eyr':
            if not (value.isdigit() and 2020 <= int(value) <= 2030):
                return False

        if field == 'hgt':
            if not value.endswith('cm') and not value.endswith('in'):
                return False

            if value.endswith('cm') and not (150 <= int(value[:-2]) <= 193):
                return False

            if value.endswith('in') and not (59 <= int(value[:-2]) <= 76):
                return False

        if field == 'hcl':
            if not (value[0] == '#' and len(value) == 7 and all(c in '0123456789abcdef' for c in value[1:])):
                return False

        if field == 'ecl':
            if not (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                return False

        if field == 'pid':
            if not (len(value) == 9 and value.isdigit()):
                return False

    return True


with Path('input.txt').open() as file:
    valid_count = 0
    valid_count2 = 0
    passport = {}
    for line in file:
        if not line.strip():
            valid_count += 1 if is_valid(passport) else 0
            valid_count2 += 1 if is_valid2(passport) else 0
            passport = {}
            continue
        for part in line.strip().split():
            field, value = part.split(':')
            passport[field] = value
    valid_count += 1 if passport and is_valid(passport) else 0
    valid_count2 += 1 if passport and is_valid2(passport) else 0

print(valid_count)
print(valid_count2)
