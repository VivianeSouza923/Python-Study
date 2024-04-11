'''
(Acumulador) Apresentar o total da soma obtida dos cem primeiros números inteiros
(1+2+3+4+5+6+7+...+97+98+99+100)
'''
contador = 1
soma = 0
while contador <= 100:
    soma = soma + contador
    #print(contador)
    contador += 1

print('Somatório dos 100 primeiros números: ', soma)

