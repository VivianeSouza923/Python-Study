# Crie um programa que solicite a altura e o peso do usuário, calcule o IMC e forneça uma classificação baseada nos valores obtidos.


altura = float(input('Qual a sua altura?'))
massa = float(input('Qual a sua massa?'))


imc = massa / pow(altura, 2)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 24.9:
    print('Você está com o peso normal.')
elif 25 <= imc <= 29:
    print('Você está com sobrepeso.')
elif 30 <= imc <= 34.9:
    print('Você está com obesidade classe I')
elif 35 <= imc <= 39.9:
    print('Você está com obesidade classe II')
elif imc >= 40:
    print('Você está com obesidade classe III')