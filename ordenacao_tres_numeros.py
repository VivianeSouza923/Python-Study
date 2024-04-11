'''
        9. Ordenação de Três Números:
        ◦ Solicite três números ao usuário e imprima os números em ordem crescente.
'''

numero = int(input('Digite o primeiro número: '))
numero1 = int(input('Digite o segundo número: '))
numero2 = int(input('Digite o terceiro número: '))


lista_numeros = [numero, numero1, numero2]

print(sorted(lista_numeros))