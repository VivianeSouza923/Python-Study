'''

    É uma função usada para classificar os elementos de um iterável em crescente ou decrescente.

    sorted(iterável, *, key=None, reverse=False) - o * é só pra indicar que os argumentos seguintes (que são opcionais) devem 
    ter nomes.
    - key: é a função que será chamada em cada elemento do iterável para gerar uma chave de classificação.
    - reverse: é um valor booleano que indica se a ordem deve ser reversa, decrescente. O default é False.

'''

# Ordenando uma lista de números em ordem crescente
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Ordenando uma lista de strings em ordem decrescente
palavras = ['banana', 'maçã', 'laranja', 'abacaxi']
palavras_ordenadas = sorted(palavras, reverse=True)
print(palavras_ordenadas)  # Saída: ['maçã', 'laranja', 'banana', 'abacaxi']


tuplas = [(1, 'b'), (2, 'a'), (3, 'c')]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(tuplas_ordenadas)  # Saída: [(2, 'a'), (1, 'b'), (3, 'c')]

