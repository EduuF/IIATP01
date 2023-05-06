from collections import deque
import itertools

class BFS:
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

    def bfs(self, start, goal):
        queue = deque([([start], 0)])
        visited = set([start])
        expanded_states = 0

        while queue:
            path, cost = queue.popleft()
            node = path[-1]
            expanded_states += 1

            if node == goal:
                if self.printOuNao:
                    self.passosIntermediarios = path  # Armazena apenas os estados no caminho ótimo
                return cost, expanded_states

            for next_node, new_cost in self.neighbors(node, cost):
                if next_node not in visited:
                    visited.add(next_node)
                    new_path = list(path)
                    new_path.append(next_node)
                    queue.append((new_path, new_cost))


    def neighbors(self, node, cost):
        neighbors_list = []

        for i in range(len(node)):
            for j in range(i + 1, len(node)):
                if node[i] > node[j]:  # Adicionada a condição de troca válida
                    next_node = list(node)
                    next_node[i], next_node[j] = next_node[j], next_node[i]
                    next_node = tuple(next_node)
                    new_cost = cost + self.calculate_swap_cost(node, i, j)
                    neighbors_list.append((next_node, new_cost))

        return neighbors_list

    def ordena_elementos(self):
        start = tuple(self.grafo.elementos)
        goal = tuple(sorted(self.grafo.elementos))

        if start == goal:
            return start, 0

        self.cost, self.expanded_states = self.bfs(start, goal)


    def printResultado(self):
        print(f"{self.cost} {self.expanded_states}" )
        for estadoExpandido in self.passosIntermediarios:
            print(" ".join([str(x) for x in estadoExpandido]))
