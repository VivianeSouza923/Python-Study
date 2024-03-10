'''
        1. Soma de Dois Números:
        ◦ Crie um programa que solicite dois números ao usuário e imprima a soma deles.
'''




def soma(num1, num2):
    res = num1 + num2
    return res

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

res = soma(num1, num2)

print(f'A soma de {num1} e {num2} é {res}')