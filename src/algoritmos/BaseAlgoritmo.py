from abc import ABC, abstractmethod

class OrdenacaoAlgoritmo(ABC):
    def __init__(self, grafo):
        self.grafo = grafo
        self.printOuNao = False
        self.passosIntermediarios = []
        self.expanded_states = 0
        self.cost = 0

    def setPrintOuNao(self, printOuNao):
        self.printOuNao = printOuNao

    def set_grafo(self, grafo):
        self.grafo = grafo

    def is_sorted(self, node):
        for i in range(len(node) - 1):
            if node[i] > node[i + 1]:
                return False
        return True

    def neighbors(self, node, g_cost):
        neighbors_list = []

        for i in range(len(node)):
            for j in range(i + 1, len(node)):
                if node[i] > node[j]:  # Condição de troca válida
                    next_node = list(node)
                    next_node[i], next_node[j] = next_node[j], next_node[i]
                    next_node = tuple(next_node)
                    new_g_cost = g_cost + self.grafo.matrizDeAdj[i][
                        j]  # Usa diretamente os valores da matriz de adjacência do grafo
                    neighbors_list.append((next_node, new_g_cost))

        return neighbors_list

    def ordena_elementos(self):
        start = tuple(self.grafo.elementos)
        if self.is_sorted(start):
            return start, 0
        self.cost, self.expanded_states = self.busca(start)

    def printResultado(self):
        print(f"{self.cost} {self.expanded_states}")
        for estadoExpandido in self.passosIntermediarios:
            print(" ".join([str(x) for x in estadoExpandido]))

    @abstractmethod
    def busca(self, start):
        pass
