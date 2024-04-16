'''
    getattr(objeto, nome_do_atributo[, valor_padrao])
    É usada para obter o valor de atributo de um objeto, dado o nome do tributo como
    uma string. 

'''

class Pessoa:
    # método que tem o nome e idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
# instanciando, criando um objeto.
pessoa = Pessoa("Alice", 30)

# quero o nome de pessoa. Qual é? O getattr retorna isso pra mim
nome = getattr(pessoa, "nome")
print(nome)  # Saída: "Alice"

'''
    aqui vemos o emprego do terceiro parâmetro. Como não há altura no método, 
    ele retorna o valor que eu coloquei para o terceiro elemento, como se fosse default.
'''
altura = getattr(pessoa, "altura", 170)
print(altura)  # Saída: 170, pois "altura" não é um atributo de pessoa
