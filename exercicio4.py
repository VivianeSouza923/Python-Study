num = float(input('Digite o primeiro número: '))
num1 = float(input('Digite o segundo número: '))

operacao = input('Digite a operação matemática desejada: ')

if operacao == '+':
	soma = num + num1
	print(f'{num} + {num1} = {soma}')
elif operacao == '-':
	sub = num - num1
	print(f'{num} - {num1} = {sub}')
elif operacao == '*':
	mul = num * num1
	print(f'{num} * {num1} = {mul}')
elif operacao == '/':
	div = num / num1
	print(f'{num} / {num1} = {div}')
else: 
	print('A operação digitada é inválida.')