'''
    Usada para verificar se determinado objeto contém determinado atributo. Se tiver,
    o retorno da função é True.

    hasattr(objeto, nome_do_atributo)
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 30)

tem_nome = hasattr(pessoa, "nome")
print(tem_nome)  # Saída: True, porque o objeto pessoa tem o atributo "nome"

tem_altura = hasattr(pessoa, "altura")
print(tem_altura)  # Saída: False, porque o objeto pessoa não tem o atributo "altura"
