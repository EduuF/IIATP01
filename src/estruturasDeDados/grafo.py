class Grafo:
    def __init__(self, elementos):
        self.elementos = elementos
        self.matrizDeAdj = []
        self.constroiMatrizDeAdj(elementos)

    def constroiMatrizDeAdj(self, elementos):
        numeroDeElementos = len(elementos)
        self.matrizDeAdj = [[0] * numeroDeElementos for _ in range(numeroDeElementos)]

        for i, elem in enumerate(elementos):
            for j, otherElem in enumerate(elementos):
                if i != j:  # Excluindo a ligação do elemento com ele mesmo
                    if abs(i - j) == 1:  # Caso os elementos sejam vizinhos
                        self.matrizDeAdj[i][j] = 2
                    else:
                        self.matrizDeAdj[i][j] = 4

    # Printar o grafo para ajudar na depuração do código ao longo da cosntrução dos algoritmos
    def __str__(self):
        result = []
        for i, elem in enumerate(self.elementos):
            adjacentes = ", ".join(f"{otherElem}: {self.matrizDeAdj[i][j]}" for j, otherElem in enumerate(self.elementos) if i != j)
            result.append(f'{elem}: {{{adjacentes}}}')
        return "\n".join(result)