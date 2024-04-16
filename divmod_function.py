'''
    A função divmod() faz a divisão entre dois números (inteiros ou não, daí eu posso
    definir o número de casas decimais.). A função retorna tanto o quonciente, quanto o
    resto. E esse retorno é dado através de tupla (quociente, resto).

    divmod(dividendo, divisor) 
'''

resultado = divmod(10, 3)
print(resultado)  # Saída: (3, 1), pois 10 dividido por 3 é 3 com resto 1


resultado = divmod(10.5, 3)
print(resultado)  # Saída: (3.0, 1.5), pois 10.5 dividido por 3 é 3.0 com resto 1.5
