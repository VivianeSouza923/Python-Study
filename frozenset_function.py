'''
    frozenset(iteravel)
    Função cria um objeto imutável semelhante a um conjunto (set)
'''

conjunto = {1, 2, 3}
conjunto_imutavel = frozenset(conjunto)
print(conjunto_imutavel)  # Saída: frozenset({1, 2, 3})
