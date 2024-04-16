# crio uma lista com alguns elementos
lista = [True, True, True, False]
'''
    o all vai pegar o resultado de todos os elementos da lista e vai retornar True
    se todos os elementos da lista forem avaliados como verdadeiros, ou seja,
    diferentes zeros, vazios, false ou none.
    Neste caso, eu estou atribuindo esse resultado à variável none. 
    A função all recebe como parâmetro o que eu quero avaliar (lista, tupla etc.)
    
'''
resultado = all(lista)

# agora a gente visualiza o resultado de all.
if resultado:
    print("Todos os elementos da lista são verdadeiros.")
else:
    print("Pelo menos um elemento da lista é falso.")
