'''
    9. Ordenação de Lista
        ◦ Crie um programa que solicite ao usuário uma lista de números, ordene a lista em ordem crescente e imprima-a.
'''

lista = input("Digite sua lista de números: ")

lista_mesmo = lista.split()

# list comprehensions
lista_numeros = [int(item) for item in lista_mesmo]



lista_crescente = sorted(lista_numeros)


print(lista_crescente)  
