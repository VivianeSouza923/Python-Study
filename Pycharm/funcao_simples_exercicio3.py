'''
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um
automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto
na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância
percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta
calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula:
LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
    Função para ler os valores
    Função para calcular a distância
    Função para calcular a quantidade de litros
    Função para apresentar o resultado
'''
tempo = 0
velocidade = 0
distancia = 0
litros = 0

def leitura():
    print("Digite o tempo da viagem: ")
    global tempo
    tempo = int(input())
    print("Digite a velocidade média: ")
    global velocidade
    velocidade = float(input())

def calcula_distancia():
    global distancia
    distancia = tempo * velocidade

def calcula_litros():
    global litros
    litros = distancia / 12

def resultado():
    print("Tempo: ", tempo)
    print("Velocidade: ", velocidade)
    print("Distância: ", distancia)
    print("Litros: ", litros)

if __name__ == '__main__':
    leitura()
    calcula_distancia()
    calcula_litros()
    resultado()
















