# Exemplo com uma string contendo caracteres não ASCII
string = "Olá, mundo!"
'''
    A função ascii() pega a string acima e substitui o que não é caractere ASCII pela
    sua representação de escape unicode, como
    é o caso do a com acento agudo.

    Atribuo o resultado da função aplicada à variável string à variável ascii_string.
'''
ascii_string = ascii(string)

# visualizo o resultado:
print(ascii_string)
