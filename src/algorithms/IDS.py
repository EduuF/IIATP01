from src.algorithms.BaseAlgorithm import BaseAlgorithm

class IDS(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

    # Itera o limite de profundidade
    def search_algorithm(self, start):
        depth = 0
        while True:
            cost, found, expanded_states, path = self.dfs_limit(start, depth)
            if found:
                if self.print_results:
                    self.intermediate_steps = path
                return cost, expanded_states
            depth += 1

    def dfs_limit(self, node, limit):
        open_list = [(node, 0, [node], 0)] # estado atual, found, path até agora, depth
        closed_list = set()
        expanded_states = 0

        while open_list:
            current_state, cost_so_far, path_so_far, current_depth = open_list.pop()
            if self.is_ordered(current_state):
                return cost_so_far, True, expanded_states, path_so_far
            closed_list.add(current_state)
            expanded_states += 1

            if current_depth + 1 <= limit:
                for next_node, new_cost in self.get_neighbors(current_state, cost_so_far):
                    if next_node not in closed_list:
                        new_path = path_so_far + [next_node]
                        next_depth = current_depth + 1
                        open_list.append((next_node, new_cost, new_path, next_depth))

        return 0, False, expanded_states, []
