from src.algoritmos.BaseAlgoritmo import OrdenacaoAlgoritmo
import heapq

class AEstrela(OrdenacaoAlgoritmo):
    def __init__(self, grafo):
        super().__init__(grafo)

    def h(self, state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j]:
                    inversions += 1
        return inversions * 2

    def busca(self, start):
        open_list = [(self.h(start), start, 0, [start])]  # A lista de prioridades armazena (f, estado, g, caminho)
        closed_list = set()
        expanded_states = 0

        while open_list:
            f, current, g, path = heapq.heappop(open_list)
            if self.is_sorted(current):
                if self.printOuNao:
                    self.passosIntermediarios = path  # Armazena apenas os estados no caminho ótimo
                return g, expanded_states

            closed_list.add(current)

            for next_node, new_g in self.neighbors(current, g):
                if next_node not in closed_list:
                    new_h = self.h(next_node)
                    new_path = path + [next_node]  # Adiciona o próximo nó ao caminho
                    heapq.heappush(open_list, (new_g + new_h, next_node, new_g, new_path))
                    expanded_states += 1
