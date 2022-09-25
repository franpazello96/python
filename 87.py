matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
maiorValor = 0
somaDaColuna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posicao{linha} e {coluna}"))
print(matriz)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()

for linha in range(0,3):
    somaDaColuna += matriz[l][2]

for coluna in range(0,3):
    if coluna == 0:
        maiorValor = matriz[1][coluna]
    elif matriz[1][c] > maiorValor:
        maiorValor = matriz[1][coluna]

print(somaPares)
print(somaDaColuna)
print(maiorValor) 