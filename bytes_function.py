# Criando um objeto bytes a partir de uma lista de inteiros
lista = [65, 66, 67]

'''
    É semelhante à bytearray, mas com uma diferença: Ao invés de criar uma array de
    bytes mutáveis, ela cria uma array de bytes imutável (não mutável).
'''
byte_objeto = bytes(lista)
byte_nome = bytes("Vitória Pinto de Souza", "utf-8")
print(byte_objeto)
print(byte_nome)