from utils.getInputs import *
from utils.gerenciadorDeAlgoritmos import *

if __name__ == '__main__':

    algSelecionado, elementos, printOuNao = getInputs()
    alg = gerenciadorDeAlgoritmos(algSelecionado, elementos)

    alg.setPrintOuNao(printOuNao)
    alg.ordena_elementos()
    alg.printResultado()









