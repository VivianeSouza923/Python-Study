'''
Leia um número inteiro e apresenta as seguintes mensagens:
“O valor está na faixa permitida”, caso o valor esteja entre 1 e 9
“O valor está fora da faixa permitida”, caso o valor seja menor que 1 OU maior que 9
'''
print('Digite um número: ')
valor = int(input())

if (valor >= 1 and valor <= 9):
    print('O valor está na faixa permitida')
elif (valor < 1 or valor > 11):
    print('O valor está fora da faixa permitida')