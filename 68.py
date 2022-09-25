from random import randint
soma = 0
vitoria = 0


while True:
    jogador = int(input("Jogue um numero"))
    computador = randint(0,10)
    soma = computador + jogador
    opcao = ""
    while opcao not in "PI":
        opcao = str(input("Deseja ser PAR ou Impar")).strip().upper()[0]
    print(f"o computaodr =  {computador} E o Jogador = {jogador} total de {soma}")
    print("deu par" if soma % 2 == 0 else  "deu impar")
    if opcao == "P":
        if soma % 2 == 0:
            print(f"o computaodr =  {computador} E o Jogador = {jogador}! Voce venceu")
            vitoria += 1
        else:
            print("Voce perdeu")
            break
    elif opcao == "I":
        if soma % 2 == 1:
            print("Voce venceu")
            vitoria +=1
        else:
            print("Voce perdeu")
            break

print(f"voce venceu{vitoria}")

