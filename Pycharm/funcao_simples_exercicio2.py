'''
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a
temperatura em graus Celsius
    Função para ler os valores
    Função para fazer o cálculo
    Função para mostrar o resultado
'''
C = 0
F = 0

def leitura():
    print("Digite a temperatura em graus Celsius: ")
    global C
    C = float(input())

def conversao():
    global F
    F = (9 * C + 160) / 5

def resultado():
    print("Temperatura em F: ", F)

if __name__ == '__main__':
    leitura()
    conversao()
    resultado()