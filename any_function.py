# crio uma lista com alguns elementos
lista = [False, False, True, False]
'''
    a function any retorna True se pelo menos 1 item da lista for verdadeiro, ou
    seja, ela pode ser entendida como a porta or, lembra?
    Eu atribuo o resulta da lista em função de any à variável resultado.
    any(lista, tupla etc.) - True se pelo menos um elemento dessa lista, tupla etc.
    for verdadeiro.
'''
resultado = any(lista)

# visualizar o resultado de lista com a any.
if resultado:
    print("Pelo menos um elemento da lista é verdadeiro.")
else:
    print("Todos os elementos da lista são falsos.")
