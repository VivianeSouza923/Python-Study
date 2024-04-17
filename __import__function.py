'''
É uma função embutida que é utilizada para importar módulos dinamicamente durante a execução do programa. É uma maneira mais 
flexível de importar móddulos, em comparação com a declaração 'import' padrão.

__import__(nome_do_módulo, globals=None, locals=None, fromlist=(), level=0)
com exceção do nome do módulo, toddos os parÂmetros são opcionais. 

'''

math_module = __import__('math')
print(math_module.sqrt(25))  # Saída: 5.0
