'''
    filter(funcao_de_filtro, iteravel)
    A função filter é usada para filtrar elementos de uma sequência usando uma função
    de filtro que retorna True ou False para cada elemento.

    ELa retorna um iterador, um objeto interável que produz apenas elementos para os 
    quais a função de filtro retorna True.


'''

# criei minha função de filtro. Aqui vemos que eu quero números pares.
def filtro_pares(numero):
    return numero % 2 == 0

# faço uma lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# depois faço a filtragem com a função filter() e armazeno o resultado na variável pares
pares = filter(filtro_pares, numeros)

for numero in pares:
    print(numero)
