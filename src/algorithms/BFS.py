from src.algorithms.BaseAlgorithm import BaseAlgorithm
from collections import deque

class BFS(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

    def search_algorithm(self, start):
        open_list = deque([(start, 0, [start])])
        closed_list = set()
        closed_list.add(start)
        expanded_states = 0

        while open_list:
            current_state, cost_so_far, path_so_far = open_list.popleft()
            if self.is_ordered(current_state):
                if self.print_results:
                    self.intermediate_steps = path_so_far
                return cost_so_far, expanded_states

            expanded_states += 1

            for next_node, new_cost in self.get_neighbors(current_state, cost_so_far):
                if next_node not in closed_list:
                    closed_list.add(next_node)
                    new_path = path_so_far + [next_node]
                    open_list.append((next_node, new_cost, new_path))
