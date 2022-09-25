continuar = "S"
contadorIdade = 0
contadorSexo = 0
contadorFem = 0

while True:
    if continuar == "S":
        idade = int(input("digite sua idade"))
        sexo = str(input("digite seu sexo")).strip().upper()
        continuar = str(input("Deseja continuar S/N")).strip().upper()
        if idade > 18:
            contadorIdade += 1
        if sexo == "M":
            contadorSexo += 1
        if sexo == "F" and idade < 20:
            contadorFem +=1
    else:
        break
print(f"pessoas maiores de 18 anos {contadorIdade}, homens cadastrados {contadorSexo}, mulheres com menos de 20 anos {contadorFem}")
