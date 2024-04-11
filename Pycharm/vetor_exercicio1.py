'''
Leia um vetor A de 10 elementos inteiros e um valor individual X. A seguir,
imprimir os índices do vetor A em que aparece um valor igual a X
'''
import numpy

vetor = numpy.empty(10, dtype=numpy.int32)
for posicao in range(0,10):
    print("Digite o valor ", posicao + 1, ": ")
    vetor[posicao] = int(input())

print("Digite um número a ser pesquisado: ")
X = int(input())

for posicao in range(0,10):
    if vetor[posicao] == X:
        print(X, "foi encontrado na posição ", posicao)