listagem = ("lapis", 1.75,
            "borracha", 2.00,
            "caderno", 15.00,
            "estojo", 5.00,)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"{listagem[pos]:>7.2f}")
