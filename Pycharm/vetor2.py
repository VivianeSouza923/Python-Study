import numpy

vetor = numpy.empty(5)

for posicao in range(0,5):
    print("Digite o valor ", posicao + 1, ": ")
    valor = float(input())
    vetor[posicao] = valor

for posicao in range(0,5):
    print(vetor[posicao])