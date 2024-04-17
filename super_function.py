'''
    A função super() em Pyhton é usadda para acessar métodos e atributos de uma classe pai (superclasse) em uma classe filha
    (subclasse).

    super([classe], [objeto]) - ambos os parâmetros são opcionais. 

'''

class Pai:
    def saudacao(self):
        return "Olá do Pai"

class Filho(Pai):
    def saudacao(self):
        return "Olá do Filho"


class Filho(Pai):
    def saudacao(self):
        return super().saudacao()  # Chama o método saudacao() da classe Pai

filho = Filho()
print(filho.saudacao())  # Saída: "Olá do Pai"
