'''
        10. Calculadora de IMC (Índice de Massa Corporal):
        ◦ Peça o peso (em kg) e a altura (em metros) ao usuário e calcule o IMC usando a fórmula: IMC=altura2peso​.

'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / pow(altura, 2)

print(f'O seu IMC é: {imc}')