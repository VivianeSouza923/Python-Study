'''
    A função complex() cria um número complexo. 

'''

'''
    posso criar um número complexo, só atribuindo a função sem nenhum parâmetro 
    a uma variável, mas daí o número complexo será nulo, ou seja, 0 + 0j
'''
numero_complexo = complex()
print(numero_complexo)  # Saída: 0j

# posso passar um parâmetro, mas ai ele vai ser considerado o real, ou seja, 2 + 0j
numero_complexo = complex(2)
print(numero_complexo)  

# posso passar dois parâmetros, daí o primeiro será o real e o segundo o imaginário
numero_complexo = complex(3, 4)
print(numero_complexo)  # Saída: (3+4j)

# também posso passar o número complexo por string, pois a função também pode receber string
numero_complexo = complex("2+3j")
print(numero_complexo)  # Saída: (2+3j)


