'''
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

    A função é usada para compilar código Python em objetos de código, que podem
    então ser executaddos pelo interpretador Python.

    É como se fosse uma compilação INDIRETA, saca? É basicamente isso.


'''

codigo_fonte = "print('Olá, mundo!')"
codigo_compilado = compile(codigo_fonte, "", "exec")
exec(codigo_compilado)
