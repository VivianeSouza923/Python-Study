# Faça um programa que solicite dois números ao usuário, realize as quatro operações básicas (adição, subtração, multiplicação e divisão) e imprima os resultados.


numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

adicao = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

print(f'A adição dos números digitados resulta em: {adicao}')
print(f'A subtração dos números digitados resulta em: {subtracao}')
print(f'A multiplicação dos números digitados resulta em: {multiplicacao}')
print(f'A divisão dos números digitados resulta em: {divisao}')

