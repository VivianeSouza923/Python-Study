'''
    É usada para converter um valor para um número inteiro. Ela pode converter strings
    que representam números inteiros em números inteiros propriamente ditos.
    Óbvio que ela não pode converter um "olá" em número inteiro, por exemplo.

'''

numero_texto = "42"
numero_inteiro = int(numero_texto)
print(numero_inteiro)  # Saída: 42

numero_ponto_flutuante = 3.14
numero_inteiro = int(numero_ponto_flutuante)
print(numero_inteiro)  # Saída: 3
