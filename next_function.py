'''
    A função next() é usada para obter o próximo item do iterador. 

    next(iterador, padrão) - padrão(opcional) serve para ser retornado StopIteration (posso costumizar) se o iterador estiver 
    esgotado e não houver mais itens a serem recuperados.  

'''

lista = [1, 2, 3, 4, 5]
iterador = iter(lista)

print(next(iterador))  # Saída: 1
print(next(iterador))  # Saída: 2
print(next(iterador))  # Saída: 3


iterador = iter([])
print(next(iterador, 'Fim'))  # Saída: 'Fim'
