'''
Leia a idade do usuário e classifique-o em:
Criança – 0 a 12 anos
Adolescente – 13 a 17 anos
Adulto – acima de 18 anos (se o usuário digitar um número negativo, mostrar a mensagem que a idade
é inválida)
'''
print('Digite a idade do usuário: ')
idade = int(input())

if idade >= 0 and idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18:
    print('Adulto')
else:
    print('Idade inválida')

'''if idade >= 0 and idade <= 12:
    print('Criança')
if idade >= 13 and idade <= 17:
    print('Adolescente')
if idade >= 18:
    print('Adulto')
if idade < 0:
    print('Idade inválida')'''