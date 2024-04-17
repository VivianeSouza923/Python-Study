'''
    É usada para criar uma lista a partir de um iterável, como uma sequência (string,
    tupla, lista) ou um objeto que suporte iteração.
    list(iterável)

'''
# Convertendo uma string em uma lista de caracteres
string = "python"
lista_de_caracteres = list(string)
print(lista_de_caracteres)  # Saída: ['p', 'y', 't', 'h', 'o', 'n']

# Convertendo uma tupla em uma lista
tupla = (1, 2, 3)
lista = list(tupla)
print(lista)  # Saída: [1, 2, 3]

# Criando uma lista vazia
lista_vazia = list()
print(lista_vazia)  # Saída: []
