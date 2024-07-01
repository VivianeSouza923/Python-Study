#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:15:32 2024

@author: vivi
"""

total_prestacoes = float(input('Digite o número total de prestações: '))
prestacoes_pagas = int(input('Digite o total de prestações pagas: '))
valor_prestacao = float(input('Digite o valor de cada prestação: '))

total_pago = prestacoes_pagas * valor_prestacao
saldo_devedor = total_prestacoes * valor_prestacao - total_pago

print(f'O total pago pelo consorciado foi {total_pago} reais.')
print(f'O saldo devedor do consorciado é de {saldo_devedor} reais.')