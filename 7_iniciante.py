'''
7. Laços de Repetição:

Imprima os números de 1 a 10 usando um laço for.

Imprima a tabuada de um número escolhido pelo usuário usando um laço while.
'''

for i in range(1,11):
    print(i)


num = int(input('Escolha um número de 1 a 10: '))   

i = 1

print('\nTabuada de adição: ')
while(i < 11):
    res = num + i
    print(f'{num} + {i} = {res}')
    i += 1

i = num + 1
print('\nTabuada de Subtração: ')
while(i < num + 11):
    res = i - num
    print(f'{i} - {num} = {res}')
    i +=1

i = 1
print('\nTabuada de Multiplicação: ')
while(i < 11):
    res = num * i
    print(f'{num} * {i} = {res}')
    i += 1

i = num
print('\nTabuada de Divisão: ')
while(i < num * 11):
    res = i / num
    print(f'{i} / {num} = {int(res)}')
    i = i + num
