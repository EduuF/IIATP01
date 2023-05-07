from src.algoritmos.BFS import *
from src.algoritmos.IDS import *
from src.algoritmos.UCS import *
from src.algoritmos.G_BFS import *
from src.algoritmos.AEstrela import *

def gerenciadorDeAlgoritmos(algoritmo, grafo):

    if algoritmo == 'B':
        algBFS = BFS(grafo)
        return algBFS

    if algoritmo == 'I':
        algIDS = IDS(grafo)
        return algIDS

    if algoritmo == 'U':
        algUCS = UCS(grafo)
        return algUCS

    if algoritmo == 'A':
        algAEstrela = AEstrela(grafo)
        return algAEstrela

    if algoritmo == 'G':
        algG_BFS = GBFS(grafo)
        return algG_BFS