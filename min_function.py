'''
    A função min() é o contrário da função max(), achar o valor mínimo de um objeto iterável.
    min(iterável, default=valor_padrao, key=função)


'''

numeros = [3, 7, 2, 8, 5]
menor_numero = min(numeros)
print(menor_numero)  # Saída: 2

letras = ['a', 'b', 'c', 'z']
menor_letra = min(letras)
print(menor_letra)  # Saída: 'a'


menor_valor = min(5, 10, 3, 8)
print(menor_valor)  # Saída: 3


pontuacoes = [("Alice", 85), ("Bob", 90), ("Charlie", 80)] # tupla - (x[0], x[1])
pior_aluno = min(pontuacoes, key=lambda x: x[1])
print(pior_aluno)  # Saída: ('Charlie', 80)
