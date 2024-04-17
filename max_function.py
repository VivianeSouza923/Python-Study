'''
    A função max() é usada para encontrar o maior valor em um objeto iterável ou para
    comparar dois ou mais números etc.
    max(iterável, default=valor_padrao, key=função) - Tanto o default, quanto o key
    são opcionais. O default é o valor que será retornado caso o iterável seja vazio.
    Já o key é uma função que será aplicada a cada elemento do iterável para gerar a
    chave de comparação.
'''

numeros = [3, 7, 2, 8, 5]
maior_numero = max(numeros)
print(maior_numero)  # Saída: 8

letras = ['a', 'b', 'c', 'z']
maior_letra = max(letras)
print(maior_letra)  # Saída: 'z'


maior_valor = max(5, 10, 3, 8)
print(maior_valor)  # Saída: 10

pontuacoes = [("Alice", 85), ("Bob", 90), ("Charlie", 80)]
melhor_aluno = max(pontuacoes, key=lambda x: x[1])
print(melhor_aluno)  # Saída: ('Bob', 90)
