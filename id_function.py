'''
    A função id() retorna o identificador único do objeto. Este identificador é um
    número inteiro único para cada objeto durante sua vida útil. é útil para verificar 
    se duas variáveis se referem ao mesmo objeto. Se o id de duas variáveis é o mesmo, 
    elas apontam para o mesmo objeto na memória. 

'''

x = 42
print(id(x))  # Saída: algum número único que identifica o objeto 42

lista1 = []
lista2 = []
print(id(lista1))  # Saída: algum número único que identifica a lista1
print(id(lista2))  # Saída: algum número único que identifica a lista2

a = [1, 2, 3]
b = a
print(id(a))  # Saída: algum número único que identifica a lista a
print(id(b))  # Saída: o mesmo número único que identifica a lista b, pois b aponta para o mesmo objeto que a

