from src.algoritmos.BaseAlgoritmo import BaseAlgoritmo
from collections import deque

class BFS(BaseAlgoritmo):
    def __init__(self, grafo):
        super().__init__(grafo)

    def busca(self, start):
        queue = deque([(start, 0, [start])])  # Armazena (estado, custo, caminho)
        visited = set()
        expanded_states = 0

        while queue:
            current, g, path = queue.popleft()
            if self.estaOrdenado(current):
                if self.printOuNao:
                    self.passosIntermediarios = path  # Armazena apenas os estados no caminho ótimo
                return g, expanded_states

            visited.add(current)
            expanded_states += 1

            for next_node, new_g in self.getVizinhos(current, g):
                if next_node not in visited:
                    visited.add(next_node)
                    new_path = path + [next_node]  # Adiciona o próximo nó ao caminho
                    queue.append((next_node, new_g, new_path))
