'''
Leia as informações de um consórcio, tal como o número total de prestações,
a quantidade total de prestações pagas e o valor de cada prestação.
Calcule e mostre na tela o total pago pelo consorciado e o saldo devedor.
'''

print('Digite o numero total de prestações: ')
numero_total_prestacoes = float(input())
print('Digite a quantidade total de prestações pagas: ')
numero_prestacoes_pagas = float(input())
print('Digite o valor de cada prestação: ')
valor_prestacao = float(input())

total_pago = valor_prestacao * numero_prestacoes_pagas
saldo_devedor = valor_prestacao * (numero_total_prestacoes - numero_prestacoes_pagas)

print('Total pago: ', total_pago)
print('Saldo devedor: ', saldo_devedor)