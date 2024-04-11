'''
(Contador) Escrever um algoritmo que lê 5 valores para a variável A, um de cada vez,
e contar quantos destes valores são negativos. Após a leitura, o programa deve mostrar
a quantidade de números negativos
'''
contador = 1
negativos = 0
while contador <= 5:
    print('Digite um valor: ')
    a = float(input())
    if a < 0:
        negativos += 1
    contador += 1

print('Quantidade de números negativos: ', negativos)