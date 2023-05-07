from abc import ABC, abstractmethod

class BaseAlgoritmo(ABC):
    def __init__(self, grafo):
        self.grafo = grafo
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

    def getVizinhos(self, noAtual, custoAteAgora):
        listaDeVizinhos = []

        for i in range(len(noAtual)):
            for j in range(i + 1, len(noAtual)):
                if noAtual[i] > noAtual[j]:  # Condição de troca válida
                    next_node = list(noAtual)
                    next_node[i], next_node[j] = next_node[j], next_node[i]
                    self.grafo.constroiMatrizDeAdj(next_node)  # Atualiza os pesos da MatAdj com o novo vetor
                    next_node = tuple(next_node)
                    new_g_cost = custoAteAgora + self.grafo.matrizDeAdj[i][j]  # Usa diretamente os valores da matriz de adjacência do grafo
                    listaDeVizinhos.append((next_node, new_g_cost))


        return listaDeVizinhos

    def ordena_elementos(self):
        start = tuple(self.grafo.elementos)
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
