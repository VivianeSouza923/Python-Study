'''
    globals() retorna um dicionário representando o namespace global atual. Esse dicioná-
    rio contém todos os nomes de variáveis globais e seus respectivos valores no momento
    em que a função é chamada.
'''

def minha_funcao():
    x = 10
    print(globals())

minha_funcao()
