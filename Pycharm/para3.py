# Acumulador
soma = 0.0
media = 0.0
for contador in range(1, 6):
    print('Digite a nota ', contador)
    nota = float(input())
    soma += nota
media = soma / 5
print('Média: ', media)