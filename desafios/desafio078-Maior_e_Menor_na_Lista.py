valores = []
for i in range(0, 5):
    valores.append(int(input(f'Digite o {i+1}º valor: ')))
    if i == 0:
        maior = valores[0]
        pos_maior = 0
        menor = valores[0]
        pos_menor = 0
    if valores[i] > maior:
        maior = valores[i]
        pos_maior = i
    if valores[i] < menor:
        menor = valores[i]
        pos_menor = i
print(f'O menor valor é {menor} e está na {pos_menor+1}ª posição.')
print(f'O maior valor é {maior} e está na {pos_maior+1}ª posição.')