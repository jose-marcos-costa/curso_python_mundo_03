def leiaInt(frase):
    resp = input(f'{frase}')
    while not resp.isnumeric():
        print('{}ERRO! Digite um número inteiro válido.{}'.format('\033[31m', '\033[m'))
        resp = input(f'{frase}')
    return resp


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')