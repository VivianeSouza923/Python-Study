'''
    3. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
'''


soma = 0


for i in range(3):
    numero = int(input('Digite um número: '))
    soma = numero + soma


print(f' A soma entre os números informados é: {soma}')
