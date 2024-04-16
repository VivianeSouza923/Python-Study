# Exemplo 1: Conversão de valores numéricos
'''
 A função bool converte valores para booleano.

    a. Se o valor for zero, false, none, vazio(ou seja, não tem valor), será convertido
    para False.

    b. Se for qualquer valor que não seja os informados acima, será convertido para
    True.

'''
print(bool(0))     # False
print(bool(1))     # True
print(bool(-1))    # True
print(bool(0.0))   # False
print(bool(3.14))  # True

# Exemplo 2: Conversão de strings
print(bool(""))    # False
print(bool("Olá")) # True

# Exemplo 3: Conversão de listas
print(bool([]))    # False
print(bool([1, 2]))# True

# Exemplo 4: Conversão de None
print(bool(None))  # False
