'''
Crie um programa que leia três valores e calcule a média aritmética dos valores lidos
    Função para ler valores (recebe parâmetro e retorna o valor lido)
    Função para calcular a média (recebe como parâmetro os três valores e retorna o resultado)
    Função para mostrar o resultado (recebe como parâmetro o valor da média e imprime o
      valor, não retorna nada)
'''
def leitura(mensagem):
    print(mensagem)
    valor = int(input())
    return valor

def calcula_media(v1, v2, v3):
    return (v1 + v2 + v3) / 3

def resultado(media):
    print("Média: ", media)

if __name__ == '__main__':
    valor1 = leitura("Digite o primeiro valor: ")
    valor2 = leitura("Digite o segundo valor: ")
    valor3 = leitura("Digite o terceiro valor: ")
    media = calcula_media(valor1, valor2, valor3)
    resultado(media)