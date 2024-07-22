'''

7. Dicionários:
    • Crie um dicionário chamado pessoa com as chaves "nome", "idade", "cidade" e "profissão". Atribua valores às chaves.
    • Imprima o nome da pessoa.
    • Imprima a idade da pessoa.
    • Imprima a cidade onde a pessoa mora.
    • Imprima a profissão da pessoa.
    • Adicione uma nova chave "hobby" ao dicionário.
    • Remova a chave "profissão" do dicionário.
    • Imprima o dicionário com as chaves e valores em ordem alfabética.

'''

pessoa = {
    
    'nome' : 'Viviane',
    'idade' : 28,
    'cidade' : 'Fortaleza',
    'profissão' : 'Cientista de Dados, Engenheira de dados e software'
    

}

# imprime o nome da pessoa:

print(pessoa['nome'])

# imprime a idade da pessoa:

print(pessoa['idade'])

#imprime a cidade onde a pessoa mora:

print(pessoa['cidade'])

# imprime a profissão da pessoa:

print(pessoa['profissão'])

# adiciona uma nova chave

pessoa['hobby'] = 'Sair para comer'

print(pessoa)

# remover uma chave

del pessoa['profissão']

print(pessoa)

# imprimir o dicionário em ordem alfabéica:

for chave, valor in sorted(pessoa.items()):
    print(f'{chave}: {valor}')