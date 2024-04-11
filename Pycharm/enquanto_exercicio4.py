'''
(Validador) Ler duas notas e informar a média. Se o valor digitado for menor do que 0 (zero)
ou maior do que 10 (dez), o usuário deve digitar a nota novamente
'''

nota1 = 11
while nota1 > 10 or nota1 < 0:
    print('Digite a primeira nota: ')
    nota1 = float(input())

nota2 = -1
while nota2 > 10 or nota2 < 0:
    print('Digite a nota 2: ')
    nota2 = float(input())

media = (nota1 + nota2) / 2
print('Média: ', media)