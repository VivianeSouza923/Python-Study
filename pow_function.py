'''
    A função pow() é usada para calcular a potência de um número.
    pow(base, expoente, módulo=None)
    esse módulo é opcional. 

'''

resultado = pow(2, 3)
print(resultado)  # Saída: 8 (2 elevado à potência de 3)

resultado_modulo = pow(2, 3, 5)
print(resultado_modulo)  # Saída: 3 (2 elevado à potência de 3, e então calculado módulo 5)
# esse módulo será o resultado de: 2³ % 5 = 3, ou seja, resto de divisão.


