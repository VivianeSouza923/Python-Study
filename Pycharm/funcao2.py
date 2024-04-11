valor1 = 0
valor2 = 0
soma = 0

def leitura():
    print("Digite o valor 1: ")
    global valor1
    valor1 = int(input())
    print("Digite o valor 2: ")
    global valor2
    valor2 = int(input())

def somatorio():
    global soma
    soma = valor1 + valor2

def resultado():
    print("Soma: ", soma)

if __name__ == '__main__':
    leitura()
    somatorio()
    resultado()