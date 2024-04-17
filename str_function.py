'''
    A função str() é usada para criar uma representação em string de um objeto.

    str(objeto)

'''

numero = 42
string_numero = str(numero)
print(string_numero)  # Saída: '42'
print(type(string_numero))

lista = [1, 2, 3]
string_lista = str(lista)
print(string_lista)  # Saída: '[1, 2, 3]'

tupla = (4, 5, 6)
string_tupla = str(tupla)
print(string_tupla)  # Saída: '(4, 5, 6)'

dicionario = {'a': 1, 'b': 2}
string_dicionario = str(dicionario)
print(string_dicionario)  # Saída: "{'a': 1, 'b': 2}"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

pessoa = Pessoa("Alice", 30)
string_pessoa = str(pessoa)
print(string_pessoa)  # Saída: 'Nome: Alice, Idade: 30'
