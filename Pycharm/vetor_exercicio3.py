'''
Leia um vetor A com 10 elementos do tipo real. Construir um vetor B de mesmo tipo,
sendo que cada elemento do vetor B deve ser o cubo de cada elemento
correspondente do vetor A. Apresentar no final os dois vetores
'''
import numpy

A = numpy.empty(10)
B = numpy.empty(10)

for posicao in range(0,10):
    print('Digite o valor ', posicao, ":")
    A[posicao] = float(input())
    B[posicao] = A[posicao] * A[posicao] * A[posicao]

print('Vetor A')
print(A)
print('Vetor B')
print(B)