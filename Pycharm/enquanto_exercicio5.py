'''
(Usuário) Ler os valores de comprimento, largura e altura e apresentar o valor do volume
de uma caixa retangular. Utilize para o cálculo a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA.
Ao final do cálculo, perguntar ao usuário se deseja continuar o programa fazendo nova leitura
'''
continua = 's'
while continua == 's':
    print('Digite o comprimento: ')
    comprimento = float(input())
    print('Digite a largura: ')
    largura = float(input())
    print('Digite a altura: ')
    altura = float(input())

    volume = comprimento * largura * altura

    print('Volume: ', volume)

    print('Deseja ler mais valores (s/n)?')
    continua = input()
