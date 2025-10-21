pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['idade'])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['Peso'] = 98.5
print(f'-=' * 30)
for k, v  in pessoas.items():
    print(f'{k} = {v}')
print(f'-=' * 30)