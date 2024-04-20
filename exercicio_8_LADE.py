'''
    8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = K - 273.15,
sendo C a temperatura em Celsius e K a temperatura em Kelvin.

'''

t_K = float(input('Digite a temperatura em Kelvin:'))

t_C = t_K - 273.15

print(f'A temperatura apresentada em Kelvin é de {t_C} graus Celsius.')