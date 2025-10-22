from time import sleep
def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f and p != 0 :
        for cont in range(i, (f - p), -p):
            print(f'{cont}', end=' -> ')
            sleep(0.5)
        print('FIM!')
    if (f > i and p != 0) or p < 0:
        for cont in range(i, (f + p), p):
            print(f'{cont}', end=' -> ')
            sleep(0.5)
        print('FIM!')
    if p == 0:
        if i > f:
            p = -1
        elif f > i:
            p = 1
        for cont in range(i, (f + p), p):
            print(f'{cont}', end=' -> ')
            sleep(0.5)
        print('FIM!')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input(f'Digite o início: '))
fim = int(input(f'Digite o fim: '))
pas = int(input(f'Digite o passo: '))
contador(ini, fim, pas)


