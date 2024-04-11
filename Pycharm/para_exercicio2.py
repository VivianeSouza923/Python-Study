'''
(Acumulador) Apresentar o total da soma obtida dos cem primeiros números inteiros
(1+2+3+4+5+6+7+...+97+98+99+100)
'''
soma = 0
for contador in range(1, 101):
    soma += contador
print('Soma dos 100 primeiros números inteiros', soma)