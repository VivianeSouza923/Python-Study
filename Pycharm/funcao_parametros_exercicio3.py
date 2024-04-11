'''
Leia a idade do usuário e classifique-o em:
Criança – 0 a 12 anos
Adolescente – 13 a 17 anos
Adulto – acima de 18 anos (mostrar mensagem se o número for negativo)

    Função para ler a idade (recebe uma mensagem como parâmetro)
    Função para mostrar na tela a faixa etária, recebendo como parâmetro a idade da pessoa
'''
idade = 0

def leitura(msg):
    print(msg)
    global idade
    idade = int(input())

def faixa(id):
    if id >= 0 and id <= 12:
        print("Criança")
    elif id >= 13 and id <=17:
        print("Adolescente")
    elif id >= 18:
        print("Adulto")
    else:
        print("Idade inválida")

if __name__ == '__main__':
    leitura("Digite a idade do usuário: ")
    faixa(idade)












