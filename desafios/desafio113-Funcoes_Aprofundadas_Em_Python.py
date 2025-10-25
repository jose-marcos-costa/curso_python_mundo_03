def leiaInt(msg):
    while True:
        try:
            n = int(input(f'{msg}'))
        except (ValueError, TypeError):
            print('{}ERRO: por favor, digite um número interiro válido.{}'.format('\033[31m', '\033[m'))
            continue
        except KeyboardInterrupt:
            print('\n{}Usuário preferiu não digitar esse número.{}'.format('\033[31m', '\033[m'))
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(f'{msg}'))
        except (ValueError, TypeError):
            print('{}ERRO: por favor, digite um número real válido.{}'.format('\033[31m', '\033[m'))
            continue
        except KeyboardInterrupt:
            print('\n{}Usuário preferiu não digitar esse número.{}'.format('\033[31m', '\033[m'))
            return 0
        else:
            return n


# Programa Principal
ni = leiaInt('Digite um Inteiro: ')
nr = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {ni} e o real foi {nr}')