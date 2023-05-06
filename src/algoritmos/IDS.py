class IDS:
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

    def ids(self, start, goal):
        depth = 0
        while True:
            cost, found, expanded_states, path = self.dfs_limit(start, goal, depth)
            if found:
                if self.printOuNao:
                    self.passosIntermediarios = path
                return cost, expanded_states
            depth += 1

    def dfs_limit(self, node, goal, limit):
        stack = [(node, 0, [node])]
        visited = set()
        expanded_states = 0
        path = []

        while stack:
            current, cost, current_path = stack.pop()
            if current == goal:
                return cost, True, expanded_states, current_path
            visited.add(current)
            expanded_states += 1

            if len(current_path) - 1 < limit:  # Verifica o limite
                for next_node, new_cost in self.neighbors(current, cost):
                    if next_node not in visited:
                        new_path = current_path + [next_node]
                        stack.append((next_node, new_cost, new_path))

        return 0, False, expanded_states, path

    def neighbors(self, node, cost):
        neighbors_list = []

        for i in range(len(node)):
            for j in range(i + 1, len(node)):
                if node[i] > node[j]:  # Condição de troca válida
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

        self.cost, self.expanded_states = self.ids(start, goal)

    def printResultado(self):
        print(f"{self.cost} {self.expanded_states}")
        for estadoExpandido in self.passosIntermediarios:
            print(" ".join([str(x) for x in estadoExpandido]))
