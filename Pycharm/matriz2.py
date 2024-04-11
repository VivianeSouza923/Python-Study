import numpy

matriz = numpy.empty([2,2])

for linha in range(0,2):
    for coluna in range(0,2):
        print('Digite o valor da linha ', linha, ' e da coluna ', coluna, ': ')
        matriz[linha][coluna] = int(input())

for linha in range(0,2):
    for coluna in range(0,2):
        print(matriz[linha][coluna])