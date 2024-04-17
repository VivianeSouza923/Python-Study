'''


    A função zip() é usada para coombinar elementos de iteráveis em tuplas.
    zip(*iteráveis)

'''

# Combinando elementos de duas listas
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)
print(list(resultado))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]

# Combinando elementos de uma lista e uma tupla
tupla = (4, 5, 6)
resultado = zip(lista1, tupla)
print(list(resultado))  # Saída: [(1, 4), (2, 5), (3, 6)]

# Combinando elementos de três listas
lista3 = ['x', 'y', 'z']
resultado = zip(lista1, lista2, lista3)
print(list(resultado))  # Saída: [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]

# se os iteráveis tiverem valores diferentes, a zipagem acaba quando o mais curto acabar.
lista1 = [1, 2, 3]
lista2 = ['a', 'b']
resultado = zip(lista1, lista2)
print(list(resultado))  # Saída: [(1, 'a'), (2, 'b')]
