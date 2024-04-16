# Criando um objeto de bytearray a partir de uma string
byte_array = bytearray("Olá, mundo!", "utf-8")
'''
    a função bytearray() cria um objeto de array de bytes modificáveis. Na prática,
    só será afetados aqueles que não são caracteres ASCII, que precisam de mais de um 
    byte para serem representados.Os caracteres ASCII permanecem inalterados.

    No entanto, ainda sim a array é toda a string passada, mesmo que de diferente
    fique somente os caracteres não ASCII.
'''
print(byte_array)

# Modificando um elemento do objeto de bytearray
# observe: 
print(byte_array[0])
byte_array[0] = 72  # ASCII para 'H'
print(byte_array)

# Adicionando novos bytes ao objeto de bytearray
byte_array.extend(b" Python")
print(byte_array)
