'''
Leia um número inteiro e informe se ele é positivo ou negativo
    Função para ler o número inteiro (recebe uma mensagem)
    Função para apresentar se é positivo ou negativo, recebendo como parâmetro o número lido
'''
numero = 0

def leitura(msg):
    global numero
    print(msg)
    numero = int(input())

def positivo(num):
    if num <= 0:
        print("Negativo")
    else:
        print("Positivo")

if __name__ == '__main__':
    leitura("Digite o número: ")
    positivo(numero)
    leitura("Digite um número para saber se é positivo ou negativo: ")
    positivo(numero)