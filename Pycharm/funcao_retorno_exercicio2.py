'''
Leia um número inteiro e informe e retorne se ele é positivo
    Função para ler o valor (não recebe parâmetro e retorna o valor lido)
    Função para positivo (recebe como parâmetro o valor lido e retorna verdadeiro se for
      positivo ou falso se for negativo)
'''
def leitura():
    print("Digite um número: ")
    return int(input())

def positivo(numero):
    if numero >= 0:
        return True
    else:
        return False

if __name__ == '__main__':
    numero = leitura()
    resultado = positivo(numero)
    if resultado == True:
        print(numero, ' é positivo!')
    else:
        print(numero, ' é negativo!')