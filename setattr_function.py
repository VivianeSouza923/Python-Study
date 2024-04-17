'''
    É usada para definir o valor de um atributo de um objeto. Ela permite fazer essa atribuição, mesmo se o nome do atributo
    for determinado dinamicamente em tempo de execução.

    setattr(objeto, nome_do_atributo, valor)


'''

class Pessoa:
    pass

#instanciei
pessoa = Pessoa()

# Definindo o atributo 'nome' com o valor 'Alice'
setattr(pessoa, 'nome', 'Alice')

print(pessoa.nome)  # Saída: Alice
