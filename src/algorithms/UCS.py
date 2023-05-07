from src.algorithms.BaseAlgorithm import BaseAlgorithm
import heapq

class UCS(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

    def search(self, start):
        open_list = [(0, start, [start])]  # Priority list stores (cost, state, path)
        closed_list = set()
        expanded_states = 0

        while open_list:
            g, current, path = heapq.heappop(open_list)
            if self.is_ordered(current):
                if self.print_results:
                    self.intermediate_steps = path  # Store only the states in the optimal path
                return g, expanded_states

            closed_list.add(current)

            for next_node, new_g in self.get_neighbors(current, g):
                if next_node not in closed_list:
                    new_path = path + [next_node]  # Add the next node to the path
                    heapq.heappush(open_list, (new_g, next_node, new_path))
                    expanded_states += 1
