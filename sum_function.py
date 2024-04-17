'''

    A função sum() é usada para calcular a soma dos valores de um iterável.
    sum(iterável, start=0) - o start é opcional e informa de onde a soma vai começar. Por exemplo, start=2 indica que eu vou
    somar 2 com o sum(iterável).

'''

lista = [1, 2, 3, 4, 5]
soma = sum(lista)
print(soma)  # Saída: 15

tupla = (6, 7, 8, 9, 10)
soma = sum(tupla)
print(soma)  # Saída: 40

conjunto = {11, 12, 13, 14, 15}
soma = sum(conjunto)
print(soma)  # Saída: 65

lista = [1, 2, 3, 4, 5]
soma = sum(lista, start=10)
print(soma)  # Saída: 25

