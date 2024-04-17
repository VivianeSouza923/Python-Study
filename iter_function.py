'''
    A função iter() retorna um iterador para um objeto específico. 
    iter(objeto[, sentinel]) - sentinel é um valor especial (opcional) que define o
    critério de parada para a iteração. Caso esse valor seja fornecido, o objeto deve
    ser uma função. A iteração termina quando a função retornar o valor sentinel

'''
minha_lista = [1, 2, 3, 4, 5]
meu_iterador = iter(minha_lista)

print(next(meu_iterador))  # Saída: 1
print(next(meu_iterador))  # Saída: 2
print(next(meu_iterador))  # Saída: 3
print(meu_iterador)


