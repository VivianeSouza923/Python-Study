# crio a minha classe
class MinhaClasse:
    contador = 0
    # decorando o método:
    @classmethod 
    def incrementar_contador(cls):
        '''
        Ao decorar o método, eu não preciso instanciar, criar um objetoo quando for 
        chamá-lo

        cls está se referindo à classe.
        '''
        cls.contador += 1

# Chamando o método de classe
MinhaClasse.incrementar_contador()
print(MinhaClasse.contador)  # Saída: 1
