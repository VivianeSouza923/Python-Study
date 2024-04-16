'''
    eval(expressao)
    A função eval() é usada para avaliar uma expressão representada como String.
    Ela analisa a String como código Python e a executa como se fosse uma expressão
    Python normal, por exemplo: 1 + 1

'''

resultado = eval('2 + 2')
print(resultado)  # Saída: 4

resultado0 = '2 - 1'

resultado1 = eval(resultado0)
print(resultado1)
