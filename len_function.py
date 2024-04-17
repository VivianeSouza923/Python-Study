'''

    É usada para obter o tamanho de um objeto (que pode ser uma sequência ou uma cole-
    ção).
    len(objeto)
'''

minha_lista = [1, 2, 3, 4, 5]
tamanho_lista = len(minha_lista)
print(tamanho_lista)  # Saída: 5

minha_string = "Olá, mundo!"
tamanho_string = len(minha_string)
print(tamanho_string)  # Saída: 11, pois há 11 caracteres na string

meu_dicionario = {"a": 1, "b": 2, "c": 3}
tamanho_dicionario = len(meu_dicionario)
print(tamanho_dicionario)  # Saída: 3, pois há 3 pares chave-valor no dicionário
