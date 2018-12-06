from itertools import combinations

init_floors = [
    {'PG', 'PM', 'EG', 'EM', 'DG', 'DM'},
    {'CG', 'UG', 'RG', 'LG'},
    {'CM', 'UM', 'RM', 'LM'},
    set()
]


def checks(floors):
    for floor in floors:
        contain_not_protected = False
        contain_generator = False
        for item in floor:
            if item[1] == 'M' and item[0] + 'G' not in floor:
                contain_not_protected = True
            if item[1] == 'G':
                contain_generator = True
        if contain_generator and contain_not_protected:
            return False
    return True


def check_finish(elevator, floors):
    if elevator == (len(floors) - 1) and len(floors[-1]) == sum(map(len, init_floors)):
        return True
    return False


def show(elevator, floors):
    for i, floor in enumerate(floors[::-1]):
        f = len(floors) - i - 1
        print('L{} {} -  {}'.format(f + 1, 'E' if elevator == (f) else ' ', ' '.join(floors[f])))
    print()


visited = {}
to_discover = [(0, init_floors)]


def discover(elevator, floors):
    for stuff in list(combinations(floors[elevator], 2)) + [(e, ) for e in floors[elevator]]:
        if elevator > 0:
            new_floors = [floor.copy() for floor in floors]
            new_floors[elevator] -= set(stuff)
            new_floors[elevator - 1] |= set(stuff)
            yield elevator - 1, new_floors
        if elevator < 3:
            new_floors = [floor.copy() for floor in floors]
            new_floors[elevator] -= set(stuff)
            new_floors[elevator + 1] |= set(stuff)
            yield elevator + 1, new_floors

i = 0
while True:
    i += 1
    print(i, len(to_discover), len(visited))
    new_states = []
    for elevator, floors in to_discover:
        for new_elevator, new_floors in discover(elevator, floors):
            key = (new_elevator, str([repr(sorted(list(f))) for f in new_floors]))
            if not checks(new_floors):
                continue
            if check_finish(new_elevator, new_floors):
                print('Hooray ', i)
                exit()
            if key in visited:
                continue
            visited[key] = True
            new_states.append((new_elevator, new_floors))
    to_discover = new_states
