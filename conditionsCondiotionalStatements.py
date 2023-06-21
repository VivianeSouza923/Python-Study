# condições e declarações condicionais

# conditions

# 2 é maior que 3? ao colocar essa condição dentro do print, a saída é bool (V ou F, né)
print(2>3) #false


var_one = 1
var_two = 2

# mais condições

print(var_one < 1) #false
print(var_two >= var_one) #true

""" 
    == equals
    != does not equals
    < less than
    <= less than or equal to
    > greater than
    >= greater than or equal to


"""

# conditional statements


# definindo função, que recebe temp como parÂmetro.

def evaluate_temp(temp):

    # seta uma mensagem inicial
    message =  "Normal Temperature."

    # se a minha temperatura for maior que 38, eu vou colocar uma nova mensagem dentro da minha variável message
    if temp > 38:
        message = "fever!"

    # retorno a mensagem, claro.
    return message


print(evaluate_temp(37))
print(evaluate_temp(50))

# if ... else

# criar a função, ela recebe como parâmetro a temperatura (temp)
def evaluate_temp_with_else(temp):
    # se a temperatura for maior que 38, minha variável message recebe uma mensagem
    if temp > 38:
        message = "Fever!"

    # se não for, ela recebe outra.
    else:
        message = "Normal Temperature."

    # retorna message
    return message


print(evaluate_temp_with_else(37))
print(evaluate_temp_with_else(50))



# if... elif... else

# criada a função
def evaluate_temp_with_elif(temp):
    # vou fazer o primeiro teste
    if temp > 38:
        message = "Fever!"
    # não passou, desce pra cá. isso que aqui nada mais é do que um else-if juntos, tipo isso, entende?
    elif temp > 35:
        message = "Normal temperature."
    # finalmente o estágio final
    else:
        message = "Low temperature."
    return message


print(evaluate_temp_with_elif(37))
print(evaluate_temp_with_elif(50))
print(evaluate_temp_with_elif(33))


# more examples

def get_taxes(earnings):

    if earnings < 12000:
        tax_owed = .25 * earnings

    else:
        tax_owed = .30 * earnings
    

    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)


def get_dose(weight):

    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    
    else:

        dose = 10

    return dose


print(get_dose(12))
print(get_dose(3))
print(get_dose(35))
print(get_dose(19))
