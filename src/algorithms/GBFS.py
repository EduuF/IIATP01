from src.algorithms.BaseAlgorithm import BaseAlgorithm
import heapq

class GBFS(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

    def search(self, start):
        open_list = [(self.heuristic(start), start, [start])]
        closed_list = set()
        expanded_states = 0

        while open_list:
            h, current, path = heapq.heappop(open_list)
            if self.is_ordered(current):
                if self.print_results:
                    self.intermediate_steps = path
                return len(path) - 1, expanded_states

            closed_list.add(current)
            expanded_states += 1

            for next_node, g in self.get_neighbors(current, len(path) - 1):
                if next_node not in closed_list:
                    new_path = path + [next_node]
                    heapq.heappush(open_list, (self.heuristic(next_node), next_node, new_path))
