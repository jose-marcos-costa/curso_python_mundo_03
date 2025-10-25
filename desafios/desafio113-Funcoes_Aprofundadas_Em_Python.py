def leiaInt(frase):
    try:
        resp = int(input(f'{frase}'))
    except Exception as erro:
        print('{}ERRO {}: por favor, digite um número inteiro válido.{}'.format('\033[31m', erro.__class__, '\033[m'))
    except KeyboardInterrupt:
        print('Usuário preferiu não digitar esse número.')
    else:
        return resp

# Programa Principal
ni = leiaInt('Digite um Inteiro: ')
#nr = leiaReal('Digite um Real: ')
print(f'O valor interiro digitado foi {ni}')
# e o real foi {nr}')