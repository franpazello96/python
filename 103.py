

def ficha(jog="Desconhecido", gol=0):
    print(f"o jogador {jog} fez {gol} gols no campeonato")


nome = str(input("Nome do jogador"))
gols = str(input("numero de gols"))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
    