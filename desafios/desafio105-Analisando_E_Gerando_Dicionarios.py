def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com vária informações sobre a situação da turma.
    """
    maior = menor = soma = 0
    resumo = dict()
    resumo['total'] = len(n)
    #return resumo
    for c in range(0, len(n)):
        soma += n[c]
        if c == 0:
            maior = n[c]
            menor = n[c]
        else:
            if n[c] > maior:
                maior = n[c]
            elif n[c] < menor:
                menor = n[c]
    media = soma / len(n)
    resumo['maior'] = maior
    resumo['menor'] = menor
    resumo['media'] = media
    if sit == True:
        if media < 6:
            resumo['situacao'] = 'RUIM'
        elif 6 <= media < 7:
            resumo['situacao'] = 'RAZOÁVEL'
        elif media >= 7:
            resumo['situacao'] = 'BOA'

    return resumo

# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)