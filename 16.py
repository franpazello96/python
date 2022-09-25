galera =[]
dados = []

for contador in range(0,2):
    dados.append(str(input("nome:")))
    dados.append(int(input("idade")))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(p[0])
