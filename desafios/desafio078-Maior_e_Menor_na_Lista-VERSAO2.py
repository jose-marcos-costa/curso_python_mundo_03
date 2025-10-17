valores = []
pos_maior = []
pos_menor = []
for i in range(0, 5):
    valores.append(int(input(f'Digite o {i+1}º valor: ')))
print('=-'*30)
print(f'Você digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos,v in enumerate(valores):
    if maior == v:
        print(f'{pos+1}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos,v in enumerate(valores):
    if menor == v:
        print(f'{pos+1}...', end='')



