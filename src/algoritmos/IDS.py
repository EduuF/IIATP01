from src.algoritmos.BaseAlgoritmo import BaseAlgoritmo

class IDS(BaseAlgoritmo):
    def __init__(self, grafo):
        super().__init__(grafo)

    def busca(self, start):
        depth = 0
        while True:
            cost, found, expanded_states, path = self.dfs_limit(start, depth)
            if found:
                if self.printOuNao:
                    self.passosIntermediarios = path
                return cost, expanded_states
            depth += 1

    def dfs_limit(self, node, limit):
        stack = [(node, 0, [node])]
        visited = set()
        expanded_states = 0
        path = []

        while stack:
            current, cost, current_path = stack.pop()
            if self.estaOrdenado(current):
                return cost, True, expanded_states, current_path
            visited.add(current)
            expanded_states += 1

            if len(current_path) - 1 < limit:  # Verifica o limite
                for next_node, new_cost in self.getVizinhos(current, cost):
                    if next_node not in visited:
                        new_path = current_path + [next_node]
                        stack.append((next_node, new_cost, new_path))

        return 0, False, expanded_states, path

