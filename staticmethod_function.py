'''

É uma função embutidda em Pyhton que retorna um método estático para uma função ou método definido em uma classe.

Em Pyhton, um método estático é um método que pertence à classe, mas não recebe uma referÊncia implícita para a instância da 
classe (ou seja, ele não recebe self). Portantoo ele pode ser chamado diretamente da classe, sem precisar criar uma instância
da classe.

class MinhaClasse:
    @staticmethod
    def meu_metodo_estatico():
        # código do método estático
        pass
A sintaxe básica para usar é como um decorador.
'''

class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b
    
resultado = Calculadora.soma(3, 4)
print(resultado)  # Saída: 7

class MinhaClasse:
    valor = 10

    @staticmethod
    def metodo_estatico():
        return "Método estático"

    @classmethod
    def metodo_de_classe(cls):
        return f"Método de classe. Valor: {cls.valor}"

# Chamando os métodos diretamente da classe
print(MinhaClasse.metodo_estatico())  # Saída: Método estático
print(MinhaClasse.metodo_de_classe())  # Saída: Método de classe. Valor: 10


