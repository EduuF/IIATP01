from src.algoritmos.BFS import *
from src.algoritmos.IDS import *
from src.algoritmos.UCS import *
from src.algoritmos.G_BFS import *
from src.algoritmos.AEstrela import *

def gerenciadorDeAlgoritmos(algoritmo, elementos):

    if algoritmo == 'B':
        algBFS = BFS(elementos)
        return algBFS

    if algoritmo == 'I':
        algIDS = IDS(elementos)
        return algIDS

    if algoritmo == 'U':
        algUCS = UCS(elementos)
        return algUCS

    if algoritmo == 'A':
        algAEstrela = AEstrela(elementos)
        return algAEstrela

    if algoritmo == 'G':
        algG_BFS = GBFS(elementos)
        return algG_BFS