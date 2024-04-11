'''
        8. Fatorial:
        ◦ Crie um programa que calcule o fatorial de um número. 
        O fatorial de n é o produto de todos os números inteiros de 1 a n.

'''


def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)
    
num = 6

print(f'O fatorial do número {num} é {fatorial(num)}')
    
