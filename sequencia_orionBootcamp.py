
num_termos = 6

sequencia = [1296, 4]
pulo = 6
pulo_unidade = 4


for i in range(2, num_termos):
    pulo = pulo + 2
    sequencia.append((pulo*pulo) ** 2)
    sequencia.append(pulo_unidade + 2)
    pulo_unidade = pulo_unidade + 2

print(sequencia)
