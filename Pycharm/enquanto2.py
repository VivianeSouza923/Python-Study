# Acumulador

contador = 1
nota = 0
soma = 0
media = 0
while contador <= 5:
    print('Digite a nota ', contador)
    nota = float(input())
    soma = soma + nota
    contador += 1

print('Soma: ', soma)
media = soma / 5
print('Média: ', media)