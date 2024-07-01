'''

    5. Strings:
    • Crie uma variável chamada frase e atribua uma frase a ela.
    • Imprima a frase em maiúsculas.
    • Imprima a frase em minúsculas.
    • Imprima o tamanho da frase.
    • Imprima a frase com o primeiro caractere em maiúscula.
    • Imprima a frase com o último caractere removido.
    • Imprima a frase invertida.
    • Imprima a frase com a palavra "Python" substituída por "Java".
    • Imprima a frase com todas as vogais removidas.

'''

#frase = 'Deus é maravilhoso, justo e fiel.'
#frase_maiuscula = frase.upper()
#print(frase.upper())
#print(frase_maiuscula)
#print(frase.lower())
#print(len(frase))
#frase = 'o amor é Jesus'
#print(frase.capitalize()) # bota em maiúsculo a primeira letra
#print(frase[:-1])
#print(frase[::-1]) # o que diferencia é o passo aqui
# frase = 'Python is good'
# frase_atual = frase.replace('Python', 'Java')
# print(frase_atual)

frase = 'Deus é bom, maravilhoso e Sua bondade dura para todo o sempre'
for i in range(len(frase)):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        frase.replace('a', '')
    


