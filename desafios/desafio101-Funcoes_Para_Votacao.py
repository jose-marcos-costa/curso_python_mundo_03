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
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif (16 <= idade < 18) or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATóRIO'


# Programa Principal
print('-' * 30)
ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))
