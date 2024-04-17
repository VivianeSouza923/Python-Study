'''
    A função input() é usada para receber entradas do usuário através do teclado. Ela
    permite que o programa pare de executar temporariamente e aguarde o usuário digitar
    algum informação, que é então lida como string.
    O input sempre é lido como string, então se eu quiser, ter como entrada um inteiro,
    eu tenho que botar esse input dentro de uma função int(). um float, dentro de uma
    função float().

'''

nome = input("Digite seu nome: ")
print("Olá,", nome)

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))

print(idade, altura)

