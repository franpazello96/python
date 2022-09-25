total = contador  = mil = 0
continuar = "S"
barato = ""
menor = preco = 0
while True:
    if continuar == "S":
        produto = str(input("Digite o nome do produto"))
        preco = float(input("Digite o valor do produto"))
        continuar = str(input("Deseja continuar?")).upper()
        contador += 1
        total += preco
        if preco > 1000.00:
            mil += 1
        if contador ==1 or preco < menor:
            menor = preco
            barato = produto
    else:
        break
print(f"o valor total gasto foi de R$: {total}, a quantidade de produtos com valor maior do que R$1000,00 = {mil}, o produto mais barato foi o {barato , menor} ")
