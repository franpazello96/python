from random import randint
computador = randint(0, 10)
print("Adivinhe qual numero que eu pensei...")
acertou = 0
while True:
    palpite = int(input("Digite um numero"))
    acertou += 1
    if palpite == computador:
        print("Acertou")
        break
    else:
        print("Tente mais uma vez")
print("Foi necessario", acertou, "Palpites")