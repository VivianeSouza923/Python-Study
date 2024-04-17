'''
6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é:
F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
'''

temperatura_Celsius = float(input('Digite a temperatura em graus Celsius: '))

temperatura_Fahrenheit = temperatura_Celsius * (9.0/5.0) + 32.0

print(f'A temperatura informada em graus Celsius é {temperatura_Fahrenheit} em graus Fahrenheit')