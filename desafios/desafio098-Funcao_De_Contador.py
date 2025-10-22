from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim and passo != 0 :
        for cont in range(inicio, (fim - passo), -passo):
            print(f'{cont}', end=' -> ')
            sleep(0.5)
        print('FIM!')
    if (fim > inicio and passo != 0) or passo < 0:
        for cont in range(inicio, (fim + passo), passo):
            print(f'{cont}', end=' -> ')
            sleep(0.5)
        print('FIM!')
    if passo == 0:
        if inicio > fim:
            passo = -1
        elif fim > inicio:
            passo = 1
        for cont in range(inicio, (fim + passo), passo):
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


