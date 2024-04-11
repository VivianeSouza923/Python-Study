'''
Leia o vetor nomes e o vetor notas, nos quais devem ser informados os nomes dos alunos e as notas,
respectivamente em cada vetor. Ao final, mostrar o nome do aluno e sua nota
'''
import numpy

nomes = numpy.empty(5, dtype=object)
notas = numpy.empty(5)

for posicao in range(0,5):
    print('Digite o nome do aluno ', posicao + 1, ': ')
    nomes[posicao] = input()
    print('Digite a nota do aluno ', posicao + 1, ': ')
    notas[posicao] = float(input())

for posicao in range(0,5):
    print(nomes[posicao], ' - ', notas[posicao])