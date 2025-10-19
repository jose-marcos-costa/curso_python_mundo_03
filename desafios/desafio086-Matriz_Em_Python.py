lista = [[],[],[]]
for i in range(0, 3):
    for j in range(0, 3):
        lista[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
# print(lista)
print('-=' * 40)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {lista[i][j]:^5} ]', end='')
    print()