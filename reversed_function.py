'''
    A função reversed() é usada para inverter a ordem dos elementos de um interável.
    reversed(iterável)


'''

# Revertendo uma lista
lista = [1, 2, 3, 4, 5]
lista_invertida = reversed(lista)
print(list(lista_invertida))  # Saída: [5, 4, 3, 2, 1]

# Revertendo uma string
texto = "Python"
texto_invertido = reversed(texto)
print(''.join(texto_invertido))  # Saída: "nohtyP"

# Revertendo um objeto de range
intervalo = range(5)
intervalo_invertido = reversed(intervalo)
print(list(intervalo_invertido)) # Saída: [4, 3, 2, 1, 0]
