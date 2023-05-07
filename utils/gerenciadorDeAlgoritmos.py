from src.algoritmos.BFS import *
from src.algoritmos.IDS import *
from src.algoritmos.UCS import *
from src.algoritmos.G_BFS import *
from src.algoritmos.AEstrela import *

def gerenciadorDeAlgoritmos(algoritmo, grafo):
    match algoritmo:
        case 'B':
            algBFS = BFS(grafo)
            return algBFS
        case 'I':
            algIDS = IDS(grafo)
            return algIDS
        case 'U':
            algUCS = UCS(grafo)
            return algUCS
        case 'A':
            algAEstrela = AEstrela(grafo)
            return algAEstrela
        case 'G':
            algG_BFS = GBFS(grafo)
            return algG_BFS