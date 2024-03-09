'''
    7. Tabuada
        ◦ Crie um programa que solicite um número ao usuário e imprima a tabuada desse número.
        '''

num = int(input('Digite um número: '))

for(i = 1; i < 11; i++):
    res = i + num
    print(f'{i} + {num} = {res}')
