'''
    É usada para obter a representação literal(ou seja, exatamente como ela foi passada) de um objeto, que pode ser usada para 
    recriar o objeto usando a função eval().
    Inclusive, a repr() é a inversa da eval().

    repr(objeto)



'''

texto = "Olá, mundo!"
representacao = repr(texto)
print(representacao)  # Saída: 'Olá, mundo!'

numero = 42
representacao = repr(numero)
print(representacao)  # Saída: '42'

lista = [1, 2, 3]
representacao = repr(lista)
print(representacao)  # Saída: '[1, 2, 3]'

texto = "Olá, mundo!"
representacao = repr(texto)
novo_texto = eval(representacao)
print(novo_texto)  # Saída: Olá, mundo!

