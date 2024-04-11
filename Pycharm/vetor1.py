import numpy

vetor = numpy.empty(5)
vetor[0] = 10
vetor[1] = 20
vetor[2] = 30
vetor[3] = 40
vetor[4] = 50

#print(vetor[2])

for posicao in range(0, 5):
    print(vetor[posicao])