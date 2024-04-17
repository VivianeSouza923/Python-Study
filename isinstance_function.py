'''
    É usada para verificar se um objeto é uma instância de determina classe, ou de 
    uma tupla de classes.
    isinstance(objeto, classe_ou_tupla_de_classes)

'''

class Pessoa:
    pass

# subclasse de pessoa
class Estudante(Pessoa):
    pass

pessoa = Pessoa()
estudante = Estudante()

print(isinstance(pessoa, Pessoa))       # Saída: True
print(isinstance(estudante, Estudante)) # Saída: True
print(isinstance(estudante, Pessoa))    # Saída: True, pois Estudante é uma subclasse de Pessoa
print(isinstance(pessoa, Estudante))    # Saída: False, pois pessoa não é uma instância de Estudante
