def leitura(mensagem):
    print(mensagem)
    valor = float(input())
    return valor

def somatorio(vl1, vl2):
    return vl1 + vl2

def resultado(soma):
    print("Soma: ", soma)

if __name__ == '__main__':
    valor1 = leitura("Digite o primeiro valor: ")
    valor2 = leitura("Digite o segundo valor: ")
    soma = somatorio(valor1, valor2)
    resultado(soma)