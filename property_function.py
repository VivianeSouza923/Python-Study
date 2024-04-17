'''

    A função Property() é usada para criar uma propriedade em uma classe. Propriedades são atributos de classes especiais que
    possuem métodos especiais chamados getters, setters e deleters, permitindo um controle mais refinado sobre o acesso, a atri-
    buição e a deletação de valores de atributos.

    property(fget=None, fset=None, fdel=None, doc=None) - todos esses parâmetros são opcionais.
    fget - função que será chamada quando o valor da propriedade for acessado;
    fset - função que será chamada quando o valor da propriedade for atribuído;
    fdel - função que será chamada quando o valor da propriedade for excluído;
    doc - string de documentação para a propriedade.


'''


class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo protegido

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def del_nome(self):
        del self._nome

    nome = property(get_nome, set_nome, del_nome, "Propriedade 'nome'")
    
# usando a sintaxe de decorador. 
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo protegido

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @nome.deleter
    def nome(self):
        del self._nome

