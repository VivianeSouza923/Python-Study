'''
    delattr(objeto, nome_do_atributo)
    A função acima é usada para excluir um atributo de um objeto ou um atributo
    de uma classe se o objeto for uma instância de uma classe (lembra de classmethod?)

'''

class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor
    

objeto = MinhaClasse(42)

print(objeto.valor)  
delattr(objeto, 'valor')
print(hasattr(objeto, 'valor'))  # Saída: False, porque o atributo 'valor' foi excluído

