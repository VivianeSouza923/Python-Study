'''

    A função range() é usada para gerar uma sequência de números. 

    range(início, fim, passo) - o passo é: será contínuo ou vai de dois em dois, de trÊs em três? Pode se entender como o 
    valor de incremento da sequência também.


'''

# Gerando uma sequência de 0 a 9
sequencia = range(10)
print(list(sequencia))  # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Gerando uma sequência de 1 a 10
sequencia = range(1, 11)
print(list(sequencia))  # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Gerando uma sequência de 0 a 10 com passo 2
sequencia = range(0, 11, 2)
print(list(sequencia))  # Saída: [0, 2, 4, 6, 8, 10]
