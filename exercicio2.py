num = int(input('Digite o primeiro número: '))
num1 = int(input('Digite o segundo número: '))


if num > num1:
    print(f'O número {num} é maior que o número {num1}')
elif num1 > num:
    print(f'O número {num1} é maior que o número {num}')
else:
    print('Os dois números são iguais.')

