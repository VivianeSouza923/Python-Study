idade = int(input('Digite a sua idade: '))

if idade < 0:
    print('A idade digitada é inválida')
elif idade <= 12:
    print('É criança')
elif idade < 18:
    print('É adolescente')
else:
    print('É adulto')
    