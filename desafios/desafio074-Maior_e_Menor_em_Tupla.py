from random import randint
num1 = randint(0, 100)
num2 = randint(0, 100)
num3 = randint(0, 100)
num4 = randint(0, 100)
num5 = randint(0, 100)
numeros = (num1, num2, num3, num4, num5)
print(numeros)
maior = sorted(numeros)[0]
menor = sorted(numeros)[len(numeros)-1]
print(f'O maior número na tupla é {maior} e o menor número na tupla é {menor}.')