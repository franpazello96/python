jogo = {}
gols = []
jogo["nome"] = str(input("Nome do jogador"))
tot = int(input(f"Quantas patidas {jogo['nome']} jogou?"))

for i in range(0, tot):
    gols.append(int(input(f"Quantos gols na partida {i}?")))

jogo["gols"] = gols[:]
jogo["total"] = sum(gols)
print(jogo)
print("="*30)
