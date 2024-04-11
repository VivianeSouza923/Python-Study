'''
Leia dois números reais e uma operação, e com isso imprima o resultado de acordo com a
operação escolhida pelo usuário: adição, subtração, multiplicação e divisão.
Caso seja informada operação inválida, mostrar na tela
'''
print('Digite o primeiro valor: ')
valor1 = float(input())
print('Digite o segundo valor: ')
valor2 = float(input())
print('Digite a operação: ')
operacao = input()

if operacao == '+':
    resultado = valor1 + valor2
    print('Resultado: ', resultado)
elif operacao == '-':
    resultado = valor1 - valor2
    print('Resultado: ', resultado)
elif operacao == '*':
    resultado = valor1 * valor2
    print('Resultado: ', resultado)
elif operacao == '/':
    resultado = valor1 / valor2
    print('Resultado: ', resultado)
else:
    print('Operação inválida')

