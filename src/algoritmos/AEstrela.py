import heapq


class AEstrela:
    def __init__(self, grafo):
        self.grafo = grafo
        self.printOuNao = False
        self.ordena_elementos()
        self.passosIntermediarios = []
        self.expanded_states = 0
        self.cost = 0

    def setPrintOuNao(self, printOuNao):
        self.printOuNao = printOuNao

    def set_grafo(self, grafo):
        self.grafo = grafo

    def get_cost(self, v1, v2):
        index1 = self.grafo.elementos.index(v1)
        index2 = self.grafo.elementos.index(v2)
        return self.grafo.adjMatrix[index1][index2]

    def calculate_swap_cost(self, seq, i, j):
        return self.get_cost(seq[i], seq[j])

    def h(self, state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j]:
                    inversions += 1
        return inversions * 2

    def astar(self, start, goal):
        open_list = [(self.h(start), start, 0, [start])]  # A lista de prioridades armazena (f, estado, custo, caminho)
        closed_list = set()

        while open_list:
            f, current, g, path = heapq.heappop(open_list)
            if current == goal:
                if self.printOuNao:
                    self.passosIntermediarios = path  # Armazena apenas os estados no caminho ótimo
                return g, len(closed_list)

            closed_list.add(current)

            for next_node, new_g in self.neighbors(current, g):
                if next_node not in closed_list:
                    new_f = new_g + self.h(next_node)
                    new_path = path + [next_node]  # Adiciona o próximo nó ao caminho
                    heapq.heappush(open_list, (new_f, next_node, new_g, new_path))

    def neighbors(self, node, g_cost):
        neighbors_list = []

        for i in range(len(node)):
            for j in range(i + 1, len(node)):
                if node[i] > node[j]:  # Condição de troca válida
                    next_node = list(node)
                    next_node[i], next_node[j] = next_node[j], next_node[i]
                    next_node = tuple(next_node)
                    new_g_cost = g_cost + self.calculate_swap_cost(node, i, j)
                    neighbors_list.append((next_node, new_g_cost))

        return neighbors_list

    def ordena_elementos(self):
        start = tuple(self.grafo.elementos)
        goal = tuple(sorted(self.grafo.elementos))

        if start == goal:
            return start, 0

        self.cost, self.expanded_states = self.astar(start, goal)

    def printResultado(self):
        print(f"{self.cost} {self.expanded_states}")
        for estadoExpandido in self.passosIntermediarios:
            print(" ".join([str(x) for x in estadoExpandido]))