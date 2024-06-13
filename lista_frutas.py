'''
    Listas e Strings:
    • Criação e Acesso:
        ◦ Crie uma lista de frutas e exiba cada fruta na tela.
        ◦ Acesse elementos específicos da lista por seu índice.

            • Modificação:
        ◦ Adicione uma nova fruta à lista.
        ◦ Remova uma fruta da lista.
        ◦ Modifique um elemento da lista.

'''

frutas = ['laranja', 'maçã', 'banana']
print(frutas[0])
print(frutas[1])
print(frutas[2])

frutas.append('uva')

print(frutas)

frutas.remove('maçã')

print(frutas)

frutas[1] = 'anana'

print(frutas)