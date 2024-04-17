'''
    A função retorna um objeto de visualização de memória, que fornece uma visualização semelhante a uma matriz de um objeto de
    sequência.

    memoryview(objeto)


'''
# Criando um objeto de bytes
dados = b'abcdefgh'

# Criando um objeto de visualização de memória
visualizacao = memoryview(dados)

# Acessando o conteúdo como se fosse uma matriz de bytes
for byte in visualizacao:
    print(byte)

# Saída: 97
#        98
#        99
#        100
#        101
#        102
#        103
#        104

# criando um objeto sem ser nada de bytes:
dados0 = [1, 2, 3]

dados0_byte = bytes(dados0)

# mas precisam ser convertidos para bytes
visualizacao0 = memoryview(dados0_byte)

for letra in visualizacao0:
    print(letra)