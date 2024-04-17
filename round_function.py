'''
    É usada para arredondar um número para determinado número de casas decimais ou para o inteiro mais próximo, se nenhum número
    de casas decimais for passado.

    round(numero, ndigits) - ndigits é número de casas decimais e É OPCIONAL.

'''

# Arredondando para o inteiro mais próximo
arredondado = round(3.7)
print(arredondado)  # Saída: 4

# Arredondando para duas casas decimais
arredondado = round(3.14159, 2)
print(arredondado)  # Saída: 3.14


# Arredondando para a posição mais à esquerda da vírgula decimal, se o número de casas decimais for negativo!
arredondado = round(1234.56789, -2)
print(arredondado)  # Saída: 1200.0

# Arredondamento par, se o número estiver equidistante dos números inteiros.
arredondado = round(2.5)
print(arredondado)  # Saída: 2

