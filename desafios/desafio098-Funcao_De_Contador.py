from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim and passo != 0 :
        for i in range(inicio, (fim - passo), -passo):
            print(f'{i}', end=' -> ')
            sleep(0.5)
        print('FIM!')
    if (fim > inicio and passo != 0) or passo < 0:
        for i in range(inicio, (fim + passo), passo):
            print(f'{i}', end=' -> ')
            sleep(0.5)
        print('FIM!')
    if passo == 0:
        if inicio > fim:
            passo = -1
        elif fim > inicio:
            passo = 1
        for i in range(inicio, (fim + passo), passo):
            print(f'{i}', end=' -> ')
            sleep(0.5)
        print('FIM!')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input(f'Digite o início: '))
f = int(input(f'Digite o fim: '))
p = int(input(f'Digite o passo: '))
contador(i, f, p)


