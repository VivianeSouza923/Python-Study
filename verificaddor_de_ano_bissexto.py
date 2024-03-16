'''

    8. Verificador de Ano Bissexto
        ◦ Peça ao usuário para inserir um ano e determine se é bissexto.
'''




def ano_bissexto(ano):
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
ano = int(input("Insira o ano: "))
if ano_bissexto(ano):
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')

 
