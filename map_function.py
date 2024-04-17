'''
    É utilizada para aplicar uma função a cada item do iterável(como uma lista, tupla
    etc.). O retorno dela é um objeto de mapa, que é um iterador os resultados dessas
    aplicações de funções.

    map(função, iterável1, iterável2, ...)
'''

numeros = [1, 2, 3, 4, 5]

def quadrado(x):
    return x ** 2

quadrados = map(quadrado, numeros)
print(list(quadrados))  # Saída: [1, 4, 9, 16, 25]
