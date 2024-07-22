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
#frase_maiuscula = frase.upper() # a gente usa upper() para transformar em maiúsculo.
#print(frase.upper())
#print(frase_maiuscula)
#print(frase.lower()) # a gente usa o lower() para transformar as letras em minúsculo.
#print(len(frase)) # a gente usa o len(frase) para verificar o tamanho da frase
#frase = 'o amor é Jesus'
#print(frase.capitalize()) # bota em maiúsculo a primeira letra
#print(frase[:-1])  # remove o último caractere da frase. o -1 é o index do último caractere
#print(frase[::-1]) # o que diferencia é o passo aqui. assim imprime a frase invertida, de trás para frente.
# frase = 'Python is good'
# frase_atual = frase.replace('Python', 'Java') # usamos o replace para substituir uma palavra por outra - replace('antiga', 'nova')
# print(frase_atual)

frase = 'Deus é bom, maravilhoso e Sua bondade dura para todo o sempre' # frase normal, com as vogais
frase_sem_vogal = '' # vou criar uma variável do tipo string vazia
vogal = 'aeiouAEIOU' # uma variável contendo vogais
for letra in frase: # para cada letra dentro da frase normal
    if letra not in vogal: # eu vejo quem não é vogal
        frase_sem_vogal += letra # quem não é vogal é concatenada às outras dentro da variável que criei anteriormente
print(frase_sem_vogal) # e show

    


