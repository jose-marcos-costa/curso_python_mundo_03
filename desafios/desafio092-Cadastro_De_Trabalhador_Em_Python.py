from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - ano_nascimento
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = (trabalhador['contratação']  - ano_nascimento) + 35
for k, v in trabalhador.items():
    print(f'{k} tem valor {v}')
