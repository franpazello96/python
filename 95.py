jogo = {}
gols = []
time = []

while True:
    jogo["nome"] = str(input("Nome do jogador"))
    tot = int(input(f"Quantas patidas {jogo['nome']} jogou?"))
    jogo.clear()
    for i in range(0, tot):
        gols.append(int(input(f"Quantos gols na partida {i}?")))
    jogo["gols"] = gols[:]
    jogo["total"] = sum(gols)
    time.append(jogo.copy())
    while True:
        resp = str(input("quer continuar s/n")).upper()[0]
        if resp in "SN ":
            break
        print("ERRO! Responda apenas S ou N")
    if resp == "N":
        break
print("="*30)
print("cod", end="")
for i in jogo.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
while True:
    busca = int(input("mostrar dados de qual jogador? (999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print((f"erro nao existe o jogador com o codigo"))
    else:
        print(f'levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["nome"]):
            print(f"no jogo {i+1} fez {g} gols")