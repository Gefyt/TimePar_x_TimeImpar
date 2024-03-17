resultado = 0

valor1 = int(input('Digite o primeiro número: '))
operacao = str(input('Digite a operação que deseja: '))
valor2 = int(input('Digite outro número: '))

if operacao == '+':
    resultado = valor1 + valor2
elif operacao == '-':
    resultado = valor1 - valor2
elif operacao == '*':
    resultado = valor1 * valor2
elif operacao == '/':
    resultado = valor1 / valor2
else:
    print('Operação invalida')

print(f'{valor1} {operacao} {valor2}', '=', resultado)