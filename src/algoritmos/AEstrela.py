from src.algoritmos.BaseAlgoritmo import BaseAlgoritmo
import heapq

class AEstrela(BaseAlgoritmo):
    def __init__(self, elementos):
        super().__init__(elementos)

    def busca(self, start):
        open_list = [(self.heuristica(start), start, 0, [start])]  # A lista de prioridades armazena (f, estado, g, caminho)
        closed_list = set()
        expanded_states = 0

        while open_list:
            f, current, g, path = heapq.heappop(open_list)
            if self.estaOrdenado(current):
                if self.printOuNao:
                    self.passosIntermediarios = path  # Armazena apenas os estados no caminho ótimo
                return g, expanded_states

            closed_list.add(current)

            for next_node, new_g in self.getVizinhos(current, g):
                if next_node not in closed_list:
                    new_h = self.heuristica(next_node)
                    new_path = path + [next_node]  # Adiciona o próximo nó ao caminho
                    heapq.heappush(open_list, (new_g + new_h, next_node, new_g, new_path))
                    expanded_states += 1
