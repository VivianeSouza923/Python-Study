'''

    A função print é usada para imprimir mensagens no console/tela.

    print(valor1, valor2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    Como se pode ver, pode-se fornecer vários valores para imprimir na tela. Todos os parâmetros após os valores são opcionais.
    sep=' o que eu quero colocar como separadordos valores? O default é um espaço em branco'
    end='a string a sem impressa no final. O padrão é uma nova linha.'
    file=o objeto padrão onde a saída será enviada. POr padrão, é o sys.stdout, que é a saída padrão para o console.
    flush= um valor booleano indicando se a saída deve ser esvaziada imediatamente. O default é false.


'''

print("Olá, mundo!")
# Saída: Olá, mundo!

nome = "Alice"
idade = 25
print("Meu nome é", nome, "e tenho", idade, "anos.")
# Saída: Meu nome é Alice e tenho 25 anos.

print(1, 2, 3, sep='-', end='!')
# Saída: 1-2-3!

print("Vivi", "Alesi", sep='S2', end='*-*',flush=True)
