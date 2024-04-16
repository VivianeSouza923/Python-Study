'''
    format(valor, formato)
    A função acima é usada para formatar valores: botar quantidade de casas decimais,
    notação científica em valores etc.
'''

# aqui vamos usar format para restringir o número float a duas casas decimais.
numero = 123.456789
texto_formatado = format(numero, ".2f")
print(texto_formatado)  # Saída: "123.46"

'''
    aqui eu quero usar o format para pegar esse número, dizer que o quero 5 dígitos 
    e que o que está faltando à esquerda seja preenchidos com zeros.
'''
numero = 42
texto_formatado = format(numero, "05d")
print(texto_formatado)  # Saída: "00042"

'''
    aqui eu estou usando o format para formatar como será imprimido o texto. ^ - será
    centalizado; 10 - largura total de 10 caracteres (espaços com a palavra); s - indica
    que o valor a ser formatado é uma string.
'''
texto = "Python"
texto_formatado = format(texto, "^10s")
print(texto_formatado)  # Saída: "  Python  "

# aqui eu tôo usando o format para dar aquela conhecida "notação de engenharia"
numero = 10000
texto_formatado = format(numero, ".2e")
print(texto_formatado)  # Saída: "1.00e+04"


