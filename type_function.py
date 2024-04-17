'''

    A função type() é utilizada para obter o tipo do objeto.
    type(objeto)


'''

# Obtendo o tipo de uma variável
x = 5
tipo_x = type(x)
print(tipo_x)  # Saída: <class 'int'>

# Obtendo o tipo de uma lista
lista = [1, 2, 3]
tipo_lista = type(lista)
print(tipo_lista)  # Saída: <class 'list'>

# Obtendo o tipo de uma função
def minha_funcao():
    pass
tipo_funcao = type(minha_funcao)
print(tipo_funcao)  # Saída: <class 'function'>
