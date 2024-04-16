'''
    A função dict() serve para criar dicionários. Ela pode ser chamada de várias
    maneiras diferentes.

'''
# se eu não passar um argumento para a função, ela retorna um dicionário vazio.
dicionario_vazio = dict()
print(dicionario_vazio)  # Saída: {}

# posso chamar escrevendo exatamente o dicionário (chave: valor).
#Daí a função faz só uma cópia.
# no caso abaixo, a chave é string, por isso as ''
dicionario_existente = {'a': 1, 'b': 2, 'c': 3}
copia_dicionario = dict(dicionario_existente)
print(copia_dicionario)  # Saída: {'a': 1, 'b': 2, 'c': 3}

# posso, ao invés de fazer uma cópia acima, só passar direto na função pares de chave-valor
# chave=valor 
dicionario = dict(a=1, b=2, c=3)
print(dicionario)  # Saída: {'a': 1, 'b': 2, 'c': 3}

# posso também criar o dicionário a partir de uma lista de tuplas.
# E ESSAS TUPLAS SÃO NADA MAIS DO QUE PAR CHAVE-VALOR
pares = [('a', 1), ('b', 2), ('c', 3)]
# aqui o dicionário será criado por iteração nessa lista de tuplas.
dicionario = dict(pares)
print(dicionario)  # Saída: {'a': 1, 'b': 2, 'c': 3}



