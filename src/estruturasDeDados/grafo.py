class Grafo:
    def __init__(self, elementos):
        self.elementos = elementos
        self.adjMatrix = []
        self.buildAdjMatrix(elementos)

    def buildAdjMatrix(self, elementos):
        numeroDeElementos = len(elementos)
        self.adjMatrix = [[0] * numeroDeElementos for _ in range(numeroDeElementos)]

        for i, elem in enumerate(elementos):
            for j, otherElem in enumerate(elementos):
                if i != j:  # Excluindo a ligação do elemento com ele mesmo
                    if abs(i - j) == 1:  # Caso os elementos sejam vizinhos
                        self.adjMatrix[i][j] = 2
                    else:
                        self.adjMatrix[i][j] = 4

    def __str__(self):
        result = []
        for i, elem in enumerate(self.elementos):
            connections = ", ".join(f"{otherElem}: {self.adjMatrix[i][j]}" for j, otherElem in enumerate(self.elementos) if i != j)
            result.append(f'{elem}: {{{connections}}}')
        return "\n".join(result)