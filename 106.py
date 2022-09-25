sexo = ""

while True:
    sexo = str(input("Digite seu sexo M/F")).upper()
    if sexo == "F" or sexo == "M":
        continue
    else:
        print("Digite o novamente")