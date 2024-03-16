'''
        10. Verificador de Palíndromo
        ◦ Faça um programa que verifique se uma palavra é um palíndromo (se pode ser lida da mesma forma da esquerda para a 
        direita e vice-versa).
'''

def verifica_palindromo(palavra):
    palavra = palavra.lower()  # Convertendo para minúsculas para evitar diferenciação de maiúsculas e minúsculas
    palavra_sem_espacos = ''.join(palavra.split())  # Removendo espaços para tratar frases como palíndromos
    inverso = palavra_sem_espacos[::-1]  # Invertendo a palavra

    if palavra_sem_espacos == inverso:
        return True
    else:
        return False


entrada = input("Digite uma palavra ou frase: ")

if verifica_palindromo(entrada):
    print(f'{entrada} é um palíndromo.')
else:
    print(f'{entrada} não é um palíndromo.')
