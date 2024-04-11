valor1 = 0.0
valor2 = 0.0
soma = 0.0

def leitura():
    print("Digite o primeiro valor: ")
    global valor1
    valor1 = float(input())
    print("Digite o segundo valor: ")
    global valor2
    valor2 = float(input())

def somatorio(vl1, vl2):
    global soma
    soma = vl1 + vl2

def resultado(sm):
    print("Soma: ", sm)

if __name__ == '__main__':
    leitura()
    somatorio(valor1, valor2)
    resultado(soma)