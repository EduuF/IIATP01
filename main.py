from utils.leInputs import *
from utils.gerenciadorDeAlgoritmos import *
from src.estruturasDeDados.grafo import *

if __name__ == '__main__':

    algSelecionado, elementos, printOuNao = leInputs()
    grafoElementos = Grafo(elementos)
    alg = gerenciadorDeAlgoritmos(algSelecionado, grafoElementos)

    alg.setPrintOuNao(printOuNao)
    alg.ordena_elementos()
    alg.printResultado()









