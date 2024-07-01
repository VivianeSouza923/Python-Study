# quantidade de litros de combustível gasto na viagem?
# faz 12km por L


tempo = float(input('Digite o tempo gasto na viagem: '))
velocidade = float(input('Digite a velocidade média: '))

print(f'O tempo gasto foi de {tempo} horas.')
print(f'A velocidade média durante a viagem foi de {velocidade}.')


distancia = tempo * velocidade

print(f'A distância percorrida na viagem foi de {distancia}')

litros_usados = distancia / 12

print(f'A quantidade de litros usados na viagem foi de {litros_usados}')