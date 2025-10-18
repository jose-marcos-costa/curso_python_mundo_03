teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # Ligação entre as estruturas -> análogo ao 'lista a' = 'lista b' (Devo fazer uma cópia)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print (galera)
print(teste)