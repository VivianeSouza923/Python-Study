'''
        2. Média de Três Números:
        ◦ Faça um programa que peça três números ao usuário e imprima a média deles.
'''

# função que faz a média dos 3 números
def media_de_3(x, y, z):
    media_3 = (x + y + z)/3
    return media_3

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

media = media_de_3(num1, num2, num3)

print(f'A média dos 3 números digitados é {media}')


