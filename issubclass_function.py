'''
    É usada para verificar se uma classe é subclasse de outra (superclass).

    issubclass(classe, superclasse)

    Retorno True para verdadeiro. False para o contrário.

'''

# superclass
class Animal:
    pass
#subclass de Animal, tanto é que ela recebe como parÂmetro a superclass
class Mamifero(Animal):
    pass
# subclass de Mamífero, tanto é que ela recebe como parÂmetro a classe Mamífero
class Cachorro(Mamifero):
    pass

print(issubclass(Mamifero, Animal))  # Saída: True
print(issubclass(Cachorro, Mamifero)) # Saída: True
print(issubclass(Cachorro, Animal))  # Saída: True, pois Cachorro é uma subclasse de Mamifero que, por sua vez, é uma subclasse de Animal
print(issubclass(Animal, Cachorro))  # Saída: False, pois Animal não é uma subclasse de Cachorro
