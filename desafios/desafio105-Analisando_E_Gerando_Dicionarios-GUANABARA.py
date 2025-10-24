def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com vária informações sobre a situação da turma.
    """
    resumo = dict()
    resumo['total'] = len(n)
    resumo['maior'] = max(n)
    resumo['menor'] = min(n)
    resumo['media'] = sum(n) / len(n)
    if sit:
        if resumo['media'] < 5:
            resumo['situacao'] = 'RUIM'
        elif 5 <= resumo['media'] < 7:
            resumo['situacao'] = 'RAZOÁVEL'
        elif resumo['media'] >= 7:
            resumo['situacao'] = 'BOA'
    return resumo


# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)