from utils.leInputs import *
from utils.selecionaAlgoritmo import *
from src.estruturasDeDados.grafo import *

if __name__ == '__main__':
    algSelecionado, elementos, printOuNao = leInputs()
    grafoElementos = Grafo(elementos)
    alg = selecionaAlgoritmo(algSelecionado, grafoElementos)

    alg.setPrintOuNao(printOuNao)
    alg.ordena_elementos()
    alg.printResultado()









