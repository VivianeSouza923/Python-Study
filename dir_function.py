'''
    A função dir() serve para listar métodos e nomes de atributos de um determinado
    objeto.

    Ela retorna uma lista de strings. 
'''

objeto = "Olá, mundo!"

# aplico a função no objeto e atribuo o resulto à variável de nome lista_atributos
#passando o parâmetro, eu só vejo as coisas desse parâmetro.
lista_atributos = dir(objeto)
#visualizando resultado.
print(lista_atributos)

# se eu não passar parâmetro para dir, eu verei todas as coisas de tudo que está no escopo desse código
lista_atributos = dir()
print(lista_atributos)

