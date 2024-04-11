'''
Leia dois números inteiros e informe qual deles é o maior. Se os números forem iguais,
mostrar esta informação na tela
'''
print('Digite o primeiro número: ')
numero1 = int(input())
print('Digite o segundo número: ')
numero2 = int(input())

if numero1 > numero2:
    print(numero1, ' é maior que ', numero2)
elif numero2 > numero1:
    print(numero2, ' é maior que', numero1)
else:
    print('Os números são iguais')