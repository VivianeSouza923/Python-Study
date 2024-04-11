'''
Ler os valores de comprimento, largura e altura e apresentar o valor do volume de uma
caixa retangular. Utilize para o cálculo a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA
'''

print('Digite o valor do comprimento: ')
comprimento = float(input())
print('Digite o valor da largura: ')
largura = float(input())
print('Digite o valor da altura: ')
altura = float(input())

volume = comprimento * altura * largura

print('Volume: ', volume)