from datetime import date


def voto(ano):
    """
    -> Função imprime a disponibilidade do
    voto do cidadão.
    :param ano: Ano de nascimento do cidadão
    :return:    'NEGADO'        ->
                'OPCIONAL'      ->
                'OBRIGATÓRIO'   ->
    Função criada por José Marcos Costa
    """
    idade = date.today().year - ano
    if idade < 16:
        situacao = 'NÃO VOTA'
    elif (16 <= idade < 18) or idade > 70:
        situacao = 'VOTO OPCIONAL'
    else:
        situacao = 'VOTO OBRIGATóRIO'
    print(f'Com {idade} anos: {situacao}.')


# Programa Principal
print('-' * 30)
ano_nascimento = int(input('Em que ano você nasceu? '))
voto(ano_nascimento)