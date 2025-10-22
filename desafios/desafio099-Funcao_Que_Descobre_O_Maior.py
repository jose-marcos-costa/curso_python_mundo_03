from time import sleep


def maior(* num):
    print('-=' * 30)
    print(f'Analizando os valores passados...')
    if len(num) > 0:
        for v in num:
            print(f'{v} ', end='')
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')
    elif len(num) == 0:
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi 0')



# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
