# LISTAS EM PYTHON:

numeros_primos = [2, 3, 5, 7]

print(numeros_primos)


planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(planetas)


lista_de_listas = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
 	['g', 'h', 'i']
 	]


print(lista_de_listas)

coisas_variadas_que_gosto = ['louvar', 'LOTR', 7, help]

print(coisas_variadas_que_gosto)


print(planetas[0])
print(planetas[4])
print(planetas[-1])
print(planetas[-2])
print(planetas[-3])

# slicing

print(planetas[1:5])


# todos os planetas exceto o primeiro e o último:

print(planetas[1:-1])

# os 4 últimos planetas:

print(planetas[-4:])

# modificar listas. Quero tirar Earth e colocar Terra:

planetas[2] = 'Terra'

print(planetas)

planetas[3:] = ['a', 'b', 'c', 'd']

print(planetas)

# funções da lista:

# função len - dá o comprimento de uma lista:

print(len(planetas))

# função sorted -  retorna uma versão classificada da lista, em ordem alfabética

print(sorted(planetas))

# função sum - soma os valores da lista

print(sum(numeros_primos))

# função max - pega o máximo da lista, número máximo, maior palavra da ordem alfabética (neste caso, letra maiúscula é menor)

print(max(planetas))
print(max(numeros_primos))


# OBJETOS:

# IMAG EM PYTHON, SERVE PARA ACESSAR A PARTE IMAGINÁRIA DOS NÚMEROS COMPLEXOS

x = 6

# como x não tem parte imaginária, então esse print terá como saída 0
print(x.imag)

y = 6 - 8j

print(y.imag)


# OO em python - objetos que tem funções. Uma função anexada a um objeto é chamado de MÉTODO!!!

# MÉTODO BIT_LENGTH - O NOME É BEM SUGESTIVO 

# PARA ACESSAR MÉTODOS, É SÓ USAR A SÍNTAXE DOS PONTOS.

print(x.bit_length())

# não dá certo por ser imaginário? Isso, não é aplicado a números complexos, com parte imaginária.
	# print(y.bit_length())


# help para métodos:

help(x.bit_length)


#LIST METHODS - MÉTODOS DAS LISTAS:

# APPEND: adiciona item ao final da lista

numeros_primos.append(11)
print(numeros_primos)

help(numeros_primos.append)


# pop:  remove e retorna o último elemento de uma lista
print(numeros_primos.pop())

print(numeros_primos)

# searching list - listas de pesquisa:

# qual o index do elemnto 2 na lista numeros_primos?
print(numeros_primos.index(2))
# qual o index do elemnto 'Terra' na lista planetas?
print(planetas.index('Terra'))

#Para evitar surpresas desagradáveis, podemos usar o operador in para determinar se uma lista contém um valor específico:

print("Venus" in planetas)
print("Neptune" in planetas)

# nos dirá todos os métodos dessa lista
help(planetas)


# Tuplas: são quase a mesma coisa de listas, mas se difere na síntaxe: usa parênteses ao invés de colchetes. ALém disso, também não podem ser modificados, são imutáveis.

tupla_1 = (1, 2, 3, 4)
print(tupla_1)

# prova da segunda parte do comentário:

# tupla_1[0] = 5

z = 0.125

# razão inteira, a fração do número fracionário: as_integer_ratio()
print(z.as_integer_ratio())

help(z.as_integer_ratio())

# TROCAR DUAS VARIÁVEIS EM PYTHON?

a = 0
b = 1

a, b = b, a

print(a,b)