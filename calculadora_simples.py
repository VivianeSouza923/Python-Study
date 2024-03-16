'''
        3. Calculadora Simples:
        ◦ Crie uma calculadora simples que possa realizar operações básicas (+, -, *, /) com dois números.

'''

def soma(x, y):
    res = x + y
    return res

def subtracao(x, y):
    res = x - y
    return res

def multiplicacao(x, y):
    res = x * y
    return res

def divisao(x, y):
    res = x / y
    return res

a = 6
b = 3

resultado_soma = soma(a, b)
resultado_subtracao = subtracao(a, b)
resultado_multiplicacao = multiplicacao(a, b)
resultado_divisao = divisao(a, b)

print('CALCULADORA SIMPLES: ')
print(f'O resultado da soma é: {resultado_soma}')
print(f'O resultado da subtração é: {resultado_subtracao}')
print(f'O resultado da multiplicação é: {resultado_multiplicacao}')
print(f'O resultado da divisão é: {resultado_divisao}')
