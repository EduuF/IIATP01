from src.algorithms.BaseAlgorithm import BaseAlgorithm
import heapq

class AStar(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

    def search_algorithm(self, start):
        open_list = [(self.heuristic(start), start, 0, [start])]
        closed_list = set()
        expanded_states = 0

        while open_list:
            f, current, g, path = heapq.heappop(open_list)
            if self.is_ordered(current):
                if self.print_results:
                    self.intermediate_steps = path
                return g, expanded_states

            closed_list.add(current)

            for next_node, new_g in self.get_neighbors(current, g):
                if next_node not in closed_list:
                    new_h = self.heuristic(next_node)
                    new_path = path + [next_node]
                    heapq.heappush(open_list, (new_g + new_h, next_node, new_g, new_path))
                    expanded_states += 1
