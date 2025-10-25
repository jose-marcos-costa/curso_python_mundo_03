def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(f'{msg}'))
        except (ValueError, TypeError):
            print('{}ERRO: por favor, digite um número inteiro válido.{}'.format('\033[31m', '\033[m'))
            continue
        except KeyboardInterrupt:
            print('\n{}Usuário preferiu não digitar esse número.{}'.format('\033[31m', '\033[m'))
            return 0
        else:
            return n
