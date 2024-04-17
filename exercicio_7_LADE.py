'''
    7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é:
C = 5.0 * (F-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.

'''

t_F = float(input('Digite a temperatura em graus Fahrenheit:'))

t_C = 5.0 * (t_F-32.0)/9.0

print(f'A temperatura informada em graus Fahrenheit é {t_C}em graus Celsius.')