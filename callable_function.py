'''
    A função callable serve para verificar se um objeto pode ser chamado como uma 
    função. Ela retornará True se o objeto for função, método, classe com UM MÉTODO
    '__call__' etc. Caso contrário, ela retornará False.
'''

def minha_funcao():
    print("Olá, mundo!")

class MinhaClasse:
    def __call__(self):
        print("Método __call__ chamado!")

objeto_funcao = minha_funcao
objeto_classe = MinhaClasse()

print(callable(objeto_funcao))  # Saída: True
print(callable(objeto_classe))   # Saída: True
print(callable("Olá"))           # Saída: False
