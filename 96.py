def area(larg, comp):
    area = larg * comp
    print(f"A area do seu terreno {larg} e {comp} é de {area} m²")


l = float(input("LArgura: "))
c = float(input("Altura: "))
area(l, c)
