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
            current_heuristic, current_state, cost_so_far, path_so_far = heapq.heappop(open_list)
            closed_list.add(current_state)
            expanded_states += 1

            if self.is_ordered(current_state):
                if self.print_results:
                    self.intermediate_steps = path_so_far
                return cost_so_far, expanded_states

            for next_node, new_cost in self.get_neighbors(current_state, cost_so_far):
                if next_node not in closed_list:
                    new_heuristic = self.heuristic(next_node)
                    new_path = path_so_far + [next_node]
                    heapq.heappush(open_list, (new_cost + new_heuristic, next_node, new_cost, new_path))
