'''
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um
automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo
gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
    Função para ler os valores (recebe como parâmetro uma mensagem para ser exibida e retorna
        o valor lido)
    Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna
      a distância)
    Função para calcular a quantidade de litros (recebe como parâmetro a distância e
      retorna os litros)
    Função para apresentar o resultado (recebe como parâmetro os valores e mostrar a mensagem –
      não possui retorno)
'''
def leitura(mensagem):
    print(mensagem)
    return float(input())

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_litros(distancia):
    return distancia / 12

def resultado(t, v, d, l):
    print("Tempo: ", t)
    print("Velocidade: ", v)
    print("Distância: ", d)
    print("Litros: ", l)

if __name__ == '__main__':
    tempo = leitura("Digite o tempo gasto na viagem: ")
    velocidade = leitura("Digite a velocidade média: ")
    distancia = calcula_distancia(tempo, velocidade)
    litros = calcula_litros(distancia)
    resultado(tempo, velocidade, distancia, litros)

















