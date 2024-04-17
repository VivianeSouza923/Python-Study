'''

    É usada para criar um objeto de fatia que pode ser usado para acessar uma sequeência.

    slice(início, fim, passo)

    

'''

# Criando um objeto de fatia para extrair os elementos de índice 1 a 4 (não inclusivo)
s = slice(1, 4)
seq = ['a', 'b', 'c', 'd', 'e', 'f']
print(seq[s])  # Saída: ['b', 'c', 'd']

# Criando um objeto de fatia para extrair todos os elementos a partir do índice 2
s = slice(2, None)
seq = ['a', 'b', 'c', 'd', 'e', 'f']
print(seq[s])  # Saída: ['c', 'd', 'e', 'f']

# Criando um objeto de fatia para extrair elementos de índices pares
s = slice(None, None, 2)
seq = ['a', 'b', 'c', 'd', 'e', 'f']
print(seq[s])  # Saída: ['a', 'c', 'e']


seq = ['a', 'b', 'c', 'd', 'e', 'f']
s = slice(1, 4)
print(seq[s])  # Saída: ['b', 'c', 'd']
