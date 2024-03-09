'''
    5. Conversor de Celsius para Fahrenheit
        ◦ Crie um programa que converta uma temperatura em graus Celsius para Fahrenheit. A fórmula é: F = (C * 9/5) + 32.
'''

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicita ao usuário a entrada da temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura para Fahrenheit usando a função criada
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# Exibe o resultado
print(f"{temperatura_celsius} graus Celsius é equivalente a {temperatura_fahrenheit} graus Fahrenheit.")
