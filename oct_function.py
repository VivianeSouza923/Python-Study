'''
    A função oct() em Pyhton é usada para converter um número inteiro em uma representação octal em forma de string. 
    oct(numero)
'''

valor_decimal = 10
valor_octal = oct(valor_decimal)
print(valor_octal)  # Saída: '0o12', que é a representação octal de 10


valor_decimal_negativo = -10
valor_octal_negativo = oct(valor_decimal_negativo)
print(valor_octal_negativo)  # Saída: '-0o12', a representação octal de -10
