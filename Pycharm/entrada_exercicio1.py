'''
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e
C é a temperatura em graus Celsius '''

print('Digite a temperatura em graus Celsius: ')
C = float(input())
#print(C)
#print(type(C))

F = (9 * C + 160) / 5

print('A temperatura em graus Fahrenheit é: ', F)