'''
    6. Contador de Vogais:
        ◦ Solicite uma palavra ao usuário e conte o número de vogais na palavra.

'''

palavra = input('Digite uma palavra: ')


vogais = [letra for letra in palavra if letra.lower() in 'aeiouAEIOU']

numero_vogais = len(vogais)



print(f'O número de vogais na palavra {palavra} é {numero_vogais}')