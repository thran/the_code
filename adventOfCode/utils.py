import abc
import heapq
import itertools
from collections import deque
from functools import cached_property

import numpy as np


def array(values):
    return np.array(values).view(SmartArray)


class SmartArray(np.ndarray):
    @cached_property
    def direct_neighbors_deltas(self):
        return [ds for ds in self.neighbors_deltas if sum(d != 0 for d in ds) == 1]

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

    @staticmethod
    def change_position(position, delta):
        return tuple(x + d for x, d in zip(position, delta))

    def is_valid_position(self, position: tuple) -> bool:
        for x, size in zip(position, self.shape):
            if x < 0 or x >= size:
                return False
        return True


class Search(abc.ABC):
    def __init__(self, init_states):
        self.visited_states = set()
        self.states_to_visit = self.init_queue(init_states)

    def __call__(self):
        return self.run()

    @abc.abstractmethod
    def init_queue(self, init_states):
        ...

    @abc.abstractmethod
    def pop_state(self):
        ...

    @abc.abstractmethod
    def add_state(self, state):
        ...

    def run(self):
        while self.states_to_visit:
            self.current_state = state = self.pop_state()
            if self.get_state_hash(state) in self.visited_states:
                continue
            if self.end_condition(state):
                break
            self.on_state_visit(state)
            self.visited_states.add(self.get_state_hash(state))
            for new_state in self.next_states(state):
                if new_state in self.visited_states:
                    continue
                self.add_state(new_state)

    @abc.abstractmethod
    def next_states(self, state):
        ...

    def on_state_visit(self, state):
        pass

    def end_condition(self, state) -> bool:
        return False

    def get_state_hash(self, state):
        """For detecting visited states"""
        return state


class BFS(Search, abc.ABC):
    def init_queue(self, init_states):
        return deque(init_states)

    def pop_state(self):
        return self.states_to_visit.popleft()

    def add_state(self, state):
        self.states_to_visit.append(state)


class DFS(BFS, abc.ABC):
    def pop_state(self):
        return self.states_to_visit.pop()


class PrioritySearch(Search, abc.ABC):
    def init_queue(self, init_states):
        states = list(init_states)
        heapq.heapify(states)
        return states

    def pop_state(self):
        return heapq.heappop(self.states_to_visit)

    def add_state(self, state):
        heapq.heappush(self.states_to_visit, state)
