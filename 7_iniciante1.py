'''
Calculadora Simples: Crie uma calculadora simples que peça ao usuário para inserir dois números e uma operação (+, -, *, /) e então realize a operação e imprima o 
resultado. Inclua tratamento de erros para divisão por zero.

'''

numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))

operacao = input('Digite a operação desejada: ')


if operacao == '+':
    resultado = numero1 + numero2
    print(f'A soma entre os dois números é {resultado}.')
elif operacao == '-':
    resultado = numero1 - numero2
    print(f'A subtração entre os dois números é {resultado}.')
elif operacao == '*':
    resultado = numero1 * numero2
    print(f'A multiplicação entre os dois números é {resultado}.')
elif operacao == '/':
    if numero2 == 0:
        print('Não é possível dividir por zero.')
    else: 
        resultado = numero1 / numero2 
        print(f'A divisão entre os dois números é {resultado}.')
else:
    print('Digite uma operação válida.')