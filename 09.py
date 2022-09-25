estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

while True:
    print("=" * 10, "CARDÁPIO", "=" * 10)
    for pedido in cardapio:
        print(pedido)
    pedido = input("O que deseja comer hoje? ")
    if pedido in cardapio:
        ingredientes = cardapio[pedido]
        produzir = True
        for ingrediente in ingredientes:
            quant = estoque[ingrediente]
            if quant == 0:
                produzir = False
                break
        if produzir:
            estoque[ingrediente] -= 1
            print(f"Um {pedido} saindo no capricho!!!")
        else:
            print("Pedido não pode ser produzido")
    else:
        print("Item não localizado no cardápio!!!")