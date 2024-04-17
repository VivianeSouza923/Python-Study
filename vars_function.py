'''
A função vars() é usada para retornar um dicionário de atributos de um objeto, incluindo atributos de instância e variáveis
locais. 

vars(objeto)


'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 30)


atributos = vars(pessoa)
print(atributos)  # Saída: {'nome': 'Alice', 'idade': 30} - o retoorno da função vars mapeia os noomes dos atributoos para os valores correspondentes.
