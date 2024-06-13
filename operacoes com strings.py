'''
        • Operações com Strings:
        ◦ Crie uma string com seu nome completo e exiba o primeiro e último nome.
        ◦ Crie um programa que pede ao usuário uma frase e conta quantas palavras ela possui.
        ◦ Crie um programa que verifica se uma frase contém uma palavra específica.

'''


nome_completo = 'Viviane Pinto de Souza'

pri_nome = nome_completo[0:7]
ult_nome = nome_completo[17:]
print(pri_nome)
print(ult_nome)

frase = 'Jesus te ama!'

print(frase.__contains__('te'))

print(frase.__contains__('alesi'))