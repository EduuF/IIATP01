from src.algoritmos.BaseAlgoritmo import BaseAlgoritmo
import heapq

class UCS(BaseAlgoritmo):
    def __init__(self, grafo):
        super().__init__(grafo)

    def busca(self, start):
        open_list = [(0, start, [start])]  # A lista de prioridades armazena (custo, estado, caminho)
        closed_list = set()
        expanded_states = 0

        while open_list:
            g, current, path = heapq.heappop(open_list)
            if self.is_sorted(current):
                if self.printOuNao:
                    self.passosIntermediarios = path  # Armazena apenas os estados no caminho ótimo
                return g, expanded_states

            closed_list.add(current)

            for next_node, new_g in self.neighbors(current, g):
                if next_node not in closed_list:
                    new_path = path + [next_node]  # Adiciona o próximo nó ao caminho
                    heapq.heappush(open_list, (new_g, next_node, new_path))
                    expanded_states += 1

