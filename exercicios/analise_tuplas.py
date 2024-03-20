from random import randint

contPar = 0
contImpar = 0
valores = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
           randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

print(f'Números sorteados: {valores}\n')

print('| Time par |\n')
for n in valores:
    if n % 2 == 0:
        contPar += n
        print(n, end='   ')
print(f'\no time par tem = {contPar} pontos')

print('\n-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

print('| Time impar |\n')
for n in valores:
    if n % 2 != 0:
        contImpar += n
        print(n, end= '   ')
print(f'\no time impar tem = {contImpar} pontos')
        
    
