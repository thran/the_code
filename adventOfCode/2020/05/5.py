# start 9:45, 1. 9:58, 2: 10:02

from pathlib import Path


def get_id(seat):
    return seat[0] * 8 + seat[1]


seats = []
with Path('input.txt').open() as file:
    for line in file.readlines():
        seat = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        row = int(seat[:7], 2)
        column = int(seat[7:], 2)
        seats.append((row, column))


print(get_id(max(seats, key=get_id)))


last = None
for seat in sorted(seats):
    seat_id = get_id(seat)
    if last is not None and seat_id != last + 1:
        assert seat_id == last + 2
        print(last + 1)
        break
    else:
        last = seat_id
