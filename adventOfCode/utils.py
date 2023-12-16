import abc
import itertools
from collections import deque
from functools import cached_property

import numpy as np


def array(values):
    return np.array(values).view(SmartArray)


class SmartArray(np.ndarray):
    @cached_property
    def direct_neighbors_deltas(self):
        return [ds for ds in self.neighbors_deltas if sum(d != 0 for d in ds)]

    @cached_property
    def neighbors_deltas(self):
        deltas = []
        for delta in itertools.product([-1, 0, 1], repeat=self.ndim):
            if all(x == 0 for x in delta):
                continue
            deltas.append(delta)
        return deltas

    def direct_neighbors(self, position):
        for delta in self.direct_neighbors_deltas:
            neighbor = self.change_position(position, delta)
            if self.is_valid_position(neighbor):
                yield neighbor

    def neighbors(self, position):
        for delta in self.neighbors_deltas:
            neighbor = self.change_position(position, delta)
            if self.is_valid_position(neighbor):
                yield neighbor

    def change_position(self, position, delta):
        return tuple(x + d for x, d in zip(position, delta))

    def is_valid_position(self, position: tuple) -> bool:
        for x, size in zip(position, self.shape):
            if x < 0 or x >= size:
                return False
        return True


class Search(abc.ABC):
    def __init__(self, init_states, type_='BFS'):
        assert type_ in ['DFS', 'BFS']
        self.type = type_

        self.visited_states = set()
        self.states_to_visit = deque(init_states)

    def __call__(self):
        return self.run()

    def run(self):
        while self.states_to_visit and not self.end_condition():
            state = self.states_to_visit.popleft() if self.type == 'BFS' else self.states_to_visit.pop()
            self.on_state_visit(state)
            self.visited_states.add(state)
            for new_state in self.next_states(state):
                if new_state in self.visited_states:
                    continue
                self.states_to_visit.append(new_state)

    @abc.abstractmethod
    def next_states(self, state):
        ...

    def on_state_visit(self, state):
        pass

    def end_condition(self) -> bool:
        return False
