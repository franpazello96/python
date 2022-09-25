valores = []

while True:
    valores.append(int(input("Digite um valor")))
    resp = str(input("quer continuar"))
    if resp in "Nn":
        break
valores.sort(reverse = True)
print(f"Voce digitou {len(valores)} e sua lista é {valores}")
if 5 in valores:
    print("o valor 5 faz parte da lista")
else:
    print("o valor 5 foi encontrado na lista")
    