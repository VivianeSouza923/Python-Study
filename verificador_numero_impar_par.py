'''
    4. Verificador de Número Par ou Ímpar:
        ◦ Solicite um número ao usuário e indique se é par ou ímpar.

'''

numero = int(input('Digite um número: '))

if(numero % 2 == 0):
    print(f'O {numero} digitado é par.')

else: 

    print(f'O {numero} digitado é ímpar.')

