'''
    6. Contador de Palavras em uma Frase
        ◦ Peça ao usuário para inserir uma frase e conte o número de palavras na frase.
'''

frase = (input("Digite uma frase: "))

frase_lista = frase.split()

total = len(frase_lista)

print(total)

