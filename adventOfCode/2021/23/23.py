import json
from copy import deepcopy
import heapq

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 12521
    part_two_test_solution = 44169

    room_positions = {'A': 2, 'B': 3, 'C': 4, 'D': 5}

    def preprocess_input(self, lines):
        state = {
            'rooms': {
                'A': [lines[3][1], lines[2][3]],
                'B': [lines[3][3], lines[2][5]],
                'C': [lines[3][5], lines[2][7]],
                'D': [lines[3][7], lines[2][9]],
            },
            'hallway': [None] * 7,
            'depth': 2,
            'energy': 0,
        }
        return state

    def get_ready_rooms(self, state):
        ready_rooms = {room for room in state['rooms'] if len(set(state['rooms'][room]) - {room}) == 0}
        return ready_rooms

    def is_path_clear(self, state, room, hallway_position, to_room=False):
        room_position = self.room_positions[room]
        if hallway_position < room_position:
            if to_room:
                hallway_position += 1
            return all(state['hallway'][position] is None for position in range(hallway_position, room_position))
        else:
            if to_room:
                hallway_position -= 1
            return all(state['hallway'][position] is None for position in range(room_position, hallway_position + 1))

    def get_energy(self, state, amphipod, from_, to_):
        energy = 0

        if type(from_) is str:
            room_position = self.room_positions[from_]
            energy += state['depth'] - len(state['rooms'][from_])
            t = to_ if type(to_) is int else self.room_positions[to_]
            from_ = room_position - 1 if room_position <= t else room_position

        if type(to_) is str:
            room_position = self.room_positions[to_]
            energy += state['depth'] - len(state['rooms'][to_]) - 1
            to_ = room_position - 1 if room_position <= from_ else room_position

        from_, to_ = min(from_, to_), max(from_, to_)
        energy += to_ - from_
        for room in self.room_positions.values():
            if from_ < room <= to_:
                energy += 1
        return energy * 10 ** (self.room_positions[amphipod] - 2)

    def return_from_hallway(self, state):
        ready_rooms = {room for room in state['rooms'] if len(set(state['rooms'][room]) - {room}) == 0}
        something_moved = False
        for hallway_position, amphipod in enumerate(state['hallway']):
            if amphipod in ready_rooms and self.is_path_clear(state, amphipod, hallway_position, to_room=True):
                state['energy'] += self.get_energy(state, amphipod, hallway_position, amphipod)
                state['rooms'][amphipod].append(amphipod)
                state['hallway'][hallway_position] = None
                something_moved = True
        return something_moved

    def move_between_rooms(self, state):
        something_moved = False
        ready_rooms = self.get_ready_rooms(state)
        for room in set(state['rooms']) - ready_rooms:
            target_room = state['rooms'][room][-1]
            hallway_position = self.room_positions[room] - 1 if target_room > room else self.room_positions[room]
            if target_room in ready_rooms and self.is_path_clear(state, target_room, hallway_position, to_room=True):
                state['energy'] += self.get_energy(state, target_room, room, target_room)
                state['rooms'][target_room].append(state['rooms'][room].pop())
                something_moved = True
        return something_moved

    def possible_moves(self, state):
        ready_rooms = self.get_ready_rooms(state)
        possible_moves = []
        for room in set('ABCD') - ready_rooms:
            if not state['rooms'][room]:
                continue
            for hallway_position in range(len(state['hallway'])):
                if self.is_path_clear(state, room, hallway_position):
                    new_state = deepcopy(state)
                    amphipod = new_state['rooms'][room].pop()
                    new_state['hallway'][hallway_position] = amphipod
                    new_state['energy'] += self.get_energy(state, amphipod, room, hallway_position)
                    something_moved = True
                    while something_moved:
                        something_moved = False
                        if self.return_from_hallway(new_state) or self.move_between_rooms(new_state):
                            something_moved = True
                    possible_moves.append(new_state)
        return possible_moves
    
    def hash(self, state):
        return json.dumps(state['rooms'], sort_keys=True) + json.dumps(state['hallway'])

    def solve(self, state):
        states_to_process = []
        heap_collision_avoider = 0
        heapq.heappush(states_to_process, (state['energy'], heap_collision_avoider, state))
        visited_states = set()
        while True:
            _, _, state = heapq.heappop(states_to_process)
            state_hash = self.hash(state)
            if state_hash in visited_states:
                continue
            visited_states.add(state_hash)
            if all(p is None for p in state['hallway']) and all(room == amphipod for room, amphipods in state['rooms'].items() for amphipod in amphipods):
                return state
            for new_state in self.possible_moves(state):
                heap_collision_avoider += 1
                heapq.heappush(states_to_process, (new_state['energy'], heap_collision_avoider, new_state))

    def part_one(self, state) -> int:
        return self.solve(state)['energy']

    def part_two(self, state) -> int:
        new = {
            'A': ['D', 'D'],
            'B': ['B', 'C'],
            'C': ['A', 'B'],
            'D': ['C', 'A'],
        }

        for room, amphipods in state['rooms'].items():
            state['rooms'][room] = amphipods[:1] + new[room] + amphipods[1:]
        state['depth'] = 4

        return self.solve(state)['energy']


Level().run()
