'''
Leia um vetor de 10 elementos e apresente:
  O somatório de todos os valores
  A média de todos os valores
  A quantidade de números negativos
'''
import numpy

vetor = numpy.empty(10)
for posicao in range(0,10):
    print('Digite o valor ', posicao + 1, ': ')
    vetor[posicao] = float(input())

soma = 0.0
negativos = 0
for posicao in range(0,10):
    soma = soma + vetor[posicao]
    if vetor[posicao] < 0:
        negativos += 1

media = soma / 10
print('Soma: ', soma)
print('Média: ', media)
print('Negativos: ', negativos)