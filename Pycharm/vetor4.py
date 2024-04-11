import numpy

nomes = numpy.empty(5, dtype=object)
for posicao in range(0,5):
    print("Digite o nome ", posicao + 1, ": ")
    nomes[posicao] = input()

for posicao in range(0,5):
    print(nomes[posicao])