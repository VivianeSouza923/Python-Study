'''

    É uma função embutida que é usada para criar uma tupla.
    tuple(iterável)

'''

# Criando uma tupla a partir de uma lista
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(tupla)  # Saída: (1, 2, 3, 4, 5)

# Criando uma tupla vazia
tupla_vazia = tuple()
print(tupla_vazia)  # Saída: ()

# Criando uma tupla com elementos separados por vírgula
tupla = tuple([1, 2, 3]) # é basicamente passar a lista direto como parâmetro
print(tupla)  # Saída: (1, 2, 3)

# Criando uma tupla a partir de uma string
texto = "python"
tupla = tuple(texto)
print(tupla)  # Saída: ('p', 'y', 't', 'h', 'o', 'n')

tupla_tupla = tuple((5, 6, 7))
print(tupla_tupla)