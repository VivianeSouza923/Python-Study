'''

        7. Tabuada:
        ◦ Peça um número ao usuário e imprima a tabuada desse número.

'''

numero = int(input('Digite um número: '))

print('Tabuada da soma: ')
for i in range(1, 11):
    res = numero + i
    print(f'{i} + {numero} = {res}')

print('Tabuada da subtração: ')
for i in range(1+numero, numero+11):
    res = i - numero
    print(f'{i} - {numero} = {res}')

print('Tabuada da multiplicação: ')
for i in range(1, 11):
    res = numero * i
    print(f'{numero} * {i} = {res}')

print('Tabuada da divisão: ')
for i in range(numero, 11*numero, numero):
    res = i / numero
    print(f'{i} / {numero} = {res}')



