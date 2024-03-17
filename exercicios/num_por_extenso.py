
# Cont será a variável que armazenará a tupla 
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

# Criação de um loop infinito
while True:
    num = int(input('Digite um número entre 0 e 20: ')) # A variável 'num' solicita ao usuário o número que será mostrado por extenso
    if 0 <= num <= 20: # Condição de parada que quebrará o loop delimitando a condição do número ser aceito apenas se estiver entre 0 e 20 
        break
print(f'O número digitado foi o {cont[num]}')
