from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    def __init__(self, elements):
        self.elements = elements
        self.print_results = False
        self.intermediate_steps = []
        self.expanded_states = 0
        self.cost = 0

    def set_print_results(self, print_results):
        self.print_results = print_results

    def is_ordered(self, current_node):
        for i in range(len(current_node) - 1):
            if current_node[i] > current_node[i + 1]:
                return False
        return True

    def swap_cost(self, i, j):
        if abs(i - j) == 1:
            return 2
        else:
            return 4

    def get_neighbors(self, current_node, cost_so_far):
        neighbor_list = []

        for i in range(len(current_node)):
            for j in range(i + 1, len(current_node)):
                if current_node[i] > current_node[j]:
                    next_node = list(current_node)
                    next_node[i], next_node[j] = next_node[j], next_node[i]
                    next_node = tuple(next_node)
                    new_g_cost = cost_so_far + self.swap_cost(i, j)
                    neighbor_list.append((next_node, new_g_cost))

        return neighbor_list

    def sort_elements(self):
        start = tuple(self.elements)
        if self.is_ordered(start):
            return start, 0
        self.cost, self.expanded_states = self.search(start)

    def print_result(self):
        print(f"{self.cost} {self.expanded_states}")
        for expanded_state in self.intermediate_steps:
            print(" ".join([str(x) for x in expanded_state]))

    def heuristic(self, state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j]:
                    inversions += 1
        return inversions * 2

    @abstractmethod
    def search(self, start):
        pass

