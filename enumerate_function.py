'''
    enumerate(iterável, start=0) -> primeiro parâmetro é a sequência que eu quero
    enumerar e o segundo parÂmetro é opcional (passa de onde começa o índice)
    A função enumerate() é usada para iterar sobre uma sequência, ao mesmo tempo
    em que rastreia o índice de cada elemento da sequência. 

    O retorno dela é um objeto enumerado que produz tuplas contendo um contador
    (o índice) e o valor correpondente a cada elemento na sequência.

'''
# crio a minha lista para iterar com enumerate
frutas = ['maçã', 'banana', 'laranja']

# indice e fruta será a minha tupla, digamos assim.
# como pode se ver, estou iterando a lista frutas e vai começar com índice 6
for indice, fruta in enumerate(frutas, start=6):
    # vou printar 
    print(f'Índice: {indice}, Fruta: {fruta}')
