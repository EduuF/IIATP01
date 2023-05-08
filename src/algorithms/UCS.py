from src.algorithms.BaseAlgorithm import BaseAlgorithm
import heapq

class UCS(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

    def search_algorithm(self, start):
        open_list = [(0, start, [start])]
        closed_list = set()
        expanded_states = 0

        while open_list:
            cost_so_far, current_node, path_so_far = heapq.heappop(open_list)
            closed_list.add(current_node)

            if self.is_ordered(current_node):
                if self.print_results:
                    self.intermediate_steps = path_so_far
                return cost_so_far, expanded_states

            for next_node, new_cost in self.get_neighbors(current_node, cost_so_far):
                if next_node not in closed_list:
                    add_next_node_to_open_list = True
                    for cost, node, _ in open_list:
                        if node == next_node and new_cost >= cost:
                            add_next_node_to_open_list = False
                            break

                    if add_next_node_to_open_list:
                        new_path = path_so_far + [next_node]
                        heapq.heappush(open_list, (new_cost, next_node, new_path))
                        expanded_states += 1
