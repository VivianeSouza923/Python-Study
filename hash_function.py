'''
    hash(objeto)
    A função é usada para retornar o valor de hash do objeto. O valor de hash é um nú-
    mero inteiro que representa de forma única o conteúdo do objeto.

'''

numero = 42
valor_hash = hash(numero)
print(valor_hash)  # Saída: 42

texto = "Python"
valor_hash = hash(texto)
print(valor_hash)  # Saída: 1566053057 (o valor pode variar em diferentes execuções)


nome = 'Viviane'
valor_hash = hash(nome)
print(valor_hash)

nome0 = 'Alesi'
valor_hash = hash(nome0)
print(valor_hash)