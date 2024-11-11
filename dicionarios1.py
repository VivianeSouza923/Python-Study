'''
    2. Dicionários:
        ◦ Crie um dicionário que representa um carrinho de compras. Cada chave deve ser o nome do produto e o valor deve ser a 
        quantidade. Implemente as funções adicionar_item, remover_item, calcular_total, e imprimir_carrinho.
        ◦ Crie uma função que recebe um dicionário e retorna um novo dicionário com as chaves e valores invertidos.
        ◦ Crie uma função que recebe um dicionário e retorna uma lista com os valores em ordem crescente.


'''
# criação do dicionário com suas devidas chaves e seus devidos valores
carrinho_compras = {
    'Arroz' : 3,
    'Feijão' : 1,
    'Macarrão' : 7,
    'Café' : 2

}

def adicionar_item(chave, novo_item): # CRIAÇÃO DA FUNÇÃO QUE VAI ACRESCENTAR UM ITEM AO DICIONÁRIO
    carrinho_compras[chave] = novo_item # adicionamos o noto item assim, CRIANDO UMA COLUNA
    return carrinho_compras # retorna o novo carrinho de compras
    
    

adicionar_item('Acúcar', 6) # adiciona açúcar
print(carrinho_compras)


def remover_item(chave): # função que vai remover o item que quero (aqui só preciso da chave mesmo)
    del carrinho_compras[chave] # só deleta a coluna com o del
    return carrinho_compras # retorna o carrinho de compras atualizado

remover_item('Café') # remove café
print(carrinho_compras) 

def calcular_total(valores): # função para calcular o montante das coisas 

    valores = carrinho_compras.values() # pego somente os valores com a values(), as chaves n vem
    valores_lista = list(valores) # transformo em lista esse conjunto de valores
    soma_valores = sum(valores_lista)  # faço a soma dos itens dessa lista
    print(soma_valores)
   


calcular_total(carrinho_compras) # imprime o montante total do carrinho de compras

def calcular_total(dicio): # segunda forma
    val = 0
    for valor in dicio.values():
        val += valor 
    print(val)

calcular_total(carrinho_compras)

def imprimir_carrinho(dicio):
    print(f'Imprimir carrinho: {dicio}')

imprimir_carrinho(carrinho_compras)


def inverte_dicionario(dicio):
    dicio_invertido = dict(zip(dicio.values(), dicio.keys()))
    print(dicio_invertido)

inverte_dicionario(carrinho_compras)


def dicionario_listaOrdemCrescente(dicio):
    valores = dicio.values()
    lista = list(valores)
    print(sorted(lista))

dicionario_listaOrdemCrescente(carrinho_compras)