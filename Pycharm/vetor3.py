import numpy

vetor = numpy.empty(5)
for posicao in range(0,5):
    print("Digite o valor", posicao + 1, ":")
    vetor[posicao] = float(input())

print("Digite o valor a ser pesquisado: ")
pesquisa = float(input())

for posicao in range(0,5):
    if vetor[posicao] == pesquisa:
        print("Encontrou o valor na posição: ", posicao)