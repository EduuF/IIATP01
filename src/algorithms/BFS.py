from src.algorithms.BaseAlgorithm import BaseAlgorithm
from collections import deque

class BFS(BaseAlgorithm):
    def __init__(self, elements):
        super().__init__(elements)

    def search(self, start):
        queue = deque([(start, 0, [start])])  # Stores (state, cost, path)
        visited = set()
        expanded_states = 0

        while queue:
            current, g, path = queue.popleft()
            if self.is_ordered(current):
                if self.print_results:
                    self.intermediate_steps = path  # Store only the states in the optimal path
                return g, expanded_states

            visited.add(current)
            expanded_states += 1

            for next_node, new_g in self.get_neighbors(current, g):
                if next_node not in visited:
                    visited.add(next_node)
                    new_path = path + [next_node]  # Add the next node to the path
                    queue.append((next_node, new_g, new_path))
