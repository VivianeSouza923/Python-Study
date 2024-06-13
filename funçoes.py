'''
    Funções:
    • Criação e Chamada:
        ◦ Crie uma função que recebe dois números como parâmetro e retorna a soma deles.
        ◦ Crie uma função que converte uma temperatura de Celsius para Fahrenheit.
    • Parâmetros e Retorno:
        ◦ Crie uma função que recebe uma lista de números e retorna a média deles.
        ◦ Crie uma função que recebe uma lista de nomes e retorna o nome com mais caracteres.


'''

def soma(num, num1):
    return num + num1


print(soma(4, 9))

def C_for_F(celsius):
    Fah = (celsius * 9/5) + 32
    return Fah

print(C_for_F(10))

def lista(lista_de_numeros):
    cont = 0
    cont_div = 0
    for elemento in lista_de_numeros.copy():
        cont += elemento
        cont_div += 1
    media_num = cont/cont_div

    return media_num

print(lista([1, 2, 3]))


def nome_maior(lista_nomes):
    for elemento in lista_nomes.copy():
        len
    