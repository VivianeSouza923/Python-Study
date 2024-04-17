'''

    A função object() retorna um novo objeto vazio. Ela é a classe base de todas as classes em Python, ou seja, é a verdadeira
    classe pai. Portanto, todas as classes em Python são subclasses diretas ou indiretas de object. Ela é default se você criar
    uma classe sem especificar explicitamente uma classe pai.

'''

class MinhaClasse:
    pass

print(issubclass(MinhaClasse, object))  # Saída: True


objeto = object()
print(objeto)  # Saída: <object object at 0x7f3c10b83670>
