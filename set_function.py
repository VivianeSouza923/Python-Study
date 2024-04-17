'''
    É uma função embutida para criar um objeto conjunto, que é uma coleção não ordenada de elementos únicos.

    set(iterável)
'''

# Criando um conjunto a partir de uma lista
lista = [1, 2, 3, 3, 4, 4, 5]
conjunto = set(lista) # ela vai retirar o que se repete, pois como a definição diz: ELEMENTOS ÚNICOS.
print(conjunto)  # Saída: {1, 2, 3, 4, 5}

# Criando um conjunto a partir de uma string
texto = "python"
conjunto = set(texto)
print(conjunto)  # Saída: {'p', 'y', 't', 'h', 'o', 'n'}

#CRIANDO UM CONJUNTO VAZIO.
conjunto_vazio = set()
print(conjunto_vazio)  # Saída: set()

