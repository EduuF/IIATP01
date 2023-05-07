from abc import ABC, abstractmethod

class BaseAlgoritmo(ABC):
    def __init__(self, elementos):
        self.elementos = elementos
        self.printOuNao = False
        self.passosIntermediarios = []
        self.expanded_states = 0
        self.cost = 0

    def setPrintOuNao(self, printOuNao):
        self.printOuNao = printOuNao

    def estaOrdenado(self, noAtual):
        for i in range(len(noAtual) - 1):
            if noAtual[i] > noAtual[i + 1]:
                return False
        return True

    def custoTroca(self, i, j):
        if abs(i - j) == 1:
            return 2
        else:
            return 4

    def getVizinhos(self, noAtual, custoAteAgora):
        listaDeVizinhos = []

        for i in range(len(noAtual)):
            for j in range(i + 1, len(noAtual)):
                if noAtual[i] > noAtual[j]:  # Condição de troca válida
                    next_node = list(noAtual)
                    next_node[i], next_node[j] = next_node[j], next_node[i]
                    next_node = tuple(next_node)
                    new_g_cost = custoAteAgora + self.custoTroca(i, j)  # Calcula o custo da troca diretamente
                    listaDeVizinhos.append((next_node, new_g_cost))

        return listaDeVizinhos

    def ordena_elementos(self):
        start = tuple(self.elementos)
        if self.estaOrdenado(start):
            return start, 0
        self.cost, self.expanded_states = self.busca(start)

    def printResultado(self):
        print(f"{self.cost} {self.expanded_states}")
        for estadoExpandido in self.passosIntermediarios:
            print(" ".join([str(x) for x in estadoExpandido]))

    def heuristica(self, state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j]:
                    inversions += 1
        return inversions * 2

    @abstractmethod
    def busca(self, start):
        pass
