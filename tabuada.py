'''
    7. Tabuada
        ◦ Crie um programa que solicite um número ao usuário e imprima a tabuada desse número.
        '''

num = int(input('Digite um número: '))

print(f'Tabuada do {num} - Soma: ')
for i in range(1, 11):
    res = i + num
    print(f'{i} + {num} = {res}')

print(f'Tabuada do {num} - Subtração: ')
for i in range(num, num+9):
    res = i - num
    print(f'{i} - {num} = {res}')

print(f'Tabuada do {num} - Multiplicação: ')
for i in range(1, 11):
    res = i * num
    print(f'{num} * {i} = {res}')

print(f'Tabuada do {num} - Divisão: ')
for i in range(num, num*11, 2):
    res = i / num
    print(f'{i} / {num} = {res}')

