'''
Ler os valores de comprimento, largura e altura e apresentar o valor do volume de uma
caixa retangular. Utilize para o cálculo a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA
    Função para ler os valores (não recebe parâmetro)
    Função para efetuar o cálculo do volume, recebendo como parâmetro o comprimento,
        a largura e altura
    Função para apresentar o resultado (recebe o resultado)
'''
comprimento = 0.0
largura = 0.0
altura = 0.0
volume = 0.0

def leitura():
    print("Digite o comprimento: ")
    global comprimento
    comprimento = float(input())
    print("Digite a largura: ")
    global largura
    largura = float(input())
    print("Digite a altura: ")
    global altura
    altura = float(input())

def calcula_volume(c, l, a):
    global volume
    volume = c * l * a

def resultado(v):
    print("Volume: ", v)

if __name__ == '__main__':
    leitura()
    calcula_volume(comprimento, largura, altura)
    resultado(volume)

















