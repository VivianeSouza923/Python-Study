'''
Leia um vetor A de 10 elementos inteiros e um valor individual X. A seguir,
imprimir “Achei” se o valor X existir em A e “Não achei” caso contrário
'''
import numpy

A = numpy.empty(10, dtype=numpy.int32)
for posicao in range(0,10):
    print('Digite o valor ', posicao + 1, ': ')
    A[posicao] = int(input())

print('Digite o número a ser pesquisado: ')
X = int(input())

achei = False
for posicao in range(0,10):
    if A[posicao] == X and achei == False:
        print('Achei')
        achei = True
if achei == False:
    print('Não achei')