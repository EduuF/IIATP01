import sys

def getInputs():
    inputLido = sys.argv[1:]

    algSelecionado = inputLido[0]

    tamanhoDoVetor = int(inputLido[1])

    elementos = [int(x) for x in inputLido[2:tamanhoDoVetor+2]]
    printOuNao = (inputLido[-1:] == ["PRINT"])

    return algSelecionado, elementos, printOuNao