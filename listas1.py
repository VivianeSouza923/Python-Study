'''

6. Listas:
    • Crie uma lista chamada frutas com os nomes de 5 frutas.
    • Imprima a primeira fruta da lista.
    • Imprima a última fruta da lista.
    • Imprima o tamanho da lista.
    • Adicione uma nova fruta à lista.
    • Remova a primeira fruta da lista.
    • Imprima a lista invertida.
    • Crie uma nova lista com as frutas da lista frutas em ordem alfabética.


'''

frutas = ['banana', 'maçã', 'limão', 'mamão', 'laranja']
# print(frutas[0]) # primeira fruta da lista
# imprima a última fruta da lista:
#print(frutas[-1])
# imprima o tamanho da lista:
# print(len(frutas))
# adicione uma nova fruta à lista:
frutas.append('morango')
#print(frutas)
# remova a primeira fruta da lista:
frutas.remove(frutas[0])
#print(frutas)
# imprima a lista invertida
print(frutas[::-1])

lista_ordem = frutas
lista_ordem.sort() # colocar a lista em ordem alfabética.
print(lista_ordem)