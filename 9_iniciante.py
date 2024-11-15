'''
9. Funções:

Crie uma função que calcule a área de um retângulo.

Peça ao usuário para inserir a base e a altura do retângulo.

Chame a função e imprima a área calculada.
'''

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return print(f'A área de triângulo é: {area:.2f}')

base_tri = float(input('Digite a base do triangulo: '))
altura_tri = float(input('\nDigite a altura do triangulo: '))

area_triangulo(base_tri, altura_tri)