'''
6. Condicionais:

Peça ao usuário para inserir um número.

Verifique se o número é positivo, negativo ou zero usando instruções if, elif e else.

Imprima uma mensagem informando o resultado.

'''

num = int(input('Insira um número: '))

if num > 0:
    print('O número inserido é positivo.')
elif num < 0:
    print('O número inserido é negativo.')
else:
    print('O número inserido é 0.')
