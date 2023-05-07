from src.algorithms.BaseAlgorithm import BaseAlgorithm

class IDS(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

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
        stack = [(node, 0, [node])]
        visited = set()
        expanded_states = 0
        path = []

        while stack:
            current, cost, current_path = stack.pop()
            if self.is_ordered(current):
                return cost, True, expanded_states, current_path
            visited.add(current)
            expanded_states += 1

            if len(current_path) - 1 < limit:
                for next_node, new_cost in self.get_neighbors(current, cost):
                    if next_node not in visited:
                        new_path = current_path + [next_node]
                        stack.append((next_node, new_cost, new_path))

        return 0, False, expanded_states, path
