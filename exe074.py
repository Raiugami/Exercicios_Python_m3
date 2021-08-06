from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(sorted(numeros))
print(f'O maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)} ')
