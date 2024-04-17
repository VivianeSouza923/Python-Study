'''
    É usada para abrir arquivos em diferentes modos de operação, como leitura, escrita ou anexação. Ela retorna um objeto
    de arquivo que pode ser usado para ler ou gravar dados no arquivo. 

    open(nome_do_arquivo, modo, encoding=None)

'''
# aqui é só para ler esse arquivo. O "r" é de read
#arquivo = open("leia.txt", "r")
# aqui é para escrever nesse arquivo. o "w" é de write.
#arquivo = open("leia.txt", "w")

# aqui é para abrir o arquivo em modo binário para leitura.
#arquivo = open("leia.txt", "rb")
'''
    É uma boa prática usar a instrução with ao lidar com arquivos, pois isso garante que o arquivo seja fechado corretamente, 
    mesmo se ocorrerem exceções durante o processamento do arquivo.
'''
with open("leia.txt", "r") as arquivo:
   conteudo = arquivo.read()
   print(conteudo)



